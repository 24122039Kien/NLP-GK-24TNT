# Báo cáo tự sinh – HCB_06

Ngày: 2026-11-26 · hvalign 0.3.0 · **Trạng thái: dóng tự động, ghi chú tự động**

## 1. Số cặp

Tổng: **365** cặp.

| Thành viên | Số cặp |
|---|---|
| Huy | 365 |

| Quyển | Thành viên | Số cặp |
|---|---|---|
| 28 | Huy | 365 |

Kiểu ghép: `1-1` 238, `1-2` 114, `10-1` 7, `8-1` 2, `9-1` 1, `7-1` 1, `2-2` 1, `1-3` 1

## 2. Số dòng văn bản sạch

- `03_text_sach/han.txt`: 214 dòng
- `03_text_sach/viet.txt`: 135 dòng

## 3. Kết quả tự kiểm tra

- Kiểm định định dạng TSV/XLSX: **đạt**; cảnh báo: 1 cặp có chữ Latin ở vế Hán (thường là mã lỗi chữ chưa tra); 4 cặp trùng lặp hoàn toàn; 4 câu Hán xuất hiện ở hơn một cặp (có thể là câu lặp thật, ví dụ 帝曰)
- Luật làm sạch đã áp dụng: R03_bo_ref ×1, R06_bo_chu_han_trong_viet ×1930, R07_bo_nam_duong_lich ×5, R10_chuan_hoa_khoang_trang_dau_cau ×1, R12_loai_tru ×3
- Loại trừ (không có bản dịch / không phải chính văn): 3 khối – Bản Việt không có phần khảo bản (2); Bản Việt không có phần giáo khám (1)
- Câu không ghép được (ghi ở `work/HCB_06/khong_ghep.tsv`, không đưa vào TSV): 270
- Cặp máy gắn cờ: 25 (`lech_moc` 24, `lech_do_dai` 2, `n-m` 1); người đã xem 0
- Hiệu đính đã áp: xác nhận đúng 0, sửa chữ 0, gộp 0, bỏ cặp sai 0 (quyết định lưu ở `hieu_dinh/HCB_06__<người>.tsv`)
- Cảnh báo khi làm sạch: 1 (xem `work/HCB_06/canh_bao.tsv`)
- Ghi chú tự động (dịch rút gọn, vế Việt thêm diễn giải, câu không được dịch): 79 cặp, ghi ở cột `Ghi chú` của sheet TRUY_VET
- Phạm vi theo trả lời của giảng viên: chỉ dóng hàng phần có song ngữ; phần chỉ một bản có thì không đưa vào dữ liệu (đã liệt kê ở mục Loại trừ và Câu không ghép được).
- Tỷ lệ lỗi theo §8 Guideline: chưa chấm mẫu (tuỳ chọn: app → Nâng cao → Chấm mẫu).

## 4. Nguồn tài liệu

| Quyển | Bản | Tệp | Định dạng đọc được | Nguồn trực tuyến | revid |
|---|---|---|---|---|---|
| 28 | han | `HanThu_q028_han.txt` | wikitext | https://zh.wikisource.org/wiki/漢書/卷028上 |  |
| 28 | viet | `HanThu_q028_viet.txt` | wikitext | https://vi.wikisource.org/wiki/Biên_dịch:Hán_thư/Quyển_028_thượng |  |

## 5. Công cụ

- `hvalign` 0.3.0 (Lab/GK/hvalign), Python 3.12.6, PyYAML.
- Bước 4: tự nhận dạng định dạng nguồn (wikitext / text thuần / HTML sillok) và chuẩn hóa về một dạng.
- Bước 7: dóng 3 tầng (mục → đoạn → câu), chi phí Gale–Church + mốc can chi và tên riêng Hán Việt.
- Cấu hình: `config/project.yaml`, `config/works/HCB_06.yaml`, `config/phan_cong.tsv`.
