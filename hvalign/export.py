"""Xuất kết quả dóng hàng ra TSV + XLSX theo Guideline, tạo sổ hiệu đính, kiểm định.

Mặc định xuất vào work/<MA>/xuat/ (bản xem trước, CHƯA hiệu đính).
Chỉ khi chạy với --ban-giao mới ghi vào <MA>/04_dong_hang/ (thư mục nộp).
"""
from __future__ import annotations

import random
import re
from collections import Counter
from datetime import date
from pathlib import Path

from . import __version__
from .notes import notes_for
from .review import final_pairs
from .textutil import CJK_RE, LATIN_RE
from .xlsxlite import Sheet, read_xlsx, write_xlsx

HEADER = ["Hán", "Việt"]
NOTE = "Ghi chú"


def _clean_cell(s: str) -> str:
    return re.sub(r"[\t\r\n]+", " ", s).strip()


def out_dir(project, work: str, deliver: bool) -> Path:
    return project.work_dir(work) / "04_dong_hang" if deliver else project.scratch(work) / "xuat"


def run(project, work: str, deliver: bool = False, log=print) -> dict:
    scratch = project.scratch(work)
    if not (scratch / "alignment.jsonl").exists():
        raise FileNotFoundError(2, "không có", str(scratch / "alignment.jsonl"))
    pairs, hd = final_pairs(project, work)  # đã áp quyết định hiệu đính trong hieu_dinh/
    rows = [[_clean_cell(p["han"]), _clean_cell(p["viet"])] for p in pairs]
    notes = [_clean_cell(n) for n in notes_for(project, work, pairs)]
    note_col = bool(project.work_cfg(work).get("cot_ghi_chu"))  # cột "Ghi chú" theo yêu cầu GV (HCB_11)
    od = out_dir(project, work, deliver)
    od.mkdir(parents=True, exist_ok=True)
    tsv = od / f"{work}_parallel.tsv"
    with open(tsv, "w", encoding="utf-8", newline="\n") as f:
        f.write("".join(f"{h}\t{v}\n" for h, v in rows))

    sach = project.work_dir(work) / "03_text_sach"
    n_lines = {lang: sum(1 for _ in open(sach / f"{lang}.txt", encoding="utf-8")) for lang in ("han", "viet")}
    by_member = Counter(p["member"] for p in pairs)
    by_vol = Counter((p["vol"], p["member"]) for p in pairs)
    by_kind = Counter(p["kieu"] for p in pairs)
    stats = [["Mục", "Giá trị", "Ghi chú"],
             ["Tác phẩm", work, ""], ["Tổng số cặp", len(rows), ""],
             ["Số dòng han.txt", n_lines["han"], "03_text_sach/han.txt"],
             ["Số dòng viet.txt", n_lines["viet"], "03_text_sach/viet.txt"],
             ["Ngày xuất", date.today().isoformat(), ""],
             ["Công cụ", f"hvalign {__version__}", "Lab/GK/hvalign"],
             ["Hiệu đính: xác nhận đúng", hd["dung"], "hieu_dinh/<MA>__<người>.tsv"],
             ["Hiệu đính: sửa chữ", hd["sua"], ""], ["Hiệu đính: gộp cặp", hd["gop"], ""],
             ["Hiệu đính: bỏ cặp sai", hd["sai"], ""],
             ["Cặp có ghi chú tự động", sum(1 for n in notes if n),
              "cột Ghi chú của DONG_HANG" if note_col else "cột Ghi chú của TRUY_VET"], ["", "", ""],
             ["Thành viên", "Số cặp", ""]]
    stats += [[m, n, ""] for m, n in sorted(by_member.items())]
    stats += [["", "", ""], ["Quyển", "Số cặp", "Thành viên"]]
    stats += [[v, n, m] for (v, m), n in sorted(by_vol.items(), key=lambda x: (len(x[0][0]), x[0][0]))]
    stats += [["", "", ""], ["Kiểu ghép", "Số cặp", ""]]
    stats += [[k, n, ""] for k, n in by_kind.most_common()]
    trace = [["STT", "Mã cặp", "Quyển", "Thành viên", "Kiểu", "Chi phí", "Cờ", "Hiệu đính",
              "Mã câu Hán", "Mã câu Việt", NOTE]]
    trace += [[i, p["pid"], p["vol"], p["member"], p["kieu"], p["chi_phi"], " ".join(p["co"]), p["hd"],
               " ".join(p["han_ids"]), " ".join(p["viet_ids"]), n]
              for i, (p, n) in enumerate(zip(pairs, notes), start=1)]
    xlsx = od / f"{work}_parallel.xlsx"
    if note_col:
        main = Sheet("DONG_HANG", [HEADER + [NOTE]] + [r + [n] for r, n in zip(rows, notes)], [70, 90, 45],
                     wrap=True)
    else:
        main = Sheet("DONG_HANG", [HEADER] + rows, [70, 90], wrap=True)
    write_xlsx(xlsx, [main, Sheet("THONG_KE", stats, [22, 16, 30]),
                      Sheet("TRUY_VET", trace, [7, 14, 7, 11, 6, 8, 18, 9, 40, 40, 50])])

    where = "04_dong_hang (BÀN GIAO)" if deliver else f"work/{work}/xuat (xem trước)"
    done = hd["dung"] + hd["sua"] + hd["gop"] + hd["sai"]
    log(f"  Xuất {work}: {len(rows)} cặp → {where}"
        + (f"; đã áp {done} quyết định hiệu đính" if done else "")
        + (f" ({hd['khong_khop']} quyết định cũ không còn khớp cặp nào)" if hd["khong_khop"] else ""))
    return {"tsv": tsv, "xlsx": xlsx}


def validate(project, work: str, deliver: bool = False, log=print) -> tuple[list[str], list[str]]:
    """Kiểm định định dạng theo Guideline. Trả về (lỗi, cảnh báo)."""
    od = out_dir(project, work, deliver)
    errs, warns = [], []
    tsv, xlsx = od / f"{work}_parallel.tsv", od / f"{work}_parallel.xlsx"
    if not re.fullmatch(r"HCB_\d{2}", work):
        errs.append(f"mã tác phẩm '{work}' không đúng mẫu HCB_xx")
    for p in (tsv, xlsx):
        if not p.exists():
            errs.append(f"thiếu tệp {p.name}")
    if errs:
        return _report(work, errs, warns, log)
    raw = tsv.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        errs.append("TSV có BOM")
    if b"\r" in raw:
        errs.append("TSV có ký tự CR (phải xuống dòng LF)")
    try:
        lines = raw.decode("utf-8").split("\n")
    except UnicodeDecodeError:
        return _report(work, errs + ["TSV không phải UTF-8"], warns, log)
    if lines and lines[-1] == "":
        lines.pop()
    if not lines:
        errs.append("không có cặp nào – kiểm tra nguồn (thiếu bản Hán/Việt?) bằng: python -m hvalign inventory")
    rows = []
    for i, line in enumerate(lines, start=1):
        cols = line.split("\t")
        if len(cols) != 2:
            errs.append(f"TSV dòng {i}: có {len(cols) - 1} dấu TAB (phải đúng 1)")
            continue
        if not cols[0].strip() or not cols[1].strip():
            errs.append(f"TSV dòng {i}: có vế rỗng")
        rows.append(cols)
    wb = read_xlsx(xlsx)
    if "DONG_HANG" not in wb.sheets:
        errs.append("XLSX không có sheet DONG_HANG")
    else:
        data = wb.sheets["DONG_HANG"]
        head = data[0] if data else []
        if head not in (HEADER, HEADER + [NOTE]):
            errs.append(f"XLSX: dòng tiêu đề phải là {HEADER} (có thể thêm cột '{NOTE}'), đang là {head or '(trống)'}")
        body = [r[:2] + [""] * (2 - len(r[:2])) for r in data[1:]]
        if len(body) != len(rows):
            errs.append(f"XLSX có {len(body)} cặp, TSV có {len(rows)} cặp")
        diff = [i for i, (a, b) in enumerate(zip(rows, body), start=1) if a != b]
        if diff:
            errs.append(f"XLSX khác TSV ở {len(diff)} dòng (đầu tiên: dòng {diff[0]})")
        if wb.formulas.get("DONG_HANG"):
            errs.append(f"XLSX có {wb.formulas['DONG_HANG']} ô công thức")
        if wb.merged.get("DONG_HANG"):
            errs.append("XLSX có ô bị gộp")
    viet_cjk = sum(1 for _, v in rows if CJK_RE.search(v))
    han_latin = sum(1 for h, _ in rows if LATIN_RE.search(h))
    dup = sum(n - 1 for n in Counter(map(tuple, rows)).values() if n > 1)
    dup_han = sum(n - 1 for n in Counter(h for h, _ in rows).values() if n > 1)
    if viet_cjk:
        warns.append(f"{viet_cjk} cặp có chữ Hán ở vế Việt")
    if han_latin:
        warns.append(f"{han_latin} cặp có chữ Latin ở vế Hán (thường là mã lỗi chữ chưa tra)")
    if dup:
        warns.append(f"{dup} cặp trùng lặp hoàn toàn")
    if dup_han:
        warns.append(f"{dup_han} câu Hán xuất hiện ở hơn một cặp (có thể là câu lặp thật, ví dụ 帝曰)")
    return _report(work, errs, warns, log)


def _report(work, errs, warns, log):
    status = "ĐẠT" if not errs else f"{len(errs)} LỖI"
    log(f"  Kiểm định {work}: {status}" + (f"; {len(warns)} cảnh báo" if warns else ""))
    for e in errs:
        log(f"    ✗ {e}")
    for w in warns:
        log(f"    ! {w}")
    return errs, warns


def sample(project, work: str, n: int = 30, seed: int = 2026, log=print) -> Path:
    """Lấy ngẫu nhiên n cặp cho MỖI thành viên ra Excel để đánh giá tay (Đúng/Sai, nhãn lỗi §7)."""
    pairs = final_pairs(project, work)[0]
    rng = random.Random(seed)
    rows = [["STT", "Mã cặp", "Thành viên", "Kiểu", "Cờ", "Hán", "Việt", "Đúng/Sai", "Nhãn lỗi", "Ghi chú"]]
    for m in sorted({p["member"] for p in pairs}):
        mine = [p for p in pairs if p["member"] == m]
        for p in sorted(rng.sample(mine, min(n, len(mine))), key=lambda p: p["pid"]):
            rows.append([len(rows), p["pid"], m, p["kieu"], " ".join(p["co"]), p["han"], p["viet"], "", "", ""])
    out = project.scratch(work) / "mau" / f"{work}_mau_{n}.xlsx"
    write_xlsx(out, [Sheet("MAU", rows, [5, 14, 10, 6, 14, 50, 70, 9, 12, 30], wrap=True)])
    log(f"  Mẫu {work}: {len(rows) - 1} cặp → work/{work}/mau/{out.name} "
        "(điền cột Đúng/Sai; Nhãn lỗi: OMISSION / ADDITION / MISSING / RANH_GIOI)")
    return out
