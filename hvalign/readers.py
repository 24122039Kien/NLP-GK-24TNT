"""Bước 4 – đọc nguồn ở mọi định dạng và chuẩn hóa về MỘT dạng: danh sách khối (Block).

Định dạng được nhận dạng theo NỘI DUNG, không chỉ theo đuôi tệp:
  * wikitext : .wikitext/.wiki, hoặc .txt có markup wiki ({{…}}, == … ==, [[…]], <ref>)
  * html     : .html/.htm hoặc nội dung là trang HTML (có bộ đọc riêng cho sillok)
  * plain    : .txt không có markup → mỗi dòng khác rỗng là một đoạn

Sau bước này mọi nguồn đều có cùng dạng: khối có loại (heading/para/item/indent/title),
chú thích được giữ tại chỗ dưới dạng ⟪loại:nội dung⟫ để Bước 5 quyết định xóa hay giữ.
"""
from __future__ import annotations

import html as htmlmod
import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

from .textutil import MK_CLOSE, MK_OPEN, normalize_text, read_source

TEXT_EXTS = {".wikitext": 0, ".wiki": 0, ".mediawiki": 0, ".html": 1, ".htm": 1, ".txt": 2}


@dataclass
class Block:
    kind: str  # heading | para | item | indent | title
    text: str
    level: int = 0
    line: int = 0  # dòng trong tệp nguồn (1-based), để truy vết
    meta: dict = field(default_factory=dict)


@dataclass
class Doc:
    path: Path
    fmt: str
    fmt_reason: str
    encoding: str
    blocks: list[Block]
    meta: dict = field(default_factory=dict)
    stats: Counter = field(default_factory=Counter)
    warnings: list[str] = field(default_factory=list)


# ---------------------------------------------------------------- nhận dạng định dạng

_WIKI_SIGNS = {
    "template": re.compile(r"\{\{[^{}\n]{1,80}?(?:\||\}\})"),
    "heading": re.compile(r"^={1,6}[^=\n]+={1,6}\s*$", re.M),
    "link": re.compile(r"\[\[[^\[\]\n]+\]\]"),
    "ref": re.compile(r"<ref[\s>/]"),
    "entity": re.compile(r"&(?:sect|nbsp|lt|gt|amp);"),
    "magic": re.compile(r"__(?:NO)?TOC__"),
}
_HTML_SIGN = re.compile(r"<!DOCTYPE\s+html|<html[\s>]|<body[\s>]|<p\s+class=", re.I)


def detect_format(text: str, ext: str) -> tuple[str, str]:
    """Trả về (định dạng, lý do)."""
    ext = ext.lower()
    if ext in (".html", ".htm"):
        return "html", f"đuôi {ext}"
    if _HTML_SIGN.search(text[:20000]):
        return "html", "nội dung là trang HTML"
    hits = {k: len(p.findall(text)) for k, p in _WIKI_SIGNS.items()}
    found = ", ".join(f"{k}×{v}" for k, v in hits.items() if v)
    if ext in (".wikitext", ".wiki", ".mediawiki"):
        return "wikitext", f"đuôi {ext}" + (f" ({found})" if found else "")
    strong = hits["template"] + hits["heading"] + hits["link"] + hits["ref"] + hits["magic"]
    if strong:
        return "wikitext", f"đuôi {ext} nhưng có markup wiki ({found})"
    return "plain", f"đuôi {ext}, không có markup wiki"


# ---------------------------------------------------------------- wikitext: template

# Template bỏ hẳn (đầu đề, giấy phép, điều hướng, bố cục).
_DROP = {
    "header", "header2", "footer", "đầu đề", "đầu đề biên dịch", "giấy phép dịch",
    "pd-old", "gfdl", "cc-by-sa-4.0", "cc-by-sa-3.0", "clr", "clear", "vtext2start",
    "vtext2end", "smallrefs", "reflist", "references", "chú thích cuối trang",
    "anchor", "defaultsort", "toc", "notoc", "textquality", "process", "pd-china",
}
_DROP_RE = re.compile(r"作品$|^pd-|^cc-|^license", re.I)
_HEADER_TPL = {"header", "header2", "đầu đề", "đầu đề biên dịch"}
# Template giữ chữ của tham số đầu (hiển thị chữ bên trong).
_KEEP_FIRST = {"yl", "參", "nowrap", "small", "big", "larger", "center", "ruby", "lang-zh"}
_KEEP_LAST = {"lang"}
# Template chú thích → dấu ⟪loại:…⟫.
_NOTE = {"*": "*", "注": "注", "小注": "注", "夾注": "注", "efn": "ref", "note": "ref"}
# Template mã chữ hiếm → dấu ⟪char:…⟫ để tra bảng ở Bước 5 (R09).
_CHAR = {"skchar", "skchar2", "僻字", "ucchar"}
_NAMED_ARG = re.compile(r"^\s*([^=\s{}|\[\]]{1,30})\s*=(.*)$", re.S)


def _norm_tpl_name(name: str) -> str:
    name = name.strip().replace("_", " ")
    name = re.sub(r"^(?:template|bản mẫu|模板|模板):", "", name, flags=re.I)
    return name.lower()


def _match_braces(s: str, j: int) -> int:
    """j trỏ vào '{{'; trả về vị trí ngay sau '}}' tương ứng, -1 nếu không đóng."""
    depth, i, n = 0, j, len(s)
    while i < n:
        if s.startswith("{{", i):
            depth += 1
            i += 2
        elif s.startswith("}}", i):
            depth -= 1
            i += 2
            if depth == 0:
                return i
        else:
            i += 1
    return -1


def _split_args(inner: str) -> list[str]:
    parts, buf, dt, dl, i = [], [], 0, 0, 0
    while i < len(inner):
        two = inner[i:i + 2]
        if two in ("{{", "}}", "[[", "]]"):
            dt += (two == "{{") - (two == "}}")
            dl += (two == "[[") - (two == "]]")
            buf.append(two)
            i += 2
            continue
        c = inner[i]
        if c == "|" and dt == 0 and dl == 0:
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(c)
        i += 1
    parts.append("".join(buf))
    return parts


class _Expander:
    def __init__(self, doc: Doc):
        self.doc = doc

    def expand(self, s: str) -> str:
        out, i = [], 0
        while True:
            j = s.find("{{", i)
            if j < 0:
                out.append(s[i:])
                break
            out.append(s[i:j])
            k = _match_braces(s, j)
            if k < 0:
                self.doc.warnings.append("có '{{' không đóng; giữ nguyên phần còn lại")
                out.append(s[j:])
                break
            out.append(self.render(s[j + 2:k - 2]))
            i = k
        return "".join(out)

    def render(self, inner: str) -> str:
        parts = _split_args(inner)
        raw_name = parts[0].strip()
        name = _norm_tpl_name(raw_name)
        args = parts[1:]
        st = self.doc.stats
        st[f"tpl:{raw_name}"] += 1
        if name in _DROP or _DROP_RE.search(name):
            if name in _HEADER_TPL:
                for a in args:
                    m = _NAMED_ARG.match(a)
                    if m:
                        self.doc.meta[m.group(1).strip()] = re.sub(r"\s+", " ", m.group(2)).strip()
            return ""
        if name == "!":
            return "|"
        if name == "=":
            return "="
        pos = [a for a in args if not _NAMED_ARG.match(a)]
        if name in _NOTE:
            body = self.expand("|".join(args)).replace("\n", " ").strip()
            return f"{MK_OPEN}{_NOTE[name]}:{body}{MK_CLOSE}" if body else ""
        if name in _CHAR:
            body = "|".join(a.strip() for a in args)
            return f"{MK_OPEN}char:{raw_name}|{body}{MK_CLOSE}"
        if name in _KEEP_FIRST or name in _KEEP_LAST:
            if not pos:
                return ""
            if name == "參" and len(pos) > 1:
                self.doc.stats["參:chọn tham số 1"] += 1
                self.doc.meta.setdefault("參", []).append("|".join(p.strip() for p in pos))
            return self.expand(pos[0] if name in _KEEP_FIRST else pos[-1])
        # Template chưa biết: giữ lại thành dấu để Bước 5 báo, không âm thầm xóa chữ.
        self.doc.stats[f"tpl chưa biết:{raw_name}"] += 1
        if not args:
            return ""
        body = self.expand("|".join(args)).replace("\n", " ")
        return f"{MK_OPEN}?{raw_name}:{body}{MK_CLOSE}"


# ---------------------------------------------------------------- wikitext: dòng

_HEADING = re.compile(r"^(={1,6})\s*(.*?)\s*\1\s*$")
_LIST = re.compile(r"^([*#:;]+)\s*(.*)$")
_URL_ONLY = re.compile(r"^(?:https?://|www\.)\S+$")
_NS_DROP = re.compile(r"^\s*:?\s*(?:thể loại|category|file|tập tin|hình|image|分類|分类|文件):", re.I)
_TAG_STRIP = re.compile(
    r"</?(?:div|span|blockquote|center|small|big|sup|sub|u|s|i|b|font|p|poem|section|"
    r"onlyinclude|includeonly|tt|code|em|strong|abbr)\b[^>]*>", re.I)


def _strip_links(s: str) -> str:
    for _ in range(5):
        new = re.sub(r"\[\[([^\[\]|]*)\|([^\[\]]*)\]\]",
                     lambda m: "" if _NS_DROP.match(m.group(1)) else m.group(2), s)
        new = re.sub(r"\[\[([^\[\]|]*)\]\]",
                     lambda m: "" if _NS_DROP.match(m.group(1))
                     else re.sub(r"^:?\s*\w{1,3}:", "", m.group(1)), new)
        if new == s:
            break
        s = new
    s = re.sub(r"\[(?:https?:)?//\S+\s+([^\]]+)\]", r"\1", s)
    s = re.sub(r"\[(?:https?:)?//\S+\]", "", s)
    return s


def read_wikitext(text: str, doc: Doc, han: bool) -> None:
    st = doc.stats
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"__[A-Z]+__", "", text)
    text = re.sub(r"<noinclude>.*?</noinclude>", "", text, flags=re.S)
    n_pages = len(re.findall(r"<pages\b[^>]*/>", text))
    if n_pages:
        st["bỏ <pages/>"] += n_pages
        text = re.sub(r"<pages\b[^>]*/>", "", text)
    # dòng in đậm bị ngắt: '''Tên\n''' → '''Tên'''
    text = re.sub(r"'''([^'\n]+)\n'''", r"'''\1'''", text)

    text = _Expander(doc).expand(text)

    def ref_sub(m):
        st["ref"] += 1
        body = m.group(1).replace("\n", " ").strip()
        return f"{MK_OPEN}ref:{body}{MK_CLOSE}" if body else ""

    text = re.sub(r"<ref\b[^>]*/>", "", text)
    text = re.sub(r"<ref\b[^>]*>(.*?)</ref>", ref_sub, text, flags=re.S)
    text = re.sub(r"<references\b[^>]*/?>", "", text)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)

    in_sources = False
    for ln, line in enumerate(text.split("\n"), start=1):
        s = line.strip()
        if not s or re.fullmatch(r"-{4,}", s):
            continue
        if re.fullmatch(r"(?:Nguồn|Source|來源|来源)\s*[:：]?", s, flags=re.I):
            in_sources = True
            st["bỏ dòng 'Nguồn:'"] += 1
            continue
        kind, level = "para", 0
        m = _HEADING.match(s)
        if m:
            kind, level, s = "heading", len(m.group(1)), m.group(2)
        else:
            m = _LIST.match(s)
            if m:
                marks, s = m.group(1), m.group(2)
                kind = "indent" if marks[-1] == ":" else "item"
        s = _strip_links(s)
        s = _TAG_STRIP.sub("", s)
        if kind == "para" and re.fullmatch(r"'''(?!')(.+?)'''", s):
            kind = "title"
        s = re.sub(r"'{2,5}", "", s)
        s = htmlmod.unescape(s)
        s = re.sub(r"[ ]{2,}", " ", s).strip()
        if not s:
            continue
        if _URL_ONLY.match(s):
            doc.meta.setdefault("source_urls", []).append(s)
            st["bỏ dòng URL"] += 1
            continue
        if in_sources and kind == "item":
            st["bỏ mục trong 'Nguồn:'"] += 1
            continue
        in_sources = False
        doc.blocks.append(Block(kind, s, level, ln))


# ---------------------------------------------------------------- html (sillok + chung)

_SENT_END = "。！？」』）"


def read_html(text: str, doc: Doc, han: bool) -> None:
    st = doc.stats
    i = text.find('id="dmv01"')
    if i >= 0:  # trang bài sillok.history.go.kr
        j = text.find('id="dmv02"', i)
        seg = text[i: j if j > 0 else len(text)]
        paras = re.findall(r'<p class="paragraph">(.*?)</p>', seg, flags=re.S)
        m = re.search(r'data-title="([^"]+)"', text)
        if m:
            title = htmlmod.unescape(m.group(1)).strip()
            doc.meta["title"] = title
            doc.blocks.append(Block("heading", title, 3, 0, {"sillok": True}))
        m = re.search(r'data-id="(qsilok_[0-9_]+)"', text)
        if m:
            doc.meta["sillok_id"] = m.group(1)
        doc.fmt_reason += "; bộ đọc sillok (div#dmv01 p.paragraph)"
    else:  # HTML bất kỳ: lấy text theo khối
        body = re.sub(r"<(script|style|head)\b.*?</\1>", "", text, flags=re.S | re.I)
        body = re.sub(r"</(?:p|div|h\d|li|tr|blockquote)>|<br\s*/?>", "\n", body, flags=re.I)
        paras = body.split("\n")
    out: list[str] = []
    for p in paras:
        p = re.sub(r"<a\b[^>]*>.*?</a>", "", p, flags=re.S)  # link tra cứu nhân vật (chỉ có ảnh)
        p = re.sub(r"<[^>]+>", "", p)
        p = htmlmod.unescape(p)
        p = normalize_text(p, nfc=not han)
        p = re.sub(r"\s+", "" if han else " ", p).strip()
        if not p:
            continue
        # R02: nối đoạn bị ngắt ở chỗ nâng chữ (抬頭), ví dụ "…是</p><p>天心已厭…"
        if han and out and not out[-1].endswith(tuple(_SENT_END)):
            out[-1] += p
            st["R02 nối dòng ngắt (抬頭)"] += 1
        else:
            out.append(p)
    for p in out:
        doc.blocks.append(Block("para", p))


# ---------------------------------------------------------------- text thuần

def read_plain(text: str, doc: Doc, han: bool) -> None:
    for ln, line in enumerate(text.split("\n"), start=1):
        s = re.sub(r"[ ]{2,}", " ", line).strip()
        if not s:
            continue
        if _URL_ONLY.match(s):
            doc.meta.setdefault("source_urls", []).append(s)
            doc.stats["bỏ dòng URL"] += 1
            continue
        m = re.match(r"^(#{1,6})\s+(.+)$", s)  # đề mục kiểu Markdown, nếu có
        if m:
            doc.blocks.append(Block("heading", m.group(2), len(m.group(1)), ln))
        else:
            doc.blocks.append(Block("para", s, 0, ln))


# ---------------------------------------------------------------- điểm vào

_READERS = {"wikitext": read_wikitext, "html": read_html, "plain": read_plain}


def load_document(path: Path, lang: str, force_format: str | None = None) -> Doc:
    """Đọc một tệp nguồn bất kỳ, trả về Doc đã chuẩn hóa."""
    path = Path(path)
    raw, enc = read_source(path)
    han = lang == "han"
    fmt, reason = (force_format, "chỉ định trong cấu hình") if force_format else detect_format(raw, path.suffix)
    text = normalize_text(raw, nfc=not han) if fmt != "html" else raw
    doc = Doc(path=path, fmt=fmt, fmt_reason=reason, encoding=enc, blocks=[])
    _READERS[fmt](text, doc, han)
    if han:  # chữ Hán: bỏ khoảng trắng giữa hai chữ Hán (do ngắt dòng / dàn trang)
        for b in doc.blocks:
            b.text = re.sub(r"(?<=[^\x00-\x7f]) (?=[^\x00-\x7f])", "", b.text) \
                if not re.search("[A-Za-z]", b.text) else b.text
    return doc
