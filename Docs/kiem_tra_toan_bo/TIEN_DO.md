# Tiến độ kiểm tra toàn bộ

Cập nhật lần cuối: 2026-11-26. Kế hoạch và quy trình: `CLAUDE.md`, mục 5.

## Trạng thái các đợt

| Đợt | Tác phẩm | Trạng thái |
|---|---|---|
| 1 | HCB_04, 05, 07, 11, 13 | **XONG** 26/11 (report7 mục D), đã push bcaf883 |
| 2 | HCB_03, 06, 08, 09 | **XONG** 26/11 (report7 mục E), đã push 587a97a |
| 3 | HCB_02, 10, 12 | **XONG** 26/11 (report7 mục F) – chờ người dùng đồng ý sang đợt 4 |
| 4 | HCB_14 | chưa bắt đầu |
| 5 | HCB_01 quyển 1–10 | chưa bắt đầu |
| 6 | HCB_01 quyển 11–20 | chưa bắt đầu |

## Đang làm

Đợt 3 đã xong (commit cục bộ, chưa push), đang chờ người dùng đồng ý sang đợt 4. Kết quả ở `Docs/report7.md` mục F và `HCB_02/10/12.md`.

## Bước tiếp theo (đợt 4: HCB_14 – cả 4 người)

1. Bước 1–3 cho mọi quyển trong `phan_cong.tsv`. Manifest: `nguon_manifest.tsv` (Kiên), `_Huy`, `_Tai`; **các quyển của Đăng (HCB_14 q1328, 1331, 1346, 1359, 1384, 1420, 1428, 1463; HCB_01 q4, 9, 12, 13, 14, 18 – đợt 5–6) hầu như chưa có trong manifest** → thêm vào `Docs/nguon_manifest_Dang.tsv`.
2. **Bản Việt chép tay:** 18 tệp `.txt` không có đầu trang wikitext. Tải wikitext qua API (`action=query&prop=revisions&rvslots=main&formatversion=2`), so từng dòng; thiếu thì thay tệp (giữ tên) và cập nhật manifest. Bản Hán sillok: so với trang sillok (bài đã tải đợt trước, manifest Tài).
3. Đọc mọi cặp bằng `cong_cu/dump.py` (868 cặp, chia khúc ~150–200); điểm đã biết: Q1421, Q1445 lệch ranh giới (`批、所見是。` ↔ `Lại tâu:`).
4. Sửa lỗi hệ thống trước (cấu hình, nguồn, chấm câu R13 nếu nguồn Hán chấm thưa), rồi mới `cong_cu/hd.py` (tên theo người làm quyển).
5. Sau đợt: chạy lại cả 14 tác phẩm, kiểm chứng trên bản sao sạch, bàn giao, cập nhật report7 (mục G) và TIEN_DO.

Gợi ý chung: nguồn Hán chấm câu thưa (nối cả đoạn bằng ，) thì dùng R13 như HCB_02/03; script tải/so nguồn mẫu ở scratchpad đợt 3 (`fetch_live3.py`, `cmp3.py`) – viết lại nếu scratchpad đã bị xóa.

## Mốc sau đợt 3

- hvalign 0.3.3 (không đổi code), 14/14 kiểm định ĐẠT, dấu vân tay TSV `a16d2e1e586709fe`, kiểm thử 23/23.
- Số cặp: Kiên 3.463, Huy 3.498, Đăng 2.637, Tài 2.137.

## Mốc sau đợt 2

- hvalign 0.3.3, 14/14 kiểm định ĐẠT, dấu vân tay TSV `5983599663f5422a`, kiểm thử 23/23.
- Số cặp: Kiên 3.463, Huy 3.498, Đăng 2.637, Tài 2.115.

## Mốc sau đợt 1

- hvalign 0.3.2, 14/14 kiểm định ĐẠT, dấu vân tay TSV `5cc1173362968165`.
- Số cặp: Kiên 3.463, Huy 3.256, Đăng 2.637, Tài 2.115.

## Mốc trước khi kiểm tra

- hvalign 0.3.1, 14/14 tác phẩm kiểm định ĐẠT.
- Dấu vân tay TSV (14 tệp nối lại): `c42c5baf7219ce35`.
- Số cặp: Kiên 3.483, Huy 3.265, Đăng 2.640, Tài 2.114.
