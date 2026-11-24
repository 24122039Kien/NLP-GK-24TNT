# Báo cáo tự sinh – HCB_01

Ngày: 2026-11-24 · hvalign 0.3.0 · **Trạng thái: dóng tự động, ghi chú tự động**

## 1. Số cặp

Tổng: **3632** cặp.

| Thành viên | Số cặp |
|---|---|
| Kien | 1961 |
| chua_phan_cong | 1671 |

| Quyển | Thành viên | Số cặp |
|---|---|---|
| 1 | chua_phan_cong | 419 |
| 2 | Kien | 453 |
| 6 | Kien | 371 |
| 8 | chua_phan_cong | 437 |
| 10 | Kien | 462 |
| 15 | Kien | 352 |
| 17 | chua_phan_cong | 351 |
| 19 | chua_phan_cong | 464 |
| 20 | Kien | 323 |

Kiểu ghép: `1-1` 2876, `1-2` 652, `1-3` 68, `2-2` 13, `2-1` 9, `1-4` 5, `1-5` 5, `1-6` 2, `1-7` 1, `1-8` 1

## 2. Số dòng văn bản sạch

- `03_text_sach/han.txt`: 1159 dòng
- `03_text_sach/viet.txt`: 1288 dòng

## 3. Kết quả tự kiểm tra

- Kiểm định định dạng TSV/XLSX: **đạt**; cảnh báo: 2 cặp trùng lặp hoàn toàn; 11 câu Hán xuất hiện ở hơn một cặp (có thể là câu lặp thật, ví dụ 帝曰)
- Luật làm sạch đã áp dụng: R04_bo_chu_nho ×87, R06_bo_chu_han_trong_viet ×561, R08_bo_dong_tieu_de ×280, R10_chuan_hoa_khoang_trang_dau_cau ×86, rong_sau_lam_sach ×4
- Loại trừ (không có bản dịch / không phải chính văn): 0 khối
- Câu không ghép được (ghi ở `work/HCB_01/khong_ghep.tsv`, không đưa vào TSV): 10
- Cặp máy gắn cờ: 137 (`lech_moc` 68, `lech_do_dai` 58, `n-m` 13); người đã xem 0
- Hiệu đính đã áp: xác nhận đúng 0, sửa chữ 0, gộp 0, bỏ cặp sai 0 (quyết định lưu ở `hieu_dinh/HCB_01__<người>.tsv`)
- Cảnh báo khi làm sạch: 1 (xem `work/HCB_01/canh_bao.tsv`)
- Ghi chú tự động (dịch rút gọn, vế Việt thêm diễn giải, câu không được dịch): 4 cặp, ghi ở cột `Ghi chú` của sheet TRUY_VET
- Phạm vi theo trả lời của giảng viên: chỉ dóng hàng phần có song ngữ; phần chỉ một bản có thì không đưa vào dữ liệu (đã liệt kê ở mục Loại trừ và Câu không ghép được).
- Tỷ lệ lỗi theo §8 Guideline: chưa chấm mẫu (tuỳ chọn: app → Nâng cao → Chấm mẫu).

## 4. Nguồn tài liệu

| Quyển | Bản | Tệp | Định dạng đọc được | Nguồn trực tuyến | revid |
|---|---|---|---|---|---|
| 1 | han | `續資治通鑑_卷001.wikitext` | wikitext | (không có trong manifest) |  |
| 1 | viet | `Tục_tư_trị_thông_giám_Quyển_1.wikitext` | wikitext | (không có trong manifest) |  |
| 2 | han | `續資治通鑑_卷002.wikitext` | wikitext | https://zh.wikisource.org/wiki/%E7%BA%8C%E8%B3%87%E6%B2%BB%E9%80%9A%E9%91%91/%E5%8D%B7002 | 2358394 |
| 2 | viet | `Tục_tư_trị_thông_giám_Quyển_2.wikitext` | wikitext | https://vi.wikisource.org/wiki/T%E1%BB%A5c_t%C6%B0_tr%E1%BB%8B_th%C3%B4ng_gi%C3%A1m/Quy%E1%BB%83n_2 | 203301 |
| 6 | han | `續資治通鑑_卷006.wikitext` | wikitext | https://zh.wikisource.org/wiki/%E7%BA%8C%E8%B3%87%E6%B2%BB%E9%80%9A%E9%91%91/%E5%8D%B7006 | 2633664 |
| 6 | viet | `Tục_tư_trị_thông_giám_Quyển_6.wikitext` | wikitext | https://vi.wikisource.org/wiki/T%E1%BB%A5c_t%C6%B0_tr%E1%BB%8B_th%C3%B4ng_gi%C3%A1m/Quy%E1%BB%83n_6 | 203296 |
| 8 | han | `續資治通鑑_卷008.wikitext` | wikitext | (không có trong manifest) |  |
| 8 | viet | `Tục_tư_trị_thông_giám_Quyển_8.wikitext` | wikitext | (không có trong manifest) |  |
| 10 | han | `續資治通鑑_卷010.wikitext` | wikitext | https://zh.wikisource.org/wiki/%E7%BA%8C%E8%B3%87%E6%B2%BB%E9%80%9A%E9%91%91/%E5%8D%B7010 | 2311081 |
| 10 | viet | `Tục_tư_trị_thông_giám_Quyển_10.wikitext` | wikitext | https://vi.wikisource.org/wiki/T%E1%BB%A5c_t%C6%B0_tr%E1%BB%8B_th%C3%B4ng_gi%C3%A1m/Quy%E1%BB%83n_10 | 202674 |
| 15 | han | `續資治通鑑_卷015.wikitext` | wikitext | https://zh.wikisource.org/wiki/%E7%BA%8C%E8%B3%87%E6%B2%BB%E9%80%9A%E9%91%91/%E5%8D%B7015 | 1328859 |
| 15 | viet | `Tục_tư_trị_thông_giám_Quyển_15.wikitext` | wikitext | https://vi.wikisource.org/wiki/T%E1%BB%A5c_t%C6%B0_tr%E1%BB%8B_th%C3%B4ng_gi%C3%A1m/Quy%E1%BB%83n_15 | 202704 |
| 17 | han | `續資治通鑑_卷017.wikitext` | wikitext | (không có trong manifest) |  |
| 17 | viet | `Tục_tư_trị_thông_giám_Quyển_17.wikitext` | wikitext | (không có trong manifest) |  |
| 19 | han | `續資治通鑑_卷019.wikitext` | wikitext | (không có trong manifest) |  |
| 19 | viet | `Tục_tư_trị_thông_giám_Quyển_19.wikitext` | wikitext | (không có trong manifest) |  |
| 20 | han | `續資治通鑑_卷020.wikitext` | wikitext | https://zh.wikisource.org/wiki/%E7%BA%8C%E8%B3%87%E6%B2%BB%E9%80%9A%E9%91%91/%E5%8D%B7020 | 2260978 |
| 20 | viet | `Tục_tư_trị_thông_giám_Quyển_20.wikitext` | wikitext | https://vi.wikisource.org/wiki/T%E1%BB%A5c_t%C6%B0_tr%E1%BB%8B_th%C3%B4ng_gi%C3%A1m/Quy%E1%BB%83n_20 | 203331 |

## 5. Công cụ

- `hvalign` 0.3.0 (Lab/GK/hvalign), Python 3.11.9, PyYAML.
- Bước 4: tự nhận dạng định dạng nguồn (wikitext / text thuần / HTML sillok) và chuẩn hóa về một dạng.
- Bước 7: dóng 3 tầng (mục → đoạn → câu), chi phí Gale–Church + mốc can chi và tên riêng Hán Việt.
- Cấu hình: `config/project.yaml`, `config/works/HCB_01.yaml`, `config/phan_cong.tsv`.
