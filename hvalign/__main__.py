"""Điểm vào dòng lệnh:  python -m hvalign <lệnh> [--work HCB_01 HCB_04 …] [--ban-giao]

Lệnh:
  inventory  kiểm kê nguồn (đủ cặp, SHA-256, trùng bài)
  extract    B4: đọc nguồn (.wikitext/.txt/.html), chuẩn hóa → 02_ocr_tho/
  clean      B5: làm sạch → 03_text_sach/ + log
  segment    B6: tách câu
  align      B7: dóng hàng 3 tầng
  export     xuất TSV + XLSX (mặc định vào work/<MA>/xuat; --ban-giao: vào 04_dong_hang) + sổ hiệu đính
  validate   kiểm định TSV/XLSX theo Guideline
  report     báo cáo tự sinh work/<MA>/bao_cao.md
  run        chạy tất cả: extract → clean → segment → align → export → validate → report
  status     tóm tắt trạng thái từng tác phẩm
  mau        lấy ngẫu nhiên N cặp mỗi thành viên ra Excel để chấm Đúng/Sai (--so-cap 30)
"""
from __future__ import annotations

import argparse
import sys
import time

from . import __version__, align, clean, export, extract, inventory, report, segment
from .config import load_project
from .textutil import read_jsonl

STEPS = ["extract", "clean", "segment", "align", "export", "validate", "report"]


def status(project, works):
    print(f"  {'Mã':7} {'B4 thô':>7} {'han.txt':>8} {'viet.txt':>8} {'cặp':>6}  theo thành viên")
    for w in works:
        wd, sc = project.work_dir(w), project.scratch(w)
        raw = len(list((wd / "02_ocr_tho").glob("*/*.tsv")))
        lines = []
        for lang in ("han", "viet"):
            p = wd / "03_text_sach" / f"{lang}.txt"
            lines.append(sum(1 for _ in open(p, encoding="utf-8")) if p.exists() else 0)
        al = sc / "alignment.jsonl"
        pairs = read_jsonl(al) if al.exists() else []
        mem = {}
        for p in pairs:
            mem[p["member"]] = mem.get(p["member"], 0) + 1
        print(f"  {w:7} {raw:>7} {lines[0]:>8} {lines[1]:>8} {len(pairs):>6}  "
              + ", ".join(f"{k} {v}" for k, v in sorted(mem.items())))
    totals = {}
    for w in works:
        al = project.scratch(w) / "alignment.jsonl"
        for p in (read_jsonl(al) if al.exists() else []):
            totals[p["member"]] = totals.get(p["member"], 0) + 1
    if totals:
        print("  Tổng theo thành viên: " + ", ".join(f"{k} {v} cặp" for k, v in sorted(totals.items()))
              + "  (mục tiêu ≥ 2.000 cặp/người, sau hiệu đính)")


def main(argv=None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(prog="hvalign", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("lenh", choices=["inventory", "status", "run", "mau"] + STEPS)
    ap.add_argument("--work", nargs="+", help="mã tác phẩm (mặc định: mọi tác phẩm có trên máy)")
    ap.add_argument("--ban-giao", action="store_true", help="xuất vào <MA>/04_dong_hang (thư mục nộp)")
    ap.add_argument("--so-cap", type=int, default=30, help="số cặp mỗi thành viên cho lệnh mau")
    ap.add_argument("--version", action="version", version=f"hvalign {__version__}")
    a = ap.parse_args(argv)
    project = load_project()
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
        validation = None
        for st in steps:
            if st == "extract":
                extract.run(project, w)
            elif st == "clean":
                clean.run(project, w)
            elif st == "segment":
                segment.run(project, w)
            elif st == "align":
                align.run(project, w)
            elif st == "export":
                export.run(project, w, deliver=a.ban_giao)
            elif st == "validate":
                validation = export.validate(project, w, deliver=a.ban_giao)
                failed += bool(validation[0])
            elif st == "report":
                report.run(project, w, validation)
    if a.lenh == "run":
        print(f"\nXong {len(works)} tác phẩm trong {time.time() - t0:.1f} giây.")
        status(project, works)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
