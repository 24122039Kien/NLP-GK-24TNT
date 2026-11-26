# Tiến độ kiểm tra toàn bộ

Cập nhật lần cuối: 2026-11-26. Kế hoạch và quy trình: `CLAUDE.md`, mục 5.

## Trạng thái các đợt

| Đợt | Tác phẩm | Trạng thái |
|---|---|---|
| 1 | HCB_04, 05, 07, 11, 13 | **XONG** 26/11 (report7 mục D), đã push bcaf883 |
| 2 | HCB_03, 06, 08, 09 | **XONG** 26/11 (report7 mục E) – chờ người dùng đồng ý sang đợt 3 |
| 3 | HCB_02, 10, 12 | chưa bắt đầu |
| 4 | HCB_14 | chưa bắt đầu |
| 5 | HCB_01 quyển 1–10 | chưa bắt đầu |
| 6 | HCB_01 quyển 11–20 | chưa bắt đầu |

## Đang làm

Đợt 2 đã xong (chưa commit), đang chờ người dùng đồng ý sang đợt 3. Kết quả ở `Docs/report7.md` mục E và `HCB_03/06/08/09.md`.

## Bước tiếp theo (đợt 3: HCB_02, 10, 12 – Tài, Đăng)

1. Bước 1–3 cho cả 3 tác phẩm (manifest `Docs/nguon_manifest_Tai.tsv` / `_Dang.tsv`).
2. **Bài học đợt 2:** bản Việt mà thành viên chép từ trang hiển thị (tệp `.txt` không có `{{đầu đề…}}`) có thể **mất khối `<div>`, `<poem>`, `{{quote}}`**. Phải tải wikitext qua API (`action=query&prop=revisions&rvslots=main`), so từng dòng với tệp đang có, thiếu thì thay tệp (giữ tên) và cập nhật manifest. Đợt 4–6 (HCB_14, HCB_01) cũng phải làm bước này: HCB_01 có 14 tệp Việt, HCB_14 có 18 tệp không có đầu trang wikitext.
3. Đọc mọi cặp bằng `cong_cu/dump.py`; sửa lỗi hệ thống trước (cấu hình, nguồn), rồi mới `cong_cu/hd.py` (tên `Tai` / `Dang`).
4. Sau đợt: chạy lại cả 14 tác phẩm, kiểm chứng trên bản sao sạch, bàn giao, cập nhật report7 (mục F) và TIEN_DO.

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
