# Báo cáo tự sinh – HCB_06

Ngày: 2026-11-26 · hvalign 0.3.2 · **Trạng thái: dóng tự động, ghi chú tự động**

## 1. Số cặp

Tổng: **360** cặp.

| Thành viên | Số cặp |
|---|---|
| Huy | 360 |

| Quyển | Thành viên | Số cặp |
|---|---|---|
| 28 | Huy | 360 |

Kiểu ghép: `1-1` 342, `10-1` 8, `1-2` 4, `2-1` 3, `8-1` 2, `9-1` 1

- Phạm vi được giao (`config/phan_cong.tsv`): **cả tác phẩm** (Huy); quyển có trong nguồn và đã dóng: 28.
- Độ phủ: các cặp chứa **65.4%** số chữ Hán và **100.0%** số âm tiết Việt của `03_text_sach` (phần chưa phủ là câu không ghép được hoặc cặp bỏ khi hiệu đính; phần chỉ một bản có đã bị loại trừ từ Bước 5, không tính ở đây).

## 2. Số dòng văn bản sạch

- `03_text_sach/han.txt`: 214 dòng
- `03_text_sach/viet.txt`: 135 dòng
- Thư mục nộp: `01_nguon` (dữ liệu đã tải/crawl), `03_text_sach` (text Hán và Việt đã trích xuất và làm sạch), `04_dong_hang` (TSV + XLSX), `bao_cao.md`. Không có `02_ocr_tho`: nguồn là text số (wikitext/HTML/txt), không phải ảnh/PDF scan, nên không OCR (theo nhận xét của giảng viên 18/11). Tệp `.pdf` trong `01_nguon` là bản in của trang nguồn, lưu để đối chiếu.

## 3. Kết quả tự kiểm tra

- Kiểm định định dạng TSV/XLSX: **đạt**; cảnh báo: 1 cặp có chữ Latin ở vế Hán (thường là mã lỗi chữ chưa tra); 4 cặp trùng lặp hoàn toàn; 4 câu Hán xuất hiện ở hơn một cặp (có thể là câu lặp thật, ví dụ 帝曰)
- Luật làm sạch đã áp dụng: R03_bo_ref ×1, R06_bo_chu_han_trong_viet ×1930, R07_bo_nam_duong_lich ×5, R10_chuan_hoa_khoang_trang_dau_cau ×1, R12_loai_tru ×3
- Loại trừ (không có bản dịch / không phải chính văn): 3 khối – Bản Việt không có phần khảo bản (2); Bản Việt không có phần giáo khám (1)
- Câu không ghép được (ghi ở `work/HCB_06/khong_ghep.tsv`, không đưa vào TSV): 270
- Cặp máy gắn cờ: 20 (`lech_moc` 20, `lech_do_dai` 2); người đã xem 0
- Hiệu đính đã áp: xác nhận đúng 0, sửa chữ 0, gộp 0, bỏ cặp sai 0 (quyết định lưu ở `hieu_dinh/HCB_06__<người>.tsv`)
- Cảnh báo khi làm sạch: 1 (xem `work/HCB_06/canh_bao.tsv`)
- Ghi chú tự động (dịch rút gọn, vế Việt thêm diễn giải, câu không được dịch): 76 cặp, ghi ở cột `Ghi chú` của sheet TRUY_VET
- Phạm vi theo trả lời của giảng viên: chỉ dóng hàng phần có song ngữ; phần chỉ một bản có thì không đưa vào dữ liệu (đã liệt kê ở mục Loại trừ và Câu không ghép được).
- Tỷ lệ lỗi theo §8 Guideline: chưa chấm mẫu (tuỳ chọn: app → Nâng cao → Chấm mẫu).

## 4. Nguồn tài liệu

| Quyển | Bản | Tệp | Định dạng đọc được | Nguồn trực tuyến | revid |
|---|---|---|---|---|---|
| 28 | han | `HanThu_q028_han.txt` | wikitext | https://zh.wikisource.org/wiki/漢書/卷028上 |  |
| 28 | viet | `HanThu_q028_viet.txt` | wikitext | https://vi.wikisource.org/wiki/Biên_dịch:Hán_thư/Quyển_028_thượng |  |

## 5. Công cụ

- `hvalign` 0.3.2 (Lab/GK/hvalign), Python 3.12.6, PyYAML.
- Bước 4: tự nhận dạng định dạng nguồn (wikitext / text thuần / HTML sillok) và chuẩn hóa về một dạng.
- Bước 7: dóng 3 tầng (mục → đoạn → câu), chi phí Gale–Church + mốc can chi và tên riêng Hán Việt.
- Cấu hình: `config/project.yaml`, `config/works/HCB_06.yaml`, `config/phan_cong.tsv`.
