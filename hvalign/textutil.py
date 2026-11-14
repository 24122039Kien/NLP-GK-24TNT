"""Hàm tiện ích về văn bản: đọc tệp, chuẩn hóa Unicode, đếm chữ Hán / âm tiết Việt."""
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

# Khối chữ Hán: Ext A, URO, chữ tương thích, Ext B trở lên.
CJK_CLASS = "㐀-䶿一-鿿豈-﫿\U00020000-\U0003134f"
CJK_RE = re.compile(f"[{CJK_CLASS}]")
CJK_RUN_RE = re.compile(f"[{CJK_CLASS}]+")
# Dấu câu Hán (toàn khổ) hay gặp trong nguồn.
HAN_PUNCT = "。，、；：？！「」『』（）《》〈〉【】…—·．︰“”‘’"
# Chữ cái Latin có dấu tiếng Việt.
VI_LETTER = "A-Za-zÀ-ɏḀ-ỿ"
VI_TOKEN_RE = re.compile(f"[0-9{VI_LETTER}]+")
LATIN_RE = re.compile(f"[{VI_LETTER}]")

# Ký tự vô hình cần bỏ; khoảng trắng đặc biệt đổi thành dấu cách thường.
_INVISIBLE = dict.fromkeys(map(ord, "﻿​‎‏⁠­"), None)
_SPACES = dict.fromkeys(map(ord, "     \t"), " ")

# Dấu ngoặc dùng để đánh dấu chú thích trong text thô (không xuất hiện trong nguồn).
MK_OPEN, MK_CLOSE = "⟪", "⟫"  # ⟪ ⟫
MARKER_RE = re.compile(f"{MK_OPEN}([^{MK_OPEN}{MK_CLOSE}:]*):([^{MK_OPEN}{MK_CLOSE}]*){MK_CLOSE}")


class SourceReadError(Exception):
    pass


def read_source(path: Path) -> tuple[str, str]:
    """Đọc tệp nguồn; trả về (nội dung, mã hóa). Chỉ nhận UTF-8 / UTF-16 để không đoán sai."""
    raw = Path(path).read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        enc = "utf-8-sig"
    elif raw[:2] in (b"\xff\xfe", b"\xfe\xff"):
        enc = "utf-16"
    else:
        enc = "utf-8"
    try:
        return raw.decode(enc), enc
    except UnicodeDecodeError as e:
        raise SourceReadError(
            f"{Path(path).name}: không phải {enc.upper()} (byte lỗi ở vị trí {e.start}). "
            f"Mở tệp bằng Notepad / VS Code rồi lưu lại với mã hóa UTF-8."
        ) from None


def normalize_text(text: str, nfc: bool) -> str:
    """Chuẩn hóa chung cho mọi định dạng đầu vào.

    - bỏ BOM và ký tự vô hình, đổi CRLF/CR thành LF, khoảng trắng đặc biệt thành dấu cách;
    - NFC chỉ áp cho bản Việt: NFC đổi chữ Hán tương thích (U+F900…) sang chữ thống nhất,
      tức là sửa chữ của nguồn, nên không áp cho bản Hán.
    """
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.translate(_INVISIBLE).translate(_SPACES)
    if nfc:
        text = unicodedata.normalize("NFC", text)
    return text


def cjk_count(s: str) -> int:
    return len(CJK_RE.findall(s))


def viet_syllables(s: str) -> int:
    return len(VI_TOKEN_RE.findall(s))


def cjk_ratio(s: str) -> float:
    letters = cjk_count(s) + len(LATIN_RE.findall(s))
    return cjk_count(s) / letters if letters else 0.0


def strip_markers(s: str, keep_content: bool = False) -> str:
    """Bỏ (hoặc mở) mọi dấu chú thích ⟪loại:nội dung⟫, kể cả lồng nhau."""
    prev = None
    while prev != s:
        prev = s
        s = MARKER_RE.sub((lambda m: m.group(2)) if keep_content else "", s)
    return s


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def vol_label(volume: str) -> str:
    """'2' → 'q002', '1333' → 'q1333', 'A' → 'qA'."""
    v = str(volume).strip()
    return "q" + (v.zfill(3) if v.isdigit() else re.sub(r"[^0-9A-Za-z_-]", "_", v))


def vol_sort_key(volume: str):
    v = str(volume)
    return (0, int(v), "") if v.isdigit() else (1, 0, v)


def write_jsonl(path: Path, rows) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
            n += 1
    return n


def read_jsonl(path: Path) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def tsv_cell(s) -> str:
    return str(s).replace("\t", " ").replace("\n", " ")


def write_tsv(path: Path, header: list[str] | None, rows) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        if header:
            f.write("\t".join(header) + "\n")
        for r in rows:
            f.write("\t".join(tsv_cell(x) for x in r) + "\n")
            n += 1
    return n
