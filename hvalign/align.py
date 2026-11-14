"""Bước 7 – dóng hàng 3 tầng.

  Tầng 1  mục   : ghép đề mục theo thứ tự khi số đề mục hai bản bằng nhau; nếu không, cả quyển là một khối.
  Tầng 2  đoạn  : quy hoạch động (DP) trên các đoạn; cho phép 1–n, n–1 (đến tang2_max), 1–0, 0–1.
  Tầng 3  câu   : DP trên các đơn vị câu bên trong mỗi cặp đoạn của tầng 2.

Chi phí một kiểu ghép = −log(xác suất tiên nghiệm) + chi phí độ dài Gale–Church
                       + phạt gộp qua ranh giới câu + (mốc lệch × w) − (mốc khớp × w).
Câu không có cặp (1–0, 0–1) KHÔNG xuất ra TSV mà ghi vào work/<MA>/khong_ghep.tsv.
"""
from __future__ import annotations

import math
import statistics
from collections import Counter, defaultdict

from .anchors import AnchorIndex
from .config import ROOT
from .textutil import cjk_count, read_jsonl, viet_syllables, vol_sort_key, write_jsonl, write_tsv

TIER2_PRIORS = {(1, 1): 0.80, (1, 0): 0.01, (0, 1): 0.01, (2, 2): 0.01}


def tier2_beads(kmax: int) -> dict[tuple[int, int], float]:
    beads = dict(TIER2_PRIORS)
    for k in range(2, kmax + 1):
        beads[(1, k)] = beads[(k, 1)] = 0.08 / (k - 1) ** 1.5
    return beads


def gc_cost(l1: float, l2: float, c: float, s2: float) -> tuple[float, float]:
    """Chi phí độ dài Gale–Church; trả về (chi phí, δ)."""
    if l1 == 0 and l2 == 0:
        return 0.0, 0.0
    mean = max((l1 + l2 / c) / 2, 1.0)
    delta = (l2 - l1 * c) / math.sqrt(mean * s2)
    p = math.erfc(abs(delta) / math.sqrt(2))
    return -math.log(max(p, 1e-12)), delta


class Item:
    """Một đơn vị để dóng (câu hoặc đoạn)."""
    __slots__ = ("ids", "text", "length", "keys", "end", "flags")

    def __init__(self, ids, text, length, keys, end="hard", flags=()):
        self.ids, self.text, self.length, self.keys, self.end, self.flags = ids, text, length, keys, end, flags


def dp_align(A: list[Item], B: list[Item], beads: dict, c: float, s2: float, par: dict):
    """DP tổng quát. Trả về danh sách (i0, i1, j0, j1, chi phí, δ, khớp, lệch)."""
    n, m = len(A), len(B)
    bead_cost = {b: -math.log(p) for b, p in beads.items()}
    pa = [0]
    for x in A:
        pa.append(pa[-1] + x.length)
    pb = [0]
    for x in B:
        pb.append(pb[-1] + x.length)
    pen = {"hard": par["pen_hard"], "end": par["pen_hard"], "soft": par["pen_soft"]}

    def merge_pen(X, i0, i1):
        return sum(pen.get(X[k].end, 0.0) for k in range(i0, i1 - 1))

    def keys(X, i0, i1):
        if i1 - i0 == 1:
            return X[i0].keys
        s = set()
        for k in range(i0, i1):
            s |= X[k].keys
        return s

    def cost(i0, i1, j0, j1):
        g, d = gc_cost(pa[i1] - pa[i0], pb[j1] - pb[j0], c, s2)
        ka, kb = keys(A, i0, i1), keys(B, j0, j1)
        hit = len(ka & kb)
        miss = len(ka ^ kb)
        total = (bead_cost[(i1 - i0, j1 - j0)] + g + merge_pen(A, i0, i1) + merge_pen(B, j0, j1)
                 + par["w_miss"] * miss - par["w_hit"] * hit)
        return total, d, hit, miss

    INF = float("inf")
    D = [[INF] * (m + 1) for _ in range(n + 1)]
    back: list[list] = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0.0
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                continue
            best, arg = INF, None
            for (di, dj) in beads:
                if di > i or dj > j:
                    continue
                prev = D[i - di][j - dj]
                if prev == INF:
                    continue
                cst = cost(i - di, i, j - dj, j)
                if prev + cst[0] < best:
                    best, arg = prev + cst[0], (di, dj, cst)
            D[i][j], back[i][j] = best, arg
    out, i, j = [], n, m
    while i > 0 or j > 0:
        di, dj, cst = back[i][j]
        out.append((i - di, i, j - dj, j) + cst)
        i, j = i - di, j - dj
    return out[::-1]


def _group(units: list[dict]):
    """Gom đơn vị câu theo mục rồi theo đoạn (giữ thứ tự)."""
    secs: dict[str, dict[str, list[dict]]] = {}
    for u in units:
        secs.setdefault(u["sec"], {}).setdefault(u["block"], []).append(u)
    return secs


def run(project, work: str, log=print) -> dict:
    wcfg = project.work_cfg(work)
    ac = wcfg.get("dong_hang", {})
    scratch = project.scratch(work)
    segs = read_jsonl(scratch / "segments.jsonl")
    clean_rows = read_jsonl(scratch / "clean.jsonl")
    idx = AnchorIndex.load(ROOT)
    par = {"pen_hard": ac.get("phat_gop_qua_ranh_gioi_cung", 0.7),
           "pen_soft": ac.get("phat_gop_qua_ranh_gioi_mem", 0.0),
           "w_hit": ac.get("moc_khop", 2.0), "w_miss": ac.get("moc_lech", 0.7)}
    beads3 = {tuple(int(x) for x in k.split("-")): v for k, v in ac.get("kieu_ghep", {}).items()}
    for k in range(4, int(ac.get("gop_toi_da", 6)) + 1):  # gộp dài: danh sách nhiều ';', sillok nhiều '。'
        beads3.setdefault((1, k), 0.002 / (k - 3))
        beads3.setdefault((k, 1), 0.002 / (k - 3))
    beads2 = tier2_beads(int(ac.get("tang2_max", 8)))

    headings = defaultdict(list)  # (vol, lang) → [sec, …] theo thứ tự
    for r in clean_rows:
        if r["kind"].startswith("h"):
            headings[(r["vol"], r["lang"])].append(r["sec"])

    pairs, unpaired, stats = [], [], Counter()
    vols = sorted({s["vol"] for s in segs}, key=vol_sort_key)
    for vol in vols:
        U = {lang: [s for s in segs if s["vol"] == vol and s["lang"] == lang] for lang in ("han", "viet")}
        if not U["han"] or not U["viet"]:
            continue
        member = U["han"][0]["member"]
        items = {}
        for lang in ("han", "viet"):
            keyf = idx.han_keys if lang == "han" else idx.viet_keys
            lenf = cjk_count if lang == "han" else viet_syllables
            items[lang] = {u["id"]: Item([u["id"]], u["text"], max(lenf(u["text"]), 1), keyf(u["text"]),
                                         u["end"], tuple(u.get("flags", []))) for u in U[lang]}
        tot_h = sum(i.length for i in items["han"].values())
        tot_v = sum(i.length for i in items["viet"].values())
        c = float(ac["ty_le"]) if str(ac.get("ty_le", "auto")) != "auto" else tot_v / max(tot_h, 1)

        # ---- tầng 1: mục
        G = {lang: _group(U[lang]) for lang in ("han", "viet")}
        hs, vs = headings[(vol, "han")], headings[(vol, "viet")]
        if ac.get("tang1_muc", "auto") == "auto" and len(hs) == len(vs) and hs:
            sec_pairs = [(["s00"], ["s00"])] + [([a], [b]) for a, b in zip(hs, vs)]
            stats["tang1_ghep_muc"] += 1
        else:
            sec_pairs = [(list(G["han"]), list(G["viet"]))]
            stats["tang1_ca_quyen"] += 1

        def paragraphs(lang, secs):
            out = []
            for s in secs:
                for bid, us in G[lang].get(s, {}).items():
                    its = [items[lang][u["id"]] for u in us]
                    keys = frozenset().union(*(i.keys for i in its))
                    out.append(Item([bid], "", sum(i.length for i in its), keys, "hard",
                                    tuple(f for i in its for f in i.flags)))
            return out

        # ---- tầng 2: đoạn (2 lượt: lượt 1 ước lượng phương sai s² từ các cặp đoạn 1–1)
        s2 = float(ac["phuong_sai"]) if str(ac.get("phuong_sai", "auto")) != "auto" else 2.0
        par_pairs = []
        for rnd in range(2):
            par_pairs = []
            for hsec, vsec in sec_pairs:
                P, Q = paragraphs("han", hsec), paragraphs("viet", vsec)
                if not P and not Q:
                    continue
                for b in dp_align(P, Q, beads2, c, s2, par):
                    par_pairs.append((P[b[0]:b[1]], Q[b[2]:b[3]]))
            if rnd == 0 and str(ac.get("phuong_sai", "auto")) == "auto":
                z2 = [(sum(q.length for q in Q) - c * sum(p.length for p in P)) ** 2
                      / max((sum(p.length for p in P) + sum(q.length for q in Q) / c) / 2, 1)
                      for P, Q in par_pairs if len(P) == 1 and len(Q) == 1]
                if len(z2) >= 5:
                    s2 = max(statistics.median(z2) / 0.455, 0.3)
            else:
                break
        stats[f"s2:{vol}"] = round(s2, 2)

        # ---- tầng 3: câu
        for P, Q in par_pairs:
            if not P or not Q:
                for blk in P + Q:
                    lang = "han" if blk in P else "viet"
                    for u in G[lang][blk.ids[0].split("/")[3]][blk.ids[0]]:
                        unpaired.append((u["id"], lang, "tầng 2: cả đoạn không có cặp", u["text"]))
                stats["tang2_doan_le"] += len(P) + len(Q)
                continue
            A = [items["han"][u["id"]] for p in P for u in G["han"][p.ids[0].split("/")[3]][p.ids[0]]]
            B = [items["viet"][u["id"]] for q in Q for u in G["viet"][q.ids[0].split("/")[3]][q.ids[0]]]
            for i0, i1, j0, j1, cst, d, hit, miss in dp_align(A, B, beads3, c, s2, par):
                if i1 == i0 or j1 == j0:
                    for it, lang in [(x, "han") for x in A[i0:i1]] + [(x, "viet") for x in B[j0:j1]]:
                        unpaired.append((it.ids[0], lang, "tầng 3: câu không có cặp", it.text))
                    stats["cau_le"] += (i1 - i0) + (j1 - j0)
                    continue
                flags = sorted({f for x in A[i0:i1] for f in x.flags})
                if abs(d) > 2.5:
                    flags.append("lech_do_dai")
                if miss and not hit:
                    flags.append("lech_moc")
                if i1 - i0 > 1 and j1 - j0 > 1:
                    flags.append("n-m")
                kind = f"{i1 - i0}-{j1 - j0}"
                pairs.append({
                    "vol": vol, "member": member, "kieu": kind,
                    "han": "".join(x.text for x in A[i0:i1]),
                    "viet": " ".join(x.text for x in B[j0:j1]),
                    "han_ids": [x.ids[0] for x in A[i0:i1]], "viet_ids": [x.ids[0] for x in B[j0:j1]],
                    "chi_phi": round(cst, 3), "delta": round(d, 2), "moc_khop": hit, "moc_lech": miss,
                    "co": flags})
                stats[f"kieu:{kind}"] += 1
    for k, p in enumerate(pairs, start=1):
        p["pid"] = f"{work}:{k:05d}"
    write_jsonl(scratch / "alignment.jsonl", pairs)
    write_tsv(scratch / "khong_ghep.tsv", ["id", "ngon_ngu", "ly_do", "noi_dung"], unpaired)
    per_member = Counter(p["member"] for p in pairs)
    kinds = ", ".join(f"{k[5:]}×{v}" for k, v in sorted(stats.items(), key=lambda x: -x[1] if isinstance(x[1], int) else 0)
                      if k.startswith("kieu:"))
    log(f"  B7 {work}: {len(pairs)} cặp ({', '.join(f'{m} {n}' for m, n in per_member.items())}); "
        f"kiểu ghép: {kinds}; không ghép: {len(unpaired)} câu; "
        f"tầng 1 ghép theo mục ở {stats['tang1_ghep_muc']}/{len(vols)} quyển")
    return {"pairs": len(pairs), "per_member": dict(per_member), "unpaired": len(unpaired)}
