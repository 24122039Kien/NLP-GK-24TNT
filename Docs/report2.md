# Report 2 – Dựng khung chương trình `hvalign` (Bước 4 → 7)

**Ngày:** 2026-11-10
**Yêu cầu:**
- Chương trình nhận cả `.txt` lẫn `.wikitext` và tự chuẩn hóa về một dạng.
- Dựng trước pipeline hệ thống.

**Sản phẩm:**
- Package `Lab/GK/hvalign/` và cấu hình `Lab/GK/config/`.
- Hướng dẫn sử dụng: [huong_dan_hvalign.md](huong_dan_hvalign.md).

## Kết quả

- **Một lệnh chạy cả pipeline:** `python -m hvalign run` chạy lần lượt trích text → làm sạch → tách câu → dóng 3 tầng → xuất TSV/XLSX → kiểm định → báo cáo. Cả 7 tác phẩm phần của bạn chạy hết trong 12 giây.
- **Nhận mọi định dạng nguồn đang có trong nhóm:**
  - Định dạng được nhận theo **nội dung**: `.txt` có markup wiki được đọc như wikitext, `.txt` không có markup là text thuần, `.html` sillok có bộ đọc riêng.
  - Ngôn ngữ và số quyển được nhận từ tên tệp, chấp nhận cả kiểu `續資治通鑑_卷002.wikitext` lẫn kiểu `TTTTG_q03_han.txt` của Huy.
  - Mọi định dạng đều được chuyển về cùng một khuôn trong `02_ocr_tho/`.
- **Đã kiểm chứng việc chuẩn hóa:**
  - Chép Q2 thành `TTTTG_q02_han.txt` / `_viet.txt` thì kết quả **giống hệt** khi đọc từ `.wikitext` (184/184 và 188/188 khối).
  - Bản text thuần của Q6 (bản Việt) lưu kèm BOM và CRLF như Notepad cũng ra đúng 157/157 đoạn.
- **Kết quả trên phần của Kiên:** 3.490 cặp tự động, **chưa hiệu đính**.

| Tác phẩm | han.txt | viet.txt | Cặp | Câu không ghép |
|---|---|---|---|---|
| HCB_01 (5 quyển) | 676 | 747 | 1.961 | 0 |
| HCB_04 | 8 | 9 | 68 | 0 |
| HCB_05 | 72 | 74 | 70 | 0 |
| HCB_07 | 44 | 46 | 411 | 0 |
| HCB_11 | 59 | 60 | 516 | 0 |
| HCB_13 | 25 | 105 | 340 | 0 |
| HCB_14 (4 quyển) | 9 | 34 | 124 | 2 |

- **Chất lượng (đọc tay, chưa phải đo chính thức):**
  - 15/15 cặp lấy ngẫu nhiên ở HCB_01, 07, 11, 13 đúng nghĩa.
  - Các cặp sai tập trung ở những cặp có chi phí cao. Sổ hiệu đính đã xếp những cặp này lên đầu.
- **Kiểm định:** cả 7 tác phẩm đạt kiểm định TSV/XLSX. Excel mở được tệp xuất, với sheet `DONG_HANG` và hàng tiêu đề `Hán | Việt`. 13/13 kiểm thử tự động đạt.
- **Số đếm khớp với Check_Kien.md:** luật bỏ năm dương lịch áp dụng 20 / 76 / 71 / 1 lần ở HCB_07 / 11 / 13 / 14 (Check ghi 20 / 75 / 71 / 1). Bên Hán HCB_05 loại 17 ghi chú 按, đúng số đã đếm.

## Cách chương trình xử lý một số trường hợp

| Trường hợp | Cách xử lý |
|---|---|
| Template lồng nhau `{{*\|…{{參\|元\|玄}}…}}` | Tách bằng cách đếm cặp ngoặc. Chú thích được giữ tại chỗ dạng `⟪*:…⟫` để Bước 5 quyết định |
| Bài sillok bị ngắt ở chỗ nâng chữ (抬頭) | Nối lại khi đoạn trước chưa có dấu kết câu (9 lần) |
| HCB_05: dòng `:` bên Việt có khi là chính văn | Bên Hán: loại dòng `:` trong 卷一, 卷二. Bên Việt: chỉ loại dòng bắt đầu bằng `Theo` / `Chú:` (15 dòng). Hai ghi chú Hán còn lại không có bản dịch |
| HCB_13: mục 大理 và 校勘記 | Loại trừ theo cấu hình, có ghi lý do |
| HCB_14: một câu Việt ứng với 4–10 vế Hán | Dấu 。 của sillok là ranh giới mềm; cho phép ghép đến `10–1` |
| Lời dẫn 「…」, câu kết thúc bằng "Dụ rằng:" | Ranh giới mềm, nên được gộp mà không bị phạt |

## Điểm cần xử lý

| Vấn đề | Đề xuất |
|---|---|
| HCB_11 có 6 mã lỗi chữ (`[BD77]`, `[B258]`, `[E8E6]`, `[CF3D]`, `<曷毛>`, `<名頁>`), làm 4 cặp còn chữ Latin ở vế Hán | Tra chữ đúng rồi điền vào `resources/char_fix.tsv` |
| HCB_13 còn 3 cặp có chữ Hán ở vế Việt (ví dụ `犭朋`, `推誠順化功臣`) | Xem ở `work/HCB_13/canh_bao.tsv` và sửa khi hiệu đính |
| HCB_01:00331: bản Việt có một đoạn giải thích dài trong ngoặc mà bản Hán không có (lỗi `ADDITION`) | Xóa khi hiệu đính. Cả 7 tác phẩm chỉ có 2 chỗ như vậy nên không viết luật riêng |
| Số cặp hiện tại là số trước hiệu đính | Mỗi người phải hiệu đính phần mình rồi kiểm tra chéo (§8) trước khi tính chính thức |

## Việc bạn cần làm

1. Đọc [huong_dan_hvalign.md](huong_dan_hvalign.md) rồi chia sẻ cho nhóm. Mỗi người thêm dòng của mình vào `config/phan_cong.tsv`, chép nguồn vào `CV02_<MA>/01_nguon/` và chạy `python -m hvalign inventory`.
2. Mở `work/<MA>/bao_cao.md` và một sổ hiệu đính trong `work/<MA>/hieu_dinh/` để xem thử.
3. Các quyết định ở mục 11 của kế hoạch vẫn chưa chốt. Chương trình đang chạy theo **đề xuất mặc định**, đổi được trong cấu hình:
   - xóa chú thích ở cả hai bản;
   - xóa ghi chú 按 của HCB_05;
   - HCB_05 tính cả tác phẩm.

## Cách làm và giới hạn

- **Dóng hàng:** chi phí độ dài Gale–Church cộng mốc can chi và tên riêng.
  - Tên riêng gồm 1.057 cặp `tên Việt (chữ Hán)` thu được ngay trong bản Việt.
  - Phương sai Gale–Church được ước lượng tự động từ các cặp đoạn 1–1.
  - Các trọng số khác **đang đặt tay**, chưa được chỉnh trên bộ mẫu chuẩn (kế hoạch mục 6.4).
- **Không cài thêm thư viện:** tệp `.xlsx` do chương trình tự ghi bằng thư viện chuẩn. Mọi ô ở sheet `DONG_HANG` là chuỗi, không có công thức hay ô gộp.
- **Chưa làm:**
  - áp bản sửa từ sổ hiệu đính;
  - bộ mẫu chuẩn và đánh giá A/B/C;
  - từ điển Unihan và embedding;
  - tải lại nguồn HCB_14 của Tài.
- **Chưa thử trên dữ liệu thật của 3 bạn kia** vì máy này chưa có nguồn của họ. Riêng kiểu tên tệp của Huy đã được thử bằng bản giả lập.

## Tệp đã thay đổi trong phiên

- **Tạo mới** (trong `Lab/GK/`):
  - mã nguồn `hvalign/` (15 tệp);
  - cấu hình: `config/project.yaml`, `config/phan_cong.tsv`, `config/works/HCB_01…14.yaml` (7 tệp), `resources/char_fix.tsv`;
  - kiểm thử `tests/test_pipeline.py`;
  - `requirements.txt`, `setup.cfg`, `.gitignore`;
  - tài liệu `Docs/huong_dan_hvalign.md`, `Docs/report2.md`.
- **Sinh ra khi chạy:**
  - `CV02_*/02_ocr_tho/{han,viet}/*.tsv`;
  - `CV02_*/03_text_sach/han.txt`, `viet.txt` (trước đây là tệp 0 byte);
  - toàn bộ thư mục `work/` (tệp trung gian, không nộp).
- **Sửa:** `Docs/implementation_plan.md` (mục 0 thêm tiến độ, mục 3.1 và 3.3 cập nhật theo cách làm thực tế).
- **Không đụng tới:** `01_nguon/` (đã kiểm tra: không tệp nào thay đổi) và `04_dong_hang/` (vẫn là tệp mẫu ban đầu).

## Bước tiếp theo

1. Dựng bộ mẫu chuẩn khoảng 120 câu cho phần của Kiên để đo độ chính xác và chỉnh trọng số.
2. Viết lệnh áp bản sửa từ sổ hiệu đính (`review apply`).
3. Khi các bạn chép nguồn vào, chạy `inventory` để soát trùng bài (Q1381 / Q1384) và các nguồn HCB_14 bị sai.
