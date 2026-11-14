"""Báo cáo tự sinh cho mỗi tác phẩm (work/<MA>/bao_cao.md) – đủ 5 mục tối thiểu của Guideline."""
from __future__ import annotations

import platform
from collections import Counter
from datetime import date
from pathlib import Path

from . import __version__
from .textutil import read_jsonl


def read_tsv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines() if ln and not ln.startswith("#")]
    if not lines:
        return []
    head = lines[0].split("\t")
    return [dict(zip(head, ln.split("\t"))) for ln in lines[1:]]


def load_manifests(root: Path) -> list[dict]:
    rows = []
    for p in list((root / "Docs").glob("*manifest*.tsv")) + [root / "config" / "manifest.tsv"]:
        rows += read_tsv(p)
    return rows


def run(project, work: str, validation=None, log=print) -> Path:
    scratch = project.scratch(work)
    pairs = read_jsonl(scratch / "alignment.jsonl")
    sach = project.work_dir(work) / "03_text_sach"
    n_lines = {lang: sum(1 for _ in open(sach / f"{lang}.txt", encoding="utf-8")) for lang in ("han", "viet")}
    clean_log = read_tsv(scratch / "clean_log.tsv")
    excl = read_tsv(scratch / "loai_tru.tsv")
    unp = read_tsv(scratch / "khong_ghep.tsv")
    warns = read_tsv(scratch / "canh_bao.tsv")
    ext = read_tsv(scratch / "extract_log.tsv")
    man = load_manifests(project.root)

    L = [f"# Báo cáo tự sinh – {work}", "",
         f"Ngày: {date.today().isoformat()} · hvalign {__version__} · "
         "**Trạng thái: bản dóng tự động, CHƯA hiệu đính**", ""]
    by_member = Counter(p["member"] for p in pairs)
    L += ["## 1. Số cặp", "", f"Tổng: **{len(pairs)}** cặp.", "", "| Thành viên | Số cặp |", "|---|---|"]
    L += [f"| {m} | {n} |" for m, n in sorted(by_member.items())]
    vols = Counter((p["vol"], p["member"]) for p in pairs)
    L += ["", "| Quyển | Thành viên | Số cặp |", "|---|---|---|"]
    L += [f"| {v} | {m} | {n} |" for (v, m), n in sorted(vols.items(), key=lambda x: (len(x[0][0]), x[0][0]))]
    kinds = Counter(p["kieu"] for p in pairs)
    L += ["", "Kiểu ghép: " + ", ".join(f"`{k}` {n}" for k, n in kinds.most_common()), ""]

    L += ["## 2. Số dòng văn bản sạch", "", f"- `03_text_sach/han.txt`: {n_lines['han']} dòng",
          f"- `03_text_sach/viet.txt`: {n_lines['viet']} dòng", ""]

    L += ["## 3. Kết quả tự kiểm tra", ""]
    if validation is not None:
        errs, ws = validation
        L.append(f"- Kiểm định định dạng TSV/XLSX: **{'đạt' if not errs else str(len(errs)) + ' lỗi'}**"
                 + (f"; cảnh báo: {'; '.join(ws)}" if ws else ""))
    rules = Counter()
    for r in clean_log:
        rules[r["luat"]] += int(r["so_lan"])
    L.append("- Luật làm sạch đã áp dụng: " + ", ".join(f"{k} ×{v}" for k, v in sorted(rules.items())))
    reasons = Counter(r["ly_do"] for r in excl)
    L.append(f"- Loại trừ (không có bản dịch / không phải chính văn): {len(excl)} khối"
             + (" – " + "; ".join(f"{k} ({v})" for k, v in reasons.items()) if reasons else ""))
    L.append(f"- Câu không ghép được (ghi ở `work/{work}/khong_ghep.tsv`, không đưa vào TSV): {len(unp)}")
    flags = Counter(f for p in pairs for f in p["co"])
    L.append("- Cặp gắn cờ cần hiệu đính: " + (", ".join(f"`{k}` {v}" for k, v in flags.most_common()) or "không"))
    L.append(f"- Cảnh báo khi làm sạch: {len(warns)} (xem `work/{work}/canh_bao.tsv`)")
    L.append("- Tỷ lệ lỗi theo §8 Guideline: **chưa đo** – cần lấy mẫu kiểm tra chéo sau khi hiệu đính.")
    L.append("")

    L += ["## 4. Nguồn tài liệu", "", "| Quyển | Bản | Tệp | Định dạng đọc được | Nguồn trực tuyến | revid |",
          "|---|---|---|---|---|---|"]
    for e in ext:
        m = next((r for r in man if r.get("tep", "").endswith(e["tep"])), {})
        L.append(f"| {e['quyen']} | {e['ngon_ngu']} | `{Path(e['tep']).name}` | {e['dinh_dang']} | "
                 f"{m.get('url', '(không có trong manifest)')} | {m.get('revid', '')} |")
    L.append("")
    L += ["## 5. Công cụ", "",
          f"- `hvalign` {__version__} (Lab/GK/hvalign), Python {platform.python_version()}, PyYAML.",
          "- Bước 4: tự nhận dạng định dạng nguồn (wikitext / text thuần / HTML sillok) và chuẩn hóa về một dạng.",
          "- Bước 7: dóng 3 tầng (mục → đoạn → câu), chi phí Gale–Church + mốc can chi và tên riêng Hán Việt.",
          f"- Cấu hình: `config/project.yaml`, `config/works/{work}.yaml`, `config/phan_cong.tsv`.", ""]
    out = scratch / "bao_cao.md"
    out.write_text("\n".join(L), encoding="utf-8")
    log(f"  Báo cáo {work}: work/{work}/bao_cao.md")
    return out
