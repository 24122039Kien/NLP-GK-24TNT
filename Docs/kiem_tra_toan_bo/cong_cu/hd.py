"""Ghi quyết định hiệu đính theo SỐ THỨ TỰ cặp cuối cùng (như dump.py in ra).
    python hd.py HCB_05 Kien 59 gop "ghi chú"        gộp cặp 59 với cặp ngay sau
    python hd.py HCB_05 Kien 12 sai "ghi chú"        bỏ cặp 12
    python hd.py HCB_05 Kien 12 dung "ghi chú"       xác nhận đúng (kèm ghi chú viết tay vào cột Ghi chú)
    python hd.py HCB_05 Kien 12 sua "ghi chú" "<Hán>" "<Việt>"
Quyết định gắn với khóa máy (mã câu), dùng review.save_decision của hvalign.
"""
import sys

from hvalign import review
from hvalign.config import load_project

w, who, idx, dec = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
note = sys.argv[5] if len(sys.argv) > 5 else ""
P = load_project()
final = review.final_pairs(P, w)[0]
machine = review.machine_pairs(P, w)
mkeys = [review.key_of(p) for p in machine]
fp = final[idx - 1]
if dec == "gop":
    # cặp máy cuối cùng nằm trong cặp idx (nếu idx đã là cặp gộp thì nối tiếp chuỗi)
    last = max(i for i, p in enumerate(machine) if p["han_ids"] and p["han_ids"][-1] in fp["han_ids"]
               or p["viet_ids"] and p["viet_ids"][-1] in fp["viet_ids"])
    nxt = final[idx]
    assert machine[last + 1]["han_ids"][:1] == nxt["han_ids"][:1] or \
        machine[last + 1]["viet_ids"][:1] == nxt["viet_ids"][:1], "cặp sau không liền kề"
    review.save_decision(P, w, who, mkeys[last], "gop", gop_voi=mkeys[last + 1], note=note)
elif dec == "sua":
    review.save_decision(P, w, who, fp["khoa"], "sua", han=sys.argv[6], viet=sys.argv[7], note=note)
else:
    review.save_decision(P, w, who, fp["khoa"], dec, note=note)
new, st = review.final_pairs(P, w)
print(f"{w}: {len(final)} → {len(new)} cặp; thống kê {st}")
