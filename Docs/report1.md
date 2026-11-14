# Report 1 – Kiểm tra Bước 1 & Bước 2

**Ngày:** 2026-11-04
**Yêu cầu:** Đọc Guideline, kiểm tra và thực hiện Bước 1 (xác nhận phạm vi), Bước 2 (kiểm kê nguồn) cho mọi tác phẩm/quyển trong `nguon_manifest.tsv`, viết ra file để tự điền vào docs nhóm.
**Sản phẩm:** [Check.md](Check.md)

## Kết quả

- **Bước 1 và Bước 2 đã xong cho 7 tác phẩm** (32 tài liệu, 64 tệp). Thông tin để điền docs, gồm các trường kiểm kê của Guideline, nằm ở Phần 1 của `Check.md`, sắp theo từng tác phẩm.
- **Tệp nguồn nguyên vẹn:** 64/64 tệp khớp SHA-256 và kích thước trong manifest; 24/24 PDF Wikisource có `oldid` trùng `revid`.
- **Đã đối chiếu lại với nguồn gốc (2026-11-04):** 24/24 wikitext khớp `sha1` của đúng phiên bản trên Wikisource và chưa trang nào có bản mới hơn; tải lại 8/8 bài sillok, thân bài giống hệt tệp trên máy; 32/32 PDF có đủ các đoạn của bản text.
- **Không cần OCR:** 32/32 PDF có lớp text, không có bản scan.
- **Hai bản khớp phạm vi**, trừ các điểm dưới đây.

## Điểm cần xử lý

| Tác phẩm | Vấn đề | Đề xuất |
|---|---|---|
| HCB_13 | Bản Việt không có mục 大理 (601 chữ), dù đầu đề trang có ghi | Chỉ dùng mục 交趾 |
| HCB_11 | 6 đoạn trong mục 南蠻 dịch rút gọn (1.726 chữ, 18,7% quyển), rủi ro lỗi `OMISSION` | Dóng từng câu; câu không có bản dịch thì ghi log, không ép vào cặp |
| HCB_05 | Link trong `nguon` trỏ tới "Quyển 1", không rõ phạm vi giao; bản Hán không có dấu câu | Tạm tính cả tác phẩm; dóng theo từng khoản |
| HCB_14 | Bản Việt chỉ dịch 8 bài trong 4 quyển | Chỉ dùng 8 bài này |

## Việc bạn cần làm

1. Đối chiếu bảng tóm tắt và Phần 1 của `Check.md` với bảng phân công của nhóm, gồm cả mã đề tài `CV02` (lấy từ tên thư mục).
2. Xác nhận phạm vi HCB_05: cả tác phẩm hay chỉ Quyển 1.
3. Thống nhất với nhóm cách xử lý chú thích ở `Check.md` mục 2.2 trước khi sang Bước 5.

## Ghi nhận cho các bước sau

- **Đầu vào Bước 4:** nên dùng `.wikitext` và `.html`. Trích text từ PDF làm mất chữ hiếm ở 5 tài liệu, ngắt dòng giữa câu và đẩy đề mục xuống cuối trang (phải dùng `sort=True` của PyMuPDF).
- **Số cặp:** trần ước tính ~3.371 cặp cấp câu, cần giữ ≥59% để đạt 2.000. Dóng cấp đoạn chỉ được ~900 cặp, không đủ.
- **File Excel mẫu chưa đúng:** cả 7 file `*_parallel.xlsx` đang có sheet `Sheet1` rỗng, trong khi Guideline yêu cầu sheet `DONG_HANG` với hai cột `Hán`, `Việt`. Tôi chưa sửa vì ngoài phạm vi phiên này.
- **Công cụ:** máy chưa có `openpyxl`, sẽ cần khi xuất Excel. Có sẵn `pymupdf` và `pypdf`.
- **Hiện trạng thư mục:** `02_ocr_tho/` trống (không áp dụng vì không OCR); `03_text_sach/*.txt` và `04_dong_hang/*.tsv` đều 0 byte.

## Cách kiểm tra và giới hạn

- Script kiểm tra chạy từ thư mục tạm của phiên và không nằm trong đồ án; phương pháp ghi ở `Check.md` mục 3.3. Chúng không sửa tệp nguồn nào.
- Có 3 cờ ban đầu là sai số của phép đo, đã loại sau khi đọc lại: can chi HCB_01 Q2 (do bản Việt viết thường và dùng "Tỵ"), đoạn Q6 và đoạn Q15 (do bản Việt tách một đoạn thành nhiều dòng).
- Các số chữ, âm tiết, câu chỉ để đo đạc, chưa qua làm sạch. Tôi không đánh giá chất lượng dịch theo từng câu, nên có thể còn câu bị lược lẻ tẻ chưa phát hiện.

## Tệp đã thay đổi trong phiên

- Tạo mới: `Docs/Check.md`, `Docs/report1.md`.
- Không sửa hay xóa tệp nào khác.

## Bước tiếp theo

Khi phạm vi đã được xác nhận: Bước 3 (sao lưu, đặt tên), rồi Bước 4 và 5 (trích text từ wikitext/HTML và làm sạch vào `03_text_sach/`).
