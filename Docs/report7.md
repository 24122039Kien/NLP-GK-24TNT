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
| HCB_12 | 149 → 149 | Trang Hán 史記/卷113 vừa bị đổi tên (24/11) thành 史記 (維基文庫點校本)/卷113, nội dung không đổi. 3 cặp thiếu nhãn ở một vế vì máy bỏ tiêu đề (南越王; 太史公曰; 索隱述贊) | 3 `sua` trong `hieu_dinh/HCB_12__Tai.tsv` |

**Nguồn:** cả 6 tệp .wikitext giống hệt bản hiện hành tải qua API, không có tệp chép tay nên không bị lỗi mất khối như đợt 2. Cả 3 tác phẩm **chưa có trong manifest**: đã thêm 8 dòng (wikitext + pdf) vào `Docs/nguon_manifest_Tai.tsv` và tạo `Docs/nguon_manifest_Dang.tsv` (2 dòng), có revid, SHA-256; ngày tải lấy theo ngày commit nguồn (24/11 Tài, 26/11 Đăng). Nhờ vậy bảng nguồn trong `bao_cao.md` của 3 tác phẩm có URL và revid thay cho "(không có trong manifest)".

**Chương trình:** không đổi code (vẫn 0.3.3).

**Quy tắc mới từ người dùng (26/11):** chỗ nào hvalign không tự dóng chuẩn thì sửa tay cho chính xác (hiệu đính `gop`/`sua`/`sai`), coi là phần human in the loop, không chỉ ghi chú. Đã rà lại đợt 1–3: chỉ còn 3 cặp HCB_12 ở trên cần sửa.

**Kiểm chứng:**
- Bản sao sạch từ git (587a97a), chép đè 5 tệp (cấu hình, chấm câu, 2 manifest, hiệu đính HCB_12) và bỏ tệp hiệu đính HCB_02, chạy từ đầu: **70/70 tệp nộp giống hệt repo**.
- 14/14 kiểm định ĐẠT, `khong_khop = 0` ở mọi tác phẩm, kiểm thử 23/23. Manifest Tài + Đăng khớp SHA 58/58.
- Dấu vân tay TSV mới: `5abc170b74b6ee51`. TSV của 12 tác phẩm còn lại giống hệt trước; chỉ HCB_02 và 3 cặp HCB_12 đổi.

**Số cặp sau đợt 3:** Kiên 3.463, Huy 3.498, Đăng 2.637, **Tài 2.137** (+22).

## G. Kiểm tra toàn bộ – Đợt 4 (HCB_14 – 26 quyển của cả 4 người): XONG

Đã đọc **mọi cặp** (912 cặp sau khi sửa). Chi tiết ở `Docs/kiem_tra_toan_bo/HCB_14.md`.

**Lỗi hệ thống tìm thấy và đã sửa:**
- **Bản Hán `.txt` của Huy** (6 quyển) là bản chép tay, bị ngắt đoạn ở mỗi chữ tôn kính nâng đầu dòng. Đã thay bằng 15 bài sillok HTML gốc; chữ trùng khớp.
- **Thiếu 4 bài sillok** mà bản Việt có dịch: Q1358 có thơ ngự chế và dụ tông thất; Q1360 có tế cáo và yến cung Trùng Hoa. Đã tải bổ sung.
- **Chữ ngoài BMP bị hỏng thành `��`** (𠇶, 𥙔): sillok mã hóa bằng cặp thực thể surrogate. Đã sửa trong **hvalign 0.3.4** (`readers._unescape`), có kiểm thử, 24/24 kiểm thử đạt.
- **Thơ ngự chế:** trang Việt chép cả chữ Hán và phiên âm. Đã dùng `loai_tru`, chỉ giữ phần dịch, nên mỗi câu thơ Hán giờ ứng với đúng 1 câu dịch.
- **Q1346:** chiếu ân xá 22 điều có 1 đoạn Hán ứng với 24 đoạn Việt. Đã đặt `tang2_max: 30`.
- **Manifest:** bổ sung bản Việt của Tài, toàn bộ nguồn HCB_14 của Đăng, revid và URL từng bài sillok của Huy. 141/141 tệp khớp SHA.

**Sửa tay (human in the loop):**
- Sillok dùng 。 cả ở chỗ ngắt nhỏ, nên máy trượt 1 vế ở hầu hết các quyển. Mọi quyển đã được chia lại ranh giới bằng công cụ mới `cong_cu/chia_lai.py`. Công cụ bắt buộc chữ Hán và chữ Việt của khúc giữ nguyên tuyệt đối.
- Tổng cộng 544 `sua` và 22 `sai`; `sai` là các cặp số thứ tự "1.", "2."… của Q1346, đã ghép vào nội dung từng điều.
- Đưa 3 câu bị bỏ rơi vào cặp, bỏ 2 cụm chữ Hán sót ở vế Việt, ghi chú 2 lỗi dịch.
- Chỗ lệch đã biết ở Q1421 và Q1445 (「批、所見是。」 ↔ "Lại tâu:") đã hết.

**Kiểm chứng:**
- Chạy từ đầu trên bản sao sạch (32db2ae, chép đè code, cấu hình, nguồn, manifest và tệp hiệu đính): **70/70 tệp nộp giống hệt repo**.
- 14/14 kiểm định ĐẠT, `khong_khop = 0` ở mọi tác phẩm. Dấu vân tay TSV: `904a47c9d0bec7a3`.
- TSV của 13 tác phẩm khác giữ nguyên; `.xlsx` và `bao_cao.md` của các tác phẩm này chỉ đổi số phiên bản 0.3.3 → 0.3.4.

**Số cặp sau đợt 4:** Kiên 3.463 (HCB_14: 124), Huy 3.504 (225), **Tài 2.149** (279), **Đăng 2.663** (284).

## H. Kiểm tra toàn bộ – Đợt 5 (HCB_01 quyển 1–10 – cả 4 người): XONG

Đã đọc **mọi cặp** của quyển 1–10 (4.285 cặp, #1–#4285). Chi tiết ở `Docs/kiem_tra_toan_bo/HCB_01.md`.

**Nguồn và manifest:**
- Đã tải lại 20 trang qua API wikisource để đối chiếu. Mọi trang đều khớp bản hiện hành.
- Bổ sung manifest cho q1, q8 (Tài) và q4, q9 (Đăng); điền revid cho q3, 5, 7 (Huy). 30/30 tệp khớp SHA.

**Lỗi hệ thống đã sửa:**
- Bản Việt q1 có đoạn tiểu sử Thái Tổ dịch từ lời chú nhỏ mà bên Hán đã bỏ. Đã đặt `loai_tru` trong `config/works/HCB_01.yaml`.
- Trang zh/vi quyển 5 chép trùng một đoạn. Đã bỏ 2 cặp lặp, nên HCB_01 giảm từ 8.094 xuống **8.092 cặp**.

**Sửa tay (human in the loop):** 40 quyết định (37 `sua`, 2 `sai`, 1 `dung`).
- Chia lại ranh giới 9 khúc (`khuc/HCB_01/q1_a` … `q9_b`). Lớn nhất là q9 #3421–3425: tiêu đề 太宗…皇帝 trong nguồn zh đặt sau đoạn tiểu sử, làm máy trượt 1 vế.
- Bỏ phần ngoặc là bản dịch lời chú nhỏ `{{*|…}}` ở 6 cặp.
- Sửa lỗi chữ của nguồn zh:
  - chữ PUA (渾瑊, 踰);
  - chữ ghép bộ (扌晉 → 搢, 衤復 → 複, 钅句 → 鉤);
  - ký tự rác ở 3 cặp.
- Lỗi chữ có nghĩa (餘斌, ngày can chi sai thứ tự) và lỗi thiếu dấu của bản dịch được giữ nguyên.

**Kiểm chứng:**
- Chạy từ đầu trên bản sao sạch (3142d80 + toàn bộ thay đổi chưa commit), chạy 2 lần: **70/70 tệp nộp giống repo**, chỉ khác ô ngày.
- 14/14 kiểm định ĐẠT, `khong_khop = 0` ở mọi tác phẩm, 24/24 kiểm thử đạt. Dấu vân tay TSV: `3881da12c970ac7b`.
- TSV của 13 tác phẩm khác giữ nguyên. `.xlsx` và `bao_cao.md` của các tác phẩm này chỉ khác ngày xuất, nên giữ bản đã commit.

**Điểm mở (đã chốt, xem mục H1):** `.xlsx` có ô "Ngày xuất" (`hvalign/export.py`), đổi theo ngày chạy.

**Số cặp sau đợt 5:** Kiên 3.463 (HCB_01: 1.955), Huy **3.502** (2.124), Tài 2.149 (1.672), Đăng 2.663 (2.341).

### H1. Bỏ ô "Ngày xuất" trong `.xlsx` (hvalign 0.3.5, 27/11)

- **Lý do:** mẫu `example.xlsx` của giảng viên chỉ có một sheet với 2 cột, không có ô ngày. Guideline chỉ cho phép thêm sheet thống kê, không yêu cầu ghi ngày. Ô này làm `.xlsx` của cả 14 tác phẩm đổi mỗi khi chạy vào ngày khác, trái với yêu cầu "chạy lại phải ra đúng kết quả". Người dùng chốt bỏ.
- **Thay đổi:** bỏ dòng "Ngày xuất" ở sheet `THONG_KE` (`hvalign/export.py`). Sheet `DONG_HANG` và `TRUY_VET` không đổi. Ngày chạy vẫn ghi ở `bao_cao.md`. Thêm kiểm thử: `THONG_KE` không có ô ngày và xuất lại ra `.xlsx` giống hệt từng byte.
- **Kiểm chứng:**
  - 24/24 kiểm thử đạt; 14/14 kiểm định ĐẠT; dấu vân tay TSV vẫn `3881da12c970ac7b`.
  - So với bản đã commit: `DONG_HANG` và `TRUY_VET` của cả 14 tác phẩm giống hệt; `THONG_KE` chỉ mất dòng ngày và đổi dòng "Công cụ" sang 0.3.5.
  - Bản sao sạch: 70/70 tệp nộp giống repo, `.xlsx` giống từng byte.

## I. Kiểm tra toàn bộ – Đợt 6 (HCB_01 quyển 11–20 – cả 4 người): XONG

Đợt này còn chốt thêm một việc: **làm theo Guideline** (sheet `DONG_HANG`, tiêu đề `Hán`/`Việt`, TSV LF), không theo `example.xlsx` của giảng viên. Chương trình vốn đã làm như vậy nên không phải sửa code.

**Phạm vi:** 3.807 cặp (#4286–#8092), đã đọc hết 3.807/3.807 cặp. Tính cả đợt 5, đã đọc đủ 8.092/8.092 cặp HCB_01. Chi tiết từng quyển ở `Docs/kiem_tra_toan_bo/HCB_01.md`.

**Bước 1–3 (nguồn):**
- Tải lại 20 trang qua API wikisource (`GK_tam/dot6_live`). 16 tệp `.wikitext` giống hệt bản hiện hành. 4 tệp `.txt` của Huy (q11, q16) đủ chữ, không lệch chữ nào.
- Bổ sung manifest: Tài q17, q19 (+8 dòng); Đăng q12, 13, 14, 18 (+8 dòng); Huy điền revid q11, q16. 28/28 tệp nguồn của q11–20 có trong manifest, SHA khớp.

**Sửa tay (41 quyết định: 37 `sua`, 4 `dung`):**
- **Chia lại ranh giới, 8 khúc** (`khuc/HCB_01/q11_a`, `q14_a`, `q15_a`, `q16_a`, `q18_a`, `q19_a`, `q19_b`, `q20_a`). Lỗi đều cùng một dạng: một vế Việt ngắn ở ranh giới (như "Hoàng đế nổi giận…", "Sách Quân chí nói") bị máy dính sang cặp bên cạnh. Tệp khúc dựng bằng công cụ mới `cong_cu/mkkhuc.py`: chỉ cần nêu đoạn chữ mở đầu mỗi cặp mới, không chép tay chữ nào.
- **Chữ PUA của nguồn zh:** ghép lại 5 chữ (#5019 巇, #6179 棲, #6314 穡, #6998 楊礪, #7316 秕).
- **Chữ ghép bộ:** sửa 4 chữ (#5667 牸, #7157 và #7358 鄜, #7451 捲).
- **Rác do bộ chuyển phồn–giản:** 備位元 → 備位 (#5373); 乙太 → 以太 (#4855, #7657, và #3386 ở q9, đợt 5 đã bỏ sót). Đã quét cả 14 tác phẩm: chỉ HCB_01 có loại lỗi này.
- **Dấu và chữ thừa:** #4869, #5385, #6288, #6583, #7135.
- **Để nguyên, có ghi chú `dung`:** 4 chữ không xác định được chữ gốc (PUA #5723, #6109, #6625; 钅屈 #6686). Không đoán, để khỏi đưa chữ sai vào ngữ liệu.
- **Không phải sửa:** #7772. Tiêu đề đế hiệu 真宗… trong nguồn zh là dòng đề mục `== … ==` nên bị bỏ như mọi đề mục; bản Việt viết tên hiệu liền trong câu.

**Kiểm chứng:**
- 14/14 kiểm định ĐẠT, `khong_khop = 0`, 24/24 kiểm thử. Dấu vân tay TSV: `afb9a88ede60aa8b`.
- Chỉ HCB_01 đổi: 37 dòng TSV, đúng bằng 37 quyết định `sua`. 13 tác phẩm còn lại giống từng byte, kể cả `.xlsx`, vì từ 0.3.5 không còn ô ngày.
- Bản sao sạch, chạy 2 lần: 70/70 tệp nộp giống repo.

**Số cặp sau đợt 6 (không đổi):** Kiên 3.463, Huy 3.502, Tài 2.149, Đăng 2.663. HCB_01: 8.092 cặp, 81 quyết định hiệu đính.

**Kết thúc kiểm tra toàn bộ:** cả 6 đợt đã xong. Đã đọc mọi cặp của 14 tác phẩm.
