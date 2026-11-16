"""Ghi chú tự động cho từng cặp – để người không phải tự phân tích.

Theo câu trả lời của giảng viên (Lab/GK/QA, 16/11/2026):
  * chỉ dóng hàng phần có song ngữ; phần nào không có bản dịch thì không cần dóng;
  * bản dịch rút gọn vẫn dùng được nếu xác định được nội dung tương ứng, nhưng phải
    đánh dấu rõ cặp bị lược bỏ / dịch rút gọn và nêu phần bị lược, câu hoàn toàn không
    được dịch (nếu có) – bằng cột "Ghi chú" trong file .xlsx.

Máy tự viết ghi chú dựa trên:
  * độ dài: số âm tiết Việt so với mức thường gặp của chính tác phẩm (âm tiết / chữ Hán);
  * mốc: tên riêng, can chi chỉ có ở vế Hán (bản Việt không nhắc tới);
  * chú thích trong ngoặc của dịch giả;
  * câu không ghép được (work/<MA>/khong_ghep.tsv) → ghi vào cặp đứng ngay trước nó.
"""
from __future__ import annotations

import bisect
import re
from pathlib import Path

from .anchors import CANCHI, AnchorIndex
from .textutil import cjk_count, viet_syllables

NGAN = 0.5          # vế Việt < 50% độ dài thường gặp → dịch rút gọn
NGAN_VUNG_RUT_GON = 0.7  # trong vùng đã biết là dịch rút gọn (cờ rut_gon) thì ngưỡng nới hơn
DAI = 2.0           # vế Việt > 2 lần độ dài thường gặp → có thêm diễn giải
_PAREN = re.compile(r"\([^()]{40,}\)")


def _short(s: str, n: int = 60) -> str:
    s = s.strip()
    return s if len(s) <= n else s[:n].rstrip() + "…"


def ratio_base(pairs: list[dict]) -> float:
    h = sum(cjk_count(p["han"]) for p in pairs)
    v = sum(viet_syllables(p["viet"]) for p in pairs)
    return v / h if h else 1.0


def _names(idx: AnchorIndex | None, han: str, viet: str) -> list[str]:
    if idx is None:
        return []
    out = []
    for k in sorted(idx.han_keys(han) - idx.viet_keys(viet)):
        h = k.split(":", 1)[1]
        v = CANCHI.get(h) or ", ".join(sorted(idx.han2viet.get(h, [])))
        out.append(f"{h} ({v.title()})" if v else h)
    return out


def pair_note(p: dict, c: float, idx: AnchorIndex | None = None) -> str:
    han, viet = p["han"], p["viet"]
    h = max(cjk_count(han), 1)
    r = viet_syllables(viet) / (c * h)
    flags = set(p.get("co_may", p.get("co", [])))
    parts = []
    if h >= 8 and (r < NGAN or ("rut_gon" in flags and r < NGAN_VUNG_RUT_GON)):
        s = f"Dịch rút gọn: vế Việt chỉ dài khoảng {round(r * 100)}% mức thường gặp"
        names = _names(idx, han, viet)
        if names:
            s += "; bản Việt không nhắc tới: " + ", ".join(names[:6])
        parts.append(s)
    elif r > DAI and viet_syllables(viet) >= 15:
        parts.append(f"Vế Việt dài gấp khoảng {r:.1f} lần mức thường gặp: có thể có diễn giải "
                     "hoặc nội dung dịch giả thêm vào")
    m = _PAREN.search(viet)
    if m:
        parts.append(f"Vế Việt có chú thích của dịch giả: «{_short(m.group(0), 50)}»")
    return "; ".join(parts)


def _unpaired(path: Path) -> list[tuple[str, str, str]]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").splitlines()[1:]:
        cols = line.split("\t")
        if len(cols) >= 4:
            out.append((cols[0], cols[1], cols[3]))
    return out


def notes_for(project, work: str, pairs: list[dict], idx: AnchorIndex | None = None) -> list[str]:
    """Ghi chú cho từng cặp (cùng thứ tự với pairs). Chuỗi rỗng = không có gì cần lưu ý."""
    if idx is None:
        try:
            idx = AnchorIndex.load(project.root)
        except OSError:
            idx = None
    c = ratio_base(pairs)
    notes = [pair_note(p, c, idx) for p in pairs]
    # câu không ghép được → ghi vào cặp đứng ngay trước (mã câu cùng tác phẩm so sánh được theo thứ tự chữ)
    last = {lang: [p[f"{lang}_ids"][-1] for p in pairs] for lang in ("han", "viet")}
    for uid, lang, text in _unpaired(project.scratch(work) / "khong_ghep.tsv"):
        if lang not in last or not pairs:
            continue
        i = max(bisect.bisect_left(last[lang], uid) - 1, 0)
        s = (f"Câu Hán ngay sau không có bản dịch, không đưa vào dữ liệu: «{_short(text)}»" if lang == "han"
             else f"Câu Việt ngay sau không có trong bản Hán, không đưa vào dữ liệu: «{_short(text)}»")
        notes[i] = f"{notes[i]}; {s}" if notes[i] else s
    for i, p in enumerate(pairs):
        if p.get("ghi_chu_hd"):
            notes[i] = f"{notes[i]}; {p['ghi_chu_hd']}" if notes[i] else p["ghi_chu_hd"]
    return notes
