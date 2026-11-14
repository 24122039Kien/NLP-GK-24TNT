"""Tìm tệp nguồn trong 01_nguon/, nhận ngôn ngữ và số quyển, ghép thành cặp Hán–Việt.

Chấp nhận cả hai kiểu đặt tên đang có trong nhóm:
  01_nguon/han/續資治通鑑_卷002.wikitext   ↔  01_nguon/viet/Tục_tư_trị_thông_giám_Quyển_2.wikitext
  01_nguon/TTTTG_q03_han.txt               ↔  01_nguon/TTTTG_q03_viet.txt
Nếu cùng một tài liệu có nhiều định dạng (.wikitext và .txt cùng tên gốc) thì chọn theo thứ tự
.wikitext > .html > .txt. PDF không dùng để trích text (chỉ để đối chiếu).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from .readers import TEXT_EXTS
from .textutil import cjk_ratio, read_source, vol_sort_key

_VOL_PATTERNS = [
    re.compile(r"卷(?:之)?0*(\d+)"),
    re.compile(r"Quyển[ _]0*(\d+)", re.I),
    re.compile(r"(?:^|[_\-. ])q0*(\d+)(?=[_\-. ]|$)", re.I),
    re.compile(r"qsilok_\d+_0*(\d+)_"),
]
_LANG_SUFFIX = {
    "han": re.compile(r"(?:^|[_\-. ])(?:han|hn|zh|hantext)(?=[_\-. ]|$)", re.I),
    "viet": re.compile(r"(?:^|[_\-. ])(?:viet|vi|vn)(?=[_\-. ]|$)", re.I),
}


@dataclass
class SourceFile:
    path: Path
    lang: str
    volume: str
    lang_reason: str


@dataclass
class VolumeSources:
    volume: str
    member: str
    han: list[Path] = field(default_factory=list)
    viet: list[Path] = field(default_factory=list)


def guess_volume(name: str) -> str | None:
    for p in _VOL_PATTERNS:
        m = p.search(name)
        if m:
            return str(int(m.group(1)))
    return None


def guess_lang(path: Path, nguon_dir: Path) -> tuple[str, str]:
    rel = [p.lower() for p in path.relative_to(nguon_dir).parts[:-1]]
    for lang in ("han", "viet"):
        if lang in rel:
            return lang, f"thư mục {lang}/"
    for lang, pat in _LANG_SUFFIX.items():
        if pat.search(path.stem):
            return lang, "hậu tố tên tệp"
    try:
        text, _ = read_source(path)
    except Exception:
        return "unknown", "không đọc được"
    r = cjk_ratio(text[:20000])
    return ("han" if r > 0.5 else "viet"), f"nội dung (tỷ lệ chữ Hán {r:.2f})"


def discover(nguon_dir: Path) -> list[SourceFile]:
    files = [p for p in nguon_dir.rglob("*") if p.is_file() and p.suffix.lower() in TEXT_EXTS]
    # cùng tên gốc, khác định dạng → giữ định dạng ưu tiên
    best: dict[tuple[Path, str], Path] = {}
    for p in files:
        key = (p.parent, p.stem)
        if key not in best or TEXT_EXTS[p.suffix.lower()] < TEXT_EXTS[best[key].suffix.lower()]:
            best[key] = p
    out = []
    for p in sorted(best.values()):
        lang, why = guess_lang(p, nguon_dir)
        out.append(SourceFile(p, lang, guess_volume(p.stem) or "", why))
    return out


def plan_sources(project, work: str, wcfg: dict) -> tuple[list[VolumeSources], list[str]]:
    """Trả về danh sách quyển (đã ghép Hán–Việt) và các cảnh báo."""
    wdir = project.work_dir(work)
    warnings: list[str] = []
    if wcfg.get("sources"):  # khai báo tay trong config/works/<MA>.yaml
        vols = []
        for s in wcfg["sources"]:
            v = str(s["volume"])
            vs = VolumeSources(v, s.get("member") or project.member_of(work, v))
            for lang in ("han", "viet"):
                paths = s.get(lang) or []
                paths = [paths] if isinstance(paths, str) else paths
                getattr(vs, lang).extend(project.root / p for p in paths)
            vols.append(vs)
        return vols, warnings

    found = discover(wdir / "01_nguon")
    for f in found:
        if f.lang == "unknown":
            warnings.append(f"{f.path.name}: không xác định được ngôn ngữ")
    by_lang = {lang: [f for f in found if f.lang == lang] for lang in ("han", "viet")}
    default_vol = str(wcfg.get("quyen_mac_dinh", "1"))
    # Mỗi bên chỉ có một quyển → ghép luôn dù số quyển trong tên tệp khác nhau / không có.
    vols_of = {lang: {f.volume or default_vol for f in fs} for lang, fs in by_lang.items()}
    single = len(vols_of["han"]) == 1 and len(vols_of["viet"]) == 1
    groups: dict[str, VolumeSources] = {}
    for lang, fs in by_lang.items():
        for f in fs:
            v = (next(iter(vols_of["han"])) if single else (f.volume or default_vol))
            if v not in groups:
                groups[v] = VolumeSources(v, project.member_of(work, v))
            getattr(groups[v], lang).append(f.path)
    vols = [groups[k] for k in sorted(groups, key=vol_sort_key)]
    for vs in vols:
        for lang in ("han", "viet"):
            if not getattr(vs, lang):
                warnings.append(f"quyển {vs.volume}: thiếu bản {'Hán' if lang == 'han' else 'Việt'}")
    return vols, warnings
