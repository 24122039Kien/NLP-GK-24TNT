# Báo cáo tự sinh – HCB_01

Ngày: 2026-11-25 · hvalign 0.3.0 · **Trạng thái: dóng tự động, ghi chú tự động**

## 1. Số cặp

Tổng: **2343** cặp.

| Thành viên | Số cặp |
|---|---|
| Dang | 2343 |

| Quyển | Thành viên | Số cặp |
|---|---|---|
| 4 | Dang | 398 |
| 9 | Dang | 405 |
| 12 | Dang | 413 |
| 13 | Dang | 374 |
| 14 | Dang | 337 |
| 18 | Dang | 416 |

Kiểu ghép: `1-1` 1890, `1-2` 393, `1-3` 43, `2-2` 7, `2-1` 5, `1-5` 3, `1-4` 2

## 2. Số dòng văn bản sạch

- `03_text_sach/han.txt`: 743 dòng
- `03_text_sach/viet.txt`: 789 dòng

## 3. Kết quả tự kiểm tra

- Kiểm định định dạng TSV/XLSX: **đạt**; cảnh báo: 1 cặp trùng lặp hoàn toàn; 5 câu Hán xuất hiện ở hơn một cặp (có thể là câu lặp thật, ví dụ 帝曰)
- Luật làm sạch đã áp dụng: R06_bo_chu_han_trong_viet ×512, R08_bo_dong_tieu_de ×1, R10_chuan_hoa_khoang_trang_dau_cau ×1
- Loại trừ (không có bản dịch / không phải chính văn): 0 khối
- Câu không ghép được (ghi ở `work/HCB_01/khong_ghep.tsv`, không đưa vào TSV): 0
- Cặp máy gắn cờ: 46 (`lech_moc` 23, `lech_do_dai` 17, `n-m` 7); người đã xem 0
- Hiệu đính đã áp: xác nhận đúng 0, sửa chữ 0, gộp 0, bỏ cặp sai 0 (quyết định lưu ở `hieu_dinh/HCB_01__<người>.tsv`)
- Cảnh báo khi làm sạch: 3 (xem `work/HCB_01/canh_bao.tsv`)
- Ghi chú tự động (dịch rút gọn, vế Việt thêm diễn giải, câu không được dịch): 0 cặp, ghi ở cột `Ghi chú` của sheet TRUY_VET
- Phạm vi theo trả lời của giảng viên: chỉ dóng hàng phần có song ngữ; phần chỉ một bản có thì không đưa vào dữ liệu (đã liệt kê ở mục Loại trừ và Câu không ghép được).
- Tỷ lệ lỗi theo §8 Guideline: chưa chấm mẫu (tuỳ chọn: app → Nâng cao → Chấm mẫu).

## 4. Nguồn tài liệu

| Quyển | Bản | Tệp | Định dạng đọc được | Nguồn trực tuyến | revid |
|---|---|---|---|---|---|
| 4 | han | `續資治通鑑_卷004.wikitext` | wikitext | https://zh.wikisource.org/wiki/%E7%BA%8C%E8%B3%87%E6%B2%BB%E9%80%9A%E9%91%91/%E5%8D%B7004 | 2299538 |
| 4 | viet | `Tục_tư_trị_thông_giám_Quyển_4.wikitext` | wikitext | https://vi.wikisource.org/wiki/T%E1%BB%A5c_t%C6%B0_tr%E1%BB%8B_th%C3%B4ng_gi%C3%A1m/Quy%E1%BB%83n_4 | 202706 |
| 9 | han | `續資治通鑑_卷009.wikitext` | wikitext | https://zh.wikisource.org/wiki/%E7%BA%8C%E8%B3%87%E6%B2%BB%E9%80%9A%E9%91%91/%E5%8D%B7009 | 2606561 |
| 9 | viet | `Tục_tư_trị_thông_giám_Quyển_9.wikitext` | wikitext | https://vi.wikisource.org/wiki/T%E1%BB%A5c_t%C6%B0_tr%E1%BB%8B_th%C3%B4ng_gi%C3%A1m/Quy%E1%BB%83n_9 | 202681 |
| 12 | han | `續資治通鑑_卷012.wikitext` | wikitext | https://zh.wikisource.org/wiki/%E7%BA%8C%E8%B3%87%E6%B2%BB%E9%80%9A%E9%91%91/%E5%8D%B7012 | 1515100 |
| 12 | viet | `Tục_tư_trị_thông_giám_Quyển_12.wikitext` | wikitext | https://vi.wikisource.org/wiki/T%E1%BB%A5c_t%C6%B0_tr%E1%BB%8B_th%C3%B4ng_gi%C3%A1m/Quy%E1%BB%83n_12 | 203303 |
| 13 | han | `續資治通鑑_卷013.wikitext` | wikitext | https://zh.wikisource.org/wiki/%E7%BA%8C%E8%B3%87%E6%B2%BB%E9%80%9A%E9%91%91/%E5%8D%B7013 | 2601957 |
| 13 | viet | `Tục_tư_trị_thông_giám_Quyển_13.wikitext` | wikitext | https://vi.wikisource.org/wiki/T%E1%BB%A5c_t%C6%B0_tr%E1%BB%8B_th%C3%B4ng_gi%C3%A1m/Quy%E1%BB%83n_13 | 202698 |
| 14 | han | `續資治通鑑_卷014.wikitext` | wikitext | https://zh.wikisource.org/wiki/%E7%BA%8C%E8%B3%87%E6%B2%BB%E9%80%9A%E9%91%91/%E5%8D%B7014 | 2271043 |
| 14 | viet | `Tục_tư_trị_thông_giám_Quyển_14.wikitext` | wikitext | https://vi.wikisource.org/wiki/T%E1%BB%A5c_t%C6%B0_tr%E1%BB%8B_th%C3%B4ng_gi%C3%A1m/Quy%E1%BB%83n_14 | 202701 |
| 18 | han | `續資治通鑑_卷018.wikitext` | wikitext | https://zh.wikisource.org/wiki/%E7%BA%8C%E8%B3%87%E6%B2%BB%E9%80%9A%E9%91%91/%E5%8D%B7018 | 2260856 |
| 18 | viet | `Tục_tư_trị_thông_giám_Quyển_18.wikitext` | wikitext | https://vi.wikisource.org/wiki/T%E1%BB%A5c_t%C6%B0_tr%E1%BB%8B_th%C3%B4ng_gi%C3%A1m/Quy%E1%BB%83n_18 | 202715 |

## 5. Công cụ

- `hvalign` 0.3.0 (Lab/GK/hvalign), Python 3.11.6, PyYAML.
- Bước 4: tự nhận dạng định dạng nguồn (wikitext / text thuần / HTML sillok) và chuẩn hóa về một dạng.
- Bước 7: dóng 3 tầng (mục → đoạn → câu), chi phí Gale–Church + mốc can chi và tên riêng Hán Việt.
- Cấu hình: `config/project.yaml`, `config/works/HCB_01.yaml`, `config/phan_cong.tsv`.
