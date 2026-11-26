# Báo cáo phiên 7 – Điều chỉnh theo nhận xét của giảng viên; chuẩn bị kiểm tra toàn bộ

**Ngày:** 2026-11-26 · **hvalign:** 0.3.0 → 0.3.1

## A. Nhận xét của giảng viên về bản demo (18/11)

| Nhận xét | Đã làm |
|---|---|
| "Kết quả dóng hàng tốt, có ghi chú rõ ràng" | Giữ nguyên cách ghi chú. |
| "Cần xác nhận HCB_11 chỉ mới thực hiện 1 phần" | Bản demo chỉ trích 49 cặp đầu. Bản đầy đủ dóng toàn bộ Hậu Hán thư quyển 86, đúng phạm vi được giao: **512 cặp, độ phủ 100% chữ Hán và 100% âm tiết Việt**. Mọi `bao_cao.md` có thêm dòng phạm vi được giao, số quyển đã dóng và độ phủ, để giảng viên thấy ngay. |
| "Output cuối cùng nên có 03_text_sach (text Hán và Việt đã trích xuất, làm sạch)" | Mỗi thư mục nộp và gói `.zip` đều có `03_text_sach/han.txt` và `viet.txt`. Đã xóa 56 tệp text cũ do chương trình riêng của Tài đặt vào `03_text_sach` của HCB_01, 02, 12, 14. Các tệp này làm từ nguồn cũ (có những quyển đã thay vì sai bài), nên không khớp với dóng hàng. |
| "Nguồn không phải ảnh/PDF scan thì không cần folder 02" | Bỏ `02_ocr_tho` khỏi 14 thư mục nộp và khỏi gói `.zip`. Text thô chuyển vào `work/<MA>/02_ocr_tho` (không nộp). `bao_cao.md` ghi rõ lý do. |
| "Có thể bổ sung folder 01 (dữ liệu đã tải/crawl)" | Giữ `01_nguon`. Tệp `.pdf` trong đó là bản in trang nguồn để đối chiếu. |

Câu trả lời gợi ý cho giảng viên về HCB_11: *"Bản demo em chỉ trích 49 cặp đầu cho gọn. Bản nộp chính thức đã dóng toàn bộ quyển 86 (512 cặp, phủ 100% văn bản hai bên). Phần dịch rút gọn được ghi ở cột Ghi chú."*

## B. Thay đổi chương trình (0.3.1)

- **`config.py`:** thêm `Project.raw_dir(work)` = `work/<MA>/02_ocr_tho`.
- **`extract.py`:**
  - Bước 4 ghi text thô vào `raw_dir`.
  - Tự dọn `CV02_<MA>/02_ocr_tho` cũ. Chỉ xóa tệp do hvalign sinh ra; tệp người tự đặt vào thì giữ.
  - Thêm `harvest_sources()`.
- **`anchors.py`:** mốc tên riêng lấy thẳng từ bản Việt trong `01_nguon` của mọi tác phẩm, có cache theo chữ ký tệp. Bộ tên trùng khít bộ cũ (3.786 cặp), nên kết quả dóng không đổi, và mọi máy vẫn ra cùng kết quả.
- **`clean.py`, `__main__.py`:** đọc text thô từ `raw_dir`.
- **`app.py`, `index.html`:** gói `.zip` gồm `01_nguon`, `03_text_sach`, `04_dong_hang`, `bao_cao.md`.
- **`report.py`:** thêm phạm vi được giao, số quyển đã dóng, độ phủ (chữ Hán / âm tiết Việt), và ghi chú cấu trúc thư mục nộp.
- **`xlsxlite.py`:** `.xlsx` ghi với thời điểm cố định, nên cùng dữ liệu thì giống hệt từng byte. Trước đây mỗi lần chạy, git đều báo 14 tệp `.xlsx` bị đổi.
- **`tests/`:** thêm 2 kiểm thử (cấu trúc nộp, mốc lấy từ 01_nguon, `.xlsx` ổn định). 20/20 đạt.
- **Tài liệu:** đã cập nhật README, `huong_dan_hvalign.md` (mục 4.1, 7, 9) và thêm `CLAUDE.md`.

## C. Kiểm chứng

- 14 TSV và 28 tệp `03_text_sach` giống hệt trước khi sửa. Dấu vân tay TSV vẫn là `c42c5baf7219ce35`.
- Hai lần chạy liên tiếp: 70/70 tệp nộp giống hệt, kể cả `.xlsx` và `bao_cao.md`.
- Bản sao sạch từ git, còn `02_ocr_tho` cũ như máy chưa cập nhật: chạy xong tự dọn 14 thư mục `02_ocr_tho`, và 70/70 tệp nộp giống hệt repo.
- Số cặp không đổi: Kiên 3.483, Huy 3.265, Đăng 2.640, Tài 2.114. Kiểm định 14/14 ĐẠT.

## D. Kiểm tra toàn bộ – Đợt 1 (HCB_04, 05, 07, 11, 13 – phần của Kiên): XONG

Đã đọc **mọi cặp** của 5 tác phẩm (khoảng 1.400 cặp), đối chiếu Hán ↔ Việt. Chi tiết từng tác phẩm ở `Docs/kiem_tra_toan_bo/HCB_xx.md`.

| Tác phẩm | Tài liệu, nguồn, text | Cặp trước → sau | Lỗi tìm thấy | Cách sửa |
|---|---|---|---|---|
| HCB_04 | Đủ, SHA khớp, trọn bài | 68 → 68 | 0 | – |
| HCB_05 | Đủ, SHA khớp | 70 → 68 | 2 chỗ lệch ranh giới (59–60; 8–9 sau khi đổi Bước 6) | gộp |
| HCB_07 | Đủ, SHA khớp | 411 → 411 | 1 (386–387, "Toại đến, Tả tướng quân nói:") | sửa tận gốc ở Bước 6 |
| HCB_11 | Đủ, SHA khớp; bản Việt rút gọn | 512 → 499 | 5 chỗ lệch ranh giới ở lời tâu dài (Lý Cố, Trình Bao, Chu Phủ) | gộp, kèm ghi chú phần bị lược |
| HCB_13 | Đủ, SHA khớp | 340 → 338 | 1 (22–24, chiếu phong Bộ Lĩnh) | gộp, kèm ghi chú |

**Sửa tận gốc (hvalign 0.3.2):** bên Việt không còn tách câu sau dấu ':'.
- Bên Hán 曰：「…」 vốn là một câu. Bên Việt mà tách "X nói:" ra thì phần này hay bị ghép nhầm vào câu đứng trước.
- Đã so từng khối thay đổi trên cả 14 tác phẩm. Sửa đúng khoảng 90 chỗ ở HCB_01, cùng HCB_07 #386, HCB_11 (4 chỗ), HCB_13 (2 chỗ).
- Riêng HCB_14 (sillok), cách mới làm lệch nhiều hơn, nên giữ cách cũ (`viet_tach_sau_hai_cham: true` trong `config/works/HCB_14.yaml`). HCB_14 vẫn giữ nguyên 868 cặp như trước.
- Đã thêm kiểm thử `test_split_viet_speaker_and_quote_together`.
- Các quyết định hiệu đính bị đổi mã câu (HCB_02 của Tài, HCB_11) đã được ghi lại theo mã mới, mã cũ rút bằng `xoa`.

**Kiểm chứng:**
- Bản sao sạch từ git, áp code, cấu hình và hiệu đính mới, chạy từ đầu: **56/56 tệp nộp giống hệt repo**.
- `khong_khop = 0` ở mọi tác phẩm; 14/14 kiểm định ĐẠT; kiểm thử 21/21 đạt.
- Dấu vân tay TSV mới: `5cc1173362968165`.

**Số cặp sau đợt 1:** Kiên 3.463, Huy 3.256, Đăng 2.637, Tài 2.115 (ai cũng ≥ 2.000).

**Ảnh hưởng tới các đợt sau:** thay đổi ở Bước 6 đã làm đổi một số cặp của HCB_01 (97 khối), HCB_06 (5), HCB_08 (6), HCB_03, HCB_09, HCB_12. Các cặp này sẽ được đọc lại khi tới đợt của từng tác phẩm.

**Công cụ:** `Docs/kiem_tra_toan_bo/cong_cu/` gồm `dump.py` (in cặp theo khúc) và `hd.py` (ghi quyết định hiệu đính theo số cặp).

## E. Kiểm tra toàn bộ – Đợt 2 (HCB_03, 06, 08, 09 – phần của Huy): XONG

Đã đọc **mọi cặp** của 4 tác phẩm (1.143 cặp sau khi sửa). Chi tiết ở `Docs/kiem_tra_toan_bo/HCB_xx.md`.

| Tác phẩm | Cặp trước → sau | Lỗi chính | Cách sửa |
|---|---|---|---|
| HCB_03 | 8 → 59 | Bản Hán (Tứ khố) không có dấu câu; 2 mã chữ `SKchar` chưa tra; giới hạn tầng 2 | Chấm câu thủ công (R13 mới), tra mã chữ qua API zh.wikisource (𫝊, 𤋮), `tang2_max: 20`, `loai_tru` dòng tên sách; 2 ghi chú `dung` về chỗ dịch giả hiểu sai |
| HCB_06 | 360 → 454 | **Bản Việt tải thiếu** toàn bộ phần dịch 禹貢 trong `{{quote}}`; 10 mục Đất Tần → Đất Vệ chưa dịch; template `quote` chưa được đọc | Tải lại wikitext, `quote` → giữ nội dung, `loai_tru` 10 mục và 1 dòng lặp của nguồn |
| HCB_08 | 411 → 481 | **Bản Việt tải thiếu** các khối `<div>`, `<poem>` (đoạn Trưng Trắc, trống đồng, thư gửi Dương Quảng); markup `-{徵}-` còn trong text; hai bản chia đoạn khác nhau | Tải lại wikitext, xử lý `-{…}-`, tùy chọn `tang2_doan: false`, 2 cặp tên mốc trong `resources/han_viet_extra.tsv`, `loai_tru` lời giải thích của dịch giả, 3 `gop` |
| HCB_09 | 132 → 159 | **Bản Việt tải thiếu** khối `<div>` (Nhâm Diên ở Cửu Chân, Tích Quang); bài Tán kèm lời giải thích của dịch giả | Tải lại wikitext, `loai_tru` phần giải thích |

**Nguồn:** 3 tệp Việt (HCB_06, 08, 09) là bản Huy chép từ trang hiển thị, nên mất các khối đặc biệt. Đã thay bằng wikitext tải qua API (giữ tên tệp) và cập nhật `Docs/nguon_manifest_Huy.tsv`: URL đúng, revid, SHA-256, ngày tải 26/11. Bản Hán của 4 tác phẩm trùng với trang hiện tại. Bản Việt HCB_03 đủ nội dung. Các tác phẩm đợt 1 đều là `.wikitext` tải qua API, nên không bị lỗi này.

**Thay đổi chương trình (hvalign 0.3.3):**
- `clean.py`: luật **R13 chấm câu thủ công** (`cham_cau_thu_cong`). Chỉ thay khi bỏ dấu đi thì giống hệt từng chữ; lệch thì không dùng và ghi cảnh báo.
- `readers.py`: markup chuyển đổi phồn/giản `-{…}-` → chữ phồn thể (sửa luôn 3 chỗ `-{后}-` ở HCB_01, ranh giới cặp không đổi); template `quote` giữ nội dung.
- `align.py`: tùy chọn `dong_hang.tang2_doan: false` (dóng câu trên cả mục, bỏ ghép đoạn). Mặc định không đổi.
- `resources/han_viet_extra.tsv` (mốc tên thêm tay), `resources/cham_cau/HCB_03_q130.txt`, 2 dòng trong `char_fix.tsv`.
- 2 kiểm thử mới (R13; `-{…}-` và `quote`): 23/23 đạt. Hướng dẫn thêm mục 5I–5K.

**Kiểm chứng:**
- Bản sao sạch từ git (bcaf883), chép đè 24 tệp nguồn, cấu hình và code, chạy từ đầu: **70/70 tệp nộp giống hệt repo** (TSV, xlsx, `03_text_sach`, `bao_cao.md`).
- 14/14 kiểm định ĐẠT, `khong_khop = 0` ở mọi tác phẩm. Manifest của Huy khớp SHA 30/30.
- Dấu vân tay TSV mới: `5983599663f5422a`.
- TSV của 9 tác phẩm còn lại giống hệt trước, trừ HCB_01 (2 cặp có `-{后}-`).
- `bao_cao.md` của HCB_01, 04, 11, 13 chỉ đổi số cặp gắn cờ `lech_moc`, vì bộ mốc tên dùng chung đã có thêm tên từ các bản Việt mới tải.

**Số cặp sau đợt 2:** Kiên 3.463, **Huy 3.498** (+242), Đăng 2.637, Tài 2.115.

## F. Kiểm tra toàn bộ – Đợt 3 (HCB_02, 12 – Tài; HCB_10 – Đăng): XONG

Đã đọc **mọi cặp** của 3 tác phẩm (236 cặp sau khi sửa). Chi tiết ở `Docs/kiem_tra_toan_bo/HCB_xx.md`.

| Tác phẩm | Cặp trước → sau | Lỗi / điểm chính | Cách sửa |
|---|---|---|---|
| HCB_02 | 27 → 49 | Nguồn Hán nối cả chiếu văn bằng ，/；: một câu Hán ~500 chữ ghép với 15 câu Việt (2-15), thêm 4 cặp 1-2/1-3, 2 quyết định `gop` | Chấm câu thủ công R13 `resources/cham_cau/HCB_02.txt`: chỉ đổi 20 dấu ，/； ở chỗ bản Việt hết câu, chữ giữ nguyên. Kết quả 49 cặp đều 1-1. Bỏ `hieu_dinh/HCB_02__Tai.tsv` (2 `gop` cũ không còn cần) |
| HCB_10 | 38 → 38 | Đúng hết. **Bản Hán là giản thể** (trang zh.wikisource gắn `{{zth}}` = cần chuyển phồn thể); không có bản phồn thể dùng được | Giữ nguyên, ghi hạn chế vào `HCB_10.md`; không chuyển phồn thể bằng máy |
| HCB_12 | 149 → 149 | Đúng hết. Trang Hán 史記/卷113 vừa bị đổi tên (24/11) thành 史記 (維基文庫點校本)/卷113, nội dung không đổi | Không cần sửa |

**Nguồn:** cả 6 tệp .wikitext giống hệt bản hiện hành tải qua API, không có tệp chép tay nên không bị lỗi mất khối như đợt 2. Cả 3 tác phẩm **chưa có trong manifest**: đã thêm 8 dòng (wikitext + pdf) vào `Docs/nguon_manifest_Tai.tsv` và tạo `Docs/nguon_manifest_Dang.tsv` (2 dòng), có revid, SHA-256; ngày tải lấy theo ngày commit nguồn (24/11 Tài, 26/11 Đăng). Nhờ vậy bảng nguồn trong `bao_cao.md` của 3 tác phẩm có URL và revid thay cho "(không có trong manifest)".

**Chương trình:** không đổi code (vẫn 0.3.3).

**Kiểm chứng:**
- Bản sao sạch từ git (587a97a), chép đè 4 tệp (cấu hình, chấm câu, 2 manifest) và bỏ tệp hiệu đính HCB_02, chạy từ đầu: **70/70 tệp nộp giống hệt repo**.
- 14/14 kiểm định ĐẠT, `khong_khop = 0` ở mọi tác phẩm, kiểm thử 23/23. Manifest Tài + Đăng khớp SHA 58/58.
- Dấu vân tay TSV mới: `a16d2e1e586709fe`. TSV của 13 tác phẩm còn lại giống hệt trước; chỉ HCB_02 đổi.

**Số cặp sau đợt 3:** Kiên 3.463, Huy 3.498, Đăng 2.637, **Tài 2.137** (+22).
