"""In gọn các cặp #a–#b (mỗi cặp 2 dòng, không mã câu) để đọc nhanh khối lớn.
    python dumpc.py HCB_01 1 150
Cặp không phải 1-1 có ghi kiểu ghép; cờ máy ghi trong {}.
"""
import sys

from hvalign import review
from hvalign.config import load_project

w, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
pairs = review.final_pairs(load_project(), w)[0]
for i in range(a, min(b, len(pairs)) + 1):
    p = pairs[i - 1]
    k = "" if p["kieu"] == "1-1" else f" [{p['kieu']}]"
    fl = ",".join(p.get("co") or [])
    print(f"#{i}{k}{' {' + fl + '}' if fl else ''} {p['han']}")
    print(f"   {p['viet']}")
