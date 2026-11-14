"""Bước 5 – làm sạch text thô bằng bộ luật R01–R12; mọi luật đều ghi log số lần áp dụng.

Đầu vào : <MA>/02_ocr_tho/{han,viet}/<quyển>.tsv
Đầu ra  : <MA>/03_text_sach/han.txt, viet.txt   (mỗi dòng một đoạn, không mã)
          work/<MA>/clean.jsonl                   (cùng nội dung, có mã truy vết)
          work/<MA>/clean_log.tsv, loai_tru.tsv, canh_bao.tsv
"""
from __future__ import annotations

import re
from collections import Counter

from .config import ROOT, norm_vol
from .extract import read_raw
from .textutil import (CJK_CLASS, CJK_RE, LATIN_RE, MARKER_RE, VI_LETTER, strip_markers,
                       vol_sort_key, write_jsonl, write_tsv)

HAN_SENT_PUNCT = re.compile("[。，、；：？！]")
_CJK_RUN = f"[《〈「『]*[{CJK_CLASS}](?:[{CJK_CLASS}、・·《》〈〉「」『』 ]*[{CJK_CLASS}》〉」』])?"
_PAREN = re.compile(r"\s*[(（]([^()（）]*)[)）]")
_BARE_CJK = re.compile(_CJK_RUN)
_YEAR_GLOSS = re.compile(
    r"\s*\((?:năm\s+)?(?:khoảng\s+)?\d{1,4}(?:\s*[-–]\s*\d{1,4})?"
    r"(?:\s*(?:TCN|SCN|CN|tr\.?\s?CN))?(?:\s*dương lịch)?\)", re.I)
_KHAO_DI = re.compile(r"\s*\(\s*Khảo dị\s*[:：][^()]*\)")
_TRAILING_CITE = re.compile(r"\s*\(([^()]{1,80})\)\s*$")
_HAN_END_TITLE = re.compile(r"^《[^》]+》卷第?[〇一二三四五六七八九十百千]+(?:[上中下])?$")
_HAN_ASCII_PUNCT = str.maketrans({",": "，", ";": "；", ":": "：", "?": "？", "!": "！",
                                  "(": "（", ")": "）", "︰": "："})
_CHAR_CODE = re.compile(r"\[[0-9A-F]{4,5}\]|<[^\x00-\x7f<>]{1,6}>")


def load_char_fix() -> dict[str, str]:
    path = ROOT / "resources" / "char_fix.tsv"
    out = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("#") or "\t" not in line:
                continue
            k, v = line.split("\t")[:2]
            if k != "ma":
                out[k] = v
    return out


class Cleaner:
    def __init__(self, wcfg: dict, char_fix: dict[str, str]):
        self.rules = wcfg.get("lam_sach", {})
        self.drop_patterns = wcfg.get("bo_mau") or []
        self.char_fix = char_fix
        self.cnt: Counter = Counter()
        self.warnings: list[tuple[str, str, str]] = []

    def on(self, rule: str) -> bool:
        return bool(self.rules.get(rule, False))

    # ---- chú thích dạng ⟪loại:nội dung⟫ (R03, R04, R05, R09, template chưa biết)
    def markers(self, text: str, bid: str) -> str:
        def sub(m):
            tag, body = m.group(1), m.group(2)
            rule = {"ref": "R03_bo_ref", "*": "R04_bo_chu_nho", "注": "R05_bo_dan_nguon"}.get(tag)
            if rule:
                if self.on(rule):
                    self.cnt[rule] += 1
                    return ""
                return body
            if tag == "char":
                key = body
                if self.on("R09_sua_ma_chu") and key in self.char_fix:
                    self.cnt["R09_sua_ma_chu"] += 1
                    return self.char_fix[key]
                self.warnings.append((bid, "R09 mã chữ chưa tra được", body))
                return f"[?{body}]"
            self.warnings.append((bid, "template chưa biết, đã giữ chữ", f"{tag}: {body[:60]}"))
            return body
        prev = None
        while prev != text:
            prev = text
            text = MARKER_RE.sub(sub, text)
        return text

    def sub_count(self, rule: str, pat, repl, text: str) -> str:
        new, n = (pat.subn(repl, text) if hasattr(pat, "subn") else re.subn(pat, repl, text))
        self.cnt[rule] += n
        return new

    # ---- R06: chữ Hán xen trong bản Việt
    def strip_han_in_viet(self, text: str, bid: str) -> str:
        def paren(m):
            inner = m.group(1)
            if not CJK_RE.search(inner):
                return m.group(0)
            rest = _BARE_CJK.sub("", inner)
            self.cnt["R06_bo_chu_han_trong_viet"] += 1
            rest = re.sub(r"^[\s,;:、，]+|[\s,;:、，]+$", "", rest)
            if not re.search(f"[{VI_LETTER}0-9]", rest):
                return ""
            return m.group(0).replace(inner, rest)
        text = _PAREN.sub(paren, text)

        def bare(m):
            run = m.group(0)
            n = len(CJK_RE.findall(run))
            words = [w.strip("“”\"‘’'«»(") for w in text[:m.start()].rstrip().split(" ")[-n:]]
            ok = len(words) == n and all(re.fullmatch(f"[{VI_LETTER}]+", w) for w in words)
            if ok:
                self.cnt["R06_bo_chu_han_trong_viet"] += 1
                return ""
            self.warnings.append((bid, "R06 chữ Hán không đứng sau âm tương ứng – giữ lại, cần xem", run))
            return run
        return _BARE_CJK.sub(bare, text)

    # ---- áp mọi luật cho một khối
    def clean_block(self, b: dict, lang: str, vol_punctuated: bool) -> str | None:
        text, bid, kind = b["text"], b["id"], b["kind"]
        is_heading = kind.startswith("h")
        if is_heading:
            return strip_markers(text).strip()
        if self.on("R08_bo_dong_tieu_de"):
            if kind == "title" or self._looks_like_title(strip_markers(text), lang, vol_punctuated):
                self.cnt["R08_bo_dong_tieu_de"] += 1
                return None
        text = self.markers(text, bid)
        if lang == "viet":
            if self.on("R04_bo_chu_nho"):
                text = self.sub_count("R04_bo_chu_nho", _KHAO_DI, "", text)
            if self.on("R05_viet_dan_nguon_cuoi_khoan"):
                m = _TRAILING_CITE.search(text)
                if m and (re.search(r"\d", m.group(1)) or "《" in m.group(1)):
                    text = text[:m.start()]
                    self.cnt["R05_bo_dan_nguon"] += 1
            if self.on("R06_bo_chu_han_trong_viet"):
                text = self.strip_han_in_viet(text, bid)
            if self.on("R07_bo_nam_duong_lich"):
                text = self.sub_count("R07_bo_nam_duong_lich", _YEAR_GLOSS, "", text)
        else:
            if self.on("R08_bo_dong_tieu_de"):
                text = self.sub_count("R08_bo_dong_tieu_de", re.compile("^§"), "", text)
        for p in self.drop_patterns:
            if p.get("lang", lang) in (lang, "ca_hai"):
                text = self.sub_count("R11_bo_mau", re.compile(p["regex"]), "", text)
        if self.on("R09_sua_ma_chu"):
            for k, v in self.char_fix.items():
                if k in text:
                    self.cnt["R09_sua_ma_chu"] += text.count(k)
                    text = text.replace(k, v)
            for code in _CHAR_CODE.findall(text):
                self.warnings.append((bid, "R09 mã chữ chưa tra được", code))
        if self.on("R10_chuan_hoa_khoang_trang_dau_cau"):
            text = self._normalize(text, lang)
        if not text:
            self.cnt["rong_sau_lam_sach"] += 1
            return None
        if lang == "viet" and CJK_RE.search(text):
            self.warnings.append((bid, "bản Việt còn chữ Hán", "".join(CJK_RE.findall(text))[:40]))
        if lang == "han" and LATIN_RE.search(text):
            self.warnings.append((bid, "bản Hán còn chữ Latin", text[:60]))
        return text

    def _looks_like_title(self, text: str, lang: str, vol_punctuated: bool) -> bool:
        if lang == "han":
            if _HAN_END_TITLE.match(text):
                return True
            return vol_punctuated and not HAN_SENT_PUNCT.search(text) and len(text) <= 40
        words = text.split()
        if not vol_punctuated or re.search(r"[.,;:!?…]", text) or not words or len(words) > 25:
            return False
        caps = sum(1 for w in words if w[:1].isupper())
        return caps / len(words) >= 0.7

    def _normalize(self, text: str, lang: str) -> str:
        before = text
        if lang == "han":
            text = text.translate(_HAN_ASCII_PUNCT)
            text = re.sub(r"[\s　]+", "", text)
        else:
            text = re.sub(r"\s+", " ", text)
            text = re.sub(r"\s+([,.;:!?…)\]”’])", r"\1", text)
            text = re.sub(r"([(\[“‘])\s+", r"\1", text)
            text = re.sub(r"\(\s*\)", "", text)
            text = re.sub(r"\s{2,}", " ", text)
            text = re.sub(r"^[\s,;:.]+", "", text)
        text = text.strip()
        if text != before:
            self.cnt["R10_chuan_hoa_khoang_trang_dau_cau"] += 1
        return text


def _excluded(rules: list[dict], lang: str, vol: str, row: dict, heading: str) -> str | None:
    for r in rules:
        if r.get("lang", "ca_hai") not in (lang, "ca_hai"):
            continue
        if "quyen" in r and norm_vol(str(r["quyen"])) != vol:
            continue
        if "muc" in r and r["muc"] not in heading:
            continue
        if "loai" in r and row["kind"] != r["loai"]:
            continue
        if "regex" in r and not re.search(r["regex"], strip_markers(row["text"])):
            continue
        if "id" in r and not any(row["id"].startswith(p) for p in ([r["id"]] if isinstance(r["id"], str) else r["id"])):
            continue
        if not any(k in r for k in ("muc", "loai", "regex", "id", "quyen")):
            continue
        return r.get("ly_do", "loại trừ theo cấu hình")
    return None


def run(project, work: str, log=print) -> dict:
    wcfg = project.work_cfg(work)
    wdir = project.work_dir(work)
    scratch = project.scratch(work)
    cleaner = Cleaner(wcfg, load_char_fix())
    excl_rules = wcfg.get("loai_tru") or []
    risk_rules = wcfg.get("co_rui_ro") or []
    rows_out, excluded, log_rows = [], [], []
    text_lines = {"han": [], "viet": []}
    raw_dir = wdir / "02_ocr_tho"
    vol_files = sorted({p.stem for p in raw_dir.glob("*/*.tsv")}, key=lambda s: vol_sort_key(s[1:].lstrip("0") or "0"))
    for vl in vol_files:
        for lang in ("han", "viet"):
            path = raw_dir / lang / f"{vl}.tsv"
            if not path.exists():
                continue
            head = path.read_text(encoding="utf-8").split("\n", 1)[0]
            m = re.search(r"quyển (\S+)", head)
            vol = norm_vol(m.group(1)) if m else vl[1:]
            # thành viên do Bước 4 ghi vào đầu tệp (từ phan_cong.tsv hoặc 'member:' trong cấu hình sources)
            mm = re.search(r"thành viên: (\S+)", head)
            member = mm.group(1) if mm else project.member_of(work, vol)
            raw = read_raw(path)
            content = [r for r in raw if not r["kind"].startswith("h")]
            punct = (sum(1 for r in content if ("。" if lang == "han" else ".") in r["text"])
                     > 0.5 * max(1, len(content)))
            before = Counter(cleaner.cnt)
            heading, tail_excl = "", None
            for r in raw:
                if r["kind"].startswith("h"):
                    heading = strip_markers(r["text"])
                why = tail_excl or _excluded(excl_rules, lang, vol, r, heading)
                if why:
                    excluded.append((r["id"], lang, why, strip_markers(r["text"], keep_content=True)))
                    cleaner.cnt["R12_loai_tru"] += 1
                    if any(x.get("den_het_quyen") and _excluded([x], lang, vol, r, heading) for x in excl_rules):
                        tail_excl = why
                    continue
                text = cleaner.clean_block(r, lang, punct)
                if text is None:
                    continue
                flags = [x.get("co", "rui_ro") for x in risk_rules
                         if x.get("lang", lang) == lang and re.search(x["regex"], text)]
                sec = r["id"].split("/")[3]
                rows_out.append({"id": r["id"], "vol": vol, "lang": lang, "member": member,
                                 "kind": r["kind"], "sec": sec, "text": text, "flags": flags})
                if not r["kind"].startswith("h") or wcfg.get("van_ban_sach_gom_de_muc"):
                    text_lines[lang].append(text)
            diff = cleaner.cnt - before
            log_rows += [(vol, lang, k, v) for k, v in sorted(diff.items())]

    sach = wdir / "03_text_sach"
    sach.mkdir(parents=True, exist_ok=True)
    for lang in ("han", "viet"):
        with open(sach / f"{lang}.txt", "w", encoding="utf-8", newline="\n") as f:
            f.write("".join(t + "\n" for t in text_lines[lang]))
    write_jsonl(scratch / "clean.jsonl", rows_out)
    write_tsv(scratch / "clean_log.tsv", ["quyen", "ngon_ngu", "luat", "so_lan"], log_rows)
    write_tsv(scratch / "loai_tru.tsv", ["id", "ngon_ngu", "ly_do", "noi_dung"], excluded)
    write_tsv(scratch / "canh_bao.tsv", ["id", "loai", "chi_tiet"], cleaner.warnings)
    log(f"  B5 {work}: han.txt {len(text_lines['han'])} dòng, viet.txt {len(text_lines['viet'])} dòng; "
        f"loại trừ {len(excluded)} khối; {len(cleaner.warnings)} cảnh báo; "
        + ", ".join(f"{k.split('_')[0]}×{v}" for k, v in sorted(cleaner.cnt.items())))
    return {"han": len(text_lines["han"]), "viet": len(text_lines["viet"]), "warnings": len(cleaner.warnings)}
