# Report 6 – App tối giản: Làm tự động → Nhìn qua → Tải về

**Ngày:** 2026-11-16

**Yêu cầu:**
- App cũ khó hiểu và còn nhiều việc tay. Sửa để nhóm phải phân tích ít nhất: chỉ cần nhìn qua rồi tải về.
- Điều chỉnh theo câu trả lời của giảng viên (ảnh trong `QA/`).
- Đối chiếu định dạng đầu ra với tệp mẫu `example.zip`.

**Sản phẩm:** `hvalign` 0.3.0.

## 1. Câu trả lời của giảng viên và cách chương trình làm theo

| Tác phẩm | Câu trả lời | Chương trình làm gì |
|---|---|---|
| Chung (HCB_02, 06, 09, 10, 12, 13) | Chỉ dóng hàng phần có song ngữ; phần nào không có bản dịch thì không cần dóng | Đã làm như vậy từ trước: vùng không có bản dịch nằm trong `loai_tru`, câu lẻ nằm trong `khong_ghep.tsv`, cả hai không vào TSV. Báo cáo tự sinh nay ghi rõ quy tắc này |
| HCB_11 Q86 | Bản rút gọn vẫn dóng được nếu xác định được nội dung tương ứng. Phải đánh dấu rõ câu bị lược bỏ hoặc dịch rút gọn, bằng một cột "Ghi chú" trong file `.xlsx`, nêu phần bị lược và câu không được dịch | Máy **tự viết ghi chú** (`hvalign/notes.py`). `config/works/HCB_11.yaml` có `cot_ghi_chu: true`, nên sheet `DONG_HANG` của HCB_11 có cột thứ ba `Ghi chú`. 32/516 cặp có ghi chú. TSV vẫn đúng 2 cột |
| HCB_14 | Được lấy bản Hán ở sillok.history.go.kr; chỉ làm phần có song ngữ | Đúng với cách đang làm. Lệnh tải sillok vẫn là việc của Tài |

Ví dụ ghi chú máy tự viết:

- `Dịch rút gọn: vế Việt chỉ dài khoảng 62% mức thường gặp; bản Việt không nhắc tới: 蠻夷 (Man Di)`
- `Vế Việt có chú thích của dịch giả: «(Liêu từ trước thời Thái Tổ đã có lễ tế núi. Nghi…»` (HCB_01)
- `Câu Việt ngay sau không có trong bản Hán, không đưa vào dữ liệu: «Lại dụ rằng:»` (HCB_14)

"Mức thường gặp" là tỷ lệ âm tiết Việt / chữ Hán đo trên chính tác phẩm đó. Ngưỡng: ngắn hơn 50% (trong đoạn đã biết là rút gọn: 70%), dài hơn 2 lần, hoặc có đoạn trong ngoặc dài từ 40 ký tự.

## 2. Đối chiếu với `example.zip`

`example.zip` có `example.tsv` (210 cặp, Sử ký – Ngũ đế bản kỷ) và `example.xlsx`.

| Điểm | `example` | `hvalign` | Kết luận |
|---|---|---|---|
| TSV: 2 cột, phân cách TAB, không dòng tiêu đề, UTF-8 không BOM | Đúng như vậy | Như vậy | Khớp |
| TSV: xuống dòng | CRLF (Windows), dòng cuối không có ký tự xuống dòng | LF | Guideline không quy định; LF là chuẩn của TSV nên giữ |
| TSV dòng 1 | Dùng **dấu cách thay cho TAB** | – | Lỗi trong tệp mẫu (Guideline cấm); chương trình kiểm định chặn lỗi này |
| XLSX: tên sheet | `Sheet1` | `DONG_HANG` | Theo Guideline mục 3 ("sheet tên DONG_HANG") |
| XLSX: tiêu đề | `han`, `vi` | `Hán`, `Việt` | Theo Guideline mục 3 ("tiêu đề `Hán` và `Việt`") |
| XLSX: định dạng tiêu đề | Đậm, nền xanh lá `#93C47D`, căn giữa | Nay giống hệt | Đã chỉnh cho giống mẫu |
| XLSX: nội dung trùng TSV, không gộp ô, không công thức | Đúng | Đúng, có kiểm định | Khớp |

Tệp mẫu lệch Guideline ở tên sheet và tiêu đề. Chương trình theo Guideline vì đó là văn bản quy định ("bắt buộc"). **Nên hỏi lại giảng viên một câu** cho chắc: "nộp sheet `DONG_HANG` với tiêu đề `Hán`/`Việt` như Guideline, đúng không ạ?". Nếu cô muốn theo mẫu thì chỉ cần sửa 2 hằng số trong `hvalign/export.py`.

## 3. App mới

**Trang chính** chỉ còn 3 bước:

1. **▶ Làm tự động tất cả.** Chạy hết Bước 4 → 7, xuất, kiểm định, báo cáo; 7 tác phẩm của Kiên mất khoảng 17 giây.
2. **Xem nhanh** (không bắt buộc). Tab *Cặp có ghi chú* chỉ có 39/3.490 cặp, phần lớn ở HCB_11. Nút **Bỏ** dùng cho cặp sai rõ ràng, có Hoàn tác và Lấy lại.
3. **⬇ Tải về** hoặc **⬇ Tải tất cả.** Máy tự cập nhật bản xuất và kiểm định, rồi tải `.zip`. Mỗi tác phẩm là một thư mục `CV02_<MA>/` gồm `01_nguon`, `02_ocr_tho`, `03_text_sach`, `04_dong_hang` (tsv + xlsx) và `bao_cao.md`, đúng Guideline mục 2.

Thẻ tác phẩm có nhãn trạng thái `✓ Sẵn sàng`, `Sẽ tự cập nhật` hoặc `Lỗi định dạng`. Thanh đầu trang ghi số cặp mỗi người so với 2.000.

**Công cụ nâng cao** (`/nang-cao`) là app cũ, giữ nguyên chức năng: hiệu đính từng cặp bằng phím, chấm mẫu §8, bàn giao vào `04_dong_hang` trong repo.

**Đã bỏ:**
- Sổ Excel `work/<MA>/hieu_dinh/*.xlsx`: sửa trong đó không được áp nên dễ gây nhầm.
- Yêu cầu bắt buộc phải hiệu đính và chấm mẫu trước khi nộp.

## 4. Kiểm tra đã làm

- **Kiểm thử tự động:** 18/18 đạt, thêm 2 kiểm thử:
  - ghi chú: rút gọn, dài, câu không được dịch;
  - cột `Ghi chú` trong DONG_HANG vẫn qua kiểm định, TSV vẫn 2 cột.
- **Thử trên bản sao trong scratchpad,** không ghi gì vào `hieu_dinh/` thật:
  - "Làm tự động tất cả": 7/7 ĐẠT;
  - "Tải tất cả": tệp `.zip` 15 MB, 7 thư mục đúng cấu trúc; số dòng TSV và XLSX khớp nhau và khớp từng ô;
  - Bỏ, Hoàn tác, Lấy lại; sau khi Bỏ, thẻ chuyển sang `Sẽ tự cập nhật`, tải về thì cập nhật xong mới tải;
  - chặn tải tác phẩm chưa sẵn sàng (409), mã tác phẩm lạ (400), Host lạ (403).
- **Giao diện trên Chrome:**
  - không có lỗi JavaScript;
  - bề rộng điện thoại 375px không tràn ngang.

## 5. Điều cần biết

- **Ghi chú tự động chỉ dựa vào độ dài và tên riêng**, không hiểu nghĩa câu. Trong vùng dịch rút gọn của HCB_11 có vài cặp lệch ranh giới, ví dụ `政不施焉，則君子不臣其人。` ↔ `Sứ giả nói:`. Những cặp này đều nằm trong tab *Cặp có ghi chú*. Nên lướt 32 cặp đó và bấm **Bỏ** cặp sai.
- **HCB_11 còn 4 mã chữ chưa tra** ở vế Hán: `[BD77]`, `[B258]`, `[E8E6]`, `[CF3D]`. Đây là việc R09 của Huy; giải theo Big5/GBK không ra chữ đúng.
- **`hieu_dinh/HCB_01__Kien.tsv`** (chưa commit) là các lần bấm thử hôm 14/11, đã hoàn tác hết, nên không ảnh hưởng kết quả. Có thể xóa.
- **Thư mục `example/`** (giải nén từ `example.zip`) và `QA/` chưa được thêm vào git.

## 6. Tệp đã thay đổi (chưa commit)

- **Mới:**
  - `hvalign/notes.py`;
  - `hvalign/app_static/index.html` (trang chính mới);
  - `Docs/report6.md`.
- **Đổi tên:** `app_static/index.html` thành `app_static/advanced.html` (thêm liên kết về trang chính).
- **Sửa:**
  - `hvalign/app.py`: trang chính, `/api/home`, `/api/pairs`, `/api/download`, chế độ "prepare";
  - `export.py`: cột `Ghi chú`, kiểm định chấp nhận cột này, bỏ sổ Excel cũ;
  - `report.py`: ghi chú, quy tắc phạm vi;
  - `review.py`: giữ cờ máy và ghi chú người sau khi áp quyết định;
  - `xlsxlite.py`: tiêu đề nền xanh như mẫu;
  - `__init__.py`: 0.3.0;
  - `config/project.yaml` và `config/works/HCB_11.yaml` (`cot_ghi_chu`);
  - `tests/test_pipeline.py`;
  - `README.md`, `Docs/huong_dan_hvalign.md` (mục 0, 1, 6, 7, 11), `Docs/phan_viec_hvalign.md`.
