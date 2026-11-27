# Tiến độ kiểm tra toàn bộ

Cập nhật lần cuối: 2026-11-27. Kế hoạch và quy trình: `CLAUDE.md`, mục 5.

## Trạng thái các đợt

| Đợt | Tác phẩm | Trạng thái |
|---|---|---|
| 1 | HCB_04, 05, 07, 11, 13 | **XONG** 26/11 (report7 mục D), đã push bcaf883 |
| 2 | HCB_03, 06, 08, 09 | **XONG** 26/11 (report7 mục E), đã push 587a97a |
| 3 | HCB_02, 10, 12 | **XONG** 26/11 (report7 mục F), đã push 32db2ae |
| 4 | HCB_14 | **XONG** 26/11 (report7 mục G), đã push 3142d80 |
| 5 | HCB_01 quyển 1–10 | **XONG** 27/11 (report7 mục H), đã push 5123b3e |
| 6 | HCB_01 quyển 11–20 | **XONG** 27/11 (report7 mục I), đã commit (chưa push) |

## Đang làm

Không có việc dở. **Kiểm tra toàn bộ đã xong cả 6 đợt**: mọi cặp của 14 tác phẩm đã được đọc. Chi tiết HCB_01 ở `Docs/kiem_tra_toan_bo/HCB_01.md`.

Nếu sau này sửa code hay cấu hình làm máy dóng lại:
1. Chạy `python -m hvalign run`.
2. Kiểm `khong_khop = 0`. Nếu lệch, xóa quyết định của quyển đó và áp lại tệp khúc ở `khuc/`.
3. Kiểm chứng trên bản sao sạch ở `GK_tam`, rồi bàn giao bằng `GK_tam/deliver_all.py`.

## Mốc sau đợt 6

- hvalign 0.3.5 (không đổi code), 14/14 kiểm định ĐẠT, `khong_khop = 0`, dấu vân tay TSV `afb9a88ede60aa8b`, kiểm thử 24/24.
- Số cặp: Kiên 3.463, Huy 3.502, Đăng 2.663, Tài 2.149. HCB_01: 8.092 cặp; 81 quyết định hiệu đính.

## Mốc sau khi bỏ ô ngày trong `.xlsx` (27/11)

- hvalign 0.3.5 (bỏ ô "Ngày xuất", report7 mục H1), 14/14 kiểm định ĐẠT, dấu vân tay TSV `3881da12c970ac7b` (không đổi), kiểm thử 24/24. Số cặp không đổi.

## Mốc sau đợt 5

- hvalign 0.3.4 (không đổi code), 14/14 kiểm định ĐẠT, `khong_khop = 0`, dấu vân tay TSV `3881da12c970ac7b`, kiểm thử 24/24.
- Số cặp: Kiên 3.463, Huy 3.502, Đăng 2.663, Tài 2.149. HCB_01: 8.092 cặp; 40 quyết định hiệu đính.

## Mốc sau đợt 4

- hvalign 0.3.4, 14/14 kiểm định ĐẠT, dấu vân tay TSV `904a47c9d0bec7a3`, kiểm thử 24/24.
- Số cặp: Kiên 3.463, Huy 3.504, Đăng 2.663, Tài 2.149.

## Mốc sau đợt 3

- hvalign 0.3.3 (không đổi code), 14/14 kiểm định ĐẠT, dấu vân tay TSV `5abc170b74b6ee51`, kiểm thử 23/23.
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
