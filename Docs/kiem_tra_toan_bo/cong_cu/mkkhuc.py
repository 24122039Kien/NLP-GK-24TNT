"""Dựng tệp khúc HB/VB từ các cặp #a–#b hiện tại và các mốc mở đầu từng cặp mới.
    python Docs/kiem_tra_toan_bo/cong_cu/mkkhuc.py HCB_01 a b out.txt "chú thích" --h "mốc Hán 2" "mốc Hán 3" ... --v "mốc Việt 2" ...
Mốc = đoạn chữ mở đầu cặp mới thứ 2, 3, ... (tìm lần lượt từ trái sang)."""
import sys
from hvalign import review
from hvalign.config import load_project
w, a, b, out, note = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5]
rest = sys.argv[6:]; hi, vi = rest.index("--h"), rest.index("--v")
hm, vm = rest[hi + 1:vi], rest[vi + 1:]
assert len(hm) == len(vm), "số mốc Hán và Việt phải bằng nhau"
P = review.final_pairs(load_project(), w)[0][a - 1:b]
def cut(text, marks):
    parts, pos = [], 0
    for m in marks:
        j = text.find(m, pos + 1)
        assert j > 0, f"không thấy mốc: {m}"
        parts.append(text[pos:j].strip()); pos = j
    parts.append(text[pos:].strip()); return parts
H = cut(" ".join(p["han"] for p in P).replace(" ", ""), hm)
V = cut(" ".join(p["viet"] for p in P), vm)
with open(out, "w", encoding="utf-8", newline="\n") as f:
    f.write(f"# {note}\nHB: {'|'.join(H)}\nVB: {'|'.join(V)}\n")
for h, v in zip(H, V): print("H:", h, "\nV:", v)
