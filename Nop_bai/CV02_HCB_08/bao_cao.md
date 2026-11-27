# Báo cáo tự sinh – HCB_08

Ngày: 2026-11-27 · hvalign 0.3.5 · **Trạng thái: dóng tự động, ghi chú tự động; người đã xem 1/48 cặp máy gắn cờ**

## 1. Số cặp

Tổng: **481** cặp.

| Thành viên | Số cặp |
|---|---|
| Huy | 481 |

| Quyển | Thành viên | Số cặp |
|---|---|---|
| 24 | Huy | 481 |

Kiểu ghép: `1-1` 431, `1-2` 35, `2-1` 6, `1-3` 6, `2-3` 2, `4-2` 1

- Phạm vi được giao (`config/phan_cong.tsv`): **cả tác phẩm** (Huy); quyển có trong nguồn và đã dóng: 24.
- Độ phủ: các cặp chứa **100.0%** số chữ Hán và **100.0%** số âm tiết Việt của `03_text_sach` (phần chưa phủ là câu không ghép được hoặc cặp bỏ khi hiệu đính; phần chỉ một bản có đã bị loại trừ từ Bước 5, không tính ở đây).

## 2. Số dòng văn bản sạch

- `03_text_sach/han.txt`: 66 dòng
- `03_text_sach/viet.txt`: 99 dòng
- Thư mục nộp: `01_nguon` (dữ liệu đã tải/crawl), `03_text_sach` (text Hán và Việt đã trích xuất và làm sạch), `04_dong_hang` (TSV + XLSX), `bao_cao.md`. Không có `02_ocr_tho`: nguồn là text số (wikitext/HTML/txt), không phải ảnh/PDF scan, nên không OCR (theo nhận xét của giảng viên 18/11). Tệp `.pdf` trong `01_nguon` là bản in của trang nguồn, lưu để đối chiếu.

## 3. Kết quả tự kiểm tra

- Kiểm định định dạng TSV/XLSX: **đạt**
- Luật làm sạch đã áp dụng: R03_bo_ref ×9, R06_bo_chu_han_trong_viet ×67, R07_bo_nam_duong_lich ×23, R10_chuan_hoa_khoang_trang_dau_cau ×2, R12_loai_tru ×3
- Loại trừ (không có bản dịch / không phải chính văn): 3 khối – Lời giải thích của dịch giả cho bài Tán, bản Hán không có (3)
- Câu không ghép được (ghi ở `work/HCB_08/khong_ghep.tsv`, không đưa vào TSV): 0
- Cặp máy gắn cờ: 48 (`lech_moc` 47, `lech_do_dai` 1); người đã xem 1
- Hiệu đính đã áp: xác nhận đúng 0, sửa chữ 0, gộp 3, bỏ cặp sai 0 (quyết định lưu ở `hieu_dinh/HCB_08__<người>.tsv`)
- Cảnh báo khi làm sạch: 3 (xem `work/HCB_08/canh_bao.tsv`)
- Ghi chú tự động (dịch rút gọn, vế Việt thêm diễn giải, câu không được dịch): 3 cặp, ghi ở cột `Ghi chú` của sheet TRUY_VET
- Phạm vi theo trả lời của giảng viên: chỉ dóng hàng phần có song ngữ; phần chỉ một bản có thì không đưa vào dữ liệu (đã liệt kê ở mục Loại trừ và Câu không ghép được).
- Tỷ lệ lỗi theo §8 Guideline: chưa chấm mẫu (tuỳ chọn: app → Nâng cao → Chấm mẫu).

## 4. Nguồn tài liệu

| Quyển | Bản | Tệp | Định dạng đọc được | Nguồn trực tuyến | revid |
|---|---|---|---|---|---|
| 24 | han | `HauHanThu_q24_han.txt` | wikitext | https://zh.wikisource.org/wiki/後漢書/卷24 |  |
| 24 | viet | `HauHanThu_q24_viet.txt` | wikitext | https://vi.wikisource.org/wiki/Biên_dịch:Hậu_Hán_thư/Quyển_24 | 204355 |

## 5. Công cụ

- `hvalign` 0.3.5 (Lab/GK/hvalign), Python 3.12.6, PyYAML.
- Bước 4: tự nhận dạng định dạng nguồn (wikitext / text thuần / HTML sillok) và chuẩn hóa về một dạng.
- Bước 7: dóng 3 tầng (mục → đoạn → câu), chi phí Gale–Church + mốc can chi và tên riêng Hán Việt.
- Cấu hình: `config/project.yaml`, `config/works/HCB_08.yaml`, `config/phan_cong.tsv`.
