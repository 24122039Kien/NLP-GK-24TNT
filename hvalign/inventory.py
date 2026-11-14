"""Kiểm kê nguồn (đầu Bước 4): đủ cặp Hán–Việt chưa, khớp SHA-256 với manifest không, có trùng bài không."""
from __future__ import annotations

import re
from collections import defaultdict

from .report import load_manifests
from .sources import plan_sources
from .textutil import sha256_file


def run(project, works: list[str], log=print) -> int:
    manifests = load_manifests(project.root)
    by_sha: dict[str, list[str]] = defaultdict(list)
    by_sillok: dict[str, list[str]] = defaultdict(list)
    problems = 0
    for work in works:
        wcfg = project.work_cfg(work)
        if not (project.work_dir(work) / "01_nguon").exists():
            log(f"  {work}: chưa có thư mục 01_nguon trên máy này")
            continue
        vols, warnings = plan_sources(project, work, wcfg)
        log(f"  {work}: {len(vols)} quyển")
        for w in warnings:
            log(f"    ! {w}")
            problems += 1
        for vs in vols:
            parts = []
            for lang in ("han", "viet"):
                files = getattr(vs, lang)
                exts = ",".join(sorted({p.suffix for p in files})) or "-"
                parts.append(f"{lang} {len(files)} tệp ({exts})")
                for p in files:
                    sha = sha256_file(p)
                    label = f"{work} q{vs.volume} {lang} {p.name}"
                    by_sha[sha].append(label)
                    # mã bài sillok: trong tên tệp hoặc trong nội dung (danh sách "Nguồn:" của bản Việt,
                    # tệp .txt gộp nhiều bài) → phát hiện cùng một bài nằm ở hai quyển / hai thành viên
                    try:
                        head = p.read_text(encoding="utf-8", errors="replace")[:300000]
                    except OSError:
                        head = ""
                    for sid in set(re.findall(r"qsilok_\d+_\d+_[\d_]+\d", p.name + "\n" + head)):
                        by_sillok[sid].append(label)
                    rel = p.relative_to(project.root).as_posix()
                    m = [r for r in manifests if r.get("tep") == rel]
                    if m and m[0].get("sha256") and m[0]["sha256"] != sha:
                        log(f"    ✗ {rel}: SHA-256 KHÁC manifest (tệp đã bị sửa?)")
                        problems += 1
                    elif not m:
                        log(f"    · {rel}: không có trong manifest")
            log(f"    quyển {vs.volume:>5} [{vs.member}]: " + "; ".join(parts))
    for sha, labels in by_sha.items():
        if len(labels) > 1:
            log(f"  ! Trùng nội dung (cùng SHA-256): {' | '.join(labels)}")
            problems += 1
    for sid, labels in by_sillok.items():
        if len({tuple(lb.split(" ")[:2]) for lb in labels}) > 1:
            log(f"  ! Bài sillok {sid} xuất hiện ở nhiều quyển: {' | '.join(labels)}")
            problems += 1
    log(f"  Kiểm kê xong: {problems} vấn đề")
    return problems
