"""Bước 4 – trích text thô có mã truy vết vào <MA>/02_ocr_tho/{han,viet}/<quyển>.tsv.

Khuôn tệp (giống nhau cho mọi định dạng nguồn):
    # dòng chú thích: nguồn, định dạng nhận dạng được, mã hóa, sha256
    id <TAB> loai <TAB> noi_dung
loai: h1…h6 (đề mục), para (đoạn), item (khoản *), indent (dòng thụt ':'), title (dòng tiêu đề in đậm).
"""
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

from . import __version__
from .readers import load_document
from .sources import plan_sources
from .textutil import CJK_RUN_RE, sha256_file, strip_markers, vol_label, write_tsv

RAW_HEADER = ["id", "loai", "noi_dung"]


def read_raw(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        cols = line.split("\t")
        if cols[:3] == RAW_HEADER:
            continue
        rows.append({"id": cols[0], "kind": cols[1], "text": cols[2] if len(cols) > 2 else ""})
    return rows


def _harvest(text: str, bid: str, acc: dict) -> None:
    """Thu cặp 'Phúc Khang An (福康安)' / 'Giao Chỉ 交趾': số âm tiết đứng ngay trước = số chữ Hán."""
    for m in CJK_RUN_RE.finditer(text):
        han = m.group(0)
        n = len(han)
        if n > 8:
            continue
        pre = text[:m.start()].rstrip()
        if pre.endswith("("):
            if not text[m.end():].lstrip().startswith(")"):
                continue
            pre = pre[:-1].rstrip()
        words = pre.split(" ")[-n:]
        if len(words) != n or not all(re.fullmatch(r"[A-Za-zÀ-ỹĐđ]+", w) for w in words):
            continue
        if not words[0][0].isupper():
            continue
        viet = " ".join(words)
        rec = acc.setdefault((viet, han), {"n": 0, "id": bid})
        rec["n"] += 1


def run(project, work: str, log=print) -> dict:
    wcfg = project.work_cfg(work)
    wdir = project.work_dir(work)
    scratch = project.scratch(work)
    vols, warnings = plan_sources(project, work, wcfg)
    for w in warnings:
        log(f"  ! {w}")
    out_dir = wdir / "02_ocr_tho"
    force = wcfg.get("dinh_dang_nguon") or {}
    log_rows, pairs, summary = [], {}, Counter()
    for vs in vols:
        vl = vol_label(vs.volume)
        for lang in ("han", "viet"):
            paths = getattr(vs, lang)
            if not paths:
                continue
            comments, rows = [], []
            sec, par, last_heading = 0, 0, None
            for path in paths:
                doc = load_document(path, lang, force.get(lang))
                rel = path.relative_to(wdir) if path.is_relative_to(wdir) else path
                sha = sha256_file(path)
                comments.append(f"# nguon: {rel.as_posix()} | dinh_dang: {doc.fmt} ({doc.fmt_reason})"
                                f" | ma_hoa: {doc.encoding} | sha256: {sha}")
                for b in doc.blocks:
                    if b.kind == "heading":
                        if b.meta.get("sillok") and b.text == last_heading:
                            continue  # nhiều bài sillok cùng ngày → cùng một mục
                        sec += 1
                        par = 0
                        last_heading = b.text
                        rows.append((f"{work}/{vl}/{lang}/s{sec:02d}/h", f"h{b.level}", b.text))
                    else:
                        par += 1
                        rows.append((f"{work}/{vl}/{lang}/s{sec:02d}/p{par:03d}", b.kind, b.text))
                        if lang == "viet":
                            _harvest(strip_markers(b.text), rows[-1][0], pairs)
                tpl = ", ".join(f"{k[4:]}×{v}" for k, v in sorted(doc.stats.items()) if k.startswith("tpl:"))
                other = ", ".join(f"{k}×{v}" for k, v in sorted(doc.stats.items()) if not k.startswith("tpl:"))
                log_rows.append((vs.volume, lang, vs.member, rel.as_posix(), doc.fmt, doc.fmt_reason,
                                 doc.encoding, len(doc.blocks), tpl, other, "; ".join(doc.warnings)))
                summary[f"{lang}:{doc.fmt}"] += 1
            header = [f"# hvalign {__version__} | {work} quyển {vs.volume} | {lang} | thành viên: {vs.member}"]
            path_out = out_dir / lang / f"{vl}.tsv"
            path_out.parent.mkdir(parents=True, exist_ok=True)
            with open(path_out, "w", encoding="utf-8", newline="\n") as f:
                f.write("\n".join(header + comments) + "\n")
                f.write("\t".join(RAW_HEADER) + "\n")
                for r in rows:
                    f.write("\t".join(x.replace("\t", " ") for x in r) + "\n")
            residual = sum(1 for r in rows if re.search(r"\{\{|\}\}|\[\[|<ref|</?[a-zA-Z]+[ >/]", r[2]))
            if residual:
                log(f"  ! {path_out.name} ({lang}): {residual} dòng còn markup chưa xử lý")
            summary["files"] += 1
            summary["rows"] += len(rows)

    write_tsv(scratch / "extract_log.tsv",
              ["quyen", "ngon_ngu", "thanh_vien", "tep", "dinh_dang", "ly_do_nhan_dang", "ma_hoa",
               "so_khoi", "template", "khac", "canh_bao"], log_rows)
    write_tsv(scratch / "hv_pairs.tsv", ["viet", "han", "so_lan", "vi_du_id"],
              sorted(((v, h, r["n"], r["id"]) for (v, h), r in pairs.items()), key=lambda x: -x[2]))
    fmts = ", ".join(f"{k}×{v}" for k, v in sorted(summary.items()) if ":" in k)
    log(f"  B4 {work}: {len(vols)} quyển, {summary['files']} tệp text thô, {summary['rows']} dòng; "
        f"định dạng nguồn: {fmts}; {len(pairs)} cặp tên Việt–Hán thu hoạch")
    return {"volumes": len(vols), "rows": summary["rows"], "pairs": len(pairs)}
