# Báo cáo tự sinh – HCB_14

Ngày: 2026-11-26 · hvalign 0.3.4 · **Trạng thái: dóng tự động, ghi chú tự động; người đã xem 80/101 cặp máy gắn cờ**

## 1. Số cặp

Tổng: **912** cặp.

| Thành viên | Số cặp |
|---|---|
| Dang | 284 |
| Huy | 225 |
| Kien | 124 |
| Tai | 279 |

| Quyển | Thành viên | Số cặp |
|---|---|---|
| 1327 | Huy | 26 |
| 1328 | Dang | 86 |
| 1331 | Dang | 14 |
| 1333 | Kien | 62 |
| 1335 | Tai | 23 |
| 1337 | Tai | 21 |
| 1339 | Kien | 23 |
| 1346 | Dang | 85 |
| 1357 | Kien | 30 |
| 1358 | Tai | 63 |
| 1359 | Dang | 3 |
| 1360 | Tai | 22 |
| 1361 | Huy | 66 |
| 1362 | Tai | 42 |
| 1363 | Huy | 70 |
| 1381 | Huy | 38 |
| 1384 | Dang | 12 |
| 1410 | Tai | 11 |
| 1419 | Huy | 6 |
| 1420 | Dang | 17 |
| 1421 | Tai | 86 |
| 1428 | Dang | 46 |
| 1429 | Huy | 19 |
| 1438 | Kien | 9 |
| 1445 | Tai | 11 |
| 1463 | Dang | 21 |

Kiểu ghép: `1-1` 339, `3-1` 152, `2-1` 127, `4-1` 72, `5-1` 58, `6-1` 56, `2-2` 35, `7-1` 23, `1-2` 15, `8-1` 13, `10-1` 12, `9-1` 9, `1-3` 1

- Phạm vi được giao (`config/phan_cong.tsv`): 26 quyển; đã dóng **26/26** (đủ).
- Độ phủ: các cặp chứa **100.0%** số chữ Hán và **100.0%** số âm tiết Việt của `03_text_sach` (phần chưa phủ là câu không ghép được hoặc cặp bỏ khi hiệu đính; phần chỉ một bản có đã bị loại trừ từ Bước 5, không tính ở đây).

## 2. Số dòng văn bản sạch

- `03_text_sach/han.txt`: 81 dòng
- `03_text_sach/viet.txt`: 296 dòng
- Thư mục nộp: `01_nguon` (dữ liệu đã tải/crawl), `03_text_sach` (text Hán và Việt đã trích xuất và làm sạch), `04_dong_hang` (TSV + XLSX), `bao_cao.md`. Không có `02_ocr_tho`: nguồn là text số (wikitext/HTML/txt), không phải ảnh/PDF scan, nên không OCR (theo nhận xét của giảng viên 18/11). Tệp `.pdf` trong `01_nguon` là bản in của trang nguồn, lưu để đối chiếu.

## 3. Kết quả tự kiểm tra

- Kiểm định định dạng TSV/XLSX: **đạt**; cảnh báo: 12 cặp trùng lặp hoàn toàn; 17 câu Hán xuất hiện ở hơn một cặp (có thể là câu lặp thật, ví dụ 帝曰)
- Luật làm sạch đã áp dụng: R03_bo_ref ×9, R06_bo_chu_han_trong_viet ×417, R07_bo_nam_duong_lich ×14, R10_chuan_hoa_khoang_trang_dau_cau ×70, R12_loai_tru ×63
- Loại trừ (không có bản dịch / không phải chính văn): 63 khối – Thơ ngự chế Q1358: nguyên văn chữ Hán, phiên âm, nhãn và Dịch thơ (đã giữ Dịch nghĩa) (27); Thơ ngự chế Q1421: nguyên văn chữ Hán, phiên âm và nhãn (giữ Dịch thơ) (18); Thơ ngự chế Q1428: nguyên văn chữ Hán, phiên âm và nhãn (giữ Dịch thơ) (18)
- Câu không ghép được (ghi ở `work/HCB_14/khong_ghep.tsv`, không đưa vào TSV): 3
- Cặp máy gắn cờ: 101 (`lech_moc` 58, `n-m` 35, `lech_do_dai` 11); người đã xem 80
- Hiệu đính đã áp: xác nhận đúng 0, sửa chữ 544, gộp 0, bỏ cặp sai 22 (quyết định lưu ở `hieu_dinh/HCB_14__<người>.tsv`)
- Cảnh báo khi làm sạch: 4 (xem `work/HCB_14/canh_bao.tsv`)
- Ghi chú tự động (dịch rút gọn, vế Việt thêm diễn giải, câu không được dịch): 8 cặp, ghi ở cột `Ghi chú` của sheet TRUY_VET
- Phạm vi theo trả lời của giảng viên: chỉ dóng hàng phần có song ngữ; phần chỉ một bản có thì không đưa vào dữ liệu (đã liệt kê ở mục Loại trừ và Câu không ghép được).
- Tỷ lệ lỗi theo §8 Guideline: chưa chấm mẫu (tuỳ chọn: app → Nâng cao → Chấm mẫu).

## 4. Nguồn tài liệu

| Quyển | Bản | Tệp | Định dạng đọc được | Nguồn trực tuyến | revid |
|---|---|---|---|---|---|
| 1327 | han | `清實錄_高宗純皇帝實錄_卷1327_qsilok_007_1327_0010_0010_0120_0020.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1327_0010_0010_0120_0020 |  |
| 1327 | viet | `ThanhThucLuc_q1327_viet.txt` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1327 | 204133 |
| 1328 | han | `清實錄_高宗純皇帝實錄_卷1328_qsilok_007_1328_0010_0010_0030_0030.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1328_0010_0010_0030_0030 |  |
| 1328 | han | `清實錄_高宗純皇帝實錄_卷1328_qsilok_007_1328_0010_0010_0030_0040.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1328_0010_0010_0030_0040 |  |
| 1328 | han | `清實錄_高宗純皇帝實錄_卷1328_qsilok_007_1328_0010_0010_0030_0050.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1328_0010_0010_0030_0050 |  |
| 1328 | han | `清實錄_高宗純皇帝實錄_卷1328_qsilok_007_1328_0010_0010_0030_0060.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1328_0010_0010_0030_0060 |  |
| 1328 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1328.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1328 | 196352 |
| 1331 | han | `清實錄_高宗純皇帝實錄_卷1331_qsilok_007_1331_0010_0010_0010_0010.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1331_0010_0010_0010_0010 |  |
| 1331 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1331.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1331 | 196222 |
| 1333 | han | `清實錄_高宗純皇帝實錄_卷1333_qsilok_007_1333_0010_0010_0060_0030.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1333_0010_0010_0060_0030 |  |
| 1333 | han | `清實錄_高宗純皇帝實錄_卷1333_qsilok_007_1333_0010_0010_0060_0040.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1333_0010_0010_0060_0040 |  |
| 1333 | han | `清實錄_高宗純皇帝實錄_卷1333_qsilok_007_1333_0010_0010_0060_0050.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1333_0010_0010_0060_0050 |  |
| 1333 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1333.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1333 | 196240 |
| 1335 | han | `清實錄_高宗純皇帝實錄_卷1335_qsilok_007_1335_0010_0010_0090_0020.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1335_0010_0010_0090_0020 |  |
| 1335 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1335.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1335 | 196241 |
| 1337 | han | `清實錄_高宗純皇帝實錄_卷1337_qsilok_007_1337_0010_0010_0050_0030.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1337_0010_0010_0050_0030 |  |
| 1337 | han | `清實錄_高宗純皇帝實錄_卷1337_qsilok_007_1337_0010_0010_0110_0030.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1337_0010_0010_0110_0030 |  |
| 1337 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1337.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1337 | 196242 |
| 1339 | han | `清實錄_高宗純皇帝實錄_卷1339_qsilok_007_1339_0010_0010_0080_0040.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1339_0010_0010_0080_0040 |  |
| 1339 | han | `清實錄_高宗純皇帝實錄_卷1339_qsilok_007_1339_0010_0010_0080_0050.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1339_0010_0010_0080_0050 |  |
| 1339 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1339.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1339 | 196246 |
| 1346 | han | `清實錄_高宗純皇帝實錄_卷1346_qsilok_007_1346_0010_0010_0010_0080.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1346_0010_0010_0010_0080 |  |
| 1346 | han | `清實錄_高宗純皇帝實錄_卷1346_qsilok_007_1346_0010_0010_0030_0040.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1346_0010_0010_0030_0040 |  |
| 1346 | han | `清實錄_高宗純皇帝實錄_卷1346_qsilok_007_1346_0010_0010_0050_0030.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1346_0010_0010_0050_0030 |  |
| 1346 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1346.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1346 | 196266 |
| 1357 | han | `清實錄_高宗純皇帝實錄_卷1357_qsilok_007_1357_0010_0010_0090_0020.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1357_0010_0010_0090_0020 |  |
| 1357 | han | `清實錄_高宗純皇帝實錄_卷1357_qsilok_007_1357_0010_0010_0110_0030.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1357_0010_0010_0110_0030 |  |
| 1357 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1357.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1357 | 196257 |
| 1358 | han | `清實錄_高宗純皇帝實錄_卷1358_qsilok_007_1358_0010_0010_0020_0010.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1358_0010_0010_0020_0010 |  |
| 1358 | han | `清實錄_高宗純皇帝實錄_卷1358_qsilok_007_1358_0010_0010_0050_0020.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1358_0010_0010_0050_0020 |  |
| 1358 | han | `清實錄_高宗純皇帝實錄_卷1358_qsilok_007_1358_0010_0010_0060_0020.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1358_0010_0010_0060_0020 |  |
| 1358 | han | `清實錄_高宗純皇帝實錄_卷1358_qsilok_007_1358_0010_0010_0100_0040.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1358_0010_0010_0100_0040 |  |
| 1358 | han | `清實錄_高宗純皇帝實錄_卷1358_qsilok_007_1358_0010_0010_0110_0010.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1358_0010_0010_0110_0010 |  |
| 1358 | han | `清實錄_高宗純皇帝實錄_卷1358_qsilok_007_1358_0010_0010_0110_0020.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1358_0010_0010_0110_0020 |  |
| 1358 | han | `清實錄_高宗純皇帝實錄_卷1358_qsilok_007_1358_0010_0010_0110_0030.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1358_0010_0010_0110_0030 |  |
| 1358 | han | `清實錄_高宗純皇帝實錄_卷1358_qsilok_007_1358_0010_0010_0140_0010.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1358_0010_0010_0140_0010 |  |
| 1358 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1358.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1358 | 196291 |
| 1359 | han | `清實錄_高宗純皇帝實錄_卷1359_qsilok_007_1359_0010_0010_0010_0010.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1359_0010_0010_0010_0010 |  |
| 1359 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1359.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1359 | 196260 |
| 1360 | han | `清實錄_高宗純皇帝實錄_卷1360_qsilok_007_1360_0010_0010_0010_0010.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1360_0010_0010_0010_0010 |  |
| 1360 | han | `清實錄_高宗純皇帝實錄_卷1360_qsilok_007_1360_0010_0010_0110_0030.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1360_0010_0010_0110_0030 |  |
| 1360 | han | `清實錄_高宗純皇帝實錄_卷1360_qsilok_007_1360_0010_0010_0120_0010.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1360_0010_0010_0120_0010 |  |
| 1360 | han | `清實錄_高宗純皇帝實錄_卷1360_qsilok_007_1360_0010_0010_0120_0020.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1360_0010_0010_0120_0020 |  |
| 1360 | han | `清實錄_高宗純皇帝實錄_卷1360_qsilok_007_1360_0010_0010_0120_0030.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1360_0010_0010_0120_0030 |  |
| 1360 | han | `清實錄_高宗純皇帝實錄_卷1360_qsilok_007_1360_0010_0010_0120_0050.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1360_0010_0010_0120_0050 |  |
| 1360 | han | `清實錄_高宗純皇帝實錄_卷1360_qsilok_007_1360_0010_0010_0130_0040.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1360_0010_0010_0130_0040 |  |
| 1360 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1360.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1360 | 196262 |
| 1361 | han | `清實錄_高宗純皇帝實錄_卷1361_qsilok_007_1361_0010_0010_0040_0020.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1361_0010_0010_0040_0020 |  |
| 1361 | han | `清實錄_高宗純皇帝實錄_卷1361_qsilok_007_1361_0010_0010_0050_0010.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1361_0010_0010_0050_0010 |  |
| 1361 | han | `清實錄_高宗純皇帝實錄_卷1361_qsilok_007_1361_0010_0010_0070_0040.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1361_0010_0010_0070_0040 |  |
| 1361 | han | `清實錄_高宗純皇帝實錄_卷1361_qsilok_007_1361_0010_0010_0100_0020.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1361_0010_0010_0100_0020 |  |
| 1361 | han | `清實錄_高宗純皇帝實錄_卷1361_qsilok_007_1361_0010_0010_0120_0010.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1361_0010_0010_0120_0010 |  |
| 1361 | viet | `ThanhThucLuc_q1361_viet.txt` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1361 | 196264 |
| 1362 | han | `清實錄_高宗純皇帝實錄_卷1362_qsilok_007_1362_0010_0010_0050_0020.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1362_0010_0010_0050_0020 |  |
| 1362 | han | `清實錄_高宗純皇帝實錄_卷1362_qsilok_007_1362_0010_0010_0120_0030.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1362_0010_0010_0120_0030 |  |
| 1362 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1362.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1362 | 196268 |
| 1363 | han | `清實錄_高宗純皇帝實錄_卷1363_qsilok_007_1363_0010_0010_0020_0050.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1363_0010_0010_0020_0050 |  |
| 1363 | han | `清實錄_高宗純皇帝實錄_卷1363_qsilok_007_1363_0010_0010_0070_0040.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1363_0010_0010_0070_0040 |  |
| 1363 | han | `清實錄_高宗純皇帝實錄_卷1363_qsilok_007_1363_0010_0010_0100_0020.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1363_0010_0010_0100_0020 |  |
| 1363 | han | `清實錄_高宗純皇帝實錄_卷1363_qsilok_007_1363_0010_0010_0100_0030.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1363_0010_0010_0100_0030 |  |
| 1363 | viet | `ThanhThucLuc_q1363_viet.txt` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1363 | 196270 |
| 1381 | han | `清實錄_高宗純皇帝實錄_卷1381_qsilok_007_1381_0010_0010_0060_0020.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1381_0010_0010_0060_0020 |  |
| 1381 | han | `清實錄_高宗純皇帝實錄_卷1381_qsilok_007_1381_0010_0010_0060_0030.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1381_0010_0010_0060_0030 |  |
| 1381 | han | `清實錄_高宗純皇帝實錄_卷1381_qsilok_007_1381_0010_0010_0080_0010.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1381_0010_0010_0080_0010 |  |
| 1381 | viet | `ThanhThucLuc_q1381_viet.txt` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1381 | 196294 |
| 1384 | han | `清實錄_高宗純皇帝實錄_卷1384_qsilok_007_1384_0010_0010_0150_0010.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1384_0010_0010_0150_0010 |  |
| 1384 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1384.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1384 | 196296 |
| 1410 | han | `清實錄_高宗純皇帝實錄_卷1410_qsilok_007_1410_0010_0010_0090_0070.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1410_0010_0010_0090_0070 |  |
| 1410 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1410.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1410 | 196288 |
| 1419 | han | `清實錄_高宗純皇帝實錄_卷1419_qsilok_007_1419_0010_0010_0090_0010.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1419_0010_0010_0090_0010 |  |
| 1419 | viet | `ThanhThucLuc_q1419_viet.txt` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1419 | 196337 |
| 1420 | han | `清實錄_高宗純皇帝實錄_卷1420_qsilok_007_1420_0010_0010_0100_0010.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1420_0010_0010_0100_0010 |  |
| 1420 | han | `清實錄_高宗純皇帝實錄_卷1420_qsilok_007_1420_0010_0010_0120_0010.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1420_0010_0010_0120_0010 |  |
| 1420 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1420.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1420 | 196292 |
| 1421 | han | `清實錄_高宗純皇帝實錄_卷1421_qsilok_007_1421_0010_0010_0040_0010.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1421_0010_0010_0040_0010 |  |
| 1421 | han | `清實錄_高宗純皇帝實錄_卷1421_qsilok_007_1421_0010_0010_0070_0020.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1421_0010_0010_0070_0020 |  |
| 1421 | han | `清實錄_高宗純皇帝實錄_卷1421_qsilok_007_1421_0010_0010_0070_0030.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1421_0010_0010_0070_0030 |  |
| 1421 | han | `清實錄_高宗純皇帝實錄_卷1421_qsilok_007_1421_0010_0010_0070_0040.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1421_0010_0010_0070_0040 |  |
| 1421 | han | `清實錄_高宗純皇帝實錄_卷1421_qsilok_007_1421_0010_0010_0070_0050.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1421_0010_0010_0070_0050 |  |
| 1421 | han | `清實錄_高宗純皇帝實錄_卷1421_qsilok_007_1421_0010_0010_0070_0060.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1421_0010_0010_0070_0060 |  |
| 1421 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1421.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1421 | 196286 |
| 1428 | han | `清實錄_高宗純皇帝實錄_卷1428_qsilok_007_1428_0010_0010_0040_0010.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1428_0010_0010_0040_0010 |  |
| 1428 | han | `清實錄_高宗純皇帝實錄_卷1428_qsilok_007_1428_0010_0010_0040_0020.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1428_0010_0010_0040_0020 |  |
| 1428 | han | `清實錄_高宗純皇帝實錄_卷1428_qsilok_007_1428_0010_0010_0050_0020.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1428_0010_0010_0050_0020 |  |
| 1428 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1428.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1428 | 196298 |
| 1429 | han | `清實錄_高宗純皇帝實錄_卷1429_qsilok_007_1429_0010_0010_0140_0050.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1429_0010_0010_0140_0050 |  |
| 1429 | viet | `ThanhThucLuc_q1429_viet.txt` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1429 | 196314 |
| 1438 | han | `清實錄_高宗純皇帝實錄_卷1438_qsilok_007_1438_0010_0010_0020_0070.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1438_0010_0010_0020_0070 |  |
| 1438 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1438.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1438 | 196316 |
| 1445 | han | `清實錄_高宗純皇帝實錄_卷1445_qsilok_007_1445_0010_0010_0130_0050.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1445_0010_0010_0130_0050 |  |
| 1445 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1445.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1445 | 196318 |
| 1463 | han | `清實錄_高宗純皇帝實錄_卷1463_qsilok_007_1463_0010_0010_0070_0070.html` | html | https://sillok.history.go.kr/mc/id/qsilok_007_1463_0010_0010_0070_0070 |  |
| 1463 | viet | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1463.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Thanh_th%E1%BB%B1c_l%E1%BB%A5c/Cao_T%C3%B4ng_Thu%E1%BA%A7n_Ho%C3%A0ng_%C4%91%E1%BA%BF_th%E1%BB%B1c_l%E1%BB%A5c/Quy%E1%BB%83n_1463 | 196320 |

## 5. Công cụ

- `hvalign` 0.3.4 (Lab/GK/hvalign), Python 3.12.6, PyYAML.
- Bước 4: tự nhận dạng định dạng nguồn (wikitext / text thuần / HTML sillok) và chuẩn hóa về một dạng.
- Bước 7: dóng 3 tầng (mục → đoạn → câu), chi phí Gale–Church + mốc can chi và tên riêng Hán Việt.
- Cấu hình: `config/project.yaml`, `config/works/HCB_14.yaml`, `config/phan_cong.tsv`.
