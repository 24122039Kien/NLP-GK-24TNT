# NLP-GK-24TNT – Dóng hàng Hán–Việt (CV02)

Đồ án giữa kỳ môn Nhập môn NLP, nhóm 4 người (Kiên, Huy, Tài, Đăng).

- `CV02_HCB_xx/` – thư mục bàn giao theo Guideline (`01_nguon`, `02_ocr_tho`, `03_text_sach`, `04_dong_hang`)
- `hvalign/` – chương trình dóng hàng chung (Bước 4 → 7)
- `config/` – phân công và cấu hình từng tác phẩm
- `Docs/` – Guideline, kế hoạch, hướng dẫn, phân việc, báo cáo

## Bắt đầu

```
pip install -r requirements.txt
python -m pytest -q
python -m hvalign run
```

Đọc tiếp: [Docs/huong_dan_hvalign.md](Docs/huong_dan_hvalign.md) (cách dùng) và
[Docs/phan_viec_hvalign.md](Docs/phan_viec_hvalign.md) (việc của từng người).
