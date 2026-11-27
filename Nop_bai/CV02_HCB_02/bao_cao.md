# Báo cáo tự sinh – HCB_02

Ngày: 2026-11-27 · hvalign 0.3.5 · **Trạng thái: dóng tự động, ghi chú tự động**

## 1. Số cặp

Tổng: **49** cặp.

| Thành viên | Số cặp |
|---|---|
| Tai | 49 |

| Quyển | Thành viên | Số cặp |
|---|---|---|
| 1 | Tai | 49 |

Kiểu ghép: `1-1` 49

- Phạm vi được giao (`config/phan_cong.tsv`): **cả tác phẩm** (Tai); quyển có trong nguồn và đã dóng: 1.
- Độ phủ: các cặp chứa **100.0%** số chữ Hán và **100.0%** số âm tiết Việt của `03_text_sach` (phần chưa phủ là câu không ghép được hoặc cặp bỏ khi hiệu đính; phần chỉ một bản có đã bị loại trừ từ Bước 5, không tính ở đây).

## 2. Số dòng văn bản sạch

- `03_text_sach/han.txt`: 1 dòng
- `03_text_sach/viet.txt`: 17 dòng
- Thư mục nộp: `01_nguon` (dữ liệu đã tải/crawl), `03_text_sach` (text Hán và Việt đã trích xuất và làm sạch), `04_dong_hang` (TSV + XLSX), `bao_cao.md`. Không có `02_ocr_tho`: nguồn là text số (wikitext/HTML/txt), không phải ảnh/PDF scan, nên không OCR (theo nhận xét của giảng viên 18/11). Tệp `.pdf` trong `01_nguon` là bản in của trang nguồn, lưu để đối chiếu.

## 3. Kết quả tự kiểm tra

- Kiểm định định dạng TSV/XLSX: **đạt**
- Luật làm sạch đã áp dụng: R03_bo_ref ×1, R12_loai_tru ×56, R13_cham_cau_thu_cong ×1
- Loại trừ (không có bản dịch / không phải chính văn): 56 khối – Bảng nguyên văn chữ Hán + phiên âm, không phải bản dịch (9); Phụ ghi trích Minh thực lục – bản Hán không có (47)
- Câu không ghép được (ghi ở `work/HCB_02/khong_ghep.tsv`, không đưa vào TSV): 0
- Cặp máy gắn cờ: 10 (`lech_moc` 10); người đã xem 0
- Hiệu đính đã áp: xác nhận đúng 0, sửa chữ 0, gộp 0, bỏ cặp sai 0 (quyết định lưu ở `hieu_dinh/HCB_02__<người>.tsv`)
- Cảnh báo khi làm sạch: 0 (xem `work/HCB_02/canh_bao.tsv`)
- Ghi chú tự động (dịch rút gọn, vế Việt thêm diễn giải, câu không được dịch): 0 cặp, ghi ở cột `Ghi chú` của sheet TRUY_VET
- Phạm vi theo trả lời của giảng viên: chỉ dóng hàng phần có song ngữ; phần chỉ một bản có thì không đưa vào dữ liệu (đã liệt kê ở mục Loại trừ và Câu không ghép được).
- Tỷ lệ lỗi theo §8 Guideline: chưa chấm mẫu (tuỳ chọn: app → Nâng cao → Chấm mẫu).

## 4. Nguồn tài liệu

| Quyển | Bản | Tệp | Định dạng đọc được | Nguồn trực tuyến | revid |
|---|---|---|---|---|---|
| 1 | han | `平安南詔.wikitext` | wikitext | https://zh.wikisource.org/wiki/%E5%B9%B3%E5%AE%89%E5%8D%97%E8%A9%94 | 1808602 |
| 1 | viet | `Biên_dịch_Bình_An_Nam_chiếu.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:B%C3%ACnh_An_Nam_chi%E1%BA%BFu | 195870 |

## 5. Công cụ

- `hvalign` 0.3.5 (Lab/GK/hvalign), Python 3.12.6, PyYAML.
- Bước 4: tự nhận dạng định dạng nguồn (wikitext / text thuần / HTML sillok) và chuẩn hóa về một dạng.
- Bước 7: dóng 3 tầng (mục → đoạn → câu), chi phí Gale–Church + mốc can chi và tên riêng Hán Việt.
- Cấu hình: `config/project.yaml`, `config/works/HCB_02.yaml`, `config/phan_cong.tsv`.
