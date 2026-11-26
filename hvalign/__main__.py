"""Điểm vào dòng lệnh:  python -m hvalign <lệnh> [--work HCB_01 HCB_04 …] [--ban-giao]

Lệnh:
  inventory  kiểm kê nguồn (đủ cặp, SHA-256, trùng bài)
  extract    B4: đọc nguồn (.wikitext/.txt/.html), chuẩn hóa → work/<MA>/02_ocr_tho/ (không nộp)
  clean      B5: làm sạch → 03_text_sach/ + log
  segment    B6: tách câu
  align      B7: dóng hàng 3 tầng
  export     xuất TSV + XLSX (mặc định vào work/<MA>/xuat; --ban-giao: vào 04_dong_hang) + sổ hiệu đính
  validate   kiểm định TSV/XLSX theo Guideline
  report     báo cáo tự sinh work/<MA>/bao_cao.md
  run        chạy tất cả: extract → clean → segment → align → export → validate → report
  status     tóm tắt trạng thái từng tác phẩm
  mau        lấy ngẫu nhiên N cặp mỗi thành viên ra Excel để chấm Đúng/Sai (--so-cap 30)
  app        mở giao diện web (chạy, hiệu đính, chấm mẫu, bàn giao) tại http://127.0.0.1:8765
"""
from __future__ import annotations

import argparse
import sys
import time

from . import __version__, align, clean, export, extract, inventory, report, review, segment
from .config import load_project
from .textutil import SourceReadError

STEPS = ["extract", "clean", "segment", "align", "export", "validate", "report"]


def status(project, works):
    print(f"  {'Mã':7} {'B4 thô':>7} {'han.txt':>8} {'viet.txt':>8} {'cặp':>6}  theo thành viên")
    for w in works:
        wd, sc = project.work_dir(w), project.scratch(w)
        raw = len(list(project.raw_dir(w).glob("*/*.tsv")))
        lines = []
        for lang in ("han", "viet"):
            p = wd / "03_text_sach" / f"{lang}.txt"
            lines.append(sum(1 for _ in open(p, encoding="utf-8")) if p.exists() else 0)
        pairs = review.final_pairs(project, w)[0]
        mem = {}
        for p in pairs:
            mem[p["member"]] = mem.get(p["member"], 0) + 1
        print(f"  {w:7} {raw:>7} {lines[0]:>8} {lines[1]:>8} {len(pairs):>6}  "
              + ", ".join(f"{k} {v}" for k, v in sorted(mem.items())))
    totals = {}
    for w in works:
        for p in review.final_pairs(project, w)[0]:
            totals[p["member"]] = totals.get(p["member"], 0) + 1
    if totals:
        print("  Tổng theo thành viên: " + ", ".join(f"{k} {v} cặp" for k, v in sorted(totals.items()))
              + "  (mục tiêu ≥ 2.000 cặp/người, sau hiệu đính)")


def run_steps(project, w: str, steps: list[str], deliver: bool, log=print) -> int:
    validation = None
    failed = 0
    for st in steps:
        if st == "extract":
            extract.run(project, w, log=log)
        elif st == "clean":
            clean.run(project, w, log=log)
        elif st == "segment":
            segment.run(project, w, log=log)
        elif st == "align":
            align.run(project, w, log=log)
        elif st == "export":
            export.run(project, w, deliver=deliver, log=log)
        elif st == "validate":
            validation = export.validate(project, w, deliver=deliver, log=log)
            failed += bool(validation[0])
        elif st == "report":
            report.run(project, w, validation, log=log)
    return failed


def friendly_error(e: Exception, w: str) -> str | None:
    """Câu báo lỗi dễ hiểu cho các lỗi người dùng hay gặp; None nếu là lỗi lạ (lỗi chương trình)."""
    if isinstance(e, SourceReadError):
        return f"✗ {e}"
    if isinstance(e, PermissionError):
        return (f"✗ Không ghi được tệp ({e.filename or e}): tệp đang mở, thường là trong Excel. "
                "Đóng tệp rồi chạy lại.")
    if isinstance(e, FileNotFoundError):
        return (f"✗ Thiếu tệp {e.filename}. "
                f"Hãy chạy các bước trước đó, hoặc dùng: python -m hvalign run --work {w}")
    return None


def main(argv=None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    ap = argparse.ArgumentParser(prog="hvalign", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("lenh", choices=["inventory", "status", "run", "mau", "app"] + STEPS)
    ap.add_argument("--work", nargs="+", help="mã tác phẩm (mặc định: mọi tác phẩm có trên máy)")
    ap.add_argument("--ban-giao", action="store_true", help="xuất vào <MA>/04_dong_hang (thư mục nộp)")
    ap.add_argument("--so-cap", type=int, default=30, help="số cặp mỗi thành viên cho lệnh mau")
    ap.add_argument("--cong", type=int, default=8765, help="cổng cho lệnh app")
    ap.add_argument("--khong-mo-trinh-duyet", action="store_true", help="lệnh app: không tự mở trình duyệt")
    ap.add_argument("--version", action="version", version=f"hvalign {__version__}")
    a = ap.parse_args(argv)
    project = load_project()
    if a.lenh == "app":
        from . import app
        return app.serve(project, a.cong, not a.khong_mo_trinh_duyet)
    works = a.work or project.works()
    if a.lenh == "inventory":
        return 1 if inventory.run(project, works) else 0
    if a.lenh == "mau":
        for w in works:
            export.sample(project, w, a.so_cap)
        return 0
    if a.lenh == "status":
        status(project, works)
        return 0
    steps = STEPS if a.lenh == "run" else [a.lenh]
    failed = 0
    t0 = time.time()
    for w in works:
        print(f"== {w}")
        try:
            failed += run_steps(project, w, steps, a.ban_giao)
        except (SourceReadError, OSError) as e:
            msg = friendly_error(e, w)
            if msg is None:
                raise
            print(f"  {msg}")
            failed += 1
    if a.lenh == "run":
        print(f"\nXong {len(works)} tác phẩm trong {time.time() - t0:.1f} giây.")
        status(project, works)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
