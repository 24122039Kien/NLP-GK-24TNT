"""Báo cáo tự sinh cho mỗi tác phẩm (work/<MA>/bao_cao.md) – đủ 5 mục tối thiểu của Guideline."""
from __future__ import annotations

import platform
import re
from collections import Counter
from datetime import date
from pathlib import Path

from . import __version__
from . import review
from .notes import notes_for
from .textutil import CJK_RUN_RE


def _han_chars(text: str) -> int:
    return sum(len(m.group(0)) for m in CJK_RUN_RE.finditer(text))


def _viet_syll(text: str) -> int:
    return len(re.findall(r"[^\W\d_]+", CJK_RUN_RE.sub(" ", text)))


def scope_lines(project, work: str, pairs: list[dict], sach: Path) -> list[str]:
    """Phạm vi được giao, quyển đã dóng và độ phủ – để người đọc thấy ngay tác phẩm đã làm trọn hay mới một phần."""
    assigned = project.assignments().get(work, {})
    done = sorted({str(p["vol"]) for p in pairs}, key=lambda v: (len(v), v))
    vols = sorted((v for v in assigned if v != "*"), key=lambda v: (len(v), v))
    L = []
    if "*" in assigned and not vols:
        L.append(f"- Phạm vi được giao (`config/phan_cong.tsv`): **cả tác phẩm** ({assigned['*']}); "
                 f"quyển có trong nguồn và đã dóng: {', '.join(done) or 'chưa có'}.")
    else:
        miss = [v for v in vols if v not in done]
        L.append(f"- Phạm vi được giao (`config/phan_cong.tsv`): {len(vols)} quyển; đã dóng "
                 f"**{len(vols) - len(miss)}/{len(vols)}**" + (f" – còn thiếu: {', '.join(miss)}" if miss else
                                                                 " (đủ)") + ".")
        extra = [v for v in done if v not in vols]
        if extra:
            L.append(f"- Quyển có cặp nhưng không nằm trong phân công: {', '.join(extra)}.")
    text = {lang: (sach / f"{lang}.txt").read_text(encoding="utf-8") if (sach / f"{lang}.txt").exists() else ""
            for lang in ("han", "viet")}
    tot_h, tot_v = _han_chars(text["han"]), _viet_syll(text["viet"])
    in_h = sum(_han_chars(p["han"]) for p in pairs)
    in_v = sum(_viet_syll(p["viet"]) for p in pairs)
    if tot_h and tot_v:
        L.append(f"- Độ phủ: các cặp chứa **{min(in_h / tot_h, 1):.1%}** số chữ Hán và **{min(in_v / tot_v, 1):.1%}** "
                 "số âm tiết Việt của `03_text_sach` (phần chưa phủ là câu không ghép được hoặc cặp bỏ khi hiệu đính; "
                 "phần chỉ một bản có đã bị loại trừ từ Bước 5, không tính ở đây).")
    return L


def read_tsv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines() if ln and not ln.startswith("#")]
    if not lines:
        return []
    head = lines[0].split("\t")
    return [dict(zip(head, ln.split("\t"))) for ln in lines[1:]]


def load_manifests(root: Path) -> list[dict]:
    rows = []
    for p in list((root / "Docs").glob("*manifest*.tsv")) + [root / "config" / "manifest.tsv"]:
        rows += read_tsv(p)
    return rows


def run(project, work: str, validation=None, log=print) -> Path:
    scratch = project.scratch(work)
    machine = review.machine_pairs(project, work)
    pairs, hd = review.final_pairs(project, work)
    sach = project.work_dir(work) / "03_text_sach"
    n_lines = {lang: sum(1 for _ in open(sach / f"{lang}.txt", encoding="utf-8")) for lang in ("han", "viet")}
    clean_log = read_tsv(scratch / "clean_log.tsv")
    excl = read_tsv(scratch / "loai_tru.tsv")
    unp = read_tsv(scratch / "khong_ghep.tsv")
    warns = read_tsv(scratch / "canh_bao.tsv")
    ext = read_tsv(scratch / "extract_log.tsv")
    man = load_manifests(project.root)

    flagged = [p for p in machine if p["co"]]
    decided = review.handled(review.load_decisions(project, work))
    seen = sum(1 for p in flagged if review.key_of(p) in decided)
    notes = notes_for(project, work, pairs)
    n_notes = sum(1 for n in notes if n)
    state = "dóng tự động, ghi chú tự động" + (f"; người đã xem {seen}/{len(flagged)} cặp máy gắn cờ" if seen else "")
    L = [f"# Báo cáo tự sinh – {work}", "",
         f"Ngày: {date.today().isoformat()} · hvalign {__version__} · **Trạng thái: {state}**", ""]
    by_member = Counter(p["member"] for p in pairs)
    L += ["## 1. Số cặp", "", f"Tổng: **{len(pairs)}** cặp.", "", "| Thành viên | Số cặp |", "|---|---|"]
    L += [f"| {m} | {n} |" for m, n in sorted(by_member.items())]
    vols = Counter((p["vol"], p["member"]) for p in pairs)
    L += ["", "| Quyển | Thành viên | Số cặp |", "|---|---|---|"]
    L += [f"| {v} | {m} | {n} |" for (v, m), n in sorted(vols.items(), key=lambda x: (len(x[0][0]), x[0][0]))]
    kinds = Counter(p["kieu"] for p in pairs)
    L += ["", "Kiểu ghép: " + ", ".join(f"`{k}` {n}" for k, n in kinds.most_common()), ""]
    L += scope_lines(project, work, pairs, sach) + [""]

    L += ["## 2. Số dòng văn bản sạch", "", f"- `03_text_sach/han.txt`: {n_lines['han']} dòng",
          f"- `03_text_sach/viet.txt`: {n_lines['viet']} dòng",
          "- Thư mục nộp: `01_nguon` (dữ liệu đã tải/crawl), `03_text_sach` (text Hán và Việt đã trích xuất và làm "
          "sạch), `04_dong_hang` (TSV + XLSX), `bao_cao.md`. Không có `02_ocr_tho`: nguồn là text số "
          "(wikitext/HTML/txt), không phải ảnh/PDF scan, nên không OCR (theo nhận xét của giảng viên 18/11). "
          "Tệp `.pdf` trong `01_nguon` là bản in của trang nguồn, lưu để đối chiếu.", ""]

    L += ["## 3. Kết quả tự kiểm tra", ""]
    if validation is not None:
        errs, ws = validation
        L.append(f"- Kiểm định định dạng TSV/XLSX: **{'đạt' if not errs else str(len(errs)) + ' lỗi'}**"
                 + (f"; cảnh báo: {'; '.join(ws)}" if ws else ""))
    rules = Counter()
    for r in clean_log:
        rules[r["luat"]] += int(r["so_lan"])
    L.append("- Luật làm sạch đã áp dụng: " + ", ".join(f"{k} ×{v}" for k, v in sorted(rules.items())))
    reasons = Counter(r["ly_do"] for r in excl)
    L.append(f"- Loại trừ (không có bản dịch / không phải chính văn): {len(excl)} khối"
             + (" – " + "; ".join(f"{k} ({v})" for k, v in reasons.items()) if reasons else ""))
    L.append(f"- Câu không ghép được (ghi ở `work/{work}/khong_ghep.tsv`, không đưa vào TSV): {len(unp)}")
    flags = Counter(f for p in machine for f in p["co"])
    L.append(f"- Cặp máy gắn cờ: {len(flagged)} (" + (", ".join(f"`{k}` {v}" for k, v in flags.most_common())
                                                      or "không") + f"); người đã xem {seen}")
    L.append(f"- Hiệu đính đã áp: xác nhận đúng {hd['dung']}, sửa chữ {hd['sua']}, gộp {hd['gop']}, "
             f"bỏ cặp sai {hd['sai']} (quyết định lưu ở `hieu_dinh/{work}__<người>.tsv`)")
    L.append(f"- Cảnh báo khi làm sạch: {len(warns)} (xem `work/{work}/canh_bao.tsv`)")
    note_where = ("cột `Ghi chú` của sheet DONG_HANG" if project.work_cfg(work).get("cot_ghi_chu")
                  else "cột `Ghi chú` của sheet TRUY_VET")
    L.append(f"- Ghi chú tự động (dịch rút gọn, vế Việt thêm diễn giải, câu không được dịch): {n_notes} cặp, "
             f"ghi ở {note_where}")
    L.append("- Phạm vi theo trả lời của giảng viên: chỉ dóng hàng phần có song ngữ; phần chỉ một bản có "
             "thì không đưa vào dữ liệu (đã liệt kê ở mục Loại trừ và Câu không ghép được).")
    grades = review.load_grades(project)
    keys = {p["khoa"] for p in pairs}
    rates = {m: review.error_rate(grades, m, keys, work) for m in sorted(by_member)}
    if any(r["da_cham"] for r in rates.values()):
        L.append("- Tỷ lệ lỗi theo §8 Guideline (mẫu chấm chéo, chỉ tính cặp thuộc tác phẩm này):")
        for m, r in rates.items():
            if r["da_cham"]:
                lb = ", ".join(f"{k} {v}" for k, v in r["nhan"].items() if v)
                L.append(f"  - {m}: {r['sai']}/{r['da_cham']} cặp lỗi = **{r['ty_le_loi']:.1%}**"
                         + (f" ({lb})" if lb else ""))
    else:
        L.append("- Tỷ lệ lỗi theo §8 Guideline: chưa chấm mẫu (tuỳ chọn: app → Nâng cao → Chấm mẫu).")
    L.append("")

    L += ["## 4. Nguồn tài liệu", "", "| Quyển | Bản | Tệp | Định dạng đọc được | Nguồn trực tuyến | revid |",
          "|---|---|---|---|---|---|"]
    for e in ext:
        m = next((r for r in man if r.get("tep", "").endswith(e["tep"])), {})
        L.append(f"| {e['quyen']} | {e['ngon_ngu']} | `{Path(e['tep']).name}` | {e['dinh_dang']} | "
                 f"{m.get('url', '(không có trong manifest)')} | {m.get('revid', '')} |")
    L.append("")
    L += ["## 5. Công cụ", "",
          f"- `hvalign` {__version__} (Lab/GK/hvalign), Python {platform.python_version()}, PyYAML.",
          "- Bước 4: tự nhận dạng định dạng nguồn (wikitext / text thuần / HTML sillok) và chuẩn hóa về một dạng.",
          "- Bước 7: dóng 3 tầng (mục → đoạn → câu), chi phí Gale–Church + mốc can chi và tên riêng Hán Việt.",
          f"- Cấu hình: `config/project.yaml`, `config/works/{work}.yaml`, `config/phan_cong.tsv`.", ""]
    out = scratch / "bao_cao.md"
    out.write_text("\n".join(L), encoding="utf-8")
    log(f"  Báo cáo {work}: work/{work}/bao_cao.md")
    return out
