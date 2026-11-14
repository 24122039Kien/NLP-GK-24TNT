# Hướng dẫn dùng `hvalign` – chương trình dóng hàng chung của nhóm

**Dành cho:** cả nhóm (Kiên, Huy, Tài, Đăng). **Phiên bản:** 0.1.0, ngày 2026-11-10.
**Thiết kế chi tiết:** [implementation_plan.md](implementation_plan.md). **Phân việc kiểm tra:** [phan_viec_hvalign.md](phan_viec_hvalign.md).

---

## 1. Chương trình làm gì

Một lệnh chạy trọn Bước 4 → 7 của Guideline cho mọi tác phẩm có trên máy:

| Bước | Lệnh | Kết quả |
|---|---|---|
| 4 – Trích text | `extract` | `CV02_<MA>/02_ocr_tho/{han,viet}/<quyển>.tsv` |
| 5 – Làm sạch | `clean` | `CV02_<MA>/03_text_sach/han.txt`, `viet.txt` |
| 6 – Tách câu | `segment` | `work/<MA>/segments.jsonl` |
| 7 – Dóng hàng | `align` | `work/<MA>/alignment.jsonl` |
| Xuất, kiểm định, báo cáo | `export`, `validate`, `report` | `work/<MA>/xuat/<MA>_parallel.tsv`, `.xlsx`; sổ hiệu đính; `bao_cao.md` |

Kết quả dóng hàng **chưa được hiệu đính** nên mặc định chỉ xuất vào `work/<MA>/xuat/` để xem trước. Thư mục nộp `04_dong_hang/` chỉ được ghi khi thêm `--ban-giao`.

---

## 2. Cài đặt (một lần)

Cần Python 3.10 trở lên. Tại thư mục `Lab/GK`:

```
pip install -r requirements.txt
```

Chỉ cần `pyyaml`; `pytest` để chạy kiểm thử. Không cần `openpyxl`: chương trình tự ghi `.xlsx`.

---

## 3. Đưa nguồn của bạn vào

Chép tệp nguồn vào `CV02_<MA>/01_nguon/`. **Không cần đổi định dạng hay đổi tên.** Chương trình tự nhận ra:

| Câu hỏi | Chương trình tự xác định bằng | Ví dụ |
|---|---|---|
| Định dạng | Nội dung tệp, không chỉ đuôi | `.txt` có `{{…}}`, `== … ==`, `[[…]]` → đọc như wikitext; `.txt` không có markup → text thuần, mỗi dòng một đoạn; `.html` sillok → bộ đọc sillok |
| Bản Hán hay Việt | Thư mục `han/`, `viet/`; nếu không có thì hậu tố tên tệp `_han`, `_viet`; nếu vẫn không có thì tỷ lệ chữ Hán trong nội dung | `TTTTG_q03_han.txt` → Hán |
| Số quyển | Tên tệp | `卷002`, `Quyển_2`, `_q03_`, `qsilok_007_1333_…` → quyển 2, 2, 3, 1333 |
| Mã hóa | BOM | UTF-8 (có hoặc không BOM), UTF-16. Tệp mã hóa khác sẽ báo lỗi rõ ràng, không đoán bừa |

Nếu cùng một tài liệu có cả `.wikitext` và `.txt` cùng tên gốc, chương trình dùng `.wikitext`. PDF không dùng để trích text.

**Kiểm tra:** cả hai kiểu đặt tên đang có trong nhóm (của Kiên và của Huy) đều đã chạy thử. Tệp `.txt` chứa wikitext cho kết quả giống hệt tệp `.wikitext` cùng nội dung, kể cả khi lưu bằng Notepad (BOM + CRLF).

---

## 4. Khai báo phân công

Thêm các dòng của bạn vào [config/phan_cong.tsv](../config/phan_cong.tsv), các cột ngăn bằng TAB:

```
ma_tac_pham	quyen	thanh_vien
HCB_01	3	Huy
HCB_06	*	Huy
```

`*` nghĩa là cả tác phẩm. Số cặp của từng người được đếm theo tệp này.

---

## 5. Chạy

Tại `Lab/GK`:

```
python -m hvalign inventory                 # kiểm kê: đủ cặp Hán–Việt chưa, SHA-256, trùng bài
python -m hvalign run                       # chạy tất cả tác phẩm có trên máy
python -m hvalign run --work HCB_06 HCB_08  # chỉ vài tác phẩm
python -m hvalign status                    # số cặp theo tác phẩm và thành viên
python -m hvalign mau --so-cap 30           # lấy ngẫu nhiên 30 cặp/người ra Excel để chấm Đúng/Sai
python -m hvalign clean --work HCB_13       # chạy lại một bước sau khi sửa cấu hình
python -m pytest -q                         # kiểm thử tự động (13 bài)
```

Mọi bước đều chạy lại được bất kỳ lúc nào và cho cùng kết quả. Tệp nguồn trong `01_nguon/` không bao giờ bị sửa.

---

## 6. Cấu hình riêng từng tác phẩm

Tệp `config/works/<MA>.yaml` ghi đè cấu hình chung trong `config/project.yaml`. Các mục hay dùng:

```yaml
loai_tru:          # vùng không có bản dịch → không dóng, ghi vào work/<MA>/loai_tru.tsv
  - {lang: han, muc: 大理, ly_do: "Bản Việt không dịch mục 大理"}
  - {lang: viet, regex: "^(Theo |Chú:)", ly_do: "Ghi chú của người dịch"}
co_rui_ro:         # gắn cờ để ưu tiên hiệu đính
  - {lang: han, regex: "^若荆、楊無事", co: rut_gon}
lam_sach:          # bật/tắt từng luật R01–R12
  R05_viet_dan_nguon_cuoi_khoan: true
tach_cau:
  han_cham_la_ranh_gioi_mem: true      # văn bản sillok
```

Cấu hình của 7 tác phẩm phần Kiên đã có sẵn trong `config/works/`, có thể dùng làm mẫu.

---

## 7. Đọc kết quả

| Tệp | Dùng để |
|---|---|
| `work/<MA>/bao_cao.md` | Báo cáo tự sinh: số cặp, số dòng, kết quả tự kiểm tra, nguồn, công cụ (đủ 5 mục tối thiểu của Guideline) |
| `work/<MA>/hieu_dinh/<MA>_<người>.xlsx` | **Sổ hiệu đính:** cặp có cờ và chi phí cao nằm trên cùng |
| `work/<MA>/khong_ghep.tsv` | Câu không tìm được cặp; không đưa vào TSV, nên không bị tính lỗi `MISSING` |
| `work/<MA>/loai_tru.tsv` | Vùng bị loại kèm lý do |
| `work/<MA>/canh_bao.tsv` | Chỗ cần người xem: mã lỗi chữ chưa tra, chữ Hán còn trong bản Việt |
| `work/<MA>/clean_log.tsv` | Số lần áp dụng từng luật làm sạch trên từng quyển |
| `work/<MA>/mau/<MA>_mau_<N>.xlsx` | Mẫu ngẫu nhiên (lệnh `mau`) để chấm tỷ lệ đúng |

**Ý nghĩa các cờ trong sổ hiệu đính:**

| Cờ | Nghĩa |
|---|---|
| `lech_do_dai` | Độ dài hai vế lệch nhiều so với tỷ lệ chung của quyển |
| `lech_moc` | Có can chi hoặc tên riêng ở một vế mà vế kia không có |
| `rut_gon` | Thuộc đoạn đã biết là dịch rút gọn |
| `n-m` | Gộp nhiều câu ở cả hai vế |

---

## 8. Việc chưa làm

- **Áp bản sửa từ sổ hiệu đính** (`review apply`, kế hoạch mục 7.1): chưa có. Hiện chỉ mới sinh sổ hiệu đính.
- **Bộ mẫu chuẩn và đánh giá A/B/C** (kế hoạch mục 6.4): chưa có. Trọng số hiện là giá trị đặt tay, chưa được chỉnh.
- **Từ điển Unihan và embedding:** chưa dùng. Mốc hiện chỉ gồm can chi và 1.057 cặp tên riêng thu từ chính bản Việt.
- **Mã lỗi chữ:** `resources/char_fix.tsv` còn trống (HCB_11 có 6 mã như `[BD77]`, `<曷毛>`).
