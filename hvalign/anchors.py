"""Mốc dóng hàng: những thứ chắc chắn phải xuất hiện ở CẢ HAI vế của một cặp đúng.

  * can chi   : 丙申 ↔ "Bính Thân" (chuẩn hóa hoa/thường, Tỵ/Tị)
  * tên riêng : từ điển chữ Hán → âm Hán Việt thu hoạch ở Bước 4 (work/*/hv_pairs.tsv),
                ví dụ 福康安 ↔ "Phúc Khang An". Có thể bổ sung resources/han_viet_extra.tsv.

Mỗi đơn vị (câu) được gắn một tập khóa mốc ở mỗi vế; khi xét một cặp ứng viên,
khóa có ở cả hai vế là "khớp", khóa chỉ có ở một vế là "lệch".
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

GAN = dict(zip("甲乙丙丁戊己庚辛壬癸", ["giáp", "ất", "bính", "đinh", "mậu", "kỷ", "canh", "tân", "nhâm", "quý"]))
ZHI = dict(zip("子丑寅卯辰巳午未申酉戌亥",
               ["tý", "sửu", "dần", "mão", "thìn", "tị", "ngọ", "mùi", "thân", "dậu", "tuất", "hợi"]))
# 60 cặp hợp lệ (can và chi cùng tính chẵn lẻ)
CANCHI = {g + z: f"{GAN[g]} {ZHI[z]}" for i, g in enumerate(GAN) for j, z in enumerate(ZHI) if i % 2 == j % 2}
_CANCHI_RE = re.compile(f"[{''.join(GAN)}][{''.join(ZHI)}]")


def norm_viet(s: str) -> str:
    s = unicodedata.normalize("NFC", s.lower())
    s = s.replace("tỵ", "tị").replace("kỉ", "kỷ").replace("qúy", "quý")
    return " ".join(re.findall(r"[0-9a-zà-ỹđ]+", s))


class AnchorIndex:
    def __init__(self, pairs: dict[str, set[str]]):
        # chỉ dùng tên ≥ 2 chữ để tránh trùng ngẫu nhiên (帝 ↔ "đế" xuất hiện khắp nơi)
        self.han2viet = {h: {norm_viet(v) for v in vs} for h, vs in pairs.items() if len(h) >= 2}
        self.viet2han: dict[str, set[str]] = {}
        for h, vs in self.han2viet.items():
            for v in vs:
                self.viet2han.setdefault(v, set()).add(h)
        for h, v in CANCHI.items():
            self.viet2han.setdefault(v, set()).add(h)
        self.max_han = max((len(h) for h in self.han2viet), default=2)
        self.max_syl = max((len(v.split()) for v in self.viet2han), default=2)

    @classmethod
    def load(cls, root: Path) -> "AnchorIndex":
        """Thu cặp tên Việt–Hán từ text thô bản Việt của MỌI tác phẩm trong repo (<MA_DE_TAI>_HCB_xx/02_ocr_tho).

        Không đọc work/*/hv_pairs.tsv nữa: thư mục work/ chỉ có những tác phẩm đã chạy trên máy đó, nên trước
        đây mỗi máy ra kết quả dóng hơi khác nhau. Text thô nằm trong git, nên mọi máy dùng cùng một bộ mốc.
        """
        from .extract import _harvest  # tránh vòng import lúc nạp module
        from .textutil import strip_markers
        acc: dict = {}
        for f in sorted(root.glob("*_HCB_*/02_ocr_tho/viet/*.tsv")):
            for line in f.read_text(encoding="utf-8").splitlines():
                cols = line.split("\t")
                if line.startswith("#") or len(cols) < 3 or cols[0] == "id":
                    continue
                _harvest(strip_markers(cols[2]), cols[0], acc)
        pairs: dict[str, set[str]] = {}
        for (viet, han) in acc:
            pairs.setdefault(han, set()).add(viet)
        extra = root / "resources" / "han_viet_extra.tsv"
        if extra.exists():
            for line in extra.read_text(encoding="utf-8").splitlines()[1:]:
                cols = line.split("\t")
                if len(cols) >= 2 and not line.startswith("#"):
                    pairs.setdefault(cols[1], set()).add(cols[0])
        return cls(pairs)

    def han_keys(self, text: str) -> frozenset[str]:
        keys = {f"cc:{m.group(0)}" for m in _CANCHI_RE.finditer(text) if m.group(0) in CANCHI}
        n = len(text)
        for i in range(n):
            for L in range(2, min(self.max_han, n - i) + 1):
                if text[i:i + L] in self.han2viet:
                    keys.add(f"nm:{text[i:i + L]}")
        return frozenset(keys)

    def viet_keys(self, text: str) -> frozenset[str]:
        toks = norm_viet(text).split()
        keys = set()
        for i in range(len(toks)):
            for L in range(2, min(self.max_syl, len(toks) - i) + 1):
                hs = self.viet2han.get(" ".join(toks[i:i + L]))
                if hs:
                    for h in hs:
                        keys.add(f"cc:{h}" if h in CANCHI and L == 2 and " ".join(toks[i:i + L]) == CANCHI[h]
                                 else f"nm:{h}")
        return frozenset(keys)
