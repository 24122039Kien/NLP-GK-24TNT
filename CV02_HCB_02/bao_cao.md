# Báo cáo tự sinh – HCB_02

Ngày: 2026-11-24 · hvalign 0.3.0 · **Trạng thái: dóng tự động, ghi chú tự động**

## 1. Số cặp

Tổng: **10** cặp.

| Thành viên | Số cặp |
|---|---|
| chua_phan_cong | 10 |

| Quyển | Thành viên | Số cặp |
|---|---|---|
| 1 | chua_phan_cong | 10 |

Kiểu ghép: `1-4` 2, `10-1` 2, `1-2` 2, `1-7` 1, `1-6` 1, `2-1` 1, `1-1` 1

## 2. Số dòng văn bản sạch

- `03_text_sach/han.txt`: 1 dòng
- `03_text_sach/viet.txt`: 71 dòng

## 3. Kết quả tự kiểm tra

- Kiểm định định dạng TSV/XLSX: **đạt**
- Luật làm sạch đã áp dụng: R03_bo_ref ×13, R06_bo_chu_han_trong_viet ×2, R10_chuan_hoa_khoang_trang_dau_cau ×3, rong_sau_lam_sach ×1
- Loại trừ (không có bản dịch / không phải chính văn): 0 khối
- Câu không ghép được (ghi ở `work/HCB_02/khong_ghep.tsv`, không đưa vào TSV): 132
- Cặp máy gắn cờ: 5 (`lech_moc` 5, `lech_do_dai` 2); người đã xem 0
- Hiệu đính đã áp: xác nhận đúng 0, sửa chữ 0, gộp 0, bỏ cặp sai 0 (quyết định lưu ở `hieu_dinh/HCB_02__<người>.tsv`)
- Cảnh báo khi làm sạch: 172 (xem `work/HCB_02/canh_bao.tsv`)
- Ghi chú tự động (dịch rút gọn, vế Việt thêm diễn giải, câu không được dịch): 10 cặp, ghi ở cột `Ghi chú` của sheet TRUY_VET
- Phạm vi theo trả lời của giảng viên: chỉ dóng hàng phần có song ngữ; phần chỉ một bản có thì không đưa vào dữ liệu (đã liệt kê ở mục Loại trừ và Câu không ghép được).
- Tỷ lệ lỗi theo §8 Guideline: chưa chấm mẫu (tuỳ chọn: app → Nâng cao → Chấm mẫu).

## 4. Nguồn tài liệu

| Quyển | Bản | Tệp | Định dạng đọc được | Nguồn trực tuyến | revid |
|---|---|---|---|---|---|
| 1 | han | `平安南詔.wikitext` | wikitext | (không có trong manifest) |  |
| 1 | viet | `Biên_dịch_Bình_An_Nam_chiếu.wikitext` | wikitext | (không có trong manifest) |  |

## 5. Công cụ

- `hvalign` 0.3.0 (Lab/GK/hvalign), Python 3.11.9, PyYAML.
- Bước 4: tự nhận dạng định dạng nguồn (wikitext / text thuần / HTML sillok) và chuẩn hóa về một dạng.
- Bước 7: dóng 3 tầng (mục → đoạn → câu), chi phí Gale–Church + mốc can chi và tên riêng Hán Việt.
- Cấu hình: `config/project.yaml`, `config/works/HCB_02.yaml`, `config/phan_cong.tsv`.
