"""In các cặp sau hiệu đính theo khúc để đọc kiểm tra.
    python dump.py HCB_04 [từ] [đến]      (số thứ tự 1-based, giống thứ tự dòng trong TSV nộp)
"""
import sys

from hvalign import review
from hvalign.config import load_project
from hvalign.notes import notes_for

w = sys.argv[1]
a = int(sys.argv[2]) if len(sys.argv) > 2 else 1
b = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 9
P = load_project()
pairs = review.final_pairs(P, w)[0]
notes = notes_for(P, w, pairs)
print(f"{w}: {len(pairs)} cặp; in {a}–{min(b, len(pairs))}")
for i, (p, n) in enumerate(zip(pairs, notes), start=1):
    if i < a or i > b:
        continue
    hid = p["han_ids"][0].split("/", 1)[1] if p["han_ids"] else "-"
    flags = ",".join(p.get("co") or [])
    print(f"#{i} [{p['kieu']}] {hid}{' {' + flags + '}' if flags else ''}")
    print(f"  H: {p['han']}")
    print(f"  V: {p['viet']}")
    if n:
        print(f"  N: {n}")
