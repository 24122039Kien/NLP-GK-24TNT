# Báo cáo tự sinh – HCB_10

Ngày: 2026-11-26 · hvalign 0.3.1 · **Trạng thái: dóng tự động, ghi chú tự động**

## 1. Số cặp

Tổng: **38** cặp.

| Thành viên | Số cặp |
|---|---|
| Dang | 38 |

| Quyển | Thành viên | Số cặp |
|---|---|---|
| 81 | Dang | 38 |

Kiểu ghép: `1-1` 33, `1-2` 5

- Phạm vi được giao (`config/phan_cong.tsv`): **cả tác phẩm** (Dang); quyển có trong nguồn và đã dóng: 81.
- Độ phủ: các cặp chứa **100.0%** số chữ Hán và **100.0%** số âm tiết Việt của `03_text_sach` (phần chưa phủ là câu không ghép được hoặc cặp bỏ khi hiệu đính; phần chỉ một bản có đã bị loại trừ từ Bước 5, không tính ở đây).

## 2. Số dòng văn bản sạch

- `03_text_sach/han.txt`: 5 dòng
- `03_text_sach/viet.txt`: 5 dòng
- Thư mục nộp: `01_nguon` (dữ liệu đã tải/crawl), `03_text_sach` (text Hán và Việt đã trích xuất và làm sạch), `04_dong_hang` (TSV + XLSX), `bao_cao.md`. Không có `02_ocr_tho`: nguồn là text số (wikitext/HTML/txt), không phải ảnh/PDF scan, nên không OCR (theo nhận xét của giảng viên 18/11). Tệp `.pdf` trong `01_nguon` là bản in của trang nguồn, lưu để đối chiếu.

## 3. Kết quả tự kiểm tra

- Kiểm định định dạng TSV/XLSX: **đạt**
- Luật làm sạch đã áp dụng: R06_bo_chu_han_trong_viet ×18, R07_bo_nam_duong_lich ×1, R12_loai_tru ×107
- Loại trừ (không có bản dịch / không phải chính văn): 107 khối – Truyện 谯玄 – bản Việt không dịch (9); Truyện 李业 – bản Việt không dịch (7); Truyện 刘茂 – bản Việt không dịch (5); Truyện 温序 – bản Việt không dịch (4); Truyện 彭脩 – bản Việt không dịch (4); Truyện 索卢放 – bản Việt không dịch (3); Truyện 周嘉 – bản Việt không dịch (6); Truyện 范式 – bản Việt không dịch (7); Truyện 王忳 – bản Việt không dịch (3); Truyện 张武 – bản Việt không dịch (2); Truyện 陆续 – bản Việt không dịch (5); Truyện 戴封 – bản Việt không dịch (4); Truyện 李充 – bản Việt không dịch (5); Truyện 缪肜 – bản Việt không dịch (5); Truyện 陈重 – bản Việt không dịch (5); Truyện 雷义 – bản Việt không dịch (5); Truyện 范冉 – bản Việt không dịch (7); Truyện 戴就 – bản Việt không dịch (3); Truyện 赵苞 – bản Việt không dịch (4); Truyện 向栩 – bản Việt không dịch (4); Truyện 谅辅 – bản Việt không dịch (2); Truyện 刘翊 – bản Việt không dịch (5); Truyện 王烈 – bản Việt không dịch (3)
- Câu không ghép được (ghi ở `work/HCB_10/khong_ghep.tsv`, không đưa vào TSV): 0
- Cặp máy gắn cờ: 2 (`lech_moc` 2); người đã xem 0
- Hiệu đính đã áp: xác nhận đúng 0, sửa chữ 0, gộp 0, bỏ cặp sai 0 (quyết định lưu ở `hieu_dinh/HCB_10__<người>.tsv`)
- Cảnh báo khi làm sạch: 0 (xem `work/HCB_10/canh_bao.tsv`)
- Ghi chú tự động (dịch rút gọn, vế Việt thêm diễn giải, câu không được dịch): 0 cặp, ghi ở cột `Ghi chú` của sheet TRUY_VET
- Phạm vi theo trả lời của giảng viên: chỉ dóng hàng phần có song ngữ; phần chỉ một bản có thì không đưa vào dữ liệu (đã liệt kê ở mục Loại trừ và Câu không ghép được).
- Tỷ lệ lỗi theo §8 Guideline: chưa chấm mẫu (tuỳ chọn: app → Nâng cao → Chấm mẫu).

## 4. Nguồn tài liệu

| Quyển | Bản | Tệp | Định dạng đọc được | Nguồn trực tuyến | revid |
|---|---|---|---|---|---|
| 81 | han | `後漢書_卷81.wikitext` | wikitext | (không có trong manifest) |  |
| 81 | viet | `Biên_dịch_Hậu_Hán_thư_Quyển_81.wikitext` | wikitext | (không có trong manifest) |  |

## 5. Công cụ

- `hvalign` 0.3.1 (Lab/GK/hvalign), Python 3.12.6, PyYAML.
- Bước 4: tự nhận dạng định dạng nguồn (wikitext / text thuần / HTML sillok) và chuẩn hóa về một dạng.
- Bước 7: dóng 3 tầng (mục → đoạn → câu), chi phí Gale–Church + mốc can chi và tên riêng Hán Việt.
- Cấu hình: `config/project.yaml`, `config/works/HCB_10.yaml`, `config/phan_cong.tsv`.
