# Báo cáo tự sinh – HCB_10

Ngày: 2026-11-25 · hvalign 0.3.0 · **Trạng thái: dóng tự động, ghi chú tự động**

## 1. Số cặp

Tổng: **38** cặp.

| Thành viên | Số cặp |
|---|---|
| Dang | 38 |

| Quyển | Thành viên | Số cặp |
|---|---|---|
| 81 | Dang | 38 |

Kiểu ghép: `1-1` 33, `1-2` 5

## 2. Số dòng văn bản sạch

- `03_text_sach/han.txt`: 5 dòng
- `03_text_sach/viet.txt`: 5 dòng

## 3. Kết quả tự kiểm tra

- Kiểm định định dạng TSV/XLSX: **đạt**
- Luật làm sạch đã áp dụng: R06_bo_chu_han_trong_viet ×18, R07_bo_nam_duong_lich ×1, R12_loai_tru ×107
- Loại trừ (không có bản dịch / không phải chính văn): 107 khối – Bản Việt không dịch truyện này (107)
- Câu không ghép được (ghi ở `work/HCB_10/khong_ghep.tsv`, không đưa vào TSV): 0
- Cặp máy gắn cờ: 2 (`lech_moc` 2); người đã xem 0
- Hiệu đính đã áp: xác nhận đúng 0, sửa chữ 0, gộp 0, bỏ cặp sai 0 (quyết định lưu ở `hieu_dinh/HCB_10__<người>.tsv`)
- Cảnh báo khi làm sạch: 0 (xem `work/HCB_10/canh_bao.tsv`)
- Ghi chú tự động (dịch rút gọn, vế Việt thêm diễn giải, câu không được dịch): 0 cặp, ghi ở cột `Ghi chú` của sheet TRUY_VET
- Phạm vi theo trả lời của giảng viên: chỉ dóng hàng phần có song ngữ; phần chỉ một bản có thì không đưa vào dữ liệu (đã liệt kê ở mục Loại trừ và Câu không ghép được).
- Tỷ lệ lỗi theo §8 Guideline: chưa chấm mẫu (tuỳ chọn: app → Nâng cao → Chấm mẫu).

## 4. Nguồn tài liệu

| Quyển | Bản | Tệp | Định dạng đọc được | Nguồn trực tuyến | revid |
|---|---|---|---|---|---|
| 81 | han | `後漢書_卷81.wikitext` | wikitext | https://zh.wikisource.org/wiki/%E5%BE%8C%E6%BC%A2%E6%9B%B8/%E5%8D%B781 | 2319542 |
| 81 | viet | `Biên_dịch_Hậu_Hán_thư_Quyển_81.wikitext` | wikitext | https://vi.wikisource.org/wiki/Bi%C3%AAn_d%E1%BB%8Bch:H%E1%BA%ADu_H%C3%A1n_th%C6%B0/Quy%E1%BB%83n_81 | 204353 |

## 5. Công cụ

- `hvalign` 0.3.0 (Lab/GK/hvalign), Python 3.11.6, PyYAML.
- Bước 4: tự nhận dạng định dạng nguồn (wikitext / text thuần / HTML sillok) và chuẩn hóa về một dạng.
- Bước 7: dóng 3 tầng (mục → đoạn → câu), chi phí Gale–Church + mốc can chi và tên riêng Hán Việt.
- Cấu hình: `config/project.yaml`, `config/works/HCB_10.yaml`, `config/phan_cong.tsv`.
