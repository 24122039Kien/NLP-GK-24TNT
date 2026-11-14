"""Tải nguồn Hán/Việt của 7 mã tác phẩm vào <MA_DE_TAI>_<MA_TAC_PHAM>/01_nguon/{han,viet}.

- Trang Wikisource: lưu PDF (chức năng "Tải về dạng PDF" của Wikisource) và wikitext gốc.
- HCB_14 bản Hán: lấy từ các bài trên sillok.history.go.kr mà trang tiếng Việt dẫn nguồn,
  lưu HTML gốc và PDF in bằng Chrome/Edge headless.
- File đã có thì giữ nguyên, không ghi đè. Kết quả ghi vào Docs/nguon_manifest.tsv.

Chạy lại: python tai_nguon.py   (cần: pypdf)
"""
import csv
import datetime
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import pypdf

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "Docs" / "nguon_manifest.tsv"
UA = "HanVietAlignStudentProject/1.0 (university NLP course project)"
GAP = 3.0
VI = "vi.wikisource.org"
ZH = "zh.wikisource.org"
BROWSERS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]
TCTTG_QUYEN = [2, 6, 10, 15, 20]
TTL_QUYEN = [1333, 1339, 1357, 1438]
TTL_VI = "Biên dịch:Thanh thực lục/Cao Tông Thuần Hoàng đế thực lục/Quyển {}"

# Mã tác phẩm -> (trang Việt, trang Hán). None = bản Hán không nằm trên Wikisource.
WORKS = {
    "HCB_01": [(f"Tục tư trị thông giám/Quyển {q}", f"續資治通鑑/卷{q:03d}") for q in TCTTG_QUYEN],
    "HCB_04": [("Biên dịch:Gián phạt Nam Việt thư", "諫伐南越書")],
    "HCB_05": [("Biên dịch:Giao Châu ký", "交州記 (嶺南遺書本)")],
    "HCB_07": [("Biên dịch:Hán thư/Quyển 095", "漢書/卷095")],
    "HCB_11": [("Biên dịch:Hậu Hán thư/Quyển 86", "後漢書/卷86")],
    "HCB_13": [("Biên dịch:Tống sử/Quyển 488", "宋史/卷488")],
    "HCB_14": [(TTL_VI.format(q), None) for q in TTL_QUYEN],
}

_last = 0.0


def fetch(url, tries=6):
    global _last
    for i in range(tries):
        wait = _last + GAP - time.time()
        if wait > 0:
            time.sleep(wait)
        _last = time.time()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=300) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and i < tries - 1:
                ra = e.headers.get("Retry-After")
                s = int(ra) if ra and ra.isdigit() else 30 * (i + 1)
                print(f"  [{e.code}] chờ {s}s", flush=True)
                time.sleep(s)
                continue
            raise


def get_page(host, title):
    params = dict(action="query", prop="revisions", rvprop="content|timestamp|ids", rvslots="main",
                  titles=title, redirects=1, format="json", formatversion=2)
    data = json.loads(fetch(f"https://{host}/w/api.php?" + urllib.parse.urlencode(params)))
    p = data["query"]["pages"][0]
    if p.get("missing"):
        raise RuntimeError(f"Không có trang: {host} {title}")
    return p


def safe_name(title):
    return re.sub(r"[:/ ]+", "_", title)


def pdf_pages(path):
    return len(pypdf.PdfReader(str(path)).pages)


def record(rows, ma, lang, path, url, title, revid="", ts=""):
    data = path.read_bytes()
    rows.append({
        "ma_tac_pham": ma, "ngon_ngu": lang, "tieu_de": title, "url": url,
        "revid": revid, "rev_timestamp": ts,
        "tep": path.relative_to(ROOT).as_posix(),
        "dinh_dang": path.suffix.lstrip("."),
        "so_trang": pdf_pages(path) if path.suffix == ".pdf" else "",
        "so_byte": len(data), "sha256": hashlib.sha256(data).hexdigest(),
        "ngay_tai": datetime.date.today().isoformat(),
    })


def download_wiki(rows, ma, lang, host, title):
    out = ROOT / f"CV02_{ma}" / "01_nguon" / ("viet" if lang == "Việt" else "han")
    p = get_page(host, title)
    rev = p["revisions"][0]
    wikitext = rev["slots"]["main"]["content"]
    name = safe_name(p["title"])
    url = f"https://{host}/wiki/" + urllib.parse.quote(p["title"].replace(" ", "_"), safe="/:")

    txt = out / f"{name}.wikitext"
    if not txt.exists():
        txt.write_text(wikitext, encoding="utf-8", newline="\n")
    record(rows, ma, lang, txt, url, p["title"], rev["revid"], rev["timestamp"])

    pdf = out / f"{name}.pdf"
    if not pdf.exists():
        quoted = urllib.parse.quote(p["title"].replace(" ", "_"), safe="")
        data = fetch(f"https://{host}/api/rest_v1/page/pdf/{quoted}")
        if not data.startswith(b"%PDF"):
            raise RuntimeError(f"Không phải PDF: {title}")
        pdf.write_bytes(data)
    record(rows, ma, lang, pdf, url, p["title"], rev["revid"], rev["timestamp"])
    print(f"  {lang}: {name} (rev {rev['revid']})", flush=True)
    return wikitext


def print_pdf(browser, url, pdf, tries=4, timeout=90):
    for i in range(tries):
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as profile:
            proc = subprocess.Popen([browser, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                                     "--no-first-run", "--disable-extensions", f"--user-data-dir={profile}",
                                     "--virtual-time-budget=15000", f"--print-to-pdf={pdf}", url],
                                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            try:
                proc.wait(timeout=timeout)
            except subprocess.TimeoutExpired:
                subprocess.run(["taskkill", "/PID", str(proc.pid), "/T", "/F"], capture_output=True)
                proc.wait()
                print(f"  [chrome treo] thử lại {i + 1}/{tries}", flush=True)
        if pdf.exists() and pdf.read_bytes().startswith(b"%PDF") and pdf_pages(pdf) > 0:
            return
        pdf.unlink(missing_ok=True)
        time.sleep(10)
    raise RuntimeError(f"Không in được PDF: {url}")


def write_manifest(rows):
    with MANIFEST.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter="\t")
        w.writeheader()
        w.writerows(rows)


def download_sillok(rows, ma, wikitext, quyen):
    out = ROOT / f"CV02_{ma}" / "01_nguon" / "han"
    browser = next(b for b in BROWSERS if Path(b).exists())
    for url in re.findall(r"https://sillok\.history\.go\.kr/mc/id/[\w]+", wikitext):
        art = url.rsplit("/", 1)[-1]
        base = f"清實錄_高宗純皇帝實錄_卷{quyen}_{art}"
        html = out / f"{base}.html"
        if not html.exists():
            html.write_bytes(fetch(url))
        record(rows, ma, "Hán", html, url, f"高宗純皇帝實錄 卷{quyen} {art}")
        pdf = out / f"{base}.pdf"
        if not pdf.exists():
            print_pdf(browser, url, pdf)
            time.sleep(GAP)
        record(rows, ma, "Hán", pdf, url, f"高宗純皇帝實錄 卷{quyen} {art}")
        print(f"  Hán: {base}", flush=True)


def main():
    rows = []
    try:
        for ma, pairs in WORKS.items():
            print(ma, flush=True)
            for vi_title, zh_title in pairs:
                wikitext = download_wiki(rows, ma, "Việt", VI, vi_title)
                if zh_title:
                    download_wiki(rows, ma, "Hán", ZH, zh_title)
                else:
                    download_sillok(rows, ma, wikitext, vi_title.rsplit(" ", 1)[-1])
    finally:
        write_manifest(rows)
    print(f"Xong: {len(rows)} tệp, manifest: {MANIFEST}", flush=True)


if __name__ == "__main__":
    main()
