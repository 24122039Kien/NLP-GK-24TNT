# NLP-GK-24TNT – Dóng hàng Hán–Việt (CV02)

Đồ án giữa kỳ môn Nhập môn NLP, nhóm 4 người (Kiên, Huy, Tài, Đăng).

- `CV02_HCB_xx/` – thư mục bàn giao (`01_nguon`, `03_text_sach`, `04_dong_hang`, `bao_cao.md`). Không có `02_ocr_tho`: nguồn là text số, không phải ảnh/PDF scan (nhận xét của giảng viên 18/11); text thô trung gian nằm ở `work/<MA>/02_ocr_tho`, không nộp
- `hvalign/` – chương trình dóng hàng chung (Bước 4 → 7)
- `config/` – phân công và cấu hình từng tác phẩm
- `hieu_dinh/` – quyết định hiệu đính và kết quả chấm mẫu do app ghi (cần commit)
- `Docs/` – Guideline, kế hoạch, hướng dẫn, phân việc, báo cáo

## Bắt đầu

```
pip install -r requirements.txt
python -m pytest -q
python -m hvalign app        # giao diện web: Làm tự động → Nhìn qua → Tải về (.zip); Windows: nhấp đúp Mo_hvalign.bat
```

Dòng lệnh vẫn dùng được: `python -m hvalign run`, `python -m hvalign status`.

Đọc tiếp: [Docs/huong_dan_hvalign.md](Docs/huong_dan_hvalign.md) (cách dùng) và
[Docs/phan_viec_hvalign.md](Docs/phan_viec_hvalign.md) (việc của từng người).
