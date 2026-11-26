# Tiến độ kiểm tra toàn bộ

Cập nhật lần cuối: 2026-11-26. Kế hoạch và quy trình: `CLAUDE.md`, mục 5.

## Trạng thái các đợt

| Đợt | Tác phẩm | Trạng thái |
|---|---|---|
| 1 | HCB_04, 05, 07, 11, 13 | **XONG** 26/11 (report7 mục D), đã push bcaf883 |
| 2 | HCB_03, 06, 08, 09 | **XONG** 26/11 (report7 mục E), đã push 587a97a |
| 3 | HCB_02, 10, 12 | **XONG** 26/11 (report7 mục F), đã push 32db2ae |
| 4 | HCB_14 | **XONG** 26/11 (report7 mục G) – chờ người dùng đồng ý sang đợt 5 |
| 5 | HCB_01 quyển 1–10 | chưa bắt đầu |
| 6 | HCB_01 quyển 11–20 | chưa bắt đầu |

## Đang làm

Đợt 4 đã xong (commit cục bộ, chưa push), đang chờ người dùng đồng ý sang đợt 5. Kết quả ở `Docs/report7.md` mục G và `HCB_14.md`.

## Bước tiếp theo (đợt 5: HCB_01 quyển 1–10)

1. Bước 1–3 cho từng quyển. Phân công ở `phan_cong.tsv`: Tài q1, 8; Huy q3, 5, 7; Đăng q4, 9; Kiên q2, 6, 10.
   - Bản Việt chép tay (`.txt`) phải so với wikitext tải qua API (`action=query&prop=revisions&rvslots=main&formatversion=2`). Lưu ý: tệp có thể thiếu dấu "* " mà vẫn đủ nội dung.
   - Nguồn của Đăng (q4, 9) hầu như chưa có trong manifest, cần thêm vào `Docs/nguon_manifest_Dang.tsv`.
   - Nếu wikisource báo 429 thì giãn cách 8 giây và thử lại.
2. Đọc mọi cặp bằng `cong_cu/dumpq.py HCB_01 <quyển>`. Chỗ lệch thì chia lại bằng `cong_cu/chia_lai.py` (dạng `HB:`), ghi đúng tên người theo phân công. Câu Việt không có vế Hán thì tìm phần nguồn còn thiếu trước.
3. HCB_01 có khoảng 8.094 cặp, nên chia theo quyển và ghi tiến độ sau mỗi quyển.
4. Sau đợt: chạy lại cả 14 tác phẩm, kiểm `khong_khop`, kiểm chứng trên bản sao sạch, bàn giao, cập nhật report7 (mục H) và TIEN_DO.
5. Ổ C: (thư mục tạm) gần đầy. Mỗi lần kiểm chứng xong thì xóa bản sao sạch cũ trong scratchpad.

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
