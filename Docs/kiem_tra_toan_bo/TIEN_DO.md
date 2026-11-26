# Tiến độ kiểm tra toàn bộ

Cập nhật lần cuối: 2026-11-26. Kế hoạch và quy trình: `CLAUDE.md`, mục 5.

## Trạng thái các đợt

| Đợt | Tác phẩm | Trạng thái |
|---|---|---|
| 1 | HCB_04, 05, 07, 11, 13 | **XONG** 26/11 (report7 mục D) – chờ người dùng đồng ý sang đợt 2 |
| 2 | HCB_03, 06, 08, 09 | chưa bắt đầu |
| 3 | HCB_02, 10, 12 | chưa bắt đầu |
| 4 | HCB_14 | chưa bắt đầu |
| 5 | HCB_01 quyển 1–10 | chưa bắt đầu |
| 6 | HCB_01 quyển 11–20 | chưa bắt đầu |

## Đang làm

Đợt 1 đã xong, đang chờ người dùng đồng ý sang đợt 2. Kết quả ở `Docs/report7.md` mục D.

## Bước tiếp theo (đợt 2: HCB_03, 06, 08, 09 – phần của Huy)

1. Bước 1–3 cho cả 4 tác phẩm, làm giống đợt 1 (SHA với manifest `Docs/nguon_manifest_Huy.tsv`).
2. HCB_03: chỉ có 8 cặp là đoạn dài, độ phủ âm tiết Việt khoảng 74%. Bản Hán không có dấu câu, cần chấm câu, hoặc dóng theo đơn vị khác. Xem `Docs/phan_viec_hvalign.md` (việc chấm câu của Huy).
3. Đọc mọi cặp bằng `PYTHONPATH=. python Docs/kiem_tra_toan_bo/cong_cu/dump.py HCB_06 1 80`. Sửa bằng `cong_cu/hd.py`, ghi tên `Huy`.
4. Sau đợt: chạy lại, bàn giao, kiểm chứng trên bản sao sạch, cập nhật report7 và TIEN_DO.

## Mốc sau đợt 1

- hvalign 0.3.2, 14/14 kiểm định ĐẠT, dấu vân tay TSV `5cc1173362968165`.
- Số cặp: Kiên 3.463, Huy 3.256, Đăng 2.637, Tài 2.115.

## Mốc trước khi kiểm tra

- hvalign 0.3.1, 14/14 tác phẩm kiểm định ĐẠT.
- Dấu vân tay TSV (14 tệp nối lại): `c42c5baf7219ce35`.
- Số cặp: Kiên 3.483, Huy 3.265, Đăng 2.640, Tài 2.114.
