# Báo cáo tự sinh – HCB_14

Ngày: 2026-11-26 · hvalign 0.3.0 · **Trạng thái: dóng tự động, ghi chú tự động**

## 1. Số cặp

Tổng: **351** cặp.

| Thành viên | Số cặp |
|---|---|
| Kien | 124 |
| Tai | 227 |

| Quyển | Thành viên | Số cặp |
|---|---|---|
| 1333 | Kien | 62 |
| 1335 | Tai | 23 |
| 1337 | Tai | 21 |
| 1339 | Kien | 23 |
| 1357 | Kien | 30 |
| 1358 | Tai | 12 |
| 1360 | Tai | 21 |
| 1362 | Tai | 41 |
| 1410 | Tai | 11 |
| 1421 | Tai | 87 |
| 1438 | Kien | 9 |
| 1445 | Tai | 11 |

Kiểu ghép: `1-1` 110, `3-1` 66, `2-1` 51, `6-1` 25, `4-1` 24, `5-1` 20, `2-2` 14, `7-1` 10, `1-2` 8, `10-1` 5, `9-1` 3, `1-10` 3, `1-3` 3, `8-1` 3, `1-8` 2, `1-4` 2, `1-6` 1, `1-7` 1

## 2. Số dòng văn bản sạch

- `03_text_sach/han.txt`: 124 dòng
- `03_text_sach/viet.txt`: 175 dòng

## 3. Kết quả tự kiểm tra

- Kiểm định định dạng TSV/XLSX: **đạt**; cảnh báo: 3 cặp có chữ Hán ở vế Việt; 3 cặp có chữ Latin ở vế Hán (thường là mã lỗi chữ chưa tra); 4 câu Hán xuất hiện ở hơn một cặp (có thể là câu lặp thật, ví dụ 帝曰)
- Luật làm sạch đã áp dụng: R03_bo_ref ×7, R06_bo_chu_han_trong_viet ×252, R07_bo_nam_duong_lich ×4, R08_bo_dong_tieu_de ×35, R10_chuan_hoa_khoang_trang_dau_cau ×50
- Loại trừ (không có bản dịch / không phải chính văn): 0 khối
- Câu không ghép được (ghi ở `work/HCB_14/khong_ghep.tsv`, không đưa vào TSV): 38
- Cặp máy gắn cờ: 67 (`lech_moc` 48, `lech_do_dai` 17, `n-m` 14); người đã xem 0
- Hiệu đính đã áp: xác nhận đúng 0, sửa chữ 0, gộp 0, bỏ cặp sai 0 (quyết định lưu ở `hieu_dinh/HCB_14__<người>.tsv`)
- Cảnh báo khi làm sạch: 38 (xem `work/HCB_14/canh_bao.tsv`)
- Ghi chú tự động (dịch rút gọn, vế Việt thêm diễn giải, câu không được dịch): 43 cặp, ghi ở cột `Ghi chú` của sheet TRUY_VET
- Phạm vi theo trả lời của giảng viên: chỉ dóng hàng phần có song ngữ; phần chỉ một bản có thì không đưa vào dữ liệu (đã liệt kê ở mục Loại trừ và Câu không ghép được).
- Tỷ lệ lỗi theo §8 Guideline: chưa chấm mẫu (tuỳ chọn: app → Nâng cao → Chấm mẫu).

## 4. Nguồn tài liệu

| Quyển | Bản | Tệp | Định dạng đọc được | Nguồn trực tuyến | revid |
|---|---|---|---|---|---|
| 1 | han | `清實錄_大清高宗純皇帝實錄_卷之一千三百三十七.wikitext` | wikitext | (không có trong manifest) |  |
| 1 | han | `清實錄_大清高宗純皇帝實錄_卷之一千三百三十五.wikitext` | wikitext | (không có trong manifest) |  |
| 1 | han | `清實錄_大清高宗純皇帝實錄_卷之一千三百五十八.wikitext` | wikitext | (không có trong manifest) |  |
| 1 | han | `清實錄_大清高宗純皇帝實錄_卷之一千三百六十.wikitext` | wikitext | (không có trong manifest) |  |
| 1 | han | `清實錄_大清高宗純皇帝實錄_卷之一千三百六十二.wikitext` | wikitext | (không có trong manifest) |  |
| 1 | han | `清實錄_大清高宗純皇帝實錄_卷之一千四百二十一.wikitext` | wikitext | (không có trong manifest) |  |
| 1 | han | `清實錄_大清高宗純皇帝實錄_卷之一千四百十.wikitext` | wikitext | (không có trong manifest) |  |
| 1 | han | `清實錄_大清高宗純皇帝實錄_卷之一千四百四十五.wikitext` | wikitext | (không có trong manifest) |  |
| 1333 | han | `清實錄_高宗純皇帝實錄_卷1333_qsilok_007_1333_0010_0010_0060_0030.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1333_0010_0010_0060_0030 |  |
| 1333 | han | `清實錄_高宗純皇帝實錄_卷1333_qsilok_007_1333_0010_0010_0060_0040.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1333_0010_0010_0060_0040 |  |
| 1333 | han | `清實錄_高宗純皇帝實錄_卷1333_qsilok_007_1333_0010_0010_0060_0050.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1333_0010_0010_0060_0050 |  |
| 1333 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1333.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1333 | 196240 |
| 1335 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1335.wikitext` | wikitext | (không có trong manifest) |  |
| 1337 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1337.wikitext` | wikitext | (không có trong manifest) |  |
| 1339 | han | `清實錄_高宗純皇帝實錄_卷1339_qsilok_007_1339_0010_0010_0080_0040.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1339_0010_0010_0080_0040 |  |
| 1339 | han | `清實錄_高宗純皇帝實錄_卷1339_qsilok_007_1339_0010_0010_0080_0050.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1339_0010_0010_0080_0050 |  |
| 1339 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1339.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1339 | 196246 |
| 1357 | han | `清實錄_高宗純皇帝實錄_卷1357_qsilok_007_1357_0010_0010_0090_0020.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1357_0010_0010_0090_0020 |  |
| 1357 | han | `清實錄_高宗純皇帝實錄_卷1357_qsilok_007_1357_0010_0010_0110_0030.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1357_0010_0010_0110_0030 |  |
| 1357 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1357.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1357 | 196257 |
| 1358 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1358.wikitext` | wikitext | (không có trong manifest) |  |
| 1360 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1360.wikitext` | wikitext | (không có trong manifest) |  |
| 1362 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1362.wikitext` | wikitext | (không có trong manifest) |  |
| 1410 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1410.wikitext` | wikitext | (không có trong manifest) |  |
| 1421 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1421.wikitext` | wikitext | (không có trong manifest) |  |
| 1438 | han | `清實錄_高宗純皇帝實錄_卷1438_qsilok_007_1438_0010_0010_0020_0070.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1438_0010_0010_0020_0070 |  |
| 1438 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1438.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1438 | 196316 |
| 1445 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1445.wikitext` | wikitext | (không có trong manifest) |  |

## 5. Công cụ

- `hvalign` 0.3.0 (Lab/GK/hvalign), Python 3.12.6, PyYAML.
- Bước 4: tự nhận dạng định dạng nguồn (wikitext / text thuần / HTML sillok) và chuẩn hóa về một dạng.
- Bước 7: dóng 3 tầng (mục → đoạn → câu), chi phí Gale–Church + mốc can chi và tên riêng Hán Việt.
- Cấu hình: `config/project.yaml`, `config/works/HCB_14.yaml`, `config/phan_cong.tsv`.
