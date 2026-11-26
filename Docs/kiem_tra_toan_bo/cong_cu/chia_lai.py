"""Chia lại ranh giới cho một khúc cặp liền nhau mà máy dóng lệch (sửa tay = human in the loop).

    python chia_lai.py HCB_14 Huy 2 26 khuc.txt [--thu]

khuc.txt: mỗi cặp đúng là 2 dòng "H: <Hán>" và "V: <Việt>"; dòng trống và dòng '#' bỏ qua.
  Hoặc dạng gọn: "HB: <toàn bộ Hán của khúc, '|' ở ranh giới cặp>" và (tùy chọn) "VB: <Việt, '|' ở ranh giới>";
  thiếu VB thì vế Việt giữ nguyên từng cặp cũ (khi đó số đoạn HB phải bằng số cặp cũ).
Kiểm tra bắt buộc trước khi ghi: nối mọi vế Hán (và mọi vế Việt) của khúc mới phải GIỐNG HỆT khúc cũ
(bỏ qua khoảng trắng), tức là chỉ dời ranh giới, không thêm/bớt/đổi chữ nào.
Số cặp mới ≤ số cặp cũ: ghi `sua` cho từng cặp mới; các cặp cũ thừa ở cuối khúc ghi `sai` (nội dung đã dời lên).
Cặp nào không đổi thì không ghi. --thu: chỉ kiểm tra, không ghi.
--khong-ghep: cho phép khúc mới chứa thêm các câu mà máy để "không ghép" (work/<MA>/khong_ghep.tsv) – chỉ đúng
những câu đó, mỗi câu tối đa một lần; ngoài ra vẫn phải giữ nguyên chữ.
"""
import re
import sys

from hvalign import review
from hvalign.config import load_project

w, who, a, b, path = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
dry = "--thu" in sys.argv
P = load_project()
nows = lambda s: re.sub(r"\s+", "", s)

new, cur = [], {}
for line in open(path, encoding="utf-8"):
    line = line.rstrip("\n")
    if not line.strip() or line.lstrip().startswith("#"):
        continue
    if line.startswith(("HB:", "VB:")):
        continue
    tag, _, text = line.partition(":")
    tag = tag.strip()
    if tag not in ("H", "V"):
        sys.exit(f"dòng không hợp lệ: {line[:60]}")
    cur[tag] = text.strip()
    if tag == "V":
        if "H" not in cur:
            sys.exit(f"thiếu dòng H trước: {line[:60]}")
        new.append((cur["H"], cur["V"]))
        cur = {}

final = review.final_pairs(P, w)[0]
old = final[a - 1:b]
bars = {}
for line in open(path, encoding="utf-8"):
    if line.startswith(("HB:", "VB:")):
        bars[line[:2]] = [x.strip() for x in line[3:].strip().split("|")]
if bars:
    hs = bars.get("HB") or []
    vs = bars.get("VB") or [p["viet"] for p in old]
    if len(hs) != len(vs):
        sys.exit(f"✗ số đoạn Hán ({len(hs)}) khác số đoạn Việt ({len(vs)})")
    new = list(zip(hs, vs))
oh, ov = nows("".join(p["han"] for p in old)), nows("".join(p["viet"] for p in old))
nh, nv = nows("".join(h for h, _ in new)), nows("".join(v for _, v in new))
if "--khong-ghep" in sys.argv:
    import csv
    kg = csv.DictReader(open(P.root / "work" / w / "khong_ghep.tsv", encoding="utf-8"), delimiter="	")
    for r in kg:  # câu máy để "không ghép" mà khúc mới có đưa vào: bỏ ra (một lần) rồi mới so với bản cũ
        t = nows(r["noi_dung"])
        if r["ngon_ngu"] == "viet" and t and t in nv and t not in ov:
            nv = nv.replace(t, "", 1)
            print(f"  + thêm câu Việt không ghép: {r['noi_dung'][:60]}")
        elif r["ngon_ngu"] == "han" and t and t in nh and t not in oh:
            nh = nh.replace(t, "", 1)
            print(f"  + thêm câu Hán không ghép: {r['noi_dung'][:60]}")
ok = True
for name, x, y in (("Hán", oh, nh), ("Việt", ov, nv)):
    if x != y:
        ok = False
        i = next((k for k in range(min(len(x), len(y))) if x[k] != y[k]), min(len(x), len(y)))
        print(f"✗ vế {name} khác bản gốc tại ký tự {i}: gốc «{x[max(0, i - 15):i + 25]}» / mới «{y[max(0, i - 15):i + 25]}»")
if len(new) > len(old):
    ok = False
    print(f"✗ {len(new)} cặp mới > {len(old)} cặp cũ (không tách thêm cặp được, chỉ dời ranh giới hoặc gộp)")
if any(not h or not v for h, v in new):
    ok = False
    print("✗ có cặp rỗng một vế")
if not ok:
    sys.exit(1)
print(f"✓ khúc #{a}–#{b}: {len(old)} cặp → {len(new)} cặp, chữ Hán/Việt giữ nguyên")
if dry:
    sys.exit(0)

# Mỗi khóa cặp chỉ giữ MỘT quyết định (mới nhất), nên không dùng gop + sua cùng lúc:
# cặp k < len(new) nhận nội dung mới bằng `sua`; các cặp cũ thừa ở cuối khúc (nội dung đã dời vào cặp trước) → `sai`.
final = review.final_pairs(P, w)[0]
n = 0
for k, fp in enumerate(final[a - 1:b]):
    if k < len(new):
        h, v = new[k]
        if fp["han"] == h and fp["viet"] == v:
            continue
        review.save_decision(P, w, who, fp["khoa"], "sua", han=h, viet=v)
    else:
        review.save_decision(P, w, who, fp["khoa"], "sai", note="nội dung đã dời vào cặp trước (chia lại ranh giới)")
    n += 1
res, st = review.final_pairs(P, w)
print(f"đã ghi {n} quyết định; {w}: {len(res)} cặp; thống kê {st}")
