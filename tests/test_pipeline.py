"""Kiểm thử tự động cho hvalign. Chạy: python -m pytest -q (tại Lab/GK)."""
from pathlib import Path

from hvalign.align import Item, dp_align
from hvalign.anchors import AnchorIndex
from hvalign.clean import Cleaner
from hvalign.readers import detect_format, load_document
from hvalign.segment import split_han, split_viet
from hvalign.xlsxlite import Sheet, read_xlsx, write_xlsx

WIKI = """{{header|title=續資治通鑑卷第二|section=宋紀二{{*|起重光作噩正月，盡{{參|元|玄}}黓閹茂十二月。}}}}
__TOC__
太祖啟運立極皇帝
=={{YL|建隆二年}}{{*|遼應歴十一年。}}<ref>建隆二年︰辛酉</ref>==

&sect;春，正月，丙申朔，御崇元殿受朝。{{*|後改爲惠民河。}}

&sect;詔浚蔡渠，[[開元禮]]也。
"""


# ------------------------------------------------------------------ Bước 4: đọc và chuẩn hóa
def test_detect_format_by_content():
    assert detect_format(WIKI, ".txt")[0] == "wikitext"
    assert detect_format("春，正月，丙申朔。\n壬寅，幸新造船務。", ".txt")[0] == "plain"
    assert detect_format("<!DOCTYPE html><html><body></body></html>", ".txt")[0] == "html"
    assert detect_format("không có markup", ".wikitext")[0] == "wikitext"


def test_txt_with_wikitext_equals_wikitext(tmp_path: Path):
    a, b = tmp_path / "a.wikitext", tmp_path / "TTTTG_q02_han.txt"
    a.write_text(WIKI, encoding="utf-8")
    b.write_bytes(b"\xef\xbb\xbf" + WIKI.replace("\n", "\r\n").encode("utf-8"))  # BOM + CRLF như Notepad
    da, db = load_document(a, "han"), load_document(b, "han")
    assert [(x.kind, x.text) for x in da.blocks] == [(x.kind, x.text) for x in db.blocks]
    assert db.encoding == "utf-8-sig"


def test_wikitext_templates_refs_headings():
    p = Path(__file__).parent / "_tmp_wiki.wikitext"
    p.write_text(WIKI, encoding="utf-8")
    try:
        d = load_document(p, "han")
    finally:
        p.unlink()
    kinds = [b.kind for b in d.blocks]
    assert kinds == ["para", "heading", "para", "para"]
    assert d.blocks[1].text == "建隆二年⟪*:遼應歴十一年。⟫⟪ref:建隆二年︰辛酉⟫"
    assert d.blocks[2].text == "§春，正月，丙申朔，御崇元殿受朝。⟪*:後改爲惠民河。⟫"
    assert d.blocks[3].text == "§詔浚蔡渠，開元禮也。"
    assert d.meta["title"] == "續資治通鑑卷第二"  # đầu đề → siêu dữ liệu, không vào text


def test_plain_text_and_bold_title(tmp_path: Path):
    p = tmp_path / "x_viet.txt"
    p.write_text("Dòng một.\n\n  Dòng   hai.\nhttps://vi.wikisource.org/x\n", encoding="utf-8")
    assert [b.text for b in load_document(p, "viet").blocks] == ["Dòng một.", "Dòng hai."]
    q = tmp_path / "y.wikitext"
    q.write_text("'''Thái Tổ Hoàng đế\n'''\n== Năm 961 ==\nMùa xuân.\n", encoding="utf-8")
    assert [b.kind for b in load_document(q, "viet").blocks] == ["title", "heading", "para"]


def test_sillok_html_joins_taitou(tmp_path: Path):
    html = ('<div id="dmv01"><div class="view-text"><p class="paragraph">○諭曰、福康安<a href="x">'
            '<img src="i.png"></a>等奏。是</p><p class="paragraph">天心已厭棄黎氏。</p></div></div>'
            '<div id="dmv02"></div><button data-title="高宗純皇帝實錄 卷之一 六月"></button>')
    p = tmp_path / "a.html"
    p.write_text(html, encoding="utf-8")
    d = load_document(p, "han")
    assert [b.text for b in d.blocks if b.kind == "para"] == ["○諭曰、福康安等奏。是天心已厭棄黎氏。"]


# ------------------------------------------------------------------ Bước 5: làm sạch
def _cleaner(**rules):
    base = {k: True for k in ["R03_bo_ref", "R04_bo_chu_nho", "R05_bo_dan_nguon", "R06_bo_chu_han_trong_viet",
                              "R07_bo_nam_duong_lich", "R08_bo_dong_tieu_de", "R09_sua_ma_chu",
                              "R10_chuan_hoa_khoang_trang_dau_cau"]}
    base.update(rules)
    return Cleaner({"lam_sach": base}, {})


def _c(text, lang="viet", kind="para", **rules):
    return _cleaner(**rules).clean_block({"id": "x", "kind": kind, "text": text}, lang, True)


def test_r06_inline_han():
    assert _c("Phúc Khang An (福康安) tấu.") == "Phúc Khang An tấu."
    assert _c("Giao Chỉ 交趾, đầu thời Hán.") == "Giao Chỉ, đầu thời Hán."
    assert _c("đặt Giao Chỉ Thứ sử 交阯刺史 để cai quản.") == "đặt Giao Chỉ Thứ sử để cai quản."
    assert _c("Lời bàn (贊 tán).") == "Lời bàn (tán)."
    assert _c("gọi là “diệu quân 耀軍” (diễn).") == "gọi là “diệu quân” (diễn)."


def test_r06_keeps_unmatched_han_for_review():
    cl = _cleaner()
    out = cl.clean_block({"id": "x", "kind": "para", "text": "Ông đọc bài thơ: 春眠不覺曉"}, "viet", True)
    assert "春眠不覺曉" in out and cl.warnings


def test_r07_year_gloss():
    assert _c("Năm Vĩnh Thọ thứ 3 (năm 157), Trường Sa Man phản.") == "Năm Vĩnh Thọ thứ 3, Trường Sa Man phản."
    assert _c("ngày 22 (năm 1789 dương lịch) và (112 TCN).") == "ngày 22 và."
    assert _c("(Liêu, Ứng Lịch năm thứ 11)") == "(Liêu, Ứng Lịch năm thứ 11)"  # không phải năm dương lịch


def test_markers_and_titles_han():
    assert _c("§春，正月，丙申朔。⟪*:後改爲惠民河。⟫⟪ref:公元⟫", "han") == "春，正月，丙申朔。"
    assert _c("《續資治通鑑》卷第二", "han") is None
    assert _c("太祖啟運立極英武睿文神德聖功至明大孝皇帝", "han") is None
    assert _c("春，正月, 丙申朔:", "han") == "春，正月，丙申朔："
    assert _c("春。⟪*:注文⟫", "han", R04_bo_chu_nho=False) == "春。注文"  # tắt luật → giữ chữ của chú


# ------------------------------------------------------------------ Bước 6: tách câu
def test_split_han_quotes_soft():
    u = split_han("帝曰：「朕甚憂之。卿等勉之。」群臣拜謝。")
    assert [k for _, k in u] == ["soft", "hard", "end"]
    assert u[1][0] == "卿等勉之。」"
    assert [k for _, k in split_han("甲。乙。丙。", soft_period=True)] == ["soft", "soft", "end"]


def test_split_viet_protections():
    u = split_viet("Quân hơn 10.000 người, năm 112 TCN. Mùa xuân, Dụ rằng: Trẫm nghĩ vậy. hết")
    assert [t for t, _ in u] == ["Quân hơn 10.000 người, năm 112 TCN.", "Mùa xuân, Dụ rằng:",
                                 "Trẫm nghĩ vậy. hết"]
    assert [k for _, k in u] == ["hard", "soft", "end"]


# ------------------------------------------------------------------ Bước 7: dóng hàng
def test_dp_align_merges_and_anchors():
    idx = AnchorIndex({"福康安": {"Phúc Khang An"}})
    A = [Item([f"h{i}"], t, len(t), idx.han_keys(t)) for i, t in enumerate(["丙申，福康安奏事", "壬寅，大赦天下"])]
    B = [Item([f"v{i}"], t, len(t.split()), idx.viet_keys(t)) for i, t in enumerate(
        ["Ngày Bính Thân, Phúc Khang An", "tâu việc.", "Ngày Nhâm Dần, đại xá thiên hạ."])]
    assert A[0].keys == {"cc:丙申", "nm:福康安"} and B[0].keys == {"cc:丙申", "nm:福康安"}
    beads = {(1, 1): .89, (1, 2): .04, (2, 1): .04, (1, 0): .002, (0, 1): .002}
    out = dp_align(A, B, beads, 1.2, 2.0, {"pen_hard": .7, "pen_soft": 0, "w_hit": 2, "w_miss": .7})
    assert [(o[0], o[1], o[2], o[3]) for o in out] == [(0, 1, 0, 2), (1, 2, 2, 3)]


# ------------------------------------------------------------------ xuất Excel
def test_xlsx_roundtrip_strings(tmp_path: Path):
    p = tmp_path / "t.xlsx"
    rows = [["Hán", "Việt"], ["=SUM(A1)", "1.000"], ["𨓆羣臣", "a & <b>"]]
    write_xlsx(p, [Sheet("DONG_HANG", rows)])
    wb = read_xlsx(p)
    assert wb.sheets["DONG_HANG"] == rows
    assert wb.formulas["DONG_HANG"] == 0 and wb.merged["DONG_HANG"] == 0
