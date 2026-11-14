# Kế hoạch thực hiện Bước 4 – 7

**Đề tài:** CV02, dóng hàng Hán–Việt. **Phạm vi:** cả nhóm 4 người (Kiên, Huy, Tài, Đăng), mã HCB_01–HCB_14.
**Căn cứ:** [Guideline.pdf](Guideline.pdf) và 4 file kiểm tra Bước 1–2 ([Check_Kien.md](Check_Kien.md), [Check_Huy_CV02.md](Check_Huy_CV02.md), [Check_Tai_CV02.md](Check_Tai_CV02.md), [check_dang.md](check_dang.md)).
**Ngày lập:** 2026-11-10.

---

## 0. Tóm tắt

**Đề xuất:** cả nhóm dùng **một chương trình chung** (tạm gọi `hvalign`) để chạy Bước 4 → 7 cho mọi tác phẩm. Chương trình làm phần lặp lại; con người quyết định phạm vi, dựng bộ mẫu chuẩn và hiệu đính các cặp chương trình chưa chắc chắn.

| Bước | Chương trình làm | Con người làm | Đầu ra |
|---|---|---|---|
| 4 – Trích text | Gom nguồn của 4 người, tải lại những nguồn sai hoặc thiếu, trích text từ wikitext/HTML | Duyệt bảng trạng thái nguồn | `02_ocr_tho/` (text thô có mã truy vết) |
| 5 – Làm sạch | Chạy bộ luật làm sạch; mỗi luật đều ghi log | Chốt các luật còn tranh cãi; xem mẫu trước/sau | `03_text_sach/han.txt`, `viet.txt` |
| 6 – Tách câu | Tách câu Hán và Việt, có đánh dấu ranh giới "cứng" và "mềm" | Kiểm tra mẫu ranh giới | tệp trung gian `segments.jsonl` |
| 7 – Dóng hàng | Dóng 3 tầng: mục → đoạn → câu; gắn điểm tin cậy cho từng cặp | Dựng bộ mẫu chuẩn; hiệu đính cặp điểm thấp; kiểm tra chất lượng theo §8 | `04_dong_hang/*.tsv`, `*.xlsx`, báo cáo |

**Ba điểm chính của thiết kế:**
1. **Dóng theo câu, không theo đoạn.** Dóng theo đoạn chỉ được khoảng 900 cặp mỗi người (số của Kiên), không đủ 2.000.
2. **Dùng âm Hán Việt làm cầu nối.** Tên riêng, niên hiệu, can chi trong bản Việt chính là âm Hán Việt của chữ Hán (ví dụ 福康安 → Phúc Khang An), nên chuyển chữ Hán sang âm Hán Việt rồi so với bản Việt cho ra tín hiệu dóng rất mạnh mà không cần mô hình lớn.
3. **Không ép ghép câu không có bản dịch.** Câu Hán không có bản dịch (bản Việt rút gọn hoặc dịch thiếu) được ghi vào danh sách loại trừ, không đưa vào TSV. Nhờ vậy tránh được lỗi `OMISSION` và `MISSING` theo §7 của Guideline.

**Cần nhóm chốt trước khi viết code:** xem mục 11.

**Tiến độ (2026-11-10):** đã có khung chương trình `hvalign` chạy đủ Bước 4 → 7 bằng một lệnh, đã chạy trên phần của Kiên (3.490 cặp tự động, chưa hiệu đính). Cách dùng: [huong_dan_hvalign.md](huong_dan_hvalign.md); chi tiết phiên: [report2.md](report2.md).

---

## 1. Hiện trạng và hệ quả cho thiết kế

### 1.1. Hiện trạng nguồn của cả nhóm

Tổng hợp từ 4 file kiểm tra:

| Mã | Người | Tình trạng | Việc phải làm ở Bước 4–5 |
|---|---|---|---|
| HCB_01 | Cả 4 người (quyển 1–20) | Khớp | Chuẩn hóa định dạng tệp (Huy đang lưu `.txt`) |
| HCB_02 | Tài | Bản Việt thừa phiên âm, dịch nghĩa và phụ lục | Cắt phạm vi: chỉ phần chiếu văn |
| HCB_03 | Huy | Bản Hán (四庫全書本) không có dấu câu; có `{{SKchar}}` | Bảng tra `SKchar`; chấm câu bản Hán (mục 5.3) |
| HCB_04 | Kiên | Khớp | — |
| HCB_05 | Kiên | Khớp; bản Hán không có dấu câu | Chờ chốt phạm vi; dóng theo khoản |
| HCB_06 | Huy | Bản Việt chỉ bằng khoảng nửa bản Hán (7.122 âm tiết / 14.455 chữ, r≈0,49) | **Kiểm tra lại phạm vi trước khi dóng** |
| HCB_07 | Kiên | Khớp | — |
| HCB_08 | Huy | Khớp | — |
| HCB_09 | Huy | Bản Việt chỉ dịch 3 nhân vật | Cắt phạm vi |
| HCB_10 | Đăng | Bản Việt chỉ có lời tựa, truyện Lý Thiện và lời tán | Cắt phạm vi |
| HCB_11 | Kiên | 6 đoạn dịch rút gọn | Đánh dấu đoạn rủi ro |
| HCB_12 | Tài | Bản Hán thiếu 三家注 mà bản Việt có dịch | Tìm bản Hán có chú, hoặc chỉ dùng chính văn |
| HCB_13 | Kiên | Bản Việt không có mục 大理 | Cắt phạm vi |
| HCB_14 | Cả 4 người | Trích đoạn theo bài sillok. Bản Hán của Tài cho Q1358, Q1410 sai bài, Q1360 thiếu 3 ngày. Q1384 của Đăng ghi tiêu đề là 1381, trùng số với Q1381 của Huy | **Tải lại bản Hán từ sillok; kiểm tra trùng bài giữa các thành viên** |

### 1.2. Hệ quả cho thiết kế

1. **Một tác phẩm có nhiều người làm.** HCB_01 (20 quyển) và HCB_14 được chia cho cả 4 người, nhưng sản phẩm nộp là **một thư mục cho mỗi tác phẩm** (`CV02_HCB_01/`). Vì vậy chương trình phải gộp dữ liệu theo tác phẩm, đồng thời vẫn đếm được số cặp của từng người để chứng minh mỗi người đạt 2.000 cặp. Thông tin này nằm trong tệp phân công (mục 2.4).
2. **Không cần OCR.** Mọi nguồn đều đã có text (wikitext hoặc HTML). Bước 4 là trích xuất và crawl, không phải OCR.
3. **Phạm vi lệch nằm sẵn trong nguồn.** Nhiều tác phẩm chỉ được dịch một phần. Chương trình phải nhận **danh sách vùng loại trừ** trong cấu hình, không xử lý bằng tay từng lần.
4. **Chú thích đan vào thân bài.** Cả nhóm đều gặp các loại chú thích giống nhau (chữ Hán xen trong bản Việt, năm dương lịch do người dịch thêm, `<ref>`, `{{*}}`, 【攷異】). Vì vậy làm sạch phải là **một bộ luật dùng chung**, mỗi tác phẩm chỉ bật hoặc tắt luật.
5. **Số cặp mỗi người chưa đếm cùng cách.** Kiên và Huy đếm theo câu (~3.370 và ~3.860 cặp tối đa). Đăng đã ước tính khoảng 2.560. Tài đếm theo đoạn (~570), nên chưa so được với ba người kia. Chương trình sẽ đếm lại theo cùng một cách ở Bước 6 cho cả 4 người.

---

## 2. Kiến trúc chương trình

### 2.1. Luồng xử lý

```
01_nguon/ (chỉ đọc)
   │  B4: trích xuất + crawl bổ sung
   ▼
02_ocr_tho/{han,viet}/   ← text thô, mỗi dòng có mã truy vết
   │  B5: bộ luật làm sạch (+ log từng luật, + danh sách loại trừ)
   ▼
03_text_sach/han.txt, viet.txt   (+ work/clean.jsonl giữ mã truy vết)
   │  B6: tách câu (ranh giới cứng/mềm)
   ▼
work/segments.jsonl
   │  B7: dóng 3 tầng  ── tầng 1: mục/năm/bài
   │                   ── tầng 2: đoạn
   │                   ── tầng 3: câu (DP + điểm tổng hợp)
   ▼
work/alignment.jsonl ──► sổ hiệu đính (xlsx) ──► con người sửa ──► áp bản sửa (tái lập được)
   │
   ▼  xuất + kiểm định dạng
04_dong_hang/<MA>_parallel.tsv, <MA>_parallel.xlsx  +  báo cáo
```

### 2.2. Thư mục

```
Lab/GK/                          ← kho git chung của nhóm
├── hvalign/                     ← mã nguồn (package Python)
│   ├── extract.py   clean.py   segment.py   align.py
│   ├── anchors.py   export.py  validate.py  review.py   report.py
│   └── rules/                   ← từng luật làm sạch là một hàm có tên
├── config/
│   ├── phan_cong.tsv            ← ai làm tác phẩm/quyển nào
│   ├── manifest.tsv             ← gộp manifest của 4 người
│   └── works/HCB_01.yaml …      ← cấu hình riêng từng tác phẩm
├── resources/
│   ├── han_viet.tsv             ← từ điển chữ Hán → âm Hán Việt
│   └── char_fix.tsv             ← bảng thay mã lỗi chữ ([BD77], SKchar…)
├── gold/                        ← bộ mẫu dóng hàng chuẩn do người làm
├── work/                        ← tệp trung gian, KHÔNG nộp
├── tests/                       ← kiểm thử tự động (pytest)
├── CV02_HCB_01/ … CV02_HCB_14/  ← thư mục bàn giao theo Guideline
└── Docs/
```

### 2.3. Đơn vị dữ liệu và mã truy vết

Mỗi đoạn và mỗi câu đều mang một mã cố định, ví dụ `HCB_01/q002/s01/p003/u02` (tác phẩm / quyển / mục / đoạn / câu). Mã này đi theo dữ liệu qua mọi bước, nhờ đó:
- Từ một cặp trong TSV có thể lần ngược về đúng dòng trong tệp nguồn (Guideline Bước 2 yêu cầu "giữ lại thứ tự xuất hiện để đối chiếu").
- Biết cặp đó thuộc thành viên nào để đếm số cặp từng người.
- Bản sửa của người hiệu đính được lưu theo mã, nên chạy lại chương trình không làm mất phần đã sửa.

Mã truy vết **không** được ghi vào sheet `DONG_HANG` hay vào TSV, vì Guideline yêu cầu chỉ có hai cột. Mã được lưu ở tệp trung gian và ở một sheet thống kê riêng trong Excel (Guideline cho phép thêm sheet).

### 2.4. Cấu hình theo tác phẩm

**Ví dụ `config/works/HCB_13.yaml`:**

```yaml
work: HCB_13
sources:
  - volume: "488"
    member: Kien
    han:  CV02_HCB_13/01_nguon/han/宋史_卷488.wikitext
    viet: CV02_HCB_13/01_nguon/viet/Biên_dịch_Tống_sử_Quyển_488.wikitext
exclude:                        # vùng không có bản dịch → không dóng, ghi vào loai_tru.tsv
  - {lang: han, section: "大理", reason: "Bản Việt không dịch mục 大理"}
clean_profile: [strip_ref, strip_inline_han_in_viet, strip_year_gloss, fix_char_codes]
segment_profile: {han: punct, viet: default}
length_ratio: 1.12              # âm tiết Việt / chữ Hán, đo ở Bước 2
```

**Ví dụ `config/phan_cong.tsv`:**

```
ma_tac_pham  quyen  thanh_vien
HCB_01       2      Kien
HCB_01       3      Huy
HCB_14       1333   Kien
…
```

**Nguyên tắc chung:**
- `01_nguon/` chỉ đọc (Guideline Bước 3).
- Mọi bước chạy lại được bằng một lệnh và cho cùng kết quả.
- Mỗi lần chốt kết quả thì gắn phiên bản `v01`, `v02` bằng tag git; không đặt tên kiểu `final`.

---

## 3. Bước 4 – Bảo đảm mọi tác phẩm đều có text

**Mục tiêu:** mỗi (tác phẩm, quyển, ngôn ngữ) trong phân công đều có **một bản text gốc** (wikitext hoặc HTML) đúng phạm vi, đã ghi vào manifest, và trích được thành text thô có mã truy vết.

### 3.1. Gom nguồn và chuẩn hóa định dạng

1. Mỗi người chép thư mục `01_nguon/` của mình vào kho chung, theo cấu trúc `CV02_<MA>/01_nguon/{han,viet}/`.
2. Gộp 4 manifest thành `config/manifest.tsv`. Chương trình `extract.py inventory` kiểm tra:
   - Mỗi dòng trong `phan_cong.tsv` có đủ nguồn Hán và Việt chưa.
   - SHA-256 có khớp manifest không.
   - Có **trùng bài giữa các thành viên** không (cùng mã bài sillok, hoặc cùng `revid` Wikisource). Trường hợp cần soát đầu tiên: Q1381 của Huy và Q1384 của Đăng.
3. **Thống nhất định dạng (đã làm):** chương trình nhận cả `.wikitext`, `.txt` và `.html`, tự nhận dạng định dạng theo nội dung rồi chuẩn hóa về một dạng (mục 3.3). Nguồn `.txt` của Huy (`TTTTG_q03_han.txt`…) dùng được ngay, không cần đổi tên hay tải lại. Chỉ cần tải lại những nguồn sai hoặc thiếu ở mục 3.2.

### 3.2. Bổ sung nguồn sai hoặc thiếu

| Tác phẩm | Việc | Cách làm |
|---|---|---|
| HCB_14 Q1358, Q1410 (Tài) | Bản Hán đang sai bài | Lấy danh sách link sillok trong mục "Nguồn" của trang Việt rồi tải từng bài, giống cách đã làm cho phần của Kiên |
| HCB_14 Q1360 (Tài) | Bản Hán thiếu 3 ngày | Như trên |
| HCB_12 (Tài) | Bản Hán thiếu 三家注 | Tìm bản có chú (zh.wikisource hoặc ctext.org). Nếu không có bản phù hợp thì chốt chỉ dóng chính văn |
| HCB_06 (Huy) | Bản Việt chỉ bằng nửa bản Hán | Xác định phần nào chưa dịch rồi ghi vào `exclude` |

Mọi lần tải đều qua cùng một hàm: có User-Agent chung, giãn cách giữa các yêu cầu và tôn trọng `Retry-After`. Trong lúc kiểm tra lại nguồn ở Bước 2, Wikimedia đã trả lỗi 429 khi gửi quá nhanh, nên điểm này là bắt buộc.

### 3.3. Trích xuất wikitext và HTML thành text thô

Bộ đọc wikitext (`hvalign/readers.py`) tách template bằng cách đếm cặp ngoặc chứ không dùng regex, nên xử lý đúng template lồng nhau như `{{*|…{{參|元|玄}}…}}`. Không cần thư viện ngoài như `mwparserfromhell`. Định dạng được nhận theo nội dung: `.txt` có markup wiki được đọc như wikitext, `.txt` không có markup thì mỗi dòng là một đoạn.

| Thành phần | Cách xử lý ở Bước 4 |
|---|---|
| Đầu đề (`{{header}}`, `{{đầu đề…}}`) | Lấy làm siêu dữ liệu, không đưa vào text |
| Đề mục `== … ==` | Thành dòng mốc mục (dùng ở tầng 1 của Bước 7) |
| `{{YL|…}}` | Giữ chữ bên trong |
| `{{參|a|b}}` | Ghi riêng để quyết định ở Bước 5; cần tra trang Template:參 trên zh.wikisource xem chữ nào là chữ hiển thị |
| `{{*|…}}`, `{{注|…}}`, `<ref>…</ref>` | Tách thành bản ghi "chú thích" có mã, **chưa xóa**, để Bước 5 quyết định và để truy vết |
| Danh sách `*`, `:` (HCB_05) | Mỗi mục là một đoạn; ghi loại "khoản" hoặc "ghi chú 按" |
| `{{SKchar|…}}`, mã như `[BD77]` | Giữ nguyên, đánh dấu để tra bảng `char_fix.tsv` |
| HTML sillok | Lấy khối `div.view-text`; nối lại những dòng bị ngắt ở tên người và chỗ nâng chữ (抬頭) |
| Giấy phép, thể loại, "Nguồn:" | Bỏ |

**Đầu ra:** `02_ocr_tho/{han,viet}/<quyển>.tsv`, mỗi dòng có dạng `mã<TAB>loại<TAB>nội dung`. Các dòng `#` ở đầu tệp ghi nguồn, định dạng nhận dạng được, mã hóa và SHA-256. Thư mục này trong Guideline dành cho "OCR thô". Nhóm không OCR nên dùng nó cho text trích thô và ghi rõ điều này trong báo cáo.

**Thu hoạch thêm:** trước khi làm sạch, gom mọi cặp `tên Việt (chữ Hán)` trong bản Việt (ví dụ `Phúc Khang An (福康安)`) vào `work/hv_pairs.tsv`. Riêng phần của Kiên đã có gần 1.500 cụm chữ Hán xen trong bản Việt. Đây là nguồn bổ sung miễn phí cho từ điển Hán Việt ở Bước 7.

### 3.4. Tiêu chí đạt

- [ ] 100% dòng trong `phan_cong.tsv` có đủ nguồn Hán và Việt. Không còn nguồn sai bài và không có bài trùng giữa các thành viên.
- [ ] Text thô không còn `{{`, `[[`, `<ref` chưa được xử lý.
- [ ] Mỗi đoạn trong text thô đều tìm thấy trong PDF tương ứng (cùng phép kiểm tra đã dùng ở Bước 2).

---

## 4. Bước 5 – Làm sạch

### 4.1. Bộ luật làm sạch

Mỗi luật là một hàm có mã, phạm vi áp dụng, hành động (xóa, thay hoặc đưa vào danh sách loại trừ) và **ghi log số lần áp dụng trên từng tệp**. Log này chính là phần "kết quả tự kiểm tra" mà báo cáo cuối cần.

| Mã | Luật | Áp dụng | Ứng với Guideline Bước 5 |
|---|---|---|---|
| R01 | Bỏ đầu đề trang, giấy phép, link nguồn, thể loại | Tất cả | Bỏ đầu/chân trang |
| R02 | Nối dòng bị ngắt (HTML sillok, chỗ nâng chữ 天) | HCB_14 Hán | Ghép từ/câu bị ngắt |
| R03 | Bỏ `<ref>`, 校勘記, chú thích dịch giả | HCB_13, HCB_14, HCB_03… | Loại chú thích |
| R04 | Bỏ `{{*}}`, 【攷異】 ở bản Hán và "(Khảo dị: …)" ở bản Việt | HCB_01 | Loại chú thích |
| R05 | Bỏ dẫn nguồn `{{注}}` ở bản Hán và "(Ngự Lãm 829)" ở bản Việt | HCB_05 | Loại chú thích |
| R06 | Bỏ cụm chữ Hán xen trong bản Việt: `Phúc Khang An (福康安)` → `Phúc Khang An`; `Khang Đầu 糠頭` → `Khang Đầu` | Bản Việt, tất cả | Loại chú thích |
| R07 | Bỏ năm dương lịch do người dịch thêm: `(112 TCN)`, `(năm 1789 dương lịch)` | Bản Việt | Loại chú thích |
| R08 | Bỏ dòng tiêu đề kết quyển như 《續資治通鑑》卷第二 và dấu `§` | HCB_01 | Bỏ phần ngoài nội dung |
| R09 | Thay mã lỗi chữ bằng chữ đúng theo `char_fix.tsv` (`[BD77]`, `{{SKchar}}`…); mã nào chưa tra được thì giữ và báo | HCB_03, 06, 11, 13 | Sửa ký tự rác |
| R10 | Chuẩn hóa khoảng trắng; Unicode NFC cho bản Việt; dấu câu Hán về dạng toàn khổ (`,` → `，`) | Tất cả | Khoảng trắng, dấu câu |
| R11 | Bỏ phần phiên âm và chữ Hán lặp trong thơ có 4 phần, chỉ giữ dịch nghĩa | HCB_14 (Đăng), HCB_02 | Loại nội dung không tương ứng |
| R12 | Áp `exclude` trong cấu hình: chuyển cả vùng sang `loai_tru.tsv` | HCB_02, 06, 09, 10, 12, 13… | Phạm vi |

**Những gì không được đụng tới:** tên riêng, niên hiệu, con số, đơn vị và **chữ dị thể** (爲/為, 眞/真) đều giữ nguyên theo nguồn. Không chuyển giản thể sang phồn thể hay ngược lại.

Riêng R06 phải cẩn thận: bản Việt có lúc dùng chữ Hán làm chính văn chứ không phải chú thích, ví dụ thơ nguyên tác ở HCB_14. Luật chỉ xóa cụm chữ Hán **đứng ngay sau một cụm âm Hán Việt tương ứng** hoặc **nằm trong ngoặc**; mọi trường hợp khác đưa vào danh sách cần xem.

### 4.2. Dòng tiêu đề

Theo tiêu chí 7 của Guideline, cặp dóng hàng không được là dòng tiêu đề. Đề mục (năm, nhân vật, tên bài) được giữ làm **mốc cấu trúc** cho Bước 7 nhưng **không bao giờ xuất ra TSV**.

### 4.3. Đầu ra

- `03_text_sach/han.txt`, `viet.txt`: text sạch, **mỗi dòng một đoạn**, theo thứ tự quyển, không chứa mã hay dấu mốc. Báo cáo dùng số dòng của hai tệp này cho mục "số dòng Hán, số dòng Việt".
- `work/clean.jsonl`: cùng nội dung nhưng có mã truy vết.
- `work/loai_tru.tsv`: các vùng bị loại kèm lý do. Đưa vào báo cáo để giải thích vì sao không phải lỗi `MISSING`.
- `work/clean_log.tsv`: số lần áp dụng từng luật trên từng tệp.

### 4.4. Tiêu chí đạt

- [ ] Máy quét phần sót: bản Việt không còn chữ Hán (trừ trường hợp đã duyệt); không còn `(năm …)`, `{{`, `<`; bản Hán không còn chữ Latin hay dấu câu nửa khổ.
- [ ] Mỗi tác phẩm có 20 cặp đoạn trước/sau làm sạch được người xem và xác nhận không mất chữ của chính văn.
- [ ] Có kiểm thử tự động cho từng luật (ít nhất 3 ví dụ dương và 2 ví dụ âm mỗi luật).

---

## 5. Bước 6 – Tách câu

**Nguyên tắc:** Guideline nói dấu câu chỉ là gợi ý, và "không chia cơ học nếu việc chia làm mất quan hệ dịch". Vì vậy chương trình **tách mịn và đánh dấu loại ranh giới** (cứng hoặc mềm), rồi để bộ dóng hàng ở Bước 7 **gộp lại** khi cần (`n–1`, `1–n`). Tách mịn rồi gộp an toàn hơn tách thô, vì bộ dóng hàng có thể gộp chứ không thể tự cắt nhỏ.

### 5.1. Bản Hán

- **Ranh giới cứng:** sau `。！？`, giữ dấu đóng ngoặc `」』` dính vào câu trước.
- **Ranh giới mềm:** sau `；`; sau `。` ở HCB_14, vì bản sillok dùng `。` cả ở chỗ ngắt nhỏ.
- **Không tách** bên trong lời dẫn `「…」` ngắn (dưới N chữ, N chỉnh theo bộ mẫu chuẩn).

### 5.2. Bản Việt

- **Ranh giới cứng:** sau `.?!…` khi tiếp theo là khoảng trắng và chữ hoa hoặc dấu mở ngoặc kép.
- **Ranh giới mềm:** sau `;` và `:` (Guideline có nêu hai dấu này). Ví dụ "Dụ rằng:" không nên tự đứng thành một câu.
- **Bảo vệ, không tách tại:**
  - số có dấu chấm ngăn nghìn: `10.000`, `1.000`;
  - chữ viết tắt: `TCN`, `v.v.`;
  - chữ tắt trong tên riêng có dấu chấm;
  - dấu chấm nằm trong ngoặc kép.

### 5.3. Văn bản không có dấu câu

Áp dụng cho HCB_05, HCB_03 và có thể có thêm:
- **HCB_05:** đơn vị là **từng khoản** (mỗi gạch đầu dòng). Khoản đã ngắn nên không cần tách thêm.
- **HCB_03:** khoảng 1.400 chữ liền một khối. Có hai phương án:
  - (a) thử một mô hình chấm câu văn ngôn có sẵn trên HuggingFace (họ mô hình GuwenBERT/guwen-punc; cần kiểm tra tên và giấy phép trước khi dùng);
  - (b) **dự phòng:** chấm câu bằng tay, ước tính 1–2 giờ.

  Kết quả chấm câu được lưu thành tệp riêng để truy vết.

### 5.4. Tiêu chí đạt

- [ ] Kiểm thử tự động cho các trường hợp khó (số `10.000`, `TCN`, `「…」`, thơ).
- [ ] Lấy ngẫu nhiên 50 ranh giới mỗi ngôn ngữ cho người xem; tỷ lệ ranh giới sai dưới 5%.
- [ ] Đếm lại **số câu tối đa có thể ghép cho từng người** bằng cùng một công thức, thay cho các ước tính hiện đang không cùng cách đếm.

---

## 6. Bước 7 – Dóng hàng tự động

### 6.1. Ba tầng dóng hàng

Dóng thẳng hàng nghìn câu một lúc rất dễ trượt dây chuyền: một chỗ lệch kéo theo cả đoạn sau lệch. Vì vậy cần dóng từ thô đến mịn, mỗi tầng giới hạn vùng tìm kiếm cho tầng sau.

| Tầng | Đơn vị | Cách làm | Lý do |
|---|---|---|---|
| 1 | Mục / năm / bài | Theo đề mục và bảng ánh xạ đã lập ở Bước 2. Ghi đè bằng cấu hình nếu cần (ví dụ ranh giới 8 bài sillok trong HCB_14) | Cấu trúc gần như luôn 1–1, đã kiểm chứng |
| 2 | Đoạn trong mục | Quy hoạch động (DP) theo độ dài cộng mốc, như đã dùng khi kiểm tra Bước 2. Cho phép một đoạn Hán ứng với nhiều đoạn Việt (HCB_13: 25 đoạn Hán ↔ 105 đoạn Việt) | Cắt bài toán thành các khối nhỏ |
| 3 | Câu trong khối đoạn | DP với điểm tổng hợp (mục 6.2) | Ra cặp cuối cùng |

Các kiểu ghép cho phép ở tầng 3 gồm `1–1`, `1–2`, `2–1`, `1–3`, `3–1`, `2–2`, `1–0` và `0–1`:
- `1–0` và `0–1` nghĩa là một câu không có cặp. Những câu này **không xuất ra TSV** mà ghi vào `work/khong_ghep.tsv`.
- `2–2` trở lên chỉ được chọn khi không thể tách nhỏ hơn, đúng tinh thần `n–m` của Guideline.

### 6.2. Điểm tổng hợp cho một cặp ứng viên

```
điểm = w1 · độ_dài + w2 · mốc_Hán_Việt + w3 · mốc_số_và_can_chi + w4 · ngữ_nghĩa (tùy chọn) − phạt_gộp
```

**a) Độ dài (Gale–Church).** So số chữ Hán với số âm tiết Việt. Tỷ lệ chuẩn đo riêng từng tác phẩm (đã có ở Bước 2: 1,0–1,25). Đây là nền tảng, không cần tài nguyên ngoài.

**b) Mốc Hán Việt – tín hiệu mạnh nhất cho dữ liệu này.** Tên người, địa danh, chức quan, niên hiệu ở bản Việt hầu hết là âm Hán Việt của chữ Hán. Cách làm:
1. Dựng từ điển `resources/han_viet.tsv` (chữ Hán → các âm Hán Việt) từ:
   - trường `kVietnamese` của cơ sở dữ liệu Unihan (Unicode, dùng tự do);
   - các cặp thu hoạch ở Bước 4 (`work/hv_pairs.tsv`, hàng nghìn cặp tên riêng thật trong chính dữ liệu của nhóm).
2. Với mỗi câu Hán, sinh chuỗi âm Hán Việt có thể có. Với mỗi câu Việt, lấy các cụm viết hoa (tên riêng).
3. Điểm = tỷ lệ cụm tên riêng Việt khớp được với một đoạn liên tiếp trong chuỗi âm Hán Việt của câu Hán (có xét nhiều âm đọc).

   *Ví dụ:* 以天雄軍節度使符彥卿為鳳翔節度使 → "… Phù Ngạn Khanh … Phụng Tường …" ↔ câu Việt có "Phù Ngạn Khanh", "Phụng Tường" → điểm cao.

**c) Mốc số và can chi.**
- Đổi số Hán sang số (`三千餘` → 3000; `萬` → 10000) và đọc số Việt (`3.000`, `vạn`).
- So can chi `丙申` với "Bính Thân", đã chuẩn hóa hoa/thường và cách viết "Tỵ"/"Tị".
- Riêng 5 quyển HCB_01 của Kiên đã có 507 mốc can chi khớp đúng thứ tự giữa hai bản, nên gần như neo chặt vị trí.

**d) Ngữ nghĩa (tùy chọn, bật nếu đánh giá cho thấy có lợi).** Dùng mô hình embedding đa ngôn ngữ (LaBSE hoặc BGE-M3) để tính độ tương đồng giữa câu Hán và câu Việt.
- Máy hiện có GPU RTX 3050 6GB và đã cài `torch`, đủ chạy các mô hình này.
- Rủi ro: các mô hình này học chủ yếu từ tiếng Trung hiện đại, nên với văn ngôn có thể kém. Vì vậy chỉ bật khi bộ mẫu chuẩn cho thấy cải thiện (mục 6.4).

Trọng số `w1…w4` được chỉnh trên bộ mẫu chuẩn, không đoán tay.

### 6.3. So với các công cụ có sẵn

Guideline gợi ý Hunalign, Bleualign, BertAlign và Vecalign. Đề xuất **tự dựng bộ dóng DP** như trên và **dùng BertAlign làm mốc so sánh**:

| Công cụ | Phù hợp với dữ liệu này? |
|---|---|
| Hunalign | Cần từ điển song ngữ. Có thể cấp từ điển Hán Việt ở trên, nhưng Hunalign so theo từ, mà chữ Hán và âm tiết Việt không tách từ giống nhau |
| Bleualign | Cần một bản dịch máy Hán → Việt cho văn ngôn, hiện chưa có bản đủ tốt |
| BertAlign / Vecalign | Dùng embedding (như mục d). Dễ chạy, nhưng bỏ qua tín hiệu âm Hán Việt và can chi, vốn là thế mạnh của dữ liệu này |
| **DP tự dựng** | Kết hợp được cả 4 tín hiệu, chạy theo 3 tầng, hiểu vùng loại trừ và mã truy vết. Đổi lại phải tự viết và kiểm thử |

### 6.4. Bộ mẫu chuẩn và đánh giá

- **Dựng bộ mẫu:** mỗi người dóng tay khoảng **120 câu Hán** từ chính tác phẩm của mình. Chọn đủ loại: biên niên (HCB_01), truyện (HCB_07, HCB_11), đoạn bị rút gọn (HCB_11 đoạn 16), sillok (HCB_14) và văn không dấu câu (HCB_05). Tổng khoảng 500 câu, lưu ở `gold/`.
- **Thước đo:** độ chính xác và độ phủ của các cặp. Tính theo hai cách: chặt (khớp đúng ranh giới) và lỏng (có giao nhau).
- **So sánh 3 cấu hình:**
  - (A) độ dài + mốc Hán Việt + số/can chi;
  - (B) như A, thêm embedding;
  - (C) BertAlign nguyên bản.

  Chọn cấu hình tốt nhất, sau đó khóa trọng số.
- **Mục tiêu:** trước khi hiệu đính, độ chính xác cặp tự động ≥ 85%. Đây là mục tiêu tự đặt để khối lượng hiệu đính vừa sức, không phải yêu cầu của Guideline.

### 6.5. Xử lý riêng từng tác phẩm

| Tác phẩm | Xử lý riêng |
|---|---|
| HCB_05 | Đơn vị là khoản; tầng 3 gần như chỉ còn `1–1` theo khoản |
| HCB_11, HCB_06, HCB_09 | Bản Việt rút gọn: cho phép `n–1` rộng hơn. Câu Hán không có bản dịch ghi vào `khong_ghep.tsv`. Các đoạn đã biết bị rút gọn được gắn cờ để ưu tiên hiệu đính |
| HCB_13 | Ánh xạ tầng 2 kiểu `1–n` (25 ↔ 105 đoạn) |
| HCB_14 | Ranh giới bài cố định từ cấu hình. Dấu `。` ở bản Hán là ranh giới mềm, nên `n–1` rất phổ biến |

---

## 7. Hiệu đính và kiểm tra chất lượng (phần con người)

### 7.1. Sổ hiệu đính

Mỗi tác phẩm và mỗi người có một tệp `work/review/<MA>_<người>.xlsx`, **sắp theo điểm tin cậy từ thấp lên cao**.

**Các cột:** mã, Hán, Việt, kiểu ghép, điểm, cờ (lệch số, lệch tên, tỷ lệ độ dài bất thường, đoạn rút gọn), nhãn, thao tác, ghi chú.

**Nhãn:** `OK`, `OMISSION`, `ADDITION`, `MISSING`, `SỬA`.

**Thao tác người hiệu đính được dùng:**
- `gộp↓`: gộp với cặp dưới;
- `tách@<vị trí>`: tách cặp tại một vị trí;
- `bỏ`: chuyển cặp sang danh sách loại trừ.

Lệnh `hvalign review apply` đọc các thao tác này và ghi thành tệp sửa theo mã (`work/patches.jsonl`). Chạy lại chương trình thì bản sửa được áp lại, nên không ai phải sửa tay hai lần.

Tùy thời gian, có thể làm thêm một giao diện web nhỏ (ví dụ Streamlit) thay cho Excel. Đây là "giao diện hiệu đính riêng" mà Guideline §9 cho phép đề xuất.

### 7.2. Kiểm tra chất lượng theo Guideline §8

- Lấy mẫu ngẫu nhiên **ít nhất 100 cặp mỗi người** (hoặc 10% số cặp, lấy số lớn hơn). Người kiểm tra là **một thành viên khác**, không phải người đã hiệu đính phần đó.
- Tính: `Tỷ lệ lỗi = số cặp lỗi / số cặp được kiểm tra hợp lệ`.
- Ngưỡng nghiệm thu là ≤ 30%, **mục tiêu nội bộ ≤ 20%**.
- Mọi lỗi trong mẫu đều phải sửa. Sau đó chương trình **tìm các cặp có cùng dấu hiệu trên toàn file** (cùng cờ, cùng luật làm sạch, cùng vùng) để rà lại, đúng yêu cầu "rà soát lỗi tương tự trên toàn file" của §8.

### 7.3. Kiểm tra tự động trước khi xuất

- Không có ô trống. Không có tab hay xuống dòng trong một vế.
- Không có dòng tiêu đề.
- Bản Việt không còn chữ Hán; bản Hán không có chữ Latin.
- Cặp có tỷ lệ độ dài vượt 3 độ lệch chuẩn được gắn cờ.
- Số và can chi ở hai vế không khớp được gắn cờ.
- Không có cặp trùng lặp; không có câu Hán xuất hiện ở hai cặp.

---

## 8. Xuất file và báo cáo

### 8.1. TSV

- Mã hóa UTF-8, không BOM; xuống dòng `\n`.
- Mỗi dòng có dạng `Hán<TAB>Việt`, không có dòng tiêu đề (theo ví dụ trong Guideline).
- Thứ tự theo quyển, rồi theo vị trí trong quyển.

### 8.2. XLSX

- Sheet `DONG_HANG`: ô A1 là `Hán`, B1 là `Việt`; từ hàng 2 trở đi trùng từng dòng với TSV.
- Ghi mọi ô **ở dạng chuỗi**: một câu bắt đầu bằng `=` sẽ bị Excel hiểu thành công thức, mà Guideline cấm đặt công thức. Không gộp ô, không có dòng trống.
- Sheet thêm `THONG_KE` (được phép theo Guideline): số cặp theo quyển, theo người, theo kiểu ghép; kèm mã truy vết của từng cặp.
- Cần cài `openpyxl`; máy hiện chưa có.

### 8.3. Kiểm định sau xuất

`hvalign validate` đọc lại cả TSV và XLSX rồi so từng dòng phải giống hệt nhau. Lệnh này cũng kiểm tra tên file theo mẫu `<MA_TAC_PHAM>_parallel.*`.

### 8.4. Báo cáo tự sinh cho mỗi tác phẩm

Báo cáo gồm đủ 5 mục bắt buộc của Guideline:
- số cặp;
- số dòng `han.txt` và `viet.txt`;
- kết quả tự kiểm tra (log làm sạch, kết quả kiểm định, tỷ lệ lỗi mẫu);
- nguồn tài liệu (lấy từ manifest);
- công cụ đã dùng.

Kèm theo đó là **số cặp của từng thành viên**, danh sách loại trừ và lý do.

---

## 9. Trình bày theo Guideline §9 (đề xuất phương pháp khác)

| Yêu cầu §9 | Nội dung |
|---|---|
| 1. Lý do lựa chọn | Dữ liệu có cấu trúc rõ (năm, mục, bài) và rất nhiều tên riêng đọc theo âm Hán Việt, nên dóng nhiều tầng với mốc Hán Việt khai thác được thế mạnh này. Các công cụ có sẵn chỉ dựa vào độ dài hoặc embedding. Chương trình chung giúp 4 người làm giống nhau và gộp được dữ liệu theo tác phẩm |
| 2. Đầu vào / đầu ra | Vào: wikitext/HTML trong `01_nguon/`, cấu hình tác phẩm, phân công. Ra: `02_ocr_tho/`, `03_text_sach/`, `04_dong_hang/*.tsv`, `*.xlsx`, báo cáo, log |
| 3. Cách kiểm chứng | Bộ mẫu chuẩn ~500 câu (độ chính xác, độ phủ; so với BertAlign); kiểm thử tự động; lấy mẫu chéo theo §8; kiểm định TSV = XLSX |
| 4. Rủi ro và dự phòng | Xem mục 10 |
| 5. Khả năng tái lập | Mã nguồn và cấu hình trong git. `requirements.txt` ghi phiên bản thư viện. Một lệnh chạy lại toàn bộ (`hvalign run --work HCB_01`). Bản sửa tay lưu dạng tệp sửa theo mã nên áp lại được. Nguồn cố định theo `revid` và SHA-256 |

---

## 10. Rủi ro và phương án dự phòng

| Rủi ro | Dấu hiệu | Dự phòng |
|---|---|---|
| Mốc Hán Việt yếu ở văn bản ít tên riêng (luận, tán, thơ) | Điểm mốc thấp, độ chính xác trên bộ mẫu kém | Dựa thêm vào độ dài và embedding; tăng tỷ lệ hiệu đính tay ở các mục này |
| Embedding kém với văn ngôn | Cấu hình B không hơn A | Tắt embedding; không phụ thuộc vào nó |
| Bản Việt rút gọn hoặc dịch thiếu (HCB_06, 09, 11) | Nhiều `1–0`, nhiều cờ `OMISSION` | Đưa vào `khong_ghep.tsv`, không ép ghép; ghi rõ trong báo cáo |
| Thiếu cặp để đạt 2.000/người (rủi ro nhất là Tài: HCB_02, HCB_12 ngắn, HCB_14 có quyển sai) | Số đếm ở Bước 6 dưới 2.000 sau khi trừ loại trừ | Sửa nguồn HCB_14 ngay ở Bước 4; nhóm điều chỉnh phân công quyển HCB_01 (đang có "1 quyển dư" ở phần của Đăng) |
| Luật làm sạch xóa nhầm chính văn | Kiểm thử hoặc mẫu trước/sau thấy mất chữ | Luật nào cũng có log và kiểm thử; vùng không chắc thì đưa vào danh sách cần xem, không tự xóa |
| Wikimedia hoặc sillok chặn khi tải | Lỗi 429 | Giãn cách, tôn trọng `Retry-After`, lưu bản tải về để không phải tải lại |
| Viết chương trình chậm hơn dự kiến | Chưa xong tầng 3 khi đến hạn | Bản tối thiểu gồm tầng 1 + tầng 2 + Gale–Church có mốc can chi, đủ cho HCB_01 là phần lớn nhất; phần còn lại dóng bán tự động trên sổ hiệu đính |

---

## 11. Việc cần nhóm chốt trước khi viết code

| # | Câu hỏi | Đề xuất mặc định |
|---|---|---|
| 1 | Dùng chung một chương trình và một kho git cho cả nhóm? | Có; kho git riêng tư |
| 2 | Bộ luật làm sạch R03–R08, R11: xóa ở cả hai bản? | Có, như bảng mục 4.1 |
| 3 | Ghi chú khảo chứng 按 của HCB_05 (17 mục): xóa hay giữ để dóng? | Xóa (là chú thích của người biên tập) |
| 4 | Phạm vi HCB_05: cả tác phẩm hay chỉ Quyển 1? | Cả tác phẩm |
| 5 | HCB_12: tìm bản Hán có 三家注 hay chỉ dóng chính văn? | Thử tìm trong Bước 4; không có thì chỉ dùng chính văn |
| 6 | HCB_14: bổ sung bản Hán từ sillok cho Q1358, Q1410, Q1360? | Có |
| 7 | Q1381 (Huy) và Q1384 (Đăng): có trùng bài không, ai giữ? | Kiểm tra bằng mã bài sillok ở Bước 4 |
| 8 | TSV có dòng tiêu đề hay không? | Không có (Excel mới có tiêu đề) |
| 9 | Thứ tự tác phẩm và quyển trong TSV gộp của HCB_01, HCB_14? | Theo số quyển tăng dần |
| 10 | Ai kiểm tra chéo phần của ai? | Xoay vòng: Kiên → Huy → Tài → Đăng → Kiên |

---

## 12. Lộ trình đề xuất

Thứ tự và tiêu chí xong của từng giai đoạn. Thời gian cụ thể do nhóm tự xếp theo hạn nộp.

| Giai đoạn | Nội dung | Xong khi |
|---|---|---|
| G0 – Chuẩn bị | Chốt mục 11; tạo kho git; `phan_cong.tsv`; cài `openpyxl`, `mwparserfromhell` | Kho chạy được kiểm thử rỗng |
| G1 – Bước 4 | Gom nguồn, tải lại nguồn sai hoặc thiếu, trích text thô | Đạt tiêu chí mục 3.4 cho cả 14 tác phẩm |
| G2 – Bước 5 | Bộ luật làm sạch, bảng tra mã chữ, danh sách loại trừ | Đạt tiêu chí mục 4.4; có `03_text_sach/` |
| G3 – Bước 6 | Tách câu và đếm lại số câu từng người | Đạt tiêu chí mục 5.4 |
| G4 – Bộ mẫu chuẩn | Mỗi người dóng tay khoảng 120 câu (làm song song với G2–G3) | Có `gold/` khoảng 500 câu |
| G5 – Bước 7 | Bộ dóng 3 tầng; đánh giá A/B/C; khóa trọng số | Đạt mục tiêu mục 6.4 |
| G6 – Hiệu đính | Sổ hiệu đính; mỗi người sửa phần mình | Không còn cặp điểm thấp chưa xem |
| G7 – Kiểm tra chéo | Lấy mẫu §8, sửa lỗi, rà lỗi tương tự | Tỷ lệ lỗi ≤ 20% cho mọi người |
| G8 – Bàn giao | Xuất, kiểm định, báo cáo | `hvalign validate` không còn lỗi; đủ 5 mục tối thiểu của Guideline |

**Gợi ý chia việc lập trình (nhóm tự điều chỉnh):**
- Người 1: trích xuất và làm sạch (G1–G2).
- Người 2: tách câu và kiểm thử (G3).
- Người 3: bộ dóng hàng (G5).
- Người 4: sổ hiệu đính, xuất file, kiểm định và báo cáo (G6, G8).

Cả 4 người đều tham gia dựng bộ mẫu chuẩn (G4) và hiệu đính phần của mình (G6).
