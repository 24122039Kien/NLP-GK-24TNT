# Báo cáo phiên 7 – Điều chỉnh theo nhận xét của giảng viên; chuẩn bị kiểm tra toàn bộ

**Ngày:** 2026-11-26 · **hvalign:** 0.3.0 → 0.3.1

## A. Nhận xét của giảng viên về bản demo (18/11)

| Nhận xét | Đã làm |
|---|---|
| "Kết quả dóng hàng tốt, có ghi chú rõ ràng" | Giữ nguyên cách ghi chú. |
| "Cần xác nhận HCB_11 chỉ mới thực hiện 1 phần" | Bản demo chỉ trích 49 cặp đầu. Bản đầy đủ dóng toàn bộ Hậu Hán thư quyển 86, đúng phạm vi được giao: **512 cặp, độ phủ 100% chữ Hán và 100% âm tiết Việt**. Mọi `bao_cao.md` có thêm dòng phạm vi được giao, số quyển đã dóng và độ phủ, để giảng viên thấy ngay. |
| "Output cuối cùng nên có 03_text_sach (text Hán và Việt đã trích xuất, làm sạch)" | Mỗi thư mục nộp và gói `.zip` đều có `03_text_sach/han.txt` và `viet.txt`. Đã xóa 56 tệp text cũ do chương trình riêng của Tài đặt vào `03_text_sach` của HCB_01, 02, 12, 14. Các tệp này làm từ nguồn cũ (có những quyển đã thay vì sai bài), nên không khớp với dóng hàng. |
| "Nguồn không phải ảnh/PDF scan thì không cần folder 02" | Bỏ `02_ocr_tho` khỏi 14 thư mục nộp và khỏi gói `.zip`. Text thô chuyển vào `work/<MA>/02_ocr_tho` (không nộp). `bao_cao.md` ghi rõ lý do. |
| "Có thể bổ sung folder 01 (dữ liệu đã tải/crawl)" | Giữ `01_nguon`. Tệp `.pdf` trong đó là bản in trang nguồn để đối chiếu. |

Câu trả lời gợi ý cho giảng viên về HCB_11: *"Bản demo em chỉ trích 49 cặp đầu cho gọn. Bản nộp chính thức đã dóng toàn bộ quyển 86 (512 cặp, phủ 100% văn bản hai bên). Phần dịch rút gọn được ghi ở cột Ghi chú."*

## B. Thay đổi chương trình (0.3.1)

- **`config.py`:** thêm `Project.raw_dir(work)` = `work/<MA>/02_ocr_tho`.
- **`extract.py`:**
  - Bước 4 ghi text thô vào `raw_dir`.
  - Tự dọn `CV02_<MA>/02_ocr_tho` cũ. Chỉ xóa tệp do hvalign sinh ra; tệp người tự đặt vào thì giữ.
  - Thêm `harvest_sources()`.
- **`anchors.py`:** mốc tên riêng lấy thẳng từ bản Việt trong `01_nguon` của mọi tác phẩm, có cache theo chữ ký tệp. Bộ tên trùng khít bộ cũ (3.786 cặp), nên kết quả dóng không đổi, và mọi máy vẫn ra cùng kết quả.
- **`clean.py`, `__main__.py`:** đọc text thô từ `raw_dir`.
- **`app.py`, `index.html`:** gói `.zip` gồm `01_nguon`, `03_text_sach`, `04_dong_hang`, `bao_cao.md`.
- **`report.py`:** thêm phạm vi được giao, số quyển đã dóng, độ phủ (chữ Hán / âm tiết Việt), và ghi chú cấu trúc thư mục nộp.
- **`xlsxlite.py`:** `.xlsx` ghi với thời điểm cố định, nên cùng dữ liệu thì giống hệt từng byte. Trước đây mỗi lần chạy, git đều báo 14 tệp `.xlsx` bị đổi.
- **`tests/`:** thêm 2 kiểm thử (cấu trúc nộp, mốc lấy từ 01_nguon, `.xlsx` ổn định). 20/20 đạt.
- **Tài liệu:** đã cập nhật README, `huong_dan_hvalign.md` (mục 4.1, 7, 9) và thêm `CLAUDE.md`.

## C. Kiểm chứng

- 14 TSV và 28 tệp `03_text_sach` giống hệt trước khi sửa. Dấu vân tay TSV vẫn là `c42c5baf7219ce35`.
- Hai lần chạy liên tiếp: 70/70 tệp nộp giống hệt, kể cả `.xlsx` và `bao_cao.md`.
- Bản sao sạch từ git, còn `02_ocr_tho` cũ như máy chưa cập nhật: chạy xong tự dọn 14 thư mục `02_ocr_tho`, và 70/70 tệp nộp giống hệt repo.
- Số cặp không đổi: Kiên 3.483, Huy 3.265, Đăng 2.640, Tài 2.114. Kiểm định 14/14 ĐẠT.

## D. Kiểm tra toàn bộ (chưa bắt đầu)

Kế hoạch 6 đợt và quy trình ở `CLAUDE.md`, mục 5. Tiến độ ở `Docs/kiem_tra_toan_bo/TIEN_DO.md`.

Phát hiện mới: HCB_03 chỉ phủ 73,8% âm tiết Việt. Sẽ xem ở đợt 2.
