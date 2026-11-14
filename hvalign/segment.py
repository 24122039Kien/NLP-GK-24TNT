"""Bước 6 – tách câu, đánh dấu loại ranh giới sau mỗi đơn vị.

Nguyên tắc (Guideline Bước 6): tách MỊN rồi để Bước 7 GỘP lại khi cần.
  hard : ranh giới câu rõ ràng (。！？ / . ? ! trước chữ hoa) – gộp qua đây bị phạt
  soft : ranh giới phụ (；, ：, dấu câu nằm trong 「…」/“…”, 。 của sillok) – gộp qua đây không bị phạt
  end  : hết đoạn
Đầu vào : work/<MA>/clean.jsonl   Đầu ra : work/<MA>/segments.jsonl
"""
from __future__ import annotations

import re
from collections import Counter

from .textutil import read_jsonl, write_jsonl

_HAN_HARD, _HAN_SOFT = "。！？", "；"
_HAN_OPEN, _HAN_CLOSE = "「『“", "」』”"
_TRAIL = "」』”’）》〉"


def split_han(text: str, soft_period: bool = False, quote_soft: bool = True) -> list[tuple[str, str]]:
    units, buf, depth, i, n = [], [], 0, 0, len(text)
    while i < n:
        c = text[i]
        buf.append(c)
        if c in _HAN_OPEN:
            depth += 1
        elif c in _HAN_CLOSE and depth:
            depth -= 1
        if c in _HAN_HARD or c in _HAN_SOFT:
            while i + 1 < n and text[i + 1] in _TRAIL:  # dấu đóng ngoặc dính vào câu trước
                i += 1
                buf.append(text[i])
                if text[i] in _HAN_CLOSE and depth:
                    depth -= 1
            soft = c in _HAN_SOFT or (soft_period and c == "。") or (quote_soft and depth > 0)
            units.append(["".join(buf), "soft" if soft else "hard"])
            buf = []
        i += 1
    if "".join(buf).strip():
        units.append(["".join(buf), "end"])
    return _finish(units)


_VI_END = re.compile(r"[.?!…]+[”\"’')\]]*(?=\s)")
_VI_SOFT = re.compile(r"[;:](?=\s)")
_VI_NEXT_START = re.compile(r"\s+[“\"‘(\[]?[A-ZÀ-ỸĐ0-9]")
_ABBR = re.compile(r"(?:\b(?:Tp|TP|St|Th|Q)\.)$")  # viết tắt thường đứng ngay trước tên riêng


def split_viet(text: str, quote_soft: bool = True) -> list[tuple[str, str]]:
    cuts: list[tuple[int, str]] = []
    for m in _VI_END.finditer(text):
        end = m.end()
        if not _VI_NEXT_START.match(text, end):
            continue  # sau dấu chấm là chữ thường → không phải hết câu
        if _ABBR.search(text[:m.start() + 1]) and not text[m.start():end].startswith("?"):
            continue
        cuts.append((end, "hard"))
    for m in _VI_SOFT.finditer(text):
        cuts.append((m.end(), "soft"))
    cuts.sort()
    # dấu câu nằm trong ngoặc kép → ranh giới mềm
    units, start = [], 0
    for pos, kind in cuts:
        seg = text[start:pos]
        if not seg.strip():
            continue
        if quote_soft and kind == "hard" and _inside_quote(text, pos):
            kind = "soft"
        units.append([seg, kind])
        start = pos
    if text[start:].strip():
        units.append([text[start:], "end"])
    return _finish(units)


def _inside_quote(text: str, pos: int) -> bool:
    before = text[:pos]
    curly = before.count("“") - before.count("”")
    straight = before.count('"') % 2
    return curly > 0 or straight == 1


def _finish(units: list[list[str]]) -> list[tuple[str, str]]:
    out = [(u.strip(), k) for u, k in units if u.strip()]
    if out:
        out[-1] = (out[-1][0], "end")
    return out


def run(project, work: str, log=print) -> dict:
    wcfg = project.work_cfg(work)
    tc = wcfg.get("tach_cau", {})
    scratch = project.scratch(work)
    rows = read_jsonl(scratch / "clean.jsonl")
    out, stats = [], Counter()
    for r in rows:
        if r["kind"].startswith("h"):
            continue
        if r["lang"] == "han":
            units = split_han(r["text"], tc.get("han_cham_la_ranh_gioi_mem", False),
                              tc.get("trong_ngoac_kep_la_mem", True))
        else:
            units = split_viet(r["text"], tc.get("trong_ngoac_kep_la_mem", True))
        for k, (t, b) in enumerate(units, start=1):
            out.append({"id": f"{r['id']}/u{k:02d}", "block": r["id"], "vol": r["vol"], "lang": r["lang"],
                        "member": r["member"], "sec": r["sec"], "text": t, "end": b,
                        "flags": r.get("flags", [])})
            stats[(r["member"], r["lang"], "unit")] += 1
            sillok_period = (r["lang"] == "han" and tc.get("han_cham_la_ranh_gioi_mem")
                             and t.rstrip(_TRAIL).endswith("。"))
            if b in ("hard", "end") or sillok_period:
                stats[(r["member"], r["lang"], "sent")] += 1
    write_jsonl(scratch / "segments.jsonl", out)
    members = sorted({m for m, _, _ in stats})
    parts = []
    for m in members:
        h, v = stats[(m, "han", "sent")], stats[(m, "viet", "sent")]
        parts.append(f"{m}: câu Hán {h}, câu Việt {v} (đơn vị mịn {stats[(m, 'han', 'unit')]}/"
                     f"{stats[(m, 'viet', 'unit')]})")
    log(f"  B6 {work}: " + "; ".join(parts))
    return {m: min(stats[(m, "han", "sent")], stats[(m, "viet", "sent")]) for m in members}
