"""Kiểm thử tự động cho hvalign. Chạy: python -m pytest -q (tại Lab/GK)."""
from pathlib import Path

from hvalign.align import Item, dp_align
from hvalign.anchors import AnchorIndex
from hvalign.clean import Cleaner
from hvalign.readers import detect_format, load_document
from hvalign.segment import split_han, split_viet
from hvalign.textutil import SourceReadError, read_source
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


def test_non_utf8_source_gives_clear_error(tmp_path: Path):
    p = tmp_path / "x_han.txt"
    p.write_bytes("天子曰。".encode("big5"))
    try:
        read_source(p)
    except SourceReadError as e:
        assert "x_han.txt" in str(e) and "UTF-8" in str(e)
    else:
        raise AssertionError("phải báo lỗi mã hóa")


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


# ------------------------------------------------------------------ hiệu đính (app)
def _p(i, han, viet, co=()):
    return {"pid": f"T:{i:05d}", "vol": "1", "member": "A", "kieu": "1-1", "han": han, "viet": viet,
            "han_ids": [f"h{i}"], "viet_ids": [f"v{i}"], "chi_phi": 1.0, "delta": 0.0, "co": list(co)}


def test_review_apply_decisions():
    from hvalign.review import apply, handled, key_of
    P = [_p(1, "甲。", "Một."), _p(2, "乙", "Hai"), _p(3, "丙。", "ba."), _p(4, "丁。", "Bốn."), _p(5, "戊。", "Năm.")]
    k = [key_of(p) for p in P]
    dec = {k[0]: {"quyet_dinh": "dung"},
           k[1]: {"quyet_dinh": "gop", "gop_voi": k[2]},                      # gộp 2+3
           k[3]: {"quyet_dinh": "sai"},                                       # bỏ cặp 4
           k[4]: {"quyet_dinh": "sua", "han_sua": "戊己。", "viet_sua": "Năm sáu."},
           "khong|ton_tai": {"quyet_dinh": "dung"}}                           # quyết định cũ, không khớp
    out, st = apply(P, dec)
    assert [(p["han"], p["viet"], p["hd"]) for p in out] == [
        ("甲。", "Một.", "dung"), ("乙丙。", "Hai ba.", "gop"), ("戊己。", "Năm sáu.", "sua")]
    assert out[1]["kieu"] == "2-2" and out[1]["han_ids"] == ["h2", "h3"]
    assert st == {"dung": 1, "sai": 1, "sua": 1, "gop": 1, "khong_khop": 1}
    assert handled(dec)[k[2]]["quyet_dinh"] == "gop_tren"


def test_review_files_roundtrip_and_undo(tmp_path: Path):
    from hvalign import review
    from hvalign.config import Project
    pr = Project(tmp_path, {})
    review.save_decision(pr, "HCB_99", "Kiên", "a|b", "sai")
    review.save_decision(pr, "HCB_99", "Huy", "c|d", "sua", han="甲\t乙", viet="x\ny")
    assert (tmp_path / "hieu_dinh" / "HCB_99__Kiên.tsv").exists()
    review.save_decision(pr, "HCB_99", "Kiên", "a|b", "xoa")                  # hoàn tác
    d = review.load_decisions(pr, "HCB_99")
    assert list(d) == ["c|d"] and d["c|d"]["han_sua"] == "甲 乙" and d["c|d"]["nguoi"] == "Huy"
    review.save_grade(pr, "Huy", "a|b", "HCB_99", "Kiên", "sai", "OMISSION")
    review.save_grade(pr, "Huy", "c|d", "HCB_99", "Kiên", "dung")
    r = review.error_rate(review.load_grades(pr), "Kiên")
    assert r["da_cham"] == 2 and r["ty_le_loi"] == 0.5 and r["nhan"]["OMISSION"] == 1
    assert review.sample_size(3000) == 100 and review.sample_size(40) == 40 and review.sample_size(500, 50) == 50


def test_auto_notes_short_long_and_untranslated(tmp_path: Path):
    from hvalign.config import Project
    from hvalign.notes import notes_for
    pr = Project(tmp_path, {})
    P = [_p(i, "天下大事分久必合合久", "thiên hạ đại sự chia lâu tất hợp hợp lâu tất chia") for i in range(1, 6)]
    P.append(_p(6, "天下大事分久必合合久必分天下大事分久必合合久必分", "Chia rồi hợp.", co=["rut_gon"]))
    P.append(_p(7, "帝曰可。", "Vua nói được. (Đây là chú thích rất dài của dịch giả về nghi lễ tế trời đất "
                               "thời xưa, không có trong bản Hán.) Rồi mọi người lui ra hết cả."))
    (tmp_path / "work" / "HCB_99").mkdir(parents=True)
    (tmp_path / "work" / "HCB_99" / "khong_ghep.tsv").write_text(
        "id\tngon_ngu\tly_do\tnoi_dung\nh3x\than\ttầng 3\t此句無譯。\n", encoding="utf-8")
    notes = notes_for(pr, "HCB_99", P, AnchorIndex({}))
    assert notes[0] == notes[1] == "" and notes[3] == notes[4] == ""
    assert notes[2].startswith("Câu Hán ngay sau không có bản dịch") and "此句無譯" in notes[2]
    assert notes[5].startswith("Dịch rút gọn")
    assert "dài gấp" in notes[6] and "chú thích của dịch giả" in notes[6]


def test_export_note_column_and_validate(tmp_path: Path):
    import json
    from hvalign import export
    from hvalign.config import Project
    pr = Project(tmp_path, {"ma_de_tai": "CV02", "mac_dinh": {"cot_ghi_chu": True}})
    sach = tmp_path / "CV02_HCB_99" / "03_text_sach"
    sach.mkdir(parents=True)
    for lang in ("han", "viet"):
        (sach / f"{lang}.txt").write_text("x\n", encoding="utf-8")
    sc = tmp_path / "work" / "HCB_99"
    sc.mkdir(parents=True)
    P = [_p(i, "天下大事分久必合合久", "thiên hạ đại sự chia lâu tất hợp hợp lâu tất chia") for i in range(1, 6)]
    P.append(_p(6, "天下大事分久必合合久必分天下大事分久必合合久必分", "Chia rồi hợp.", co=["rut_gon"]))
    (sc / "alignment.jsonl").write_text("".join(json.dumps(p, ensure_ascii=False) + "\n" for p in P), encoding="utf-8")
    out = export.run(pr, "HCB_99", log=lambda *a: None)
    rows = read_xlsx(out["xlsx"]).sheets["DONG_HANG"]
    assert rows[0] == ["Hán", "Việt", "Ghi chú"] and rows[6][2].startswith("Dịch rút gọn") and rows[1][2:] in ([], [""])
    assert out["tsv"].read_text(encoding="utf-8").count("\t") == 6  # TSV vẫn đúng 2 cột
    errs, _ = export.validate(pr, "HCB_99", log=lambda *a: None)
    assert errs == []
