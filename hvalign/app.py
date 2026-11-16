"""Giao diện web cục bộ cho hvalign:  python -m hvalign app   →  http://127.0.0.1:8765

Chỉ dùng thư viện chuẩn của Python (không cần cài thêm). Máy chủ chỉ nghe trên 127.0.0.1, nên chỉ chính máy
mình mở được. Mọi thao tác trong giao diện đều gọi lại đúng các hàm mà dòng lệnh dùng.

Trang chính (index.html) chỉ có 3 bước: Làm tự động → Nhìn qua → Tải về (.zip đúng cấu trúc nộp).
Trang nâng cao (advanced.html, /nang-cao): hiệu đính từng cặp, chấm mẫu §8, bàn giao vào 04_dong_hang.
"""
from __future__ import annotations

import io
import json
import os
import re
import subprocess
import sys
import threading
import time
import traceback
import webbrowser
import zipfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from . import __version__, export, review
from .notes import notes_for
from .anchors import CANCHI, AnchorIndex
from .config import ROOT

STATIC = Path(__file__).parent / "app_static"
TARGET = 2000  # mục tiêu số cặp mỗi người


# ------------------------------------------------------------------ công việc chạy nền (một việc một lúc)
class Job:
    def __init__(self):
        self.lock = threading.Lock()
        self.running = False
        self.title = ""
        self.log: list[str] = []
        self.failed = 0
        self.started = self.ended = 0.0
        self.last: dict[str, dict] = {}  # tác phẩm → kết quả lần chạy gần nhất

    def state(self, since: int = 0) -> dict:
        return {"running": self.running, "title": self.title, "log": self.log[since:], "n": len(self.log),
                "failed": self.failed, "elapsed": round((self.ended or time.time()) - self.started, 1)
                if self.started else 0}

    MODES = {"run": "Chạy", "export": "Cập nhật bản xuất", "deliver": "Bàn giao", "prepare": "Làm tự động"}

    def start(self, project, works: list[str], mode: str) -> bool:
        with self.lock:
            if self.running:
                return False
            self.running, self.failed, self.log = True, 0, []
            self.title = f"{self.MODES[mode]} {', '.join(works)}"
            self.started, self.ended = time.time(), 0.0
        threading.Thread(target=self._work, args=(project, works, mode), daemon=True).start()
        return True

    def _work(self, project, works, mode):
        from .__main__ import STEPS, friendly_error, run_steps
        deliver = mode == "deliver"
        try:
            for w in works:
                self.log.append(f"== {w}")
                lines_before = len(self.log)
                steps = STEPS if mode == "run" else ["export", "validate", "report"]
                if mode == "prepare" and not (project.scratch(w) / "alignment.jsonl").exists():
                    steps = STEPS  # chưa chạy lần nào → chạy đủ các bước
                try:
                    bad = run_steps(project, w, steps, deliver, log=self.log.append)
                    ok = not bad
                except Exception as e:  # noqa: BLE001 – báo lỗi lên giao diện thay vì làm chết máy chủ
                    msg = friendly_error(e, w)
                    self.log.append(f"  {msg}" if msg else "  ✗ Lỗi chương trình (hãy báo cho nhóm):\n"
                                    + traceback.format_exc(limit=4))
                    ok = False
                self.failed += not ok
                self.last[w] = {"ok": ok, "mode": mode, "time": time.strftime("%H:%M"),
                                "log": self.log[lines_before:]}
        finally:
            self.ended = time.time()
            self.log.append(f"Xong trong {self.ended - self.started:.1f} giây"
                            + (f" – {self.failed} tác phẩm có lỗi." if self.failed else "."))
            self.running = False
            STATE.anchors = None  # tên riêng thu hoạch có thể đã đổi


class State:
    def __init__(self):
        self.project = None
        self.job = Job()
        self.anchors: AnchorIndex | None = None
        self.write_lock = threading.Lock()

    def anchor_index(self) -> AnchorIndex:
        if self.anchors is None:
            self.anchors = AnchorIndex.load(ROOT)
        return self.anchors


STATE = State()


# ------------------------------------------------------------------ dữ liệu cho giao diện
def _members(project) -> list[str]:
    ms = {m for a in project.assignments().values() for m in a.values()}
    for f in review.review_dir(project).glob("*__*.tsv"):
        ms.add(f.stem.split("__", 1)[1])
    return sorted(ms)


def overview(project) -> dict:
    works, totals = [], {}
    grades = review.load_grades(project)
    for w in project.works():
        machine = review.machine_pairs(project, w)
        final, hd = review.final_pairs(project, w)
        dec = review.handled(review.load_decisions(project, w))
        flagged = [p for p in machine if p["co"]]
        by_m: dict[str, int] = {}
        for p in final:
            by_m[p["member"]] = by_m.get(p["member"], 0) + 1
            totals[p["member"]] = totals.get(p["member"], 0) + 1
        unp = project.scratch(w) / "khong_ghep.tsv"
        xuat = project.scratch(w) / "xuat" / f"{w}_parallel.tsv"
        dec_mtime = max((f.stat().st_mtime for f in review.review_dir(project).glob(f"{w}__*.tsv")), default=0)
        delivered = project.work_dir(w) / "04_dong_hang" / f"{w}_parallel.tsv"
        works.append({
            "work": w, "has_run": bool(machine), "pairs": len(final), "members": by_m,
            "flagged": len(flagged), "seen": sum(1 for p in flagged if review.key_of(p) in dec),
            "hd": hd, "unpaired": max(sum(1 for _ in open(unp, encoding="utf-8")) - 1, 0) if unp.exists() else 0,
            "delivered": time.strftime("%d/%m %H:%M", time.localtime(delivered.stat().st_mtime))
            if delivered.exists() else "",
            "last": STATE.job.last.get(w),
            "stale": bool(machine) and (not xuat.exists() or dec_mtime > xuat.stat().st_mtime),
            "has_cfg": (project.root / "config" / "works" / f"{w}.yaml").exists(),
        })
    rates = {m: review.error_rate(grades, m) for m in sorted(totals)}
    return {"version": __version__, "works": works, "totals": totals, "target": TARGET,
            "members": _members(project), "rates": rates, "labels": review.ERROR_LABELS}


def _anchor_note(han: str, viet: str) -> list[str]:
    idx = STATE.anchor_index()
    hk, vk = idx.han_keys(han), idx.viet_keys(viet)

    def show(k):
        h = k.split(":", 1)[1]
        v = CANCHI.get(h) or ", ".join(sorted(idx.han2viet.get(h, [])))
        return f"{h} ({v.title()})" if v else h
    out = []
    if hk - vk:
        out.append("Chỉ vế Hán có: " + "; ".join(show(k) for k in sorted(hk - vk)))
    if vk - hk:
        out.append("Chỉ vế Việt có: " + "; ".join(show(k) for k in sorted(vk - hk)))
    return out


def _brief(p: dict | None) -> dict | None:
    if not p:
        return None
    return {"key": review.key_of(p), "pid": p["pid"], "han": p["han"], "viet": p["viet"]}


def review_items(project, work: str, member: str, mode: str, q: str) -> dict:
    pairs = review.machine_pairs(project, work)
    dec = review.handled(review.load_decisions(project, work))
    idx = {review.key_of(p): i for i, p in enumerate(pairs)}
    if mode == "all":
        cand = [p for p in pairs if not q or q in p["han"] or q.lower() in p["viet"].lower() or q == p["pid"]]
    else:
        cand = review.queue(pairs, dec)
    if member and member != "*":
        cand = [p for p in cand if p["member"] == member]
    total = len(cand)
    cand = cand[:300] if mode == "all" else cand
    items = []
    for p in cand:
        k = review.key_of(p)
        i = idx[k]
        why = [review.FLAG_TEXT.get(f, f) for f in p["co"] if f != "lech_moc"]
        if "lech_moc" in p["co"]:
            why += _anchor_note(p["han"], p["viet"]) or [review.FLAG_TEXT["lech_moc"]]
        d = dec.get(k)
        items.append({
            "key": k, "pid": p["pid"], "vol": p["vol"], "member": p["member"], "kieu": p["kieu"],
            "han": p["han"], "viet": p["viet"], "co": p["co"], "why": why, "risk": review.risk(p),
            "delta": p.get("delta"), "prev": _brief(pairs[i - 1] if i > 0 else None),
            "next": _brief(pairs[i + 1] if i + 1 < len(pairs) else None),
            "decision": {k2: d[k2] for k2 in ("quyet_dinh", "gop_voi", "han_sua", "viet_sua", "nguoi", "ghi_chu")}
            if d else None,
        })
    return {"items": items, "total": total, "members": sorted({p["member"] for p in pairs})}


def sample_items(project, member: str) -> dict:
    works = [w for w in project.works() if review.machine_pairs(project, w)]
    s = review.sample_for(project, member, works)
    grades = review.load_grades(project)
    items = []
    for p in s:
        g = grades.get((member, p["khoa"]))
        items.append({"key": p["khoa"], "pid": p["pid"], "work": p["tac_pham"], "vol": p["vol"],
                      "kieu": p["kieu"], "han": p["han"], "viet": p["viet"], "hd": p.get("hd", ""),
                      "grade": {k: g[k] for k in ("ket_qua", "nhan_loi", "ghi_chu", "nguoi_cham")} if g else None})
    pool = sum(1 for w in works for p in review.final_pairs(project, w)[0] if p["member"] == member)
    rate = review.error_rate(grades, member, {i["key"] for i in items})
    return {"items": items, "pool": pool, "rate": rate}


def open_path(project, rel: str) -> str:
    p = (project.root / rel).resolve()
    if not p.is_relative_to(project.root.resolve()):
        raise ValueError("chỉ mở được tệp trong thư mục đồ án")
    if not p.exists():
        if p.suffix == ".yaml" and p.parent.name == "works":  # chưa có cấu hình riêng → tạo tệp mẫu
            p.write_text(f"# Cấu hình riêng cho {p.stem}. Xem Docs/huong_dan_hvalign.md mục 5.\n",
                         encoding="utf-8")
        else:
            raise FileNotFoundError(f"chưa có {rel} – hãy chạy tác phẩm trước")
    if sys.platform.startswith("win"):
        os.startfile(p)  # noqa: S606
    elif sys.platform == "darwin":
        subprocess.Popen(["open", str(p)])
    else:
        subprocess.Popen(["xdg-open", str(p)])
    return str(p)

# ------------------------------------------------------------------ trang chính: làm tự động → nhìn qua → tải về
_CACHE: dict[tuple, object] = {}


def _mtime(p: Path) -> float:
    return p.stat().st_mtime if p.exists() else 0.0


def work_title(project, w: str) -> str:
    """Tên tác phẩm lấy từ dòng chú thích đầu của config/works/<MA>.yaml ('# HCB_11 – 後漢書 卷86 / Hậu Hán thư …')."""
    f = project.root / "config" / "works" / f"{w}.yaml"
    if f.exists():
        first = f.read_text(encoding="utf-8").splitlines()[:1]
        m = re.search(r"/\s*([^.(]+)", first[0]) if first else None
        if m:
            return m.group(1).strip()
    return ""


def _inputs_mtime(project, w: str) -> float:
    """Thời điểm sửa gần nhất của mọi thứ ảnh hưởng tới bản xuất."""
    files = [project.scratch(w) / "alignment.jsonl", project.scratch(w) / "khong_ghep.tsv",
             project.root / "config" / "project.yaml", project.root / "config" / "works" / f"{w}.yaml"]
    files += list(review.review_dir(project).glob(f"{w}__*.tsv"))
    return max((_mtime(f) for f in files), default=0.0)


def annotated(project, w: str) -> tuple[list[dict], dict, list[str]]:
    """(cặp cuối cùng, thống kê hiệu đính, ghi chú tự động) – có bộ nhớ đệm theo thời điểm sửa tệp."""
    key = ("ann", w, _inputs_mtime(project, w))
    if key not in _CACHE:
        pairs, hd = review.final_pairs(project, w)
        notes = notes_for(project, w, pairs, STATE.anchor_index()) if pairs else []
        _CACHE[key] = (pairs, hd, notes)
    return _CACHE[key]


def _xuat(project, w: str) -> tuple[Path, Path]:
    od = project.scratch(w) / "xuat"
    return od / f"{w}_parallel.tsv", od / f"{w}_parallel.xlsx"


def export_state(project, w: str) -> dict:
    """Bản xuất xem trước (work/<MA>/xuat) có sẵn, mới nhất và đạt kiểm định không."""
    tsv, xlsx = _xuat(project, w)
    if not tsv.exists() or not xlsx.exists():
        return {"ready": False, "fresh": False, "errors": []}
    fresh = min(_mtime(tsv), _mtime(xlsx)) >= _inputs_mtime(project, w)
    key = ("val", w, _mtime(tsv), _mtime(xlsx))
    if key not in _CACHE:
        _CACHE[key] = export.validate(project, w, log=lambda *a, **k: None)
    errs, warns = _CACHE[key]
    return {"ready": fresh and not errs, "fresh": fresh, "errors": errs, "warnings": warns}


def home(project) -> dict:
    works, totals = [], {}
    for w in project.works():
        has_run = (project.scratch(w) / "alignment.jsonl").exists()
        pairs, hd, notes = annotated(project, w) if has_run else ([], {}, [])
        by_m: dict[str, int] = {}
        for p in pairs:
            by_m[p["member"]] = by_m.get(p["member"], 0) + 1
            totals[p["member"]] = totals.get(p["member"], 0) + 1
        st = export_state(project, w) if has_run else {"ready": False, "fresh": False, "errors": []}
        works.append({"work": w, "title": work_title(project, w), "has_run": has_run, "pairs": len(pairs),
                      "members": by_m, "notes": sum(1 for n in notes if n),
                      "dropped": hd.get("sai", 0) if hd else 0,
                      "note_col": bool(project.work_cfg(w).get("cot_ghi_chu")),
                      "last": STATE.job.last.get(w), **st})
    return {"version": __version__, "works": works, "totals": totals, "target": TARGET,
            "members": _members(project), "code": project.code}


def pair_list(project, w: str, flt: str, q: str, offset: int, limit: int = 100) -> dict:
    pairs, _, notes = annotated(project, w)
    rows = []
    for p, n in zip(pairs, notes):
        if flt == "notes" and not n:
            continue
        if q and q not in p["han"] and q.lower() not in p["viet"].lower():
            continue
        rows.append({"key": p["khoa"], "pid": p["pid"], "vol": p["vol"], "member": p["member"],
                     "han": p["han"], "viet": p["viet"], "note": n, "hd": p.get("hd", "")})
    machine = {review.key_of(p): p for p in review.machine_pairs(project, w)}
    dropped = []
    for k, d in review.load_decisions(project, w).items():
        if d["quyet_dinh"] == "sai" and k in machine:
            m = machine[k]
            dropped.append({"key": k, "pid": m["pid"], "han": m["han"], "viet": m["viet"],
                            "nguoi": d.get("nguoi", "")})
    return {"total": len(rows), "items": rows[offset:offset + limit], "offset": offset,
            "n_all": len(pairs), "n_notes": sum(1 for n in notes if n), "dropped": dropped}


def build_zip(project, works: list[str]) -> bytes:
    """Gói đúng cấu trúc nộp của Guideline mục 2:  <MA_DE_TAI>_<MA>/01_nguon … 04_dong_hang + bao_cao.md.

    04_dong_hang lấy từ bản xuất mới nhất (work/<MA>/xuat); thư mục 04_dong_hang trong repo không bị đụng tới.
    """
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for w in works:
            top = f"{project.code}_{w}"
            wd = project.work_dir(w)
            for sub in ("01_nguon", "02_ocr_tho", "03_text_sach"):
                for f in sorted((wd / sub).rglob("*")):
                    if f.is_file():
                        z.write(f, f"{top}/{f.relative_to(wd).as_posix()}")
            for f in _xuat(project, w):
                z.write(f, f"{top}/04_dong_hang/{f.name}")
            rep = project.scratch(w) / "bao_cao.md"
            if rep.exists():
                z.write(rep, f"{top}/bao_cao.md")
    return buf.getvalue()


# ------------------------------------------------------------------ HTTP
class Handler(BaseHTTPRequestHandler):
    server_version = f"hvalign/{__version__}"

    def log_message(self, fmt, *args):  # giữ cửa sổ dòng lệnh gọn
        pass

    def _send(self, code: int, body: bytes, ctype: str):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, obj, code: int = 200):
        self._send(code, json.dumps(obj, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8")

    def _local_only(self) -> bool:
        host = (self.headers.get("Host") or "").split(":")[0]
        if host not in ("127.0.0.1", "localhost"):
            self._json({"error": "chỉ truy cập từ máy này"}, 403)
            return False
        return True

    def do_GET(self):
        if not self._local_only():
            return
        u = urlparse(self.path)
        qs = {k: v[0] for k, v in parse_qs(u.query).items()}
        P = STATE.project
        try:
            if u.path in ("/", "/index.html"):
                return self._send(200, (STATIC / "index.html").read_bytes(), "text/html; charset=utf-8")
            if u.path in ("/nang-cao", "/advanced.html"):
                return self._send(200, (STATIC / "advanced.html").read_bytes(), "text/html; charset=utf-8")
            if u.path == "/api/home":
                return self._json(home(P))
            if u.path == "/api/pairs":
                if qs["work"] not in P.works():
                    return self._json({"error": "không có tác phẩm này"}, 400)
                return self._json(pair_list(P, qs["work"], qs.get("filter", "notes"), qs.get("q", "").strip(),
                                            max(int(qs.get("offset", 0)), 0)))
            if u.path == "/api/download":
                works = [w for w in qs.get("works", "").split(",") if w]
                if not works or any(w not in P.works() for w in works):
                    return self._json({"error": "danh sách tác phẩm không hợp lệ"}, 400)
                if STATE.job.running:
                    return self._json({"error": "đang chạy một việc khác, chờ xong đã"}, 409)
                bad = [w for w in works if not export_state(P, w)["ready"]]
                if bad:
                    return self._json({"error": f"{', '.join(bad)} chưa sẵn sàng – bấm Tải về trong app để "
                                                "máy tự chuẩn bị"}, 409)
                body = build_zip(P, works)
                name = (f"{P.code}_{works[0]}" if len(works) == 1 else f"{P.code}_{len(works)}_tac_pham") + ".zip"
                self.send_response(200)
                self.send_header("Content-Type", "application/zip")
                self.send_header("Content-Disposition", f'attachment; filename="{name}"')
                self.send_header("Content-Length", str(len(body)))
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(body)
                return None
            if u.path == "/api/overview":
                return self._json(overview(P))
            if u.path == "/api/review":
                return self._json(review_items(P, qs["work"], qs.get("member", "*"), qs.get("mode", "queue"),
                                               qs.get("q", "").strip()))
            if u.path == "/api/sample":
                return self._json(sample_items(P, qs["member"]))
            if u.path == "/api/job":
                return self._json(STATE.job.state(int(qs.get("since", 0))))
            if u.path == "/api/unpaired":
                f = P.scratch(qs["work"]) / "khong_ghep.tsv"
                rows = [ln.split("\t") for ln in f.read_text(encoding="utf-8").splitlines()[1:]] if f.exists() else []
                return self._json({"rows": rows})
            self._json({"error": "không có"}, 404)
        except Exception as e:  # noqa: BLE001
            self._json({"error": f"{type(e).__name__}: {e}"}, 500)

    def do_POST(self):
        if not self._local_only():
            return
        if self.headers.get("X-HV") != "1":  # chặn trang web khác gửi lệnh tới máy chủ cục bộ
            return self._json({"error": "thiếu X-HV"}, 403)
        try:
            n = int(self.headers.get("Content-Length") or 0)
            data = json.loads(self.rfile.read(n) or b"{}")
            P = STATE.project
            path = urlparse(self.path).path
            if path == "/api/decide":
                with STATE.write_lock:
                    review.save_decision(P, data["work"], data["who"], data["key"], data["decision"],
                                         data.get("gop_voi", ""), data.get("han", ""), data.get("viet", ""),
                                         data.get("note", ""))
                return self._json({"ok": True})
            if path == "/api/grade":
                with STATE.write_lock:
                    review.save_grade(P, data["checker"], data["key"], data["work"], data["member"],
                                      data["result"], data.get("label", ""), data.get("note", ""))
                return self._json({"ok": True})
            if path == "/api/run":
                works = data.get("works") or P.works()
                bad = [w for w in works if w not in P.works()]
                if bad:
                    return self._json({"error": f"không có tác phẩm {bad}"}, 400)
                mode = data.get("mode", "run")
                if mode not in Job.MODES:
                    return self._json({"error": f"chế độ không hợp lệ: {mode}"}, 400)
                if not STATE.job.start(P, works, mode):
                    return self._json({"error": "đang chạy một việc khác, chờ xong đã"}, 409)
                return self._json({"ok": True})
            if path == "/api/open":
                return self._json({"ok": True, "path": open_path(P, data["path"])})
            self._json({"error": "không có"}, 404)
        except (ValueError, KeyError, FileNotFoundError) as e:
            self._json({"error": str(e)}, 400)
        except PermissionError as e:
            self._json({"error": f"không ghi được {e.filename or e} – tệp đang mở ở chương trình khác?"}, 400)
        except Exception as e:  # noqa: BLE001
            self._json({"error": f"{type(e).__name__}: {e}"}, 500)


def serve(project, port: int = 8765, open_browser: bool = True) -> int:
    STATE.project = project
    try:
        httpd = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    except OSError:
        print(f"✗ Cổng {port} đang bận – có thể app đã mở ở cửa sổ khác. "
              f"Mở http://127.0.0.1:{port} hoặc chạy với --cong {port + 1}")
        return 1
    url = f"http://127.0.0.1:{port}"
    print(f"hvalign {__version__} – giao diện đang chạy tại {url}\nĐóng cửa sổ này (hoặc Ctrl+C) để tắt.")
    if open_browser:
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
    return 0
