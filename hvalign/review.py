"""Hiệu đính và chấm mẫu – phần "con người trong vòng lặp", giữ ở mức tối thiểu.

Máy làm gần hết; người chỉ:
  1. xem HÀNG ĐỢI các cặp máy không chắc (có cờ), xếp theo mức rủi ro – xem đến đâu hay đến đó,
     cặp không ai xem thì giữ nguyên kết quả máy;
  2. chấm MẪU ngẫu nhiên để đo tỷ lệ lỗi theo §8 Guideline.

Quyết định được lưu thành tệp nhỏ, đưa lên git, và TỰ ÁP mỗi lần xuất – chạy lại chương trình không mất công sửa:
  hieu_dinh/<MA>__<người>.tsv          quyết định hiệu đính (mỗi người một tệp → không xung đột git)
  hieu_dinh/cham_mau__<người chấm>.tsv  kết quả chấm mẫu

Khóa của một cặp = mã các câu Hán + mã các câu Việt (ổn định giữa các lần chạy). Nếu cấu hình đổi làm cặp
bị ghép khác đi, quyết định cũ không còn khớp khóa nào và tự động bị bỏ qua.
"""
from __future__ import annotations

import hashlib
import re
from datetime import datetime
from pathlib import Path

from .textutil import read_jsonl

DIR_NAME = "hieu_dinh"
DEC_HEADER = ["thoi_gian", "khoa", "quyet_dinh", "gop_voi", "han_sua", "viet_sua", "ghi_chu"]
SAMPLE_HEADER = ["thoi_gian", "khoa", "tac_pham", "thanh_vien", "ket_qua", "nhan_loi", "ghi_chu"]
DECISIONS = {"dung", "sai", "sua", "gop", "xoa"}  # xoa = rút lại quyết định trước
ERROR_LABELS = ["OMISSION", "ADDITION", "MISSING", "RANH_GIOI"]
FLAG_WEIGHT = {"lech_do_dai": 2.0, "lech_moc": 2.0, "n-m": 1.5, "rut_gon": 1.0}
FLAG_TEXT = {
    "lech_do_dai": "Độ dài hai vế chênh nhiều so với tỷ lệ chung – có thể thiếu hoặc thừa câu.",
    "lech_moc": "Có can chi / tên riêng chỉ thấy ở một vế.",
    "n-m": "Gộp nhiều câu ở cả hai vế – ranh giới có thể sai.",
    "rut_gon": "Thuộc đoạn bản Việt dịch rút gọn (khai báo trong cấu hình).",
}


def key_of(p: dict) -> str:
    return ",".join(p["han_ids"]) + "|" + ",".join(p["viet_ids"])


def review_dir(project) -> Path:
    return project.root / DIR_NAME


def _safe_name(s: str) -> str:
    s = re.sub(r"[^\w\-]+", "_", s.strip(), flags=re.UNICODE).strip("_")
    if not s:
        raise ValueError("thiếu tên người hiệu đính")
    return s


def _cell(s) -> str:
    return re.sub(r"[\t\r\n]+", " ", str(s or "")).strip()


def _read_rows(path: Path, header: list[str]) -> list[dict]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        cols = line.split("\t")
        if cols == header:
            continue
        out.append(dict(zip(header, cols + [""] * (len(header) - len(cols)))))
    return out


def _append(path: Path, header: list[str], row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    new = not path.exists()
    with open(path, "a", encoding="utf-8", newline="\n") as f:
        if new:
            f.write("\t".join(header) + "\n")
        f.write("\t".join(_cell(row.get(h, "")) for h in header) + "\n")


def _now() -> str:
    return datetime.now().isoformat(timespec="seconds")


# ------------------------------------------------------------------ quyết định hiệu đính
def save_decision(project, work: str, who: str, key: str, decision: str,
                  gop_voi: str = "", han: str = "", viet: str = "", note: str = "") -> None:
    if decision not in DECISIONS:
        raise ValueError(f"quyết định không hợp lệ: {decision}")
    if decision == "sua" and not (_cell(han) and _cell(viet)):
        raise ValueError("sửa cặp thì cả hai vế phải có chữ")
    if decision == "gop" and not gop_voi:
        raise ValueError("gộp thì phải chỉ ra cặp gộp cùng")
    _append(review_dir(project) / f"{work}__{_safe_name(who)}.tsv", DEC_HEADER,
            {"thoi_gian": _now(), "khoa": key, "quyet_dinh": decision, "gop_voi": gop_voi,
             "han_sua": han if decision == "sua" else "", "viet_sua": viet if decision == "sua" else "",
             "ghi_chu": note})


def load_decisions(project, work: str) -> dict[str, dict]:
    """{khóa: quyết định mới nhất} gộp từ tệp của mọi người; 'xoa' rút lại quyết định trước đó."""
    rows = []
    for f in sorted(review_dir(project).glob(f"{work}__*.tsv")):
        who = f.stem.split("__", 1)[1]
        rows += [dict(r, nguoi=who) for r in _read_rows(f, DEC_HEADER)]
    latest: dict[str, dict] = {}
    for r in sorted(rows, key=lambda r: r["thoi_gian"]):
        if r["quyet_dinh"] == "xoa":
            latest.pop(r["khoa"], None)
        elif r["quyet_dinh"] in DECISIONS:
            latest[r["khoa"]] = r
    return latest


def handled(decisions: dict[str, dict]) -> dict[str, dict]:
    """Quyết định nhìn từ từng cặp: cặp bị cặp trên gộp vào cũng tính là đã xem ('gop_tren')."""
    out = dict(decisions)
    for d in decisions.values():
        if d["quyet_dinh"] == "gop" and d["gop_voi"] not in out:
            out[d["gop_voi"]] = dict(d, quyet_dinh="gop_tren", khoa=d["gop_voi"])
    return out


def apply(pairs: list[dict], decisions: dict[str, dict]) -> tuple[list[dict], dict]:
    """Áp quyết định lên danh sách cặp của máy. Trả về (cặp cuối cùng, thống kê)."""
    stats = {"dung": 0, "sai": 0, "sua": 0, "gop": 0, "khong_khop": 0}
    keys = [key_of(p) for p in pairs]
    pos = {k: i for i, k in enumerate(keys)}
    stats["khong_khop"] = sum(1 for k in decisions if k not in pos)
    out, i = [], 0
    while i < len(pairs):
        p = dict(pairs[i], khoa=keys[i], hd="")
        d = decisions.get(keys[i])
        # gộp: cặp i + cặp ngay sau (có thể nối chuỗi i → i+1 → i+2 …)
        j = i
        while d and d["quyet_dinh"] == "gop":
            if pos.get(d["gop_voi"]) != j + 1:
                stats["khong_khop"] += 1
                break
            j += 1
            q = pairs[j]
            p.update(han=p["han"] + q["han"], viet=f'{p["viet"]} {q["viet"]}',
                     han_ids=p["han_ids"] + q["han_ids"], viet_ids=p["viet_ids"] + q["viet_ids"],
                     co=[], hd="gop")
            p["kieu"] = f'{len(p["han_ids"])}-{len(p["viet_ids"])}'
            stats["gop"] += 1
            d = decisions.get(keys[j])
        i = j + 1
        if p["hd"] == "gop":  # khóa giữ là khóa cặp đầu; quyết định khác của các cặp đã gộp bỏ qua
            out.append(p)
            continue
        if d and d["quyet_dinh"] == "sai":
            stats["sai"] += 1
            continue
        if d and d["quyet_dinh"] == "sua":
            p.update(han=d["han_sua"], viet=d["viet_sua"], co=[], hd="sua")
            stats["sua"] += 1
        elif d and d["quyet_dinh"] == "dung":
            p.update(co=[], hd="dung")
            stats["dung"] += 1
        out.append(p)
    return out, stats


def machine_pairs(project, work: str) -> list[dict]:
    path = project.scratch(work) / "alignment.jsonl"
    return read_jsonl(path) if path.exists() else []


def final_pairs(project, work: str) -> tuple[list[dict], dict]:
    return apply(machine_pairs(project, work), load_decisions(project, work))


# ------------------------------------------------------------------ hàng đợi hiệu đính
def risk(p: dict) -> float:
    r = sum(FLAG_WEIGHT.get(f, 1.0) for f in p.get("co", []))
    if "lech_do_dai" in p.get("co", []):
        r += min(abs(p.get("delta", 0)) / 2, 3)
    return round(r + p.get("chi_phi", 0) / 4, 2)


def queue(pairs: list[dict], decisions: dict[str, dict]) -> list[dict]:
    """Cặp máy gắn cờ, rủi ro cao nhất lên đầu. Cặp đã có quyết định vẫn trả về (đánh dấu) để xem lại."""
    q = [p for p in pairs if p.get("co")]
    q.sort(key=lambda p: (-risk(p), p["pid"]))
    return q


# ------------------------------------------------------------------ chấm mẫu §8
def sample_size(n: int, k: int = 100) -> int:
    """Cỡ mẫu mỗi người (config/project.yaml → cham_mau.so_cap, mặc định 100). Guideline §8 chỉ đặt ngưỡng
    (≤ 30% đạt, mục tiêu ≤ 20%); 100 cặp cho sai số khoảng ±8% quanh mức 20% – đủ để kết luận đạt/không đạt."""
    return min(n, k)


def sample_for(project, member: str, works: list[str]) -> list[dict]:
    """Mẫu ổn định của một thành viên trên mọi tác phẩm: xếp theo băm(khóa), lấy N cặp đầu.
    Hiệu đính làm mất vài cặp thì các cặp còn lại trong mẫu vẫn giữ nguyên."""
    pool = []
    for w in works:
        for p in final_pairs(project, w)[0]:
            if p["member"] == member:
                pool.append(dict(p, tac_pham=w))
    pool.sort(key=lambda p: hashlib.sha1(f"2026|{p['khoa']}".encode()).hexdigest())
    k = int((project.cfg.get("cham_mau") or {}).get("so_cap", 100))
    return pool[:sample_size(len(pool), k)]


def save_grade(project, checker: str, key: str, work: str, member: str, result: str,
               label: str = "", note: str = "") -> None:
    if result not in ("dung", "sai", "xoa"):
        raise ValueError(f"kết quả không hợp lệ: {result}")
    if result == "sai" and label not in ERROR_LABELS:
        raise ValueError(f"nhãn lỗi phải là một trong {ERROR_LABELS}")
    _append(review_dir(project) / f"cham_mau__{_safe_name(checker)}.tsv", SAMPLE_HEADER,
            {"thoi_gian": _now(), "khoa": key, "tac_pham": work, "thanh_vien": member,
             "ket_qua": result, "nhan_loi": label if result == "sai" else "", "ghi_chu": note})


def load_grades(project) -> dict[tuple[str, str], dict]:
    """{(thành viên được chấm, khóa): kết quả mới nhất} từ mọi người chấm."""
    rows = []
    for f in sorted(review_dir(project).glob("cham_mau__*.tsv")):
        who = f.stem.split("__", 1)[1]
        rows += [dict(r, nguoi_cham=who) for r in _read_rows(f, SAMPLE_HEADER)]
    latest: dict[tuple[str, str], dict] = {}
    for r in sorted(rows, key=lambda r: r["thoi_gian"]):
        k = (r["thanh_vien"], r["khoa"])
        if r["ket_qua"] == "xoa":
            latest.pop(k, None)
        else:
            latest[k] = r
    return latest


def error_rate(grades: dict, member: str, keys: set[str] | None = None, work: str | None = None) -> dict:
    """Tỷ lệ lỗi = số cặp lỗi / số cặp đã chấm. keys: chỉ tính các cặp còn trong mẫu hiện tại."""
    g = [r for (m, k), r in grades.items() if m == member and (keys is None or k in keys)
         and (work is None or r["tac_pham"] == work)]
    wrong = sum(1 for r in g if r["ket_qua"] == "sai")
    return {"da_cham": len(g), "sai": wrong, "ty_le_loi": wrong / len(g) if g else None,
            "nhan": {lb: sum(1 for r in g if r["nhan_loi"] == lb) for lb in ERROR_LABELS}}
