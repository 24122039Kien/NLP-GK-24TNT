# Báo cáo tự sinh – HCB_09

Ngày: 2026-11-26 · hvalign 0.3.0 · **Trạng thái: dóng tự động, ghi chú tự động**

## 1. Số cặp

Tổng: **132** cặp.

| Thành viên | Số cặp |
|---|---|
| Huy | 132 |

| Quyển | Thành viên | Số cặp |
|---|---|---|
| 76 | Huy | 132 |

Kiểu ghép: `1-1` 122, `1-2` 3, `10-1` 2, `2-1` 2, `9-1` 1, `1-10` 1, `1-8` 1

## 2. Số dòng văn bản sạch

- `03_text_sach/han.txt`: 25 dòng
- `03_text_sach/viet.txt`: 26 dòng

## 3. Kết quả tự kiểm tra

- Kiểm định định dạng TSV/XLSX: **đạt**
- Luật làm sạch đã áp dụng: R04_bo_chu_nho ×5, R06_bo_chu_han_trong_viet ×82, R07_bo_nam_duong_lich ×13, R10_chuan_hoa_khoang_trang_dau_cau ×4, R12_loai_tru ×55
- Loại trừ (không có bản dịch / không phải chính văn): 55 khối – Bản Việt không dịch Vương Cảnh (8); Bản Việt không dịch Tần Viên (4); Bản Việt không dịch Vương Hoán (8); Bản Việt không dịch Hứa Kinh (5); Bản Việt không dịch Đệ Ngũ Phóng (4); Bản Việt không dịch Lưu Củ (6); Bản Việt không dịch Lưu Sủng (9); Bản Việt không dịch Cừu Lãm (6); Bản Việt không dịch Đồng Khôi (5)
- Câu không ghép được (ghi ở `work/HCB_09/khong_ghep.tsv`, không đưa vào TSV): 0
- Cặp máy gắn cờ: 11 (`lech_moc` 10, `lech_do_dai` 6); người đã xem 0
- Hiệu đính đã áp: xác nhận đúng 0, sửa chữ 0, gộp 0, bỏ cặp sai 0 (quyết định lưu ở `hieu_dinh/HCB_09__<người>.tsv`)
- Cảnh báo khi làm sạch: 0 (xem `work/HCB_09/canh_bao.tsv`)
- Ghi chú tự động (dịch rút gọn, vế Việt thêm diễn giải, câu không được dịch): 5 cặp, ghi ở cột `Ghi chú` của sheet TRUY_VET
- Phạm vi theo trả lời của giảng viên: chỉ dóng hàng phần có song ngữ; phần chỉ một bản có thì không đưa vào dữ liệu (đã liệt kê ở mục Loại trừ và Câu không ghép được).
- Tỷ lệ lỗi theo §8 Guideline: chưa chấm mẫu (tuỳ chọn: app → Nâng cao → Chấm mẫu).

## 4. Nguồn tài liệu

| Quyển | Bản | Tệp | Định dạng đọc được | Nguồn trực tuyến | revid |
|---|---|---|---|---|---|
| 76 | han | `HauHanThu_q76_han.txt` | wikitext | https://zh.wikisource.org/wiki/後漢書/卷76 |  |
| 76 | viet | `HauHanThu_q76_viet.txt` | wikitext | https://vi.wikisource.org/wiki/Biên_dịch:Hậu_Hán_thư/Quyển_76 |  |

## 5. Công cụ

- `hvalign` 0.3.0 (Lab/GK/hvalign), Python 3.12.6, PyYAML.
- Bước 4: tự nhận dạng định dạng nguồn (wikitext / text thuần / HTML sillok) và chuẩn hóa về một dạng.
- Bước 7: dóng 3 tầng (mục → đoạn → câu), chi phí Gale–Church + mốc can chi và tên riêng Hán Việt.
- Cấu hình: `config/project.yaml`, `config/works/HCB_09.yaml`, `config/phan_cong.tsv`.
