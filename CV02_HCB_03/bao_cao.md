# Báo cáo tự sinh – HCB_03

Ngày: 2026-11-26 · hvalign 0.3.0 · **Trạng thái: dóng tự động, ghi chú tự động**

## 1. Số cặp

Tổng: **8** cặp.

| Thành viên | Số cặp |
|---|---|
| Huy | 8 |

| Quyển | Thành viên | Số cặp |
|---|---|---|
| 130 | Huy | 8 |

Kiểu ghép: `1-10` 4, `1-2` 3, `1-1` 1

## 2. Số dòng văn bản sạch

- `03_text_sach/han.txt`: 5 dòng
- `03_text_sach/viet.txt`: 21 dòng

## 3. Kết quả tự kiểm tra

- Kiểm định định dạng TSV/XLSX: **đạt**; cảnh báo: 3 cặp có chữ Latin ở vế Hán (thường là mã lỗi chữ chưa tra)
- Luật làm sạch đã áp dụng: R06_bo_chu_han_trong_viet ×72, R07_bo_nam_duong_lich ×15, R10_chuan_hoa_khoang_trang_dau_cau ×3
- Loại trừ (không có bản dịch / không phải chính văn): 0 khối
- Câu không ghép được (ghi ở `work/HCB_03/khong_ghep.tsv`, không đưa vào TSV): 23
- Cặp máy gắn cờ: 4 (`lech_do_dai` 4, `lech_moc` 2); người đã xem 0
- Hiệu đính đã áp: xác nhận đúng 0, sửa chữ 0, gộp 0, bỏ cặp sai 0 (quyết định lưu ở `hieu_dinh/HCB_03__<người>.tsv`)
- Cảnh báo khi làm sạch: 5 (xem `work/HCB_03/canh_bao.tsv`)
- Ghi chú tự động (dịch rút gọn, vế Việt thêm diễn giải, câu không được dịch): 5 cặp, ghi ở cột `Ghi chú` của sheet TRUY_VET
- Phạm vi theo trả lời của giảng viên: chỉ dóng hàng phần có song ngữ; phần chỉ một bản có thì không đưa vào dữ liệu (đã liệt kê ở mục Loại trừ và Câu không ghép được).
- Tỷ lệ lỗi theo §8 Guideline: chưa chấm mẫu (tuỳ chọn: app → Nâng cao → Chấm mẫu).

## 4. Nguồn tài liệu

| Quyển | Bản | Tệp | Định dạng đọc được | Nguồn trực tuyến | revid |
|---|---|---|---|---|---|
| 130 | han | `DongDoSuLuoc_q130_han.txt` | wikitext | https://zh.wikisource.org/wiki/東都事略/卷130 |  |
| 130 | viet | `DongDoSuLuoc_q130_viet.txt` | wikitext | https://vi.wikisource.org/wiki/Biên_dịch:Đông_Đô_sự_lược/Quyển_130 |  |

## 5. Công cụ

- `hvalign` 0.3.0 (Lab/GK/hvalign), Python 3.12.6, PyYAML.
- Bước 4: tự nhận dạng định dạng nguồn (wikitext / text thuần / HTML sillok) và chuẩn hóa về một dạng.
- Bước 7: dóng 3 tầng (mục → đoạn → câu), chi phí Gale–Church + mốc can chi và tên riêng Hán Việt.
- Cấu hình: `config/project.yaml`, `config/works/HCB_03.yaml`, `config/phan_cong.tsv`.
