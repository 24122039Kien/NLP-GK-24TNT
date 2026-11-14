# Report 3 – Đánh giá hiện trạng `hvalign` và phân việc cho nhóm

**Ngày:** 2026-11-14
**Yêu cầu:** hvalign đã xong và chạy ổn chưa; phân việc cho các thành viên khác kiểm tra và sửa chương trình, để chương trình chạy được mọi tác phẩm của từng người.
**Sản phẩm:** [phan_viec_hvalign.md](phan_viec_hvalign.md)

## Hiện trạng (đã chạy lại hôm nay)

- **Đã chạy ổn trên 7 tác phẩm của Kiên:** 13/13 kiểm thử đạt; `run` hết 7 tác phẩm, 7/7 qua kiểm định; 3.490 cặp; `inventory` 0 vấn đề.
- **Chưa chạy trên nguồn thật của Huy, Tài, Đăng** vì máy này chưa có nguồn của họ.
- **Còn thiếu 5 phần chương trình:**
  1. tải bài sillok;
  2. chấm câu cho bản Hán không dấu (HCB_03);
  3. luật bỏ phiên âm trong thơ 4 phần (HCB_14);
  4. áp bản sửa từ sổ hiệu đính;
  5. bộ mẫu chuẩn và chỉnh trọng số.

## Cách phân việc

Mỗi phần còn thiếu giao cho người **có dữ liệu cần đến nó**, để người đó vừa viết vừa kiểm thử trên dữ liệu thật:

| Người | Phần chương trình | Vì sao |
|---|---|---|
| Huy | Bảng mã chữ (R09) và chấm câu thủ công cho HCB_03 | Có HCB_03, HCB_06 dùng `{{SKchar}}`; là người duy nhất có nguồn `.txt` |
| Tài | Lệnh `fetch-sillok` | Bản Hán HCB_14 của Tài chỉ có PDF; Q1358, Q1410 sai bài; Q1360 thiếu |
| Đăng | Luật R11 cho thơ 4 phần | Thơ ngự chế nằm trong HCB_14 của Đăng (Q1359) |
| Kiên | Kho git, gộp thay đổi, `review apply`, bộ mẫu chuẩn | Điều phối |

Trước phần riêng, cả 4 người làm **Đợt 1**: chạy chương trình trên tác phẩm của mình, chấm 30 cặp mẫu mỗi tác phẩm, rồi ghi kết quả vào `Docs/kiem_tra_hvalign_<ten>.md` theo mẫu có sẵn.

## Thay đổi chương trình trong phiên

| Thay đổi | Lý do |
|---|---|
| `inventory` đọc thêm mã bài `qsilok_…` trong nội dung tệp, không chỉ trong tên tệp | Nguồn HCB_14 của Huy là `.txt` gộp nhiều bài nên mã không có trong tên. Bản Việt có danh sách "Nguồn:", nên giờ phát hiện được ca nghi trùng Q1381/Q1384 |
| Lệnh mới `python -m hvalign mau --so-cap N` | Lấy ngẫu nhiên N cặp mỗi người ra Excel, có cột Đúng/Sai và nhãn lỗi, để cả nhóm đo chất lượng giống nhau |

Đã kiểm tra lại sau thay đổi: 13/13 kiểm thử đạt, `inventory` vẫn 0 vấn đề trên dữ liệu của Kiên (không sinh cảnh báo trùng giả), `mau` chạy được trên HCB_07.

## Việc bạn cần làm

1. **Tạo kho git riêng tư cho `Lab/GK`** và mời 3 bạn. Đợt 1 cần kho này. Thư mục hiện chưa phải kho git.
2. Gửi [phan_viec_hvalign.md](phan_viec_hvalign.md) cho nhóm và chốt thứ tự ở mục 6. Hạn chót do nhóm tự đặt.
3. Các quyết định ở mục 11 của kế hoạch vẫn chưa chốt. Phân việc này dựa trên đề xuất mặc định (ví dụ HCB_12 chỉ dóng chính văn nếu không tìm được bản có chú).

## Tệp đã thay đổi

- **Tạo:** `Docs/phan_viec_hvalign.md`, `Docs/report3.md`.
- **Sửa:**
  - `hvalign/inventory.py` (dò mã sillok trong nội dung);
  - `hvalign/export.py` (hàm `sample`);
  - `hvalign/__main__.py` (lệnh `mau`, tham số `--so-cap`);
  - `Docs/huong_dan_hvalign.md` (thêm lệnh `mau` và link phân việc).
- **Sinh ra:** `work/HCB_07/mau/HCB_07_mau_30.xlsx` (chạy thử).
