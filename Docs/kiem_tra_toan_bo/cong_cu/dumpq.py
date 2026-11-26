"""In các cặp của một (hoặc vài) quyển, kèm câu không ghép của quyển đó, để đọc kiểm tra.
    python dumpq.py HCB_14 1358 [1421 ...]
Số #n là thứ tự dòng trong TSV nộp (giống dump.py / hd.py).
"""
import csv
import sys

from hvalign import review
from hvalign.config import load_project
from hvalign.notes import notes_for

w, qs = sys.argv[1], sys.argv[2:]
P = load_project()
pairs = review.final_pairs(P, w)[0]
notes = notes_for(P, w, pairs)


def vol(p):
    ids = p["han_ids"] or p["viet_ids"]
    return ids[0].split("/")[1][1:] if ids else "?"


for q in qs:
    sel = [(i, p, n) for i, (p, n) in enumerate(zip(pairs, notes), start=1) if vol(p) == q]
    print(f"===== {w} Q{q}: {len(sel)} cặp (#{sel[0][0] if sel else '-'}–#{sel[-1][0] if sel else '-'})")
    for i, p, n in sel:
        hid = "/".join(p["han_ids"][0].split("/")[3:]) if p["han_ids"] else "-"
        vid = "/".join(p["viet_ids"][0].split("/")[3:]) if p["viet_ids"] else "-"
        flags = ",".join(p.get("co") or [])
        print(f"#{i} [{p['kieu']}] H:{hid} V:{vid}{' {' + flags + '}' if flags else ''}")
        print(f"  H: {p['han']}")
        print(f"  V: {p['viet']}")
        if n:
            print(f"  N: {n}")
    kg = P.root / "work" / w / "khong_ghep.tsv"
    if kg.exists():
        rows = [r for r in csv.DictReader(kg.open(encoding="utf-8"), delimiter="\t") if f"/q{q}/" in r["id"]]
        if rows:
            print(f"  --- {len(rows)} câu không ghép:")
            for r in rows:
                print(f"  ✗ {r['ngon_ngu']} {'/'.join(r['id'].split('/')[3:])}: {r['noi_dung']}")
