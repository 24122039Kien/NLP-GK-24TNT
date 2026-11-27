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
| 6 | HCB_01 quyển 11–20 | chưa bắt đầu (chờ người dùng đồng ý) |

## Đang làm

Không có việc dở. Đợt 5 đã xong và đã kiểm chứng; chi tiết ở `Docs/kiem_tra_toan_bo/HCB_01.md`.

## Bước tiếp theo (đợt 6: HCB_01 quyển 11–20)

Số # (theo TSV sau đợt 5, tổng 8.092 cặp) và người phụ trách:

| Quyển | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| Người | Huy | Dang | Dang | Dang | Kien | Huy | Tai | Dang | Tai | Kien |
| # | 4286–4688 | 4689–5100 | 5101–5474 | 5475–5811 | 5812–6163 | 6164–6541 | 6542–6892 | 6893–7307 | 7308–7771 | 7772–8092 |

1. Bước 1–3: tải lại 20 trang qua API wikisource vào `Lab/GK_tam/dot6_live` và so với `01_nguon`. Bổ sung manifest còn thiếu, nhất là của Đăng (q12, 13, 14, 18). Nếu wikisource báo 429 thì giãn cách 5–8 giây.
2. Đọc mọi cặp bằng `cong_cu/dumpc.py HCB_01 a b`, mỗi lượt khoảng 115 cặp, ghi vào `GK_tam/doc.txt` rồi đọc. Ghi tiến độ vào đây sau mỗi khúc.
3. Sửa:
   - Chỗ trượt ranh giới: dùng `chia_lai.py` với tệp khúc `khuc/HCB_01/q<quyển>_<x>.txt`, đúng tên người.
   - Lỗi chữ lẻ: dùng `hd.py … sua`.
   - Chữ ghép bộ đã biết: #6686 钅屈, #7157 và #7358 鹿阝 (= 鄜), #7451 扌捲. Kiểm lại số # trước khi sửa, vì có thể đã dời.
   - Xem kỹ chỗ chuyển đời vua: tiêu đề đế hiệu trong nguồn zh đặt sau đoạn tiểu sử.
4. Sau đợt: chạy lại 14 tác phẩm, kiểm `khong_khop`, kiểm chứng trên bản sao sạch ở GK_tam, bàn giao (`GK_tam/deliver_all.py`). `git checkout` lại `bao_cao.md` của tác phẩm chỉ đổi ngày (từ 0.3.5 `.xlsx` không còn ô ngày). Cập nhật report7 (mục I), HCB_01.md và TIEN_DO.

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
