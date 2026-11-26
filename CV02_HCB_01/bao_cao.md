# Báo cáo tự sinh – HCB_01

Ngày: 2026-11-26 · hvalign 0.3.0 · **Trạng thái: dóng tự động, ghi chú tự động**

## 1. Số cặp

Tổng: **8102** cặp.

| Thành viên | Số cặp |
|---|---|
| Dang | 2344 |
| Huy | 2129 |
| Kien | 1958 |
| Tai | 1671 |

| Quyển | Thành viên | Số cặp |
|---|---|---|
| 1 | Tai | 419 |
| 2 | Kien | 453 |
| 3 | Huy | 395 |
| 4 | Dang | 398 |
| 5 | Huy | 498 |
| 6 | Kien | 371 |
| 7 | Huy | 454 |
| 8 | Tai | 437 |
| 9 | Dang | 406 |
| 10 | Kien | 462 |
| 11 | Huy | 403 |
| 12 | Dang | 413 |
| 13 | Dang | 374 |
| 14 | Dang | 337 |
| 15 | Kien | 351 |
| 16 | Huy | 379 |
| 17 | Tai | 351 |
| 18 | Dang | 416 |
| 19 | Tai | 464 |
| 20 | Kien | 321 |

Kiểu ghép: `1-1` 6495, `1-2` 1382, `1-3` 149, `2-2` 29, `2-1` 24, `1-4` 9, `1-5` 8, `1-6` 4, `1-7` 1, `1-8` 1

## 2. Số dòng văn bản sạch

- `03_text_sach/han.txt`: 2642 dòng
- `03_text_sach/viet.txt`: 2844 dòng

## 3. Kết quả tự kiểm tra

- Kiểm định định dạng TSV/XLSX: **đạt**; cảnh báo: 15 cặp trùng lặp hoàn toàn; 40 câu Hán xuất hiện ở hơn một cặp (có thể là câu lặp thật, ví dụ 帝曰)
- Luật làm sạch đã áp dụng: R04_bo_chu_nho ×87, R06_bo_chu_han_trong_viet ×1442, R08_bo_dong_tieu_de ×285, R10_chuan_hoa_khoang_trang_dau_cau ×87, rong_sau_lam_sach ×4
- Loại trừ (không có bản dịch / không phải chính văn): 0 khối
- Câu không ghép được (ghi ở `work/HCB_01/khong_ghep.tsv`, không đưa vào TSV): 10
- Cặp máy gắn cờ: 1114 (`lech_moc` 1001, `lech_do_dai` 102, `n-m` 29); người đã xem 0
- Hiệu đính đã áp: xác nhận đúng 0, sửa chữ 0, gộp 0, bỏ cặp sai 0 (quyết định lưu ở `hieu_dinh/HCB_01__<người>.tsv`)
- Cảnh báo khi làm sạch: 9 (xem `work/HCB_01/canh_bao.tsv`)
- Ghi chú tự động (dịch rút gọn, vế Việt thêm diễn giải, câu không được dịch): 5 cặp, ghi ở cột `Ghi chú` của sheet TRUY_VET
- Phạm vi theo trả lời của giảng viên: chỉ dóng hàng phần có song ngữ; phần chỉ một bản có thì không đưa vào dữ liệu (đã liệt kê ở mục Loại trừ và Câu không ghép được).
- Tỷ lệ lỗi theo §8 Guideline: chưa chấm mẫu (tuỳ chọn: app → Nâng cao → Chấm mẫu).

## 4. Nguồn tài liệu

| Quyển | Bản | Tệp | Định dạng đọc được | Nguồn trực tuyến | revid |
|---|---|---|---|---|---|
| 1 | han | `續資治通鑑_卷001.wikitext` | wikitext | (không có trong manifest) |  |
| 1 | viet | `Tục_tư_trị_thông_giám_Quyển_1.wikitext` | wikitext | (không có trong manifest) |  |
| 2 | han | `續資治通鑑_卷002.wikitext` | wikitext | https://zh.wikisource.org/wiki/%E7%BA%8C%E8%B3%87%E6%B2%BB%E9%80%9A%E9%91%91/%E5%8D%B7002 | 2358394 |
| 2 | viet | `Tục_tư_trị_thông_giám_Quyển_2.wikitext` | wikitext | https://vi.wikisource.org/wiki/T%E1%BB%A5c_t%C6%B0_tr%E1%BB%8B_th%C3%B4ng_gi%C3%A1m/Quy%E1%BB%83n_2 | 203301 |
| 3 | han | `TTTTG_q03_han.txt` | wikitext | https://zh.wikisource.org/wiki/續資治通鑑/卷003 |  |
| 3 | viet | `TTTTG_q03_viet.txt` | wikitext | https://vi.wikisource.org/wiki/Tục_tư_trị_thông_giám/Quyển_3 |  |
| 4 | han | `續資治通鑑_卷004.wikitext` | wikitext | (không có trong manifest) |  |
| 4 | viet | `Tục_tư_trị_thông_giám_Quyển_4.wikitext` | wikitext | (không có trong manifest) |  |
| 5 | han | `TTTTG_q05_han.txt` | wikitext | https://zh.wikisource.org/wiki/續資治通鑑/卷005 |  |
| 5 | viet | `TTTTG_q05_viet.txt` | wikitext | https://vi.wikisource.org/wiki/Tục_tư_trị_thông_giám/Quyển_5 |  |
| 6 | han | `續資治通鑑_卷006.wikitext` | wikitext | https://zh.wikisource.org/wiki/%E7%BA%8C%E8%B3%87%E6%B2%BB%E9%80%9A%E9%91%91/%E5%8D%B7006 | 2633664 |
| 6 | viet | `Tục_tư_trị_thông_giám_Quyển_6.wikitext` | wikitext | https://vi.wikisource.org/wiki/T%E1%BB%A5c_t%C6%B0_tr%E1%BB%8B_th%C3%B4ng_gi%C3%A1m/Quy%E1%BB%83n_6 | 203296 |
| 7 | han | `TTTTG_q07_han.txt` | wikitext | https://zh.wikisource.org/wiki/續資治通鑑/卷007 |  |
| 7 | viet | `TTTTG_q07_viet.txt` | wikitext | https://vi.wikisource.org/wiki/Tục_tư_trị_thông_giám/Quyển_7 |  |
| 8 | han | `續資治通鑑_卷008.wikitext` | wikitext | (không có trong manifest) |  |
| 8 | viet | `Tục_tư_trị_thông_giám_Quyển_8.wikitext` | wikitext | (không có trong manifest) |  |
| 9 | han | `續資治通鑑_卷009.wikitext` | wikitext | (không có trong manifest) |  |
| 9 | viet | `Tục_tư_trị_thông_giám_Quyển_9.wikitext` | wikitext | (không có trong manifest) |  |
| 10 | han | `續資治通鑑_卷010.wikitext` | wikitext | https://zh.wikisource.org/wiki/%E7%BA%8C%E8%B3%87%E6%B2%BB%E9%80%9A%E9%91%91/%E5%8D%B7010 | 2311081 |
| 10 | viet | `Tục_tư_trị_thông_giám_Quyển_10.wikitext` | wikitext | https://vi.wikisource.org/wiki/T%E1%BB%A5c_t%C6%B0_tr%E1%BB%8B_th%C3%B4ng_gi%C3%A1m/Quy%E1%BB%83n_10 | 202674 |
| 11 | han | `TTTTG_q11_han.txt` | wikitext | https://zh.wikisource.org/wiki/續資治通鑑/卷011 |  |
| 11 | viet | `TTTTG_q11_viet.txt` | wikitext | https://vi.wikisource.org/wiki/Tục_tư_trị_thông_giám/Quyển_11 |  |
| 12 | han | `續資治通鑑_卷012.wikitext` | wikitext | (không có trong manifest) |  |
| 12 | viet | `Tục_tư_trị_thông_giám_Quyển_12.wikitext` | wikitext | (không có trong manifest) |  |
| 13 | han | `續資治通鑑_卷013.wikitext` | wikitext | (không có trong manifest) |  |
| 13 | viet | `Tục_tư_trị_thông_giám_Quyển_13.wikitext` | wikitext | (không có trong manifest) |  |
| 14 | han | `續資治通鑑_卷014.wikitext` | wikitext | (không có trong manifest) |  |
| 14 | viet | `Tục_tư_trị_thông_giám_Quyển_14.wikitext` | wikitext | (không có trong manifest) |  |
| 15 | han | `續資治通鑑_卷015.wikitext` | wikitext | https://zh.wikisource.org/wiki/%E7%BA%8C%E8%B3%87%E6%B2%BB%E9%80%9A%E9%91%91/%E5%8D%B7015 | 1328859 |
| 15 | viet | `Tục_tư_trị_thông_giám_Quyển_15.wikitext` | wikitext | https://vi.wikisource.org/wiki/T%E1%BB%A5c_t%C6%B0_tr%E1%BB%8B_th%C3%B4ng_gi%C3%A1m/Quy%E1%BB%83n_15 | 202704 |
| 16 | han | `TTTTG_q16_han.txt` | wikitext | https://zh.wikisource.org/wiki/續資治通鑑/卷016 |  |
| 16 | viet | `TTTTG_q16_viet.txt` | wikitext | https://vi.wikisource.org/wiki/Tục_tư_trị_thông_giám/Quyển_16 |  |
| 17 | han | `續資治通鑑_卷017.wikitext` | wikitext | (không có trong manifest) |  |
| 17 | viet | `Tục_tư_trị_thông_giám_Quyển_17.wikitext` | wikitext | (không có trong manifest) |  |
| 18 | han | `續資治通鑑_卷018.wikitext` | wikitext | (không có trong manifest) |  |
| 18 | viet | `Tục_tư_trị_thông_giám_Quyển_18.wikitext` | wikitext | (không có trong manifest) |  |
| 19 | han | `續資治通鑑_卷019.wikitext` | wikitext | (không có trong manifest) |  |
| 19 | viet | `Tục_tư_trị_thông_giám_Quyển_19.wikitext` | wikitext | (không có trong manifest) |  |
| 20 | han | `續資治通鑑_卷020.wikitext` | wikitext | https://zh.wikisource.org/wiki/%E7%BA%8C%E8%B3%87%E6%B2%BB%E9%80%9A%E9%91%91/%E5%8D%B7020 | 2260978 |
| 20 | viet | `Tục_tư_trị_thông_giám_Quyển_20.wikitext` | wikitext | https://vi.wikisource.org/wiki/T%E1%BB%A5c_t%C6%B0_tr%E1%BB%8B_th%C3%B4ng_gi%C3%A1m/Quy%E1%BB%83n_20 | 203331 |

## 5. Công cụ

- `hvalign` 0.3.0 (Lab/GK/hvalign), Python 3.12.6, PyYAML.
- Bước 4: tự nhận dạng định dạng nguồn (wikitext / text thuần / HTML sillok) và chuẩn hóa về một dạng.
- Bước 7: dóng 3 tầng (mục → đoạn → câu), chi phí Gale–Church + mốc can chi và tên riêng Hán Việt.
- Cấu hình: `config/project.yaml`, `config/works/HCB_01.yaml`, `config/phan_cong.tsv`.
