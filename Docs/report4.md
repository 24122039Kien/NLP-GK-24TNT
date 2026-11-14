# Report 4 – Đưa lên git và viết hướng dẫn thực hành `hvalign`

**Ngày:** 2026-11-14

**Yêu cầu:**
- Đưa thư mục lên repo GitHub của nhóm, rồi bỏ dòng ghi công Claude khỏi lịch sử commit.
- Viết hướng dẫn sử dụng `hvalign` theo kiểu thực hành.

**Sản phẩm:**
- Repo: https://github.com/24122039Kien/NLP-GK-24TNT
- Hướng dẫn: [huong_dan_hvalign.md](huong_dan_hvalign.md), viết lại hoàn toàn.

## Kết quả

### Git

- Đã đưa `Lab/GK` lên nhánh `main`: 165 tệp trong commit `3b806b6`, không có dòng Co-Authored-By.
- Thông tin cá nhân:
  - Repo dùng email ẩn danh của GitHub, vì tài khoản chặn push làm lộ email cá nhân.
  - Email Gmail không xuất hiện trên GitHub.
  - Cấu hình git chung trên máy không bị đổi.
- `.gitattributes` giữ nguyên từng byte của `01_nguon/`. Đã clone thử về một thư mục mới: 13/13 kiểm thử đạt, `inventory` 0 vấn đề (SHA-256 vẫn khớp manifest).
- Danh sách contributor trên GitHub (theo API) chỉ còn `24122039Kien`.

### Hướng dẫn thực hành

Hướng dẫn mới được viết theo các việc thật phải làm:
- chuẩn bị máy;
- đưa nguồn vào;
- chạy và đọc từng dòng đầu ra;
- kiểm tra kết quả theo thứ tự các bước;
- 8 tình huống sửa bằng cấu hình (5A–5H);
- hiệu đính, bàn giao;
- bảng xử lý lỗi;
- quy trình git.

Mọi ví dụ đầu ra đều chép từ lần chạy thật, kể cả ví dụ trước/sau cấu hình loại trừ ở HCB_13:

| | Không có cấu hình loại trừ | Có cấu hình |
|---|---|---|
| Cặp chứa câu của mục 大理 (bản Việt không dịch) | 6 | 0 |
| Câu không ghép | 3 | 0 |

## Lỗi chương trình phát hiện khi viết hướng dẫn và đã sửa

Để viết bảng xử lý lỗi, tôi giả lập các lỗi người mới hay gặp trên một bản clone riêng. Việc này lộ ra 5 vấn đề:

| Vấn đề | Trước | Sau |
|---|---|---|
| Tệp nguồn không phải UTF-8 (thử bằng Big5) | Dừng với Traceback; chữ tiếng Việt trong thông báo bị vỡ | `✗ X.txt: không phải UTF-8 … Mở tệp bằng Notepad / VS Code rồi lưu lại với mã hóa UTF-8.` |
| Thiếu bản Việt nên ra 0 cặp | Kiểm định vẫn báo **ĐẠT** | Báo `1 LỖI: không có cặp nào – kiểm tra nguồn …` |
| Chạy `align` khi chưa chạy các bước trước | Traceback | Nhắc chạy các bước trước, hoặc dùng `run --work …` |
| File Excel kết quả đang mở | Traceback | Nhắc đóng Excel rồi chạy lại (đã thử bằng cách khóa tệp) |
| `member:` khai báo trong `sources:` của cấu hình bị bỏ qua | Cặp hiện dưới tên `chua_phan_cong` | Bước 5 đọc tên thành viên do Bước 4 ghi trong tệp text thô |

Ngoài ra còn hai điều chỉnh khác:
- **Bỏ số phiên bản khỏi dòng đầu tệp `02_ocr_tho/*.tsv`.** Trước đây mỗi lần nâng phiên bản là toàn bộ tệp sinh ra bị đổi, và git sẽ báo xung đột vô nghĩa khi 4 người dùng các phiên bản khác nhau. Lần commit tới, 28 tệp này đổi một lần rồi sẽ ổn định.
- **Phiên bản chương trình nâng lên 0.1.1.** Có thêm 1 kiểm thử cho lỗi mã hóa, tổng 14/14 đạt.

Kết quả trên dữ liệu của Kiên không đổi: vẫn 3.490 cặp, 7/7 tác phẩm đạt kiểm định.

## Việc bạn cần làm

1. **Mời Huy, Tài, Đăng** vào repo (Settings → Collaborators).
2. **Các thay đổi trong report này chưa được commit.** Đẩy lên thì các bạn mới thấy hướng dẫn mới.

## Tệp đã thay đổi (chưa commit)

- **Viết lại:** `Docs/huong_dan_hvalign.md`.
- **Tạo mới:** `Docs/report4.md`.
- **Sửa:**
  - `hvalign/__init__.py` (phiên bản 0.1.1);
  - `hvalign/__main__.py` (báo lỗi dễ hiểu);
  - `hvalign/clean.py` (lấy tên thành viên từ tệp text thô);
  - `hvalign/export.py` (lỗi khi ra 0 cặp);
  - `hvalign/extract.py` (bỏ số phiên bản ở dòng đầu);
  - `hvalign/textutil.py` (thông báo lỗi mã hóa);
  - `tests/test_pipeline.py` (+1 kiểm thử);
  - `Docs/phan_viec_hvalign.md` (link repo, số kiểm thử, việc tạo kho git đã xong).
- **Sinh lại:** 28 tệp `CV02_*/02_ocr_tho/*.tsv`, chỉ đổi dòng đầu.
