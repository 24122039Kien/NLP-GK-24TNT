# Báo cáo tự sinh – HCB_14

Ngày: 2026-11-25 · hvalign 0.3.0 · **Trạng thái: dóng tự động, ghi chú tự động**

## 1. Số cặp

Tổng: **259** cặp.

| Thành viên | Số cặp |
|---|---|
| Dang | 259 |

| Quyển | Thành viên | Số cặp |
|---|---|---|
| 1328 | Dang | 88 |
| 1331 | Dang | 14 |
| 1346 | Dang | 56 |
| 1359 | Dang | 3 |
| 1384 | Dang | 12 |
| 1420 | Dang | 17 |
| 1428 | Dang | 48 |
| 1463 | Dang | 21 |

Kiểu ghép: `1-1` 90, `3-1` 41, `2-1` 40, `4-1` 20, `10-1` 17, `5-1` 14, `2-2` 8, `8-1` 7, `7-1` 6, `6-1` 6, `1-10` 4, `1-2` 3, `1-9` 1, `9-1` 1, `1-4` 1

## 2. Số dòng văn bản sạch

- `03_text_sach/han.txt`: 20 dòng
- `03_text_sach/viet.txt`: 110 dòng

## 3. Kết quả tự kiểm tra

- Kiểm định định dạng TSV/XLSX: **đạt**; cảnh báo: 2 cặp có chữ Hán ở vế Việt
- Luật làm sạch đã áp dụng: R03_bo_ref ×2, R06_bo_chu_han_trong_viet ×125, R07_bo_nam_duong_lich ×8, R10_chuan_hoa_khoang_trang_dau_cau ×18
- Loại trừ (không có bản dịch / không phải chính văn): 0 khối
- Câu không ghép được (ghi ở `work/HCB_14/khong_ghep.tsv`, không đưa vào TSV): 20
- Cặp máy gắn cờ: 40 (`lech_do_dai` 23, `lech_moc` 17, `n-m` 8); người đã xem 0
- Hiệu đính đã áp: xác nhận đúng 0, sửa chữ 0, gộp 0, bỏ cặp sai 0 (quyết định lưu ở `hieu_dinh/HCB_14__<người>.tsv`)
- Cảnh báo khi làm sạch: 18 (xem `work/HCB_14/canh_bao.tsv`)
- Ghi chú tự động (dịch rút gọn, vế Việt thêm diễn giải, câu không được dịch): 27 cặp, ghi ở cột `Ghi chú` của sheet TRUY_VET
- Phạm vi theo trả lời của giảng viên: chỉ dóng hàng phần có song ngữ; phần chỉ một bản có thì không đưa vào dữ liệu (đã liệt kê ở mục Loại trừ và Câu không ghép được).
- Tỷ lệ lỗi theo §8 Guideline: chưa chấm mẫu (tuỳ chọn: app → Nâng cao → Chấm mẫu).

## 4. Nguồn tài liệu

| Quyển | Bản | Tệp | Định dạng đọc được | Nguồn trực tuyến | revid |
|---|---|---|---|---|---|
| 1328 | han | `清實錄_高宗純皇帝實錄_卷1328_qsilok_007_1328_0010_0010_0030_0030.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1328_0010_0010_0030_0030 |  |
| 1328 | han | `清實錄_高宗純皇帝實錄_卷1328_qsilok_007_1328_0010_0010_0030_0040.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1328_0010_0010_0030_0040 |  |
| 1328 | han | `清實錄_高宗純皇帝實錄_卷1328_qsilok_007_1328_0010_0010_0030_0050.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1328_0010_0010_0030_0050 |  |
| 1328 | han | `清實錄_高宗純皇帝實錄_卷1328_qsilok_007_1328_0010_0010_0030_0060.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1328_0010_0010_0030_0060 |  |
| 1328 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1328.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1328 | 196352 |
| 1331 | han | `清實錄_高宗純皇帝實錄_卷1331_qsilok_007_1331_0010_0010_0010_0010.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1331_0010_0010_0010_0010 |  |
| 1331 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1331.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1331 | 196222 |
| 1346 | han | `清實錄_高宗純皇帝實錄_卷1346_qsilok_007_1346_0010_0010_0010_0080.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1346_0010_0010_0010_0080 |  |
| 1346 | han | `清實錄_高宗純皇帝實錄_卷1346_qsilok_007_1346_0010_0010_0030_0040.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1346_0010_0010_0030_0040 |  |
| 1346 | han | `清實錄_高宗純皇帝實錄_卷1346_qsilok_007_1346_0010_0010_0050_0030.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1346_0010_0010_0050_0030 |  |
| 1346 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1346.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1346 | 196266 |
| 1359 | han | `清實錄_高宗純皇帝實錄_卷1359_qsilok_007_1359_0010_0010_0010_0010.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1359_0010_0010_0010_0010 |  |
| 1359 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1359.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1359 | 196260 |
| 1384 | han | `清實錄_高宗純皇帝實錄_卷1384_qsilok_007_1384_0010_0010_0150_0010.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1384_0010_0010_0150_0010 |  |
| 1384 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1384.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1384 | 196296 |
| 1420 | han | `清實錄_高宗純皇帝實錄_卷1420_qsilok_007_1420_0010_0010_0100_0010.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1420_0010_0010_0100_0010 |  |
| 1420 | han | `清實錄_高宗純皇帝實錄_卷1420_qsilok_007_1420_0010_0010_0120_0010.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1420_0010_0010_0120_0010 |  |
| 1420 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1420.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1420 | 196292 |
| 1428 | han | `清實錄_高宗純皇帝實錄_卷1428_qsilok_007_1428_0010_0010_0040_0010.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1428_0010_0010_0040_0010 |  |
| 1428 | han | `清實錄_高宗純皇帝實錄_卷1428_qsilok_007_1428_0010_0010_0040_0020.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1428_0010_0010_0040_0020 |  |
| 1428 | han | `清實錄_高宗純皇帝實錄_卷1428_qsilok_007_1428_0010_0010_0050_0020.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1428_0010_0010_0050_0020 |  |
| 1428 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1428.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1428 | 196298 |
| 1463 | han | `清實錄_高宗純皇帝實錄_卷1463_qsilok_007_1463_0010_0010_0070_0070.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1463_0010_0010_0070_0070 |  |
| 1463 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1463.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1463 | 196320 |

## 5. Công cụ

- `hvalign` 0.3.0 (Lab/GK/hvalign), Python 3.11.6, PyYAML.
- Bước 4: tự nhận dạng định dạng nguồn (wikitext / text thuần / HTML sillok) và chuẩn hóa về một dạng.
- Bước 7: dóng 3 tầng (mục → đoạn → câu), chi phí Gale–Church + mốc can chi và tên riêng Hán Việt.
- Cấu hình: `config/project.yaml`, `config/works/HCB_14.yaml`, `config/phan_cong.tsv`.
