# Báo cáo tự sinh – HCB_11

Ngày: 2026-11-26 · hvalign 0.3.2 · **Trạng thái: dóng tự động, ghi chú tự động; người đã xem 27/85 cặp máy gắn cờ**

## 1. Số cặp

Tổng: **499** cặp.

| Thành viên | Số cặp |
|---|---|
| Kien | 499 |

| Quyển | Thành viên | Số cặp |
|---|---|---|
| 86 | Kien | 499 |

Kiểu ghép: `1-1` 448, `2-1` 36, `1-2` 4, `5-2` 2, `3-1` 2, `6-3` 2, `5-1` 1, `6-2` 1, `10-4` 1, `6-1` 1, `3-2` 1

- Phạm vi được giao (`config/phan_cong.tsv`): **cả tác phẩm** (Kien); quyển có trong nguồn và đã dóng: 86.
- Độ phủ: các cặp chứa **100.0%** số chữ Hán và **100.0%** số âm tiết Việt của `03_text_sach` (phần chưa phủ là câu không ghép được hoặc cặp bỏ khi hiệu đính; phần chỉ một bản có đã bị loại trừ từ Bước 5, không tính ở đây).

## 2. Số dòng văn bản sạch

- `03_text_sach/han.txt`: 59 dòng
- `03_text_sach/viet.txt`: 60 dòng
- Thư mục nộp: `01_nguon` (dữ liệu đã tải/crawl), `03_text_sach` (text Hán và Việt đã trích xuất và làm sạch), `04_dong_hang` (TSV + XLSX), `bao_cao.md`. Không có `02_ocr_tho`: nguồn là text số (wikitext/HTML/txt), không phải ảnh/PDF scan, nên không OCR (theo nhận xét của giảng viên 18/11). Tệp `.pdf` trong `01_nguon` là bản in của trang nguồn, lưu để đối chiếu.

## 3. Kết quả tự kiểm tra

- Kiểm định định dạng TSV/XLSX: **đạt**; cảnh báo: 4 cặp có chữ Latin ở vế Hán (thường là mã lỗi chữ chưa tra)
- Luật làm sạch đã áp dụng: R06_bo_chu_han_trong_viet ×495, R07_bo_nam_duong_lich ×76, R10_chuan_hoa_khoang_trang_dau_cau ×1
- Loại trừ (không có bản dịch / không phải chính văn): 0 khối
- Câu không ghép được (ghi ở `work/HCB_11/khong_ghep.tsv`, không đưa vào TSV): 0
- Cặp máy gắn cờ: 85 (`rut_gon` 66, `lech_moc` 28, `lech_do_dai` 9); người đã xem 27
- Hiệu đính đã áp: xác nhận đúng 11, sửa chữ 0, gộp 11, bỏ cặp sai 0 (quyết định lưu ở `hieu_dinh/HCB_11__<người>.tsv`)
- Cảnh báo khi làm sạch: 12 (xem `work/HCB_11/canh_bao.tsv`)
- Ghi chú tự động (dịch rút gọn, vế Việt thêm diễn giải, câu không được dịch): 27 cặp, ghi ở cột `Ghi chú` của sheet DONG_HANG
- Phạm vi theo trả lời của giảng viên: chỉ dóng hàng phần có song ngữ; phần chỉ một bản có thì không đưa vào dữ liệu (đã liệt kê ở mục Loại trừ và Câu không ghép được).
- Tỷ lệ lỗi theo §8 Guideline: chưa chấm mẫu (tuỳ chọn: app → Nâng cao → Chấm mẫu).

## 4. Nguồn tài liệu

| Quyển | Bản | Tệp | Định dạng đọc được | Nguồn trực tuyến | revid |
|---|---|---|---|---|---|
| 86 | han | `後漢書_卷86.wikitext` | wikitext | https://zh.wikisource.org/wiki/%E5%BE%8C%E6%BC%A2%E6%9B%B8/%E5%8D%B786 | 1523514 |
| 86 | viet | `Biên_dịch_Hậu_Hán_thư_Quyển_86.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:H%E1%BA%ADu_H%C3%A1n_th%C6%B0/Quy%E1%BB%83n_86 | 204352 |

## 5. Công cụ

- `hvalign` 0.3.2 (Lab/GK/hvalign), Python 3.12.6, PyYAML.
- Bước 4: tự nhận dạng định dạng nguồn (wikitext / text thuần / HTML sillok) và chuẩn hóa về một dạng.
- Bước 7: dóng 3 tầng (mục → đoạn → câu), chi phí Gale–Church + mốc can chi và tên riêng Hán Việt.
- Cấu hình: `config/project.yaml`, `config/works/HCB_11.yaml`, `config/phan_cong.tsv`.
