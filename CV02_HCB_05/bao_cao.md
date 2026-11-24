# Báo cáo tự sinh – HCB_05

Ngày: 2026-11-24 · hvalign 0.3.0 · **Trạng thái: dóng tự động, ghi chú tự động**

## 1. Số cặp

Tổng: **70** cặp.

| Thành viên | Số cặp |
|---|---|
| Kien | 70 |

| Quyển | Thành viên | Số cặp |
|---|---|---|
| 1 | Kien | 70 |

Kiểu ghép: `1-1` 44, `1-2` 15, `1-3` 8, `2-2` 1, `2-1` 1, `1-4` 1

## 2. Số dòng văn bản sạch

- `03_text_sach/han.txt`: 72 dòng
- `03_text_sach/viet.txt`: 74 dòng

## 3. Kết quả tự kiểm tra

- Kiểm định định dạng TSV/XLSX: **đạt**
- Luật làm sạch đã áp dụng: R05_bo_dan_nguon ×148, R06_bo_chu_han_trong_viet ×64, R10_chuan_hoa_khoang_trang_dau_cau ×40, R12_loai_tru ×33
- Loại trừ (không có bản dịch / không phải chính văn): 33 khối – Ghi chú khảo chứng 按 / trích dẫn của người biên tập (17); Bản dịch ghi chú khảo chứng 按 (dòng : hoặc khoản *) (16)
- Câu không ghép được (ghi ở `work/HCB_05/khong_ghep.tsv`, không đưa vào TSV): 0
- Cặp máy gắn cờ: 6 (`lech_moc` 3, `lech_do_dai` 2, `n-m` 1); người đã xem 0
- Hiệu đính đã áp: xác nhận đúng 0, sửa chữ 0, gộp 0, bỏ cặp sai 0 (quyết định lưu ở `hieu_dinh/HCB_05__<người>.tsv`)
- Cảnh báo khi làm sạch: 0 (xem `work/HCB_05/canh_bao.tsv`)
- Ghi chú tự động (dịch rút gọn, vế Việt thêm diễn giải, câu không được dịch): 1 cặp, ghi ở cột `Ghi chú` của sheet TRUY_VET
- Phạm vi theo trả lời của giảng viên: chỉ dóng hàng phần có song ngữ; phần chỉ một bản có thì không đưa vào dữ liệu (đã liệt kê ở mục Loại trừ và Câu không ghép được).
- Tỷ lệ lỗi theo §8 Guideline: chưa chấm mẫu (tuỳ chọn: app → Nâng cao → Chấm mẫu).

## 4. Nguồn tài liệu

| Quyển | Bản | Tệp | Định dạng đọc được | Nguồn trực tuyến | revid |
|---|---|---|---|---|---|
| 1 | han | `交州記_(嶺南遺書本).wikitext` | wikitext | https://zh.wikisource.org/wiki/%E4%BA%A4%E5%B7%9E%E8%A8%98_%28%E5%B6%BA%E5%8D%97%E9%81%BA%E6%9B%B8%E6%9C%AC%29 | 2455400 |
| 1 | viet | `Biên_dịch_Giao_Châu_ký.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:Giao_Ch%C3%A2u_k%C3%BD | 195196 |

## 5. Công cụ

- `hvalign` 0.3.0 (Lab/GK/hvalign), Python 3.11.9, PyYAML.
- Bước 4: tự nhận dạng định dạng nguồn (wikitext / text thuần / HTML sillok) và chuẩn hóa về một dạng.
- Bước 7: dóng 3 tầng (mục → đoạn → câu), chi phí Gale–Church + mốc can chi và tên riêng Hán Việt.
- Cấu hình: `config/project.yaml`, `config/works/HCB_05.yaml`, `config/phan_cong.tsv`.
