"""Đọc cấu hình: config/project.yaml, config/phan_cong.tsv, config/works/<MA>.yaml."""
from __future__ import annotations

import copy
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent  # Lab/GK
CONFIG_DIR = ROOT / "config"


def _deep_merge(base: dict, over: dict) -> dict:
    out = copy.deepcopy(base)
    for k, v in (over or {}).items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = _deep_merge(out[k], v)
        else:
            out[k] = copy.deepcopy(v)
    return out


def load_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


@dataclass
class Project:
    root: Path
    cfg: dict

    @property
    def code(self) -> str:
        return self.cfg.get("ma_de_tai", "CV02")

    @property
    def deliver_root(self) -> Path:
        """Thư mục chung chứa mọi thư mục nộp <MA_DE_TAI>_<MA> (khóa `thu_muc_nop`; trống = gốc repo)."""
        return self.root / self.cfg.get("thu_muc_nop", "")

    def work_dir(self, work: str) -> Path:
        return self.deliver_root / f"{self.code}_{work}"

    def scratch(self, work: str) -> Path:
        return self.root / "work" / work

    def raw_dir(self, work: str) -> Path:
        """Text thô Bước 4. Để trong work/ (không nộp): nguồn là text số, không phải ảnh/PDF scan, nên theo
        nhận xét của giảng viên (18/11) thư mục nộp không cần 02_ocr_tho."""
        return self.scratch(work) / "02_ocr_tho"

    def work_cfg(self, work: str) -> dict:
        defaults = self.cfg.get("mac_dinh", {})
        return _deep_merge(defaults, load_yaml(CONFIG_DIR / "works" / f"{work}.yaml"))

    def works(self) -> list[str]:
        """Mọi tác phẩm có thư mục bàn giao hoặc có tệp cấu hình."""
        found = {p.name.split("_", 1)[1] for p in self.deliver_root.glob(f"{self.code}_HCB_*") if p.is_dir()}
        found |= {p.stem for p in (CONFIG_DIR / "works").glob("HCB_*.yaml")}
        return sorted(found)

    def assignments(self) -> dict[str, dict[str, str]]:
        """{tác phẩm: {quyển hoặc '*': thành viên}} từ phan_cong.tsv."""
        out: dict[str, dict[str, str]] = {}
        path = CONFIG_DIR / "phan_cong.tsv"
        if not path.exists():
            return out
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip() or line.startswith("#"):
                continue
            cols = [c.strip() for c in line.split("\t")]
            if cols[0] == "ma_tac_pham" or len(cols) < 3:
                continue
            out.setdefault(cols[0], {})[norm_vol(cols[1])] = cols[2]
        return out

    def member_of(self, work: str, volume: str) -> str:
        a = self.assignments().get(work, {})
        return a.get(norm_vol(volume)) or a.get("*") or "chua_phan_cong"


def norm_vol(v: str) -> str:
    v = str(v).strip()
    return str(int(v)) if v.isdigit() else v


def load_project() -> Project:
    return Project(ROOT, load_yaml(CONFIG_DIR / "project.yaml"))
