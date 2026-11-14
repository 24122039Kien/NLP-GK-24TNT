# Check – Bước 1 và Bước 2

Kiểm tra ngày 2026-11-04, trên bản tải ngày 2026-11-02 ([nguon_manifest.tsv](nguon_manifest.tsv)).

**Cách đọc file này:**
- **Tóm tắt:** kết quả chung và những việc cần bạn xác nhận.
- **Phần 1:** thông tin từng tác phẩm để điền vào docs nhóm.
- **Phần 2:** việc cần xử lý ở các bước sau.
- **Phần 3:** bằng chứng kiểm tra, chỉ cần xem khi muốn đối chiếu lại.

---

## Tóm tắt

**Cả 7 tác phẩm đều dùng được và không cần OCR**, vì tất cả 32 tài liệu (64 tệp) đều có sẵn text.

**Tài liệu đã tải đúng:** đã đối chiếu lại với chính Wikisource và sillok ngày 2026-11-04, không phát hiện sai lệch (mục 3.1).

| Mã | Tác phẩm | Phạm vi | Hai bản Hán–Việt | Lưu ý |
|---|---|---|---|---|
| HCB_01 | Tục tư trị thông giám | Quyển 2, 6, 10, 15, 20 | Khớp | Không |
| HCB_04 | Gián phạt Nam Việt thư | Toàn văn | Khớp | Không |
| HCB_05 | Giao Châu ký | Tạm tính cả tác phẩm | Khớp | **Cần xác nhận phạm vi**; bản Hán không có dấu câu |
| HCB_07 | Hán thư | Quyển 095 | Khớp | Không |
| HCB_11 | Hậu Hán thư | Quyển 86 | Khớp về mục | **6 đoạn bị dịch rút gọn** |
| HCB_13 | Tống sử | Quyển 488 | Khớp một phần | **Bản Việt thiếu mục 大理**, chỉ dùng mục 交趾 |
| HCB_14 | Thanh thực lục | Quyển 1333, 1339, 1357, 1438 | Khớp, chỉ là trích đoạn | **Chỉ có 8 bài** được dịch |

**Số cặp:** ước tính tối đa khoảng 3.370 cặp nếu dóng theo câu, nên cần giữ được ít nhất 59% để đạt 2.000 cặp. Nếu dóng theo đoạn thì chỉ được khoảng 900 cặp, không đủ.

### Việc cần bạn xác nhận

1. **Phạm vi HCB_05:** cả tác phẩm hay chỉ Quyển 1? Link trong [nguon](nguon) có đuôi `#Giao_Châu_Ký_–_Quyển_1`, nhưng dòng tiêu đề không ghi quyển như các tác phẩm khác. Tôi đoán đuôi này chỉ do bấm từ mục lục, nên đã kiểm kê cả tác phẩm.
2. **Danh sách quyển và mã đề tài:** tôi không có bảng phân công gốc của nhóm, và `CV02` là lấy từ tên thư mục. Bạn đối chiếu lại với bảng phân công.
3. **Cách xử lý chú thích:** cả nhóm cần thống nhất trước Bước 5 (mục 2.2).

---

## Phần 1 – Thông tin để điền docs

Cả 32 PDF đều không thiếu, không mờ và không trùng trang. Vì vậy dòng Ghi chú dưới đây chỉ nêu điểm riêng của từng tài liệu.

Mỗi tài liệu gồm 2 tệp cùng nội dung: PDF và bản text gốc.

### HCB_01 – Tục tư trị thông giám

**Bước 1 – Xác nhận phạm vi**

| Mục | Nội dung |
|---|---|
| Mã đề tài / tác phẩm | CV02 / HCB_01 |
| Tác phẩm | Tục tư trị thông giám / 續資治通鑑 |
| Tác giả | Tất Nguyên 畢沅 |
| Phạm vi được giao | Quyển 2, 6, 10, 15, 20 |
| Nguồn | Việt: vi.wikisource; Hán: zh.wikisource |
| Định dạng | PDF Text + Text |
| Hai bản cùng phạm vi? | **Khớp.** Mốc thời gian trong đầu đề hai bản trùng nhau ở cả 5 quyển; toàn bộ 507 mốc ngày can chi của bản Hán đều có ở bản Việt, đúng thứ tự. |

**Bước 2 – Kiểm kê nguồn**

*Quyển 2*

| Trường | Bản Việt | Bản Hán |
|---|---|---|
| Tên tài liệu | Tục Tư trị thông giám, quyển 2 (Tất Nguyên; Cơ Như Tuyết dịch) | 續資治通鑑 卷第二 (畢沅) |
| Ngôn ngữ | Việt | Hán |
| Link nguồn | https://vi.wikisource.org/wiki/Tục_tư_trị_thông_giám/Quyển_2 | https://zh.wikisource.org/wiki/續資治通鑑/卷002 |
| Tên tệp | `Tục_tư_trị_thông_giám_Quyển_2` (`.pdf`, `.wikitext`) | `續資治通鑑_卷002` (`.pdf`, `.wikitext`) |
| Số trang | 16 trang; nội dung: p1–16 | 14 trang; nội dung: p1–13 |
| Định dạng | PDF Text + Text (wikitext) | PDF Text + Text (wikitext) |
| Phạm vi | Tống kỷ 2; 1/961–12/962 (Kiến Long 2–3) | Tống kỷ 2; 1/961–12/962 (Kiến Long 2–3) |
| Ghi chú | Không có | p14 là giấy phép và chú thích |

*Quyển 6*

| Trường | Bản Việt | Bản Hán |
|---|---|---|
| Tên tài liệu | Tục Tư trị thông giám, quyển 6 (Tất Nguyên; Cơ Như Tuyết dịch) | 續資治通鑑 卷第六 (畢沅) |
| Ngôn ngữ | Việt | Hán |
| Link nguồn | https://vi.wikisource.org/wiki/Tục_tư_trị_thông_giám/Quyển_6 | https://zh.wikisource.org/wiki/續資治通鑑/卷006 |
| Tên tệp | `Tục_tư_trị_thông_giám_Quyển_6` (`.pdf`, `.wikitext`) | `續資治通鑑_卷006` (`.pdf`, `.wikitext`) |
| Số trang | 15 trang; nội dung: p1–15 | 10 trang; nội dung: p1–9 |
| Định dạng | PDF Text + Text (wikitext) | PDF Text + Text (wikitext) |
| Phạm vi | Tống kỷ 6; 7/969–9/971 (Khai Bảo 2–4) | Tống kỷ 6; 7/969–9/971 (Khai Bảo 2–4) |
| Ghi chú | Không có | p10 là giấy phép và chú thích |

*Quyển 10*

| Trường | Bản Việt | Bản Hán |
|---|---|---|
| Tên tài liệu | Tục Tư trị thông giám, quyển 10 (Tất Nguyên; Cơ Như Tuyết dịch) | 續資治通鑑 第十卷 (畢沅) |
| Ngôn ngữ | Việt | Hán |
| Link nguồn | https://vi.wikisource.org/wiki/Tục_tư_trị_thông_giám/Quyển_10 | https://zh.wikisource.org/wiki/續資治通鑑/卷010 |
| Tên tệp | `Tục_tư_trị_thông_giám_Quyển_10` (`.pdf`, `.wikitext`) | `續資治通鑑_卷010` (`.pdf`, `.wikitext`) |
| Số trang | 16 trang; nội dung: p1–16 | 12 trang; nội dung: p1–11 |
| Định dạng | PDF Text + Text (wikitext) | PDF Text + Text (wikitext) |
| Phạm vi | Tống kỷ 10; 3/979–9/981 (Thái Bình Hưng Quốc 4–6) | Tống kỷ 10; 3/979–9/981 (Thái Bình Hưng Quốc 4–6) |
| Ghi chú | Không có | p12 là giấy phép và chú thích |

*Quyển 15*

| Trường | Bản Việt | Bản Hán |
|---|---|---|
| Tên tài liệu | Tục Tư trị thông giám, quyển 15 (Tất Nguyên; Cơ Như Tuyết dịch) | 續資治通鑑 第十五卷 (畢沅) |
| Ngôn ngữ | Việt | Hán |
| Link nguồn | https://vi.wikisource.org/wiki/Tục_tư_trị_thông_giám/Quyển_15 | https://zh.wikisource.org/wiki/續資治通鑑/卷015 |
| Tên tệp | `Tục_tư_trị_thông_giám_Quyển_15` (`.pdf`, `.wikitext`) | `續資治通鑑_卷015` (`.pdf`, `.wikitext`) |
| Số trang | 13 trang; nội dung: p1–12 | 9 trang; nội dung: p1–8 |
| Định dạng | PDF Text + Text (wikitext) | PDF Text + Text (wikitext) |
| Phạm vi | Tống kỷ 15; 4/989–8/991 (Đoan Củng 2–Thuần Hóa 2) | Tống kỷ 15; 4/989–8/991 (Đoan Củng 2–Thuần Hóa 2) |
| Ghi chú | p13 chỉ có link nguồn | p9 là giấy phép và chú thích |

*Quyển 20*

| Trường | Bản Việt | Bản Hán |
|---|---|---|
| Tên tài liệu | Tục Tư trị thông giám, quyển 20 (Tất Nguyên; Cơ Như Tuyết dịch) | 續資治通鑑 第二十卷 (畢沅) |
| Ngôn ngữ | Việt | Hán |
| Link nguồn | https://vi.wikisource.org/wiki/Tục_tư_trị_thông_giám/Quyển_20 | https://zh.wikisource.org/wiki/續資治通鑑/卷020 |
| Tên tệp | `Tục_tư_trị_thông_giám_Quyển_20` (`.pdf`, `.wikitext`) | `續資治通鑑_卷020` (`.pdf`, `.wikitext`) |
| Số trang | 11 trang; nội dung: p1–11 | 9 trang; nội dung: p1–8 |
| Định dạng | PDF Text + Text (wikitext) | PDF Text + Text (wikitext) |
| Phạm vi | Tống kỷ 20; 1/998–5/999 (Hàm Bình 1–2) | Tống kỷ 20; 1/998–5/999 (Hàm Bình 1–2) |
| Ghi chú | Không có | p9 chỉ có giấy phép và link |

### HCB_04 – Gián phạt Nam Việt thư

**Bước 1 – Xác nhận phạm vi**

| Mục | Nội dung |
|---|---|
| Mã đề tài / tác phẩm | CV02 / HCB_04 |
| Tác phẩm | Gián phạt Nam Việt thư / 諫伐南越書 |
| Tác giả | Lưu An 劉安 |
| Phạm vi được giao | Toàn văn |
| Nguồn | Việt: vi.wikisource; Hán: zh.wikisource |
| Định dạng | PDF Text + Text |
| Hai bản cùng phạm vi? | **Khớp.** Trang Việt ghi bản gốc là 諫伐南越書; đầu và cuối thư trùng nhau. |

**Bước 2 – Kiểm kê nguồn**

| Trường | Bản Việt | Bản Hán |
|---|---|---|
| Tên tài liệu | Gián phạt Nam Việt thư (Lưu An; bản biên dịch Wikisource) | 諫伐南越書 (劉安, 西漢) |
| Ngôn ngữ | Việt | Hán |
| Link nguồn | https://vi.wikisource.org/wiki/Biên_dịch:Gián_phạt_Nam_Việt_thư | https://zh.wikisource.org/wiki/諫伐南越書 |
| Tên tệp | `Biên_dịch_Gián_phạt_Nam_Việt_thư` (`.pdf`, `.wikitext`) | `諫伐南越書` (`.pdf`, `.wikitext`) |
| Số trang | 3 trang; nội dung: p1–3 | 3 trang; nội dung: p1–2 |
| Định dạng | PDF Text + Text (wikitext) | PDF Text + Text (wikitext) |
| Phạm vi | Toàn văn thư | Toàn văn thư |
| Ghi chú | p3 có cả cuối bài và giấy phép | p3 chỉ có giấy phép và link |

### HCB_05 – Giao Châu ký

> **Cần xác nhận:** phạm vi là cả tác phẩm hay chỉ Quyển 1 (xem phần Tóm tắt).

**Bước 1 – Xác nhận phạm vi**

| Mục | Nội dung |
|---|---|
| Mã đề tài / tác phẩm | CV02 / HCB_05 |
| Tác phẩm | Giao Châu ký / 交州記 (嶺南遺書本) |
| Tác giả | Lưu Hân Kỳ 劉欣期 (Tằng Chiêu 曾釗 sưu tầm) |
| Phạm vi được giao | Tạm tính cả tác phẩm |
| Nguồn | Việt: vi.wikisource; Hán: zh.wikisource |
| Định dạng | PDF Text + Text |
| Hai bản cùng phạm vi? | **Khớp.** Trang Việt ghi bản gốc là 交州記 (嶺南遺書本); số khoản gần như bằng nhau. Bản Việt thiếu 1 ghi chú nhỏ. |

**Bước 2 – Kiểm kê nguồn**

| Trường | Bản Việt | Bản Hán |
|---|---|---|
| Tên tài liệu | Giao Châu ký (Lưu Hân Kỳ, nhà Tấn; Tằng Chiêu sưu tầm; bản biên dịch Wikisource) | 交州記, 嶺南遺書本 (劉欣期; 曾釗 輯) |
| Ngôn ngữ | Việt | Hán |
| Link nguồn | https://vi.wikisource.org/wiki/Biên_dịch:Giao_Châu_ký | https://zh.wikisource.org/wiki/交州記_(嶺南遺書本) |
| Tên tệp | `Biên_dịch_Giao_Châu_ký` (`.pdf`, `.wikitext`) | `交州記_(嶺南遺書本)` (`.pdf`, `.wikitext`) |
| Số trang | 6 trang; nội dung: p1–5 | 5 trang; nội dung: p1–5 |
| Định dạng | PDF Text + Text (wikitext) | PDF Text + Text (wikitext) |
| Phạm vi | Quyển 1, Quyển 2, Phụ chú | 卷一, 卷二, 附 |
| Ghi chú | p6 là giấy phép. Thiếu ghi chú 章懷太子…和帝紀注引同 so với bản Hán | **Không có dấu câu.** p1 có khung chữ dọc 道光三十季春二月南海伍氏開雕…, không phải nội dung chính |

### HCB_07 – Hán thư

**Bước 1 – Xác nhận phạm vi**

| Mục | Nội dung |
|---|---|
| Mã đề tài / tác phẩm | CV02 / HCB_07 |
| Tác phẩm | Hán thư / 漢書 |
| Tác giả | Ban Cố 班固 |
| Phạm vi được giao | Quyển 095 |
| Nguồn | Việt: vi.wikisource; Hán: zh.wikisource |
| Định dạng | PDF Text + Text |
| Hai bản cùng phạm vi? | **Khớp.** 11 mục trùng từng mục; 232/234 mốc chữ Hán trong bản Việt tìm thấy ở bản Hán. |

**Bước 2 – Kiểm kê nguồn**

| Trường | Bản Việt | Bản Hán |
|---|---|---|
| Tên tài liệu | Hán thư, quyển 095 – Tây Nam Di, lưỡng Việt, Triều Tiên truyện (Ban Cố; bản biên dịch Wikisource) | 漢書 卷九十五 西南夷兩粵朝鮮傳第六十五 (班固) |
| Ngôn ngữ | Việt | Hán |
| Link nguồn | https://vi.wikisource.org/wiki/Biên_dịch:Hán_thư/Quyển_095 | https://zh.wikisource.org/wiki/漢書/卷095 |
| Tên tệp | `Biên_dịch_Hán_thư_Quyển_095` (`.pdf`, `.wikitext`) | `漢書_卷095` (`.pdf`, `.wikitext`) |
| Số trang | 12 trang; nội dung: p1–12 | 8 trang; nội dung: p1–7 |
| Định dạng | PDF Text + Text (wikitext) | PDF Text + Text (wikitext) |
| Phạm vi | Toàn quyển (11 mục) | Toàn quyển (11 mục) |
| Ghi chú | p12 có cả cuối bài và giấy phép | p8 chỉ có giấy phép và link |

### HCB_11 – Hậu Hán thư

> **Lưu ý:** 6 đoạn trong mục 南蠻 của bản Việt bị dịch rút gọn (chi tiết ở mục 2.1).

**Bước 1 – Xác nhận phạm vi**

| Mục | Nội dung |
|---|---|
| Mã đề tài / tác phẩm | CV02 / HCB_11 |
| Tác phẩm | Hậu Hán thư / 後漢書 |
| Tác giả | Phạm Diệp 范曄 |
| Phạm vi được giao | Quyển 86 |
| Nguồn | Việt: vi.wikisource; Hán: zh.wikisource |
| Định dạng | PDF Text + Text |
| Hai bản cùng phạm vi? | **Khớp về mục, có đoạn rút gọn.** 10 mục trùng nhau; 6 đoạn (18,7% quyển) dịch rút gọn. |

**Bước 2 – Kiểm kê nguồn**

| Trường | Bản Việt | Bản Hán |
|---|---|---|
| Tên tài liệu | Hậu Hán thư, quyển 86 – Nam Man, Tây Nam Di liệt truyện (Phạm Diệp; bản biên dịch Wikisource) | 後漢書 卷八十六 南蠻西南夷列傳 (范曄) |
| Ngôn ngữ | Việt | Hán |
| Link nguồn | https://vi.wikisource.org/wiki/Biên_dịch:Hậu_Hán_thư/Quyển_86 | https://zh.wikisource.org/wiki/後漢書/卷86 |
| Tên tệp | `Biên_dịch_Hậu_Hán_thư_Quyển_86` (`.pdf`, `.wikitext`) | `後漢書_卷86` (`.pdf`, `.wikitext`) |
| Số trang | 13 trang; nội dung: p1–13 | 9 trang; nội dung: p1–9 |
| Định dạng | PDF Text + Text (wikitext) | PDF Text + Text (wikitext) |
| Phạm vi | Toàn quyển (10 mục) | Toàn quyển (10 mục) |
| Ghi chú | p13 có cả cuối bài và giấy phép. 6 đoạn dịch rút gọn | p9 chỉ còn đoạn 贊. Có mã lỗi chữ như `[BD77]` |

### HCB_13 – Tống sử

> **Lưu ý:** bản Việt không có mục 大理, nên chỉ dùng mục 交趾.

**Bước 1 – Xác nhận phạm vi**

| Mục | Nội dung |
|---|---|
| Mã đề tài / tác phẩm | CV02 / HCB_13 |
| Tác phẩm | Tống sử / 宋史 |
| Tác giả | Thoát Thoát 脫脫 |
| Phạm vi được giao | Quyển 488 (đề xuất chỉ dùng mục 交趾) |
| Nguồn | Việt: vi.wikisource; Hán: zh.wikisource |
| Định dạng | PDF Text + Text |
| Hai bản cùng phạm vi? | **Khớp một phần.** Mục 交趾 khớp từ đầu đến cuối; mục 大理 (601 chữ) không có bản dịch, dù đầu đề trang Việt có ghi "Đại Lý". |

**Bước 2 – Kiểm kê nguồn**

| Trường | Bản Việt | Bản Hán |
|---|---|---|
| Tên tài liệu | Tống sử, quyển 488 – Ngoại quốc tứ: Giao Chỉ (Thoát Thoát; bản biên dịch Wikisource) | 宋史 卷四百八十八 列傳卷第二百四十七 外國四 交趾 大理 |
| Ngôn ngữ | Việt | Hán |
| Link nguồn | https://vi.wikisource.org/wiki/Biên_dịch:Tống_sử/Quyển_488 | https://zh.wikisource.org/wiki/宋史/卷488 |
| Tên tệp | `Biên_dịch_Tống_sử_Quyển_488` (`.pdf`, `.wikitext`) | `宋史_卷488` (`.pdf`, `.wikitext`) |
| Số trang | 14 trang; nội dung: p1–12 | 7 trang; nội dung: p1–7 |
| Định dạng | PDF Text + Text (wikitext) | PDF Text + Text (wikitext) |
| Phạm vi | Chỉ mục Giao Chỉ | 交趾 ở p1–6 (dùng); 大理 ở p6–7 (ngoài phạm vi) |
| Ghi chú | p12–13 có chú thích và giấy phép. **p14 trống** | p7 có 校勘記 |

### HCB_14 – Thanh thực lục

> **Lưu ý:** bản Việt chỉ dịch 8 bài trong 4 quyển, nên chỉ dùng được 8 bài này.

**Bước 1 – Xác nhận phạm vi**

| Mục | Nội dung |
|---|---|
| Mã đề tài / tác phẩm | CV02 / HCB_14 |
| Tác phẩm | Thanh thực lục – Cao Tông thực lục / 清實錄·高宗純皇帝實錄 |
| Tác giả | (trang nguồn không ghi) |
| Phạm vi được giao | Quyển 1333, 1339, 1357, 1438 (thực tế 8 bài) |
| Nguồn | Việt: vi.wikisource; Hán: sillok.history.go.kr |
| Định dạng | PDF Text + Text (HTML) |
| Hai bản cùng phạm vi? | **Khớp, nhưng chỉ là trích đoạn.** Ngày tháng và nội dung cả 8 bài đều khớp. |

**Bước 2 – Kiểm kê nguồn**

Thông tin chung của cả 8 bài Hán:

- Ngôn ngữ: Hán
- Số trang: mỗi bài 2 trang; nội dung ở p1
- Định dạng: PDF Text + Text (HTML)
- Ghi chú: p2 chỉ có chân trang tiếng Hàn. PDF được in từ HTML. Thân bài bị ngắt dòng ở tên người và chỗ nâng chữ 天

*Quyển 1333 – bản Việt*

| Trường | Nội dung |
|---|---|
| Tên tài liệu | Thanh thực lục – Cao Tông Thuần Hoàng đế thực lục, quyển 1333 (bản biên dịch Wikisource) |
| Ngôn ngữ | Việt |
| Link nguồn | https://vi.wikisource.org/wiki/Biên_dịch:Thanh_thực_lục/Cao_Tông_Thuần_Hoàng_đế_thực_lục/Quyển_1333 |
| Tên tệp | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1333` (`.pdf`, `.wikitext`) |
| Số trang | 3 trang; nội dung: p1–3 |
| Định dạng | PDF Text + Text (wikitext) |
| Phạm vi | 3 bài ngày 22/6 Càn Long 54 (1789) |
| Ghi chú | p3 có cả cuối bài và danh sách nguồn |

*Quyển 1333 – bản Hán* (高宗純皇帝實錄 卷之一千三百三十三)

- **Bài 3/8, ngày 22/6 – dụ về việc phong Nguyễn Quang Bình**
  - Link: https://sillok.history.go.kr/mc/id/qsilok_007_1333_0010_0010_0060_0030
  - Tệp: `清實錄_高宗純皇帝實錄_卷1333_qsilok_007_1333_0010_0010_0060_0030` (`.pdf`, `.html`)
- **Bài 4/8, ngày 22/6 – sắc dụ gửi Nguyễn Quang Bình**
  - Link: https://sillok.history.go.kr/mc/id/qsilok_007_1333_0010_0010_0060_0040
  - Tệp: `清實錄_高宗純皇帝實錄_卷1333_qsilok_007_1333_0010_0010_0060_0040` (`.pdf`, `.html`)
- **Bài 5/8, ngày 22/6 – sách văn phong vương**
  - Link: https://sillok.history.go.kr/mc/id/qsilok_007_1333_0010_0010_0060_0050
  - Tệp: `清實錄_高宗純皇帝實錄_卷1333_qsilok_007_1333_0010_0010_0060_0050` (`.pdf`, `.html`)

*Quyển 1339 – bản Việt*

| Trường | Nội dung |
|---|---|
| Tên tài liệu | Thanh thực lục – Cao Tông Thuần Hoàng đế thực lục, quyển 1339 (bản biên dịch Wikisource) |
| Ngôn ngữ | Việt |
| Link nguồn | https://vi.wikisource.org/wiki/Biên_dịch:Thanh_thực_lục/Cao_Tông_Thuần_Hoàng_đế_thực_lục/Quyển_1339 |
| Tên tệp | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1339` (`.pdf`, `.wikitext`) |
| Số trang | 2 trang; nội dung: p1 |
| Định dạng | PDF Text + Text (wikitext) |
| Phạm vi | 2 bài ngày 23/9 Càn Long 54 (1789) |
| Ghi chú | p2 chỉ có danh sách nguồn và link. Chú Hán sai: "Lê Duy Chỉ 潛匿" (潛匿 nghĩa là "ẩn náu"; tên đúng là 黎維祇) |

*Quyển 1339 – bản Hán* (高宗純皇帝實錄 卷之一千三百三十九)

- **Bài 4/7, ngày 23/9 – hoãn việc Tôn Vĩnh Thanh vào kinh**
  - Link: https://sillok.history.go.kr/mc/id/qsilok_007_1339_0010_0010_0080_0040
  - Tệp: `清實錄_高宗純皇帝實錄_卷1339_qsilok_007_1339_0010_0010_0080_0040` (`.pdf`, `.html`)
- **Bài 5/7, ngày 23/9 – việc Lê Duy Chỉ**
  - Link: https://sillok.history.go.kr/mc/id/qsilok_007_1339_0010_0010_0080_0050
  - Tệp: `清實錄_高宗純皇帝實錄_卷1339_qsilok_007_1339_0010_0010_0080_0050` (`.pdf`, `.html`)

*Quyển 1357 – bản Việt*

| Trường | Nội dung |
|---|---|
| Tên tài liệu | Thanh thực lục – Cao Tông Thuần Hoàng đế thực lục, quyển 1357 (bản biên dịch Wikisource) |
| Ngôn ngữ | Việt |
| Link nguồn | https://vi.wikisource.org/wiki/Biên_dịch:Thanh_thực_lục/Cao_Tông_Thuần_Hoàng_đế_thực_lục/Quyển_1357 |
| Tên tệp | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1357` (`.pdf`, `.wikitext`) |
| Số trang | 2 trang; nội dung: p1–2 |
| Định dạng | PDF Text + Text (wikitext) |
| Phạm vi | 2 bài ngày 25 và 27/6 Càn Long 55 (1790) |
| Ghi chú | p2 có cả cuối bài và danh sách nguồn |

*Quyển 1357 – bản Hán* (高宗純皇帝實錄 卷之一千三百五十七)

- **Bài 2/2, ngày 25/6 – truyền đơn cung ứng**
  - Link: https://sillok.history.go.kr/mc/id/qsilok_007_1357_0010_0010_0090_0020
  - Tệp: `清實錄_高宗純皇帝實錄_卷1357_qsilok_007_1357_0010_0010_0090_0020` (`.pdf`, `.html`)
- **Bài 3/3, ngày 27/6 – truyền đơn cung ứng**
  - Link: https://sillok.history.go.kr/mc/id/qsilok_007_1357_0010_0010_0110_0030
  - Tệp: `清實錄_高宗純皇帝實錄_卷1357_qsilok_007_1357_0010_0010_0110_0030` (`.pdf`, `.html`)

*Quyển 1438 – bản Việt*

| Trường | Nội dung |
|---|---|
| Tên tài liệu | Thanh thực lục – Cao Tông Thuần Hoàng đế thực lục, quyển 1438 (bản biên dịch Wikisource) |
| Ngôn ngữ | Việt |
| Link nguồn | https://vi.wikisource.org/wiki/Biên_dịch:Thanh_thực_lục/Cao_Tông_Thuần_Hoàng_đế_thực_lục/Quyển_1438 |
| Tên tệp | `Biên_dịch_Thanh_thực_lục_Cao_Tông_Thuần_Hoàng_đế_thực_lục_Quyển_1438` (`.pdf`, `.wikitext`) |
| Số trang | 1 trang; nội dung: p1 |
| Định dạng | PDF Text + Text (wikitext) |
| Phạm vi | 1 bài ngày 3/10 Càn Long 58 (1793) |
| Ghi chú | Không có |

*Quyển 1438 – bản Hán* (高宗純皇帝實錄 卷之一千四百三十八)

- **Bài 7/8, ngày 3/10 – cống phẩm của Nguyễn Quang Toản**
  - Link: https://sillok.history.go.kr/mc/id/qsilok_007_1438_0010_0010_0020_0070
  - Tệp: `清實錄_高宗純皇帝實錄_卷1438_qsilok_007_1438_0010_0010_0020_0070` (`.pdf`, `.html`)

---

## Phần 2 – Việc cần xử lý ở các bước sau

### 2.1. HCB_11: 6 đoạn dịch rút gọn

Tôi đã đọc cả 6 đoạn và xác nhận đều bị rút gọn. Tổng 1.726 chữ, bằng 18,7% quyển.

| Đoạn trong 南蠻 (đánh số từ 0) | Mở đầu bản Hán | Chữ Hán / âm tiết Việt | Ví dụ phần bị lược ở bản Việt |
|---|---|---|---|
| 16 | 若荆、楊無事，發之可也 | 456 / 218 | Các câu 其不可一也…; lời đồn 虜來尙可，尹來殺我; câu cuối 宜即拜良等，便道之官 |
| 9 | 交阯之南有越裳國 | 150 / 94 | Lời sứ giả 道路悠遠…; lời Chu Công 德不加焉… |
| 24 | 至於中興，郡守常率以征伐 | 381 / 263 | Lời đối đáp của Trình Bao bị tóm lược mạnh |
| 7 | 永壽三年十一月 | 276 / 200 | Lời can của Hồ Sảng và lời đáp của Lý Túc |
| 6 | 順帝永和元年 | 256 / 205 | Tờ tấu của Ngư Hủ (虞詡) chỉ còn một câu |
| 10 | 及楚子稱霸，朝貢百越 | 207 / 175 | 南北五百里; 會稽 (quê Tôn Hạnh); 威政大行，獻命歲至 |

**Đề xuất:**
- Dóng từng câu, ưu tiên kiểu `n–1` với phần tóm lược.
- Câu Hán không có bản dịch thì **không ép vào cặp** mà ghi vào log riêng. Nếu ép vào, cặp đó dễ bị tính lỗi `OMISSION` theo tiêu chí 2 của Guideline.
- Khi kiểm tra chất lượng, nên lấy mẫu dày hơn ở 6 đoạn này.

### 2.2. Thống nhất cách xử lý chú thích (trước Bước 5)

Guideline yêu cầu loại chú thích ngoài nội dung chính.

| Loại | Ở đâu | Đề xuất |
|---|---|---|
| Cụm chữ Hán xen trong bản Việt, như `(福康安)` | HCB_01: Q6 139, Q10 80, Q15 94, Q20 13; HCB_05: 92; HCB_07: 286; HCB_11: 499; HCB_13: 232; HCB_14: 56 | Xóa |
| Năm dương lịch do người dịch thêm, như `(112 TCN)` | HCB_07: 20; HCB_11: 75; HCB_13: 71; HCB_14: 1 | Xóa, vì bản Hán không có |
| Chú 【攷異】 và chú nhỏ `{{*}}` | HCB_01 Q2: Hán 39 chú nhỏ (25 chú 【攷異】); Việt chỉ dịch 4 chú | Xóa ở cả hai bản |
| Dẫn nguồn `{{注}}` và "(Ngự Lãm 829)" | HCB_05: 77 chú | Xóa ở cả hai bản |
| Ghi chú khảo chứng 按 của người biên tập | HCB_05: Hán 17, Việt 16 | Xóa ở cả hai bản; nếu giữ thì được thêm khoảng 16 cặp |
| 校勘記 và chú thích dịch giả (`<ref>`) | HCB_13: Hán 18, Việt 26 | Xóa |
| Mã lỗi `[BD77]`, `[B258]`, `[E8E6]`, `[CF3D]`; thẻ `<曷毛>`, `<名頁>` | HCB_11 | Tra bản khác để khôi phục chữ, không xóa |
| Mã chữ ghép `[犭+朋]`, `[巾+雇]` | HCB_13: Hán 3, Việt 4 | Giữ theo nguồn hoặc thay bằng chữ đúng nếu tra được |

Hai trường hợp cần xem riêng:
- `{{注|歌曲說牛力强弱耕具輕重也}}` và `{{注|呼郭切}}` ở HCB_05 là chú giải, không phải dẫn nguồn.
- Bản Việt HCB_01 Q2 viết can chi lẫn hoa/thường, có dạng "Tỵ" và dạng "ngày mồng 1 tháng Giáp Tý". Nếu dùng can chi làm mốc tự động thì phải chuẩn hóa trước.
- Bản Hán HCB_01 Q2 có dòng cuối 《續資治通鑑》卷第二 không phải nội dung, cần bỏ khi làm sạch.

### 2.3. Tệp nên dùng cho Bước 4

**Nên dùng `.wikitext` và `.html`; chỉ dùng PDF để xem và đối chiếu.** Lý do là khi trích text từ PDF:
- Mất chữ hiếm ở 5 tài liệu: Hán Q2 (4), Hán Q15 (1), Hán HCB_05 (1), Hán HCB_13 (4), Việt HCB_13 (1).
- Mất cả chữ dựng bằng template, ví dụ 玄 trong 玄黓 và 玄冥 ở Q2.
- Bị ngắt dòng cứng giữa câu, và lẫn chân trang, giấy phép.
- Đề mục bị đẩy xuống cuối trang nếu dùng PyMuPDF mặc định (phải dùng `sort=True`).

Vì không cần OCR, thư mục `02_ocr_tho/` sẽ để trống; nên ghi "không áp dụng" trong báo cáo cuối.

### 2.4. Ước tính số cặp

Đây là số ước tính từ dấu câu, chưa phải kết quả dóng hàng. "Tối đa" là số nhỏ hơn giữa số câu Hán và số câu Việt.

| Tác phẩm | Chữ Hán | Âm tiết Việt | Đoạn Hán | Câu Hán / Việt | Tối đa |
|---|---|---|---|---|---|
| HCB_01 Q2 | 8.111 | 10.178 | 182 | 428 / 451 | 428 |
| HCB_01 Q6 | 7.947 | 9.396 | 131 | 363 / 390 | 363 |
| HCB_01 Q10 | 8.904 | 10.386 | 162 | 430 / 442 | 430 |
| HCB_01 Q15 | 6.926 | 8.178 | 99 | 330 / 352 | 330 |
| HCB_01 Q20 | 6.340 | 7.760 | 104 | 308 / 315 | 308 |
| HCB_04 | 1.717 | 1.973 | 8 | 66 / 70 | 66 |
| HCB_05 | 2.137 | 2.603 | 89 khoản | không có dấu câu / 184 | 89 |
| HCB_07 | 7.574 | 8.903 | 44 | 395 / 398 | 395 |
| HCB_11 | 9.215 | 9.189 | 59 | 573 / 512 | 512 |
| HCB_13 (chỉ 交趾) | 7.057 | 7.925 | 25 | 325 / 343 | 325 |
| HCB_14 | 2.909 | 3.014 | 8 bài | 388 / 125 | 125 |
| **Tổng** | **68.837** | **79.505** | **911** | | **~3.371** |

- Số thực tế sẽ thấp hơn, vì có câu phải gộp hoặc loại. Chưa rõ giữ lại được bao nhiêu; chỉ biết cần **ít nhất 59%** để đạt 2.000 cặp.
- HCB_01 chiếm hơn nửa tổng số (1.859 cặp) nên là nguồn chính.
- Số của HCB_05 đang tính cả 17 ghi chú 按; nếu xóa theo mục 2.2 thì còn 72.
- Số câu Hán của HCB_14 cao vì bản này dùng dấu 。 cả ở chỗ ngắt nhỏ, nên không so trực tiếp được với số câu Việt.

---

## Phần 3 – Bằng chứng kiểm tra

### 3.1. Kiểm tra tệp

| Hạng mục | Kết quả |
|---|---|
| Đối chiếu với manifest | 64/64 tệp khớp SHA-256 và kích thước; không thiếu, không thừa tệp |
| Đối chiếu với Wikisource | 24/24 wikitext khớp `sha1` và kích thước của đúng phiên bản trên máy chủ; chưa trang nào có bản mới hơn (kiểm tra 2026-11-04) |
| Đối chiếu với sillok | Tải lại 8/8 bài, thân bài giống hệt tệp trên máy |
| Danh sách được giao | Trang mục lục trong `nguon` có đủ 5 quyển HCB_01 và 4 quyển HCB_14; 8/8 nguồn sillok do trang Việt dẫn đều đã tải |
| Nguồn Hán đúng bản gốc | Trang Việt của HCB_04, 05, 07, 11, 13 ghi bản gốc trùng trang Hán đã tải. HCB_01 không ghi, nên xác nhận bằng mốc thời gian và can chi. HCB_14 xác nhận bằng link nguồn và ngày tháng |
| Nội dung PDF so với bản text | 32/32 PDF có đủ các đoạn; chỉ mất chữ hiếm và chữ dựng bằng template (mục 2.3) |
| Phiên bản PDF | 24/24 PDF Wikisource có `oldid` trùng `revid` trong manifest (8 PDF sillok không có revid) |
| Số trang | 32/32 PDF khớp cột `so_trang` |
| Scan hay text | 32/32 PDF có lớp text; không có ảnh nào lớn hơn 300×300 px |
| Trùng trang | Không có |
| Trang trống | Chỉ có p14 của bản Việt HCB_13 |
| Bản Hán và Việt chung một file | Không có, nên không cần bước tách |

### 3.2. Đối chiếu từng tác phẩm

Mỗi tác phẩm có mẫu đầu – giữa – cuối (đã đọc trực tiếp, chỉ để xác nhận đúng tác phẩm, không phải kết quả dóng hàng) và bảng ánh xạ cấu trúc theo yêu cầu của Guideline.

Trong các bảng, **r = số âm tiết Việt / số chữ Hán**. Mức thường gặp là 1,1–1,3; dưới 0,85 là dấu hiệu dịch rút gọn.

#### HCB_01

Mốc ngày can chi của bản Hán tìm thấy ở bản Việt: Q2 121/121, Q6 92/92, Q10 139/139, Q15 75/75, Q20 80/80. Trong Q2 có 3 mốc viết khác dạng (như "ngày mồng 1 tháng Giáp Tý" cho 甲子朔), đã đọc và xác nhận.

| Quyển | Vị trí | Hán | Việt |
|---|---|---|---|
| Q2 | Đầu | 春，正月，丙申朔，御崇元殿受朝 | Mùa xuân, tháng giêng, ngày Bính Thân tức mồng 1, Hoàng đế ngự điện Sùng Nguyên nhận triều hạ |
| Q2 | Giữa | 詔州縣不得役僑居民。 | Chiếu các châu, huyện không được bắt phu dịch dân ngụ cư. |
| Q2 | Cuối | 南漢主納李託二女，長爲貴妃，次爲美人 | Nam Hán chủ nạp 2 con gái của Lý Thác, người chị làm Quý phi, người em làm Mỹ nhân |
| Q6 | Đầu | 秋，七月，丙寅，以天雄軍節度使符彥卿為鳳翔節度使。 | Mùa thu, tháng 7, ngày Bính Dần, lấy Tiết độ sứ Thiên Hùng quân Phù Ngạn Khanh (符彥卿) làm Tiết độ sứ Phụng Tường. |
| Q6 | Giữa | 冬，十月，辛卯，潘美等破南漢開建寨 | Mùa đông, tháng 10, ngày Tân Mão, Phan Mỹ và các tướng phá trại Khai Kiến của Nam Hán |
| Q6 | Cuối | 壬子，遼主如歸化州。甲寅，如南京。 | Ngày Nhâm Tý, Liêu chúa đi Quy Hóa châu. Ngày Giáp Dần, đến Nam Kinh. |
| Q10 | Đầu | 三月，庚辰朔，駐蹕鎮州。 | Tháng 3, ngày Canh Thìn là mồng 1, xa giá dừng ở Trấn châu. |
| Q10 | Giữa | 初，西南夷不供朝貢，刑部郎中許仲宣為西川轉運使 | Ban đầu, Tây Nam Di không vào triều cống, Lang trung Bộ Hình Hứa Trọng Tuyên làm Chuyển vận sứ Tây Xuyên |
| Q10 | Cuối | 丙辰，知易州白繼贇敗遼兵于平塞寨。 | Ngày Bính Thìn, Tri Dịch châu là Bạch Kế Vân (白繼贇) đánh bại quân Liêu ở trại Bình Tái. |
| Q15 | Đầu | 夏，四月，國子博士李覺上言曰 | Mùa hạ, tháng 4, Quốc tử bác sĩ Lý Giác (李覺) dâng sớ nói |
| Q15 | Giữa | 丁酉，以御製詩文藏于秘閣。 | Ngày Đinh Dậu, đem thơ văn do Hoàng đế ngự chế cất vào Bí các. |
| Q15 | Cuối | 丁亥，并州言契丹四百餘口內附。 | Ngày Đinh Hợi, từ Tinh châu báo có hơn 400 người Khiết Đan nội phụ. |
| Q20 | Đầu | 帝名恒，太宗第三子也，母曰元德皇后李氏。 | …húy là Hằng (恒), là con trai thứ ba của Thái Tông, mẹ là Nguyên Đức hoàng hậu Lý thị. |
| Q20 | Giữa | 宰相呂端久病，詔免朝謁，就中書視事 | Tể tướng Lữ Đoan bệnh đã lâu, chiếu miễn việc vào chầu, chỉ đến Trung thư xử lý công việc |
| Q20 | Cuối | 帝納其言，即停前詔。 | Hoàng đế nghe theo lời, liền đình chỉ chiếu trước. |

| Quyển | Mục Hán ↔ Việt | Chữ Hán | Âm tiết Việt | Đoạn Hán / Việt | r |
|---|---|---|---|---|---|
| Q2 | 建隆二年 ↔ Kiến Long 2 (961) | 4.495 | 5.582 | 86 / 87 | 1,24 |
| Q2 | 建隆三年 ↔ Kiến Long 3 (962) | 3.596 | 4.576 | 95 / 98 | 1,27 |
| Q6 | 開寶二年 ↔ Khai Bảo 2 (969) | 1.615 | 2.012 | 31 / 31 | 1,25 |
| Q6 | 開寶三年 ↔ Khai Bảo 3 (970) | 3.369 | 3.959 | 45 / 49 | 1,18 |
| Q6 | 開寶四年 ↔ Khai Bảo 4 (971) | 2.963 | 3.425 | 55 / 77 | 1,16 |
| Q10 | 太平興國四年 ↔ Thái Bình Hưng Quốc 4 (979) | 4.368 | 4.887 | 83 / 86 | 1,12 |
| Q10 | 太平興國五年 ↔ Thái Bình Hưng Quốc 5 (980) | 2.527 | 2.972 | 50 / 53 | 1,18 |
| Q10 | 太平興國六年 ↔ Thái Bình Hưng Quốc 6 (981) | 2.009 | 2.509 | 29 / 32 | 1,25 |
| Q15 | 端拱二年 ↔ Đoan Củng 2 (989) | 2.974 | 3.474 | 23 / 50 | 1,17 |
| Q15 | 淳化元年 ↔ Thuần Hóa 1 (990) | 1.854 | 2.120 | 39 / 46 | 1,14 |
| Q15 | 淳化二年 ↔ Thuần Hóa 2 (991) | 2.098 | 2.584 | 37 / 37 | 1,23 |
| Q20 | Mở đầu 帝名恒… ↔ Chân Tông… húy là Hằng | 166 | 217 | 1 / 1 | 1,31 |
| Q20 | 咸平元年 ↔ Hàm Bình 1 (998) | 3.983 | 4.846 | 72 / 72 | 1,22 |
| Q20 | 咸平二年 ↔ Hàm Bình 2 (999) | 2.191 | 2.697 | 31 / 31 | 1,23 |

Q2 còn có dòng mở đầu 太祖啟運… ↔ Thái Tổ Khải Vận… (20 chữ / 20 âm tiết). Q10 bản Việt có dòng miếu hiệu đứng riêng, còn bản Hán đặt miếu hiệu trong đề mục.

#### HCB_04

Toàn văn: 1.717 chữ Hán, 1.973 âm tiết Việt, r = 1,15. Có 8 đoạn Hán và 9 đoạn Việt, do bản Việt tách đoạn đầu làm 2.

| Vị trí | Hán | Việt |
|---|---|---|
| Đầu | 陛下臨天下，布德施惠 | Bệ hạ thống trị thiên hạ, ban bố đức huệ |
| Giữa | 不習南方地形者，多以越為人衆兵彊 | Kẻ không quen địa hình phương Nam thường cho rằng người Việt đông, binh mạnh |
| Cuối | 臣安竊恐將吏之以十萬之師為一使之任也！ | Thần An trộm e tướng lại lấy mười vạn quân để làm thay công việc của một sứ giả vậy! |

#### HCB_05

| Vị trí | Hán | Việt |
|---|---|---|
| Đầu | 糠頭山在合浦海口傳云越王舂米於此積糠所成 | Núi Khang Đầu 糠頭 ở cửa biển Hợp Phố 合浦, truyền rằng Việt Vương giã gạo ở đây, tích tụ thành núi. |
| Giữa | 豆蔻似杬樹味辛 | Cây đậu khấu 豆蔻 giống cây viên 杬樹, vị cay |
| Cuối | 姚文咸交州記曰尉佗作朝殿以朝天子 | Điện triều kiến của Triệu Đà được ông xây dựng để làm lễ triều kiến thiên tử. |

Khoản đếm theo dấu đầu dòng; bản Việt đặt lệch dấu vài dòng so với bản Hán.

| Phần Hán ↔ Việt | Chữ Hán | Âm tiết Việt | Khoản + ghi chú (Hán) | Khoản + ghi chú (Việt) | r |
|---|---|---|---|---|---|
| 交洲記卷一 ↔ Quyển 1 | 1.222 | 1.452 | 37 + 11 | 38 + 12 | 1,19 |
| 交州記卷二 ↔ Quyển 2 | 877 | 1.109 | 33 + 6 | 33 + 5 | 1,26 |
| 附 ↔ Phụ chú | 38 | 42 | 2 | 2 | 1,11 |

#### HCB_07

232/234 mốc chữ Hán trong bản Việt tìm thấy ở bản Hán.

| Vị trí | Hán | Việt |
|---|---|---|
| Đầu | 南夷君長以十數，夜郎最大。 | Thủ lĩnh Nam Di có hàng chục người, Dạ Lang (夜郎) lớn nhất. |
| Giữa | 元鼎五年秋，衞尉路博多爲伏波將軍 | Mùa thu năm Nguyên Đỉnh thứ 5 (112 TCN), Vệ úy Lộ Bác Đa (路博多) làm Phục Ba tướng quân |
| Cuối | 贊曰：楚、粵之先，暦世有土。 | Tiên tổ của Sở và Việt trải qua nhiều đời đều có đất đai. |

| Mục Hán ↔ Việt | Chữ Hán | Âm tiết Việt | Đoạn Hán / Việt | r |
|---|---|---|---|---|
| 西南夷 ↔ Tây Nam Di | 2.308 | 2.545 | 10 / 10 | 1,10 |
| 南粵·武王趙佗 ↔ Nam Việt·Vũ Vương Triệu Đà | 1.408 | 1.606 | 6 / 8 | 1,14 |
| 文王趙胡 ↔ Văn Vương Triệu Hồ | 243 | 305 | 2 / 2 | 1,26 |
| 明王趙嬰齊 ↔ Minh Vương Triệu Anh Tề | 93 | 124 | 1 / 1 | 1,33 |
| 哀王趙興 ↔ Ai Vương Triệu Hưng | 828 | 968 | 3 / 3 | 1,17 |
| 術陽侯趙建德 ↔ Thuật Dương hầu Triệu Kiến Đức | 290 | 362 | 2 / 2 | 1,25 |
| 蒼梧王趙光 ↔ Thương Ngô vương Triệu Quang | 141 | 180 | 2 / 2 | 1,28 |
| 閩粵、東甌 ↔ Mân Việt, Đông Âu | 1.042 | 1.272 | 9 / 9 | 1,22 |
| 朝鮮 ↔ Triều Tiên | 1.089 | 1.356 | 8 / 8 | 1,25 |
| 贊 ↔ Lời bàn | 132 | 185 | 1 / 2 | 1,40 |

#### HCB_11

456/459 mốc chữ Hán trong bản Việt tìm thấy ở bản Hán.

| Vị trí | Hán | Việt |
|---|---|---|
| Đầu | 昔高辛氏有犬戎之寇 | Xưa thời Cao Tân Thị (高辛氏) có giặc Khuyển Nhung (犬戎) quấy nhiễu |
| Giữa | 肅宗元和中，蜀郡王追爲太守 | Thời Túc Tông (肅宗), niên hiệu Nguyên Hòa (元和), Vương Truy (王追) người Thục Quận làm Thái thú |
| Cuối | 贊曰：百蠻蠢居，仞彼方徼。 | Tán rằng: Trăm giống Man sống hỗn tạp, chiếm giữ nơi biên giới phương xa. |

| Mục Hán ↔ Việt | Chữ Hán | Âm tiết Việt | Đoạn Hán / Việt | r |
|---|---|---|---|---|
| 南蠻 ↔ Nam Man | 4.646 | 4.145 | 25 / 25 | **0,89** |
| 西南夷 ↔ Tây Nam Di | 434 | 519 | 3 / 3 | 1,20 |
| 滇王 ↔ Điền vương | 599 | 693 | 4 / 4 | 1,16 |
| 哀牢夷 ↔ Ai Lao di | 1.028 | 1.019 | 7 / 7 | 0,99 |
| 邛都夷 ↔ Cung Đô di | 688 | 697 | 4 / 4 | 1,01 |
| 莋都夷 ↔ Tác Đô di | 971 | 1.045 | 10 / 11 | 1,08 |
| 冉駹夷 ↔ Nhiễm Máng di | 274 | 325 | 2 / 2 | 1,19 |
| 白馬氐 ↔ Bạch Mã Đê | 225 | 273 | 2 / 2 | 1,21 |
| 論 ↔ Bình luận | 300 | 379 | 1 / 1 | 1,26 |
| 贊 ↔ Tán thán | 50 | 94 | 1 / 1 | 1,88 |

Hai mục 哀牢夷 và 邛都夷 có r≈1,0, thấp hơn mức thường gặp nhưng không có đoạn nào dưới ngưỡng; nên soát kỹ hơn khi dóng. Mục 贊 có r cao do thể văn, không phải lỗi.

#### HCB_13

| Vị trí | Hán | Việt |
|---|---|---|
| Đầu | 交阯，本漢初南越之地 | Giao Chỉ 交趾, đầu thời Hán vốn là đất Nam Việt 南越 |
| Giữa | 四年，龍廷稱權安南靜海軍留後，遣弟峯州刺史明昶 | Năm thứ 4 (1007), Long Đình xưng Quyền An Nam Tĩnh Hải quân Lưu hậu, sai em là Thứ sử Phong Châu Minh Sưởng |
| Cuối mục 交趾 | 八年，明堂禮成，日煚、威晃各加食邑，賜鞍馬等物。 | Năm thứ 8 (1272), lễ Minh Đường 明堂禮 hoàn thành… ban ngựa yên và các vật phẩm. |

Từ "Đại Lý" trong thân bài Việt chỉ xuất hiện ở một chỗ, khi nói về Triệu Trí Chi. Một đoạn Hán dài ứng với nhiều đoạn Việt ngắn; bảng dưới là dóng thô theo độ dài, đoạn đánh số từ 0.

| Đoạn Hán | Mở đầu bản Hán | Đoạn Việt | Mở đầu bản Việt | Chữ Hán | Âm tiết Việt | r |
|---|---|---|---|---|---|---|
| H00 | 交阯，本漢初南越之地 | V000–006 | Giao Chỉ 交趾, đầu thời Hán… | 182 | 217 | 1,19 |
| H01 | 乾德初，昌文死 | V007–011 | Đầu niên hiệu Càn Đức… | 338 | 381 | 1,13 |
| H02 | 太宗即位，璉又遣使 | V012–018 | Tống Thái Tông vừa lên ngôi… | 448 | 514 | 1,15 |
| H03 | 七年春，桓懼朝廷 | V019–020 | Năm thứ 7 mùa xuân… | 285 | 325 | 1,14 |
| H04 | 雍熙二年 | V021–023 | Năm Ung Hi thứ 2 (985) | 325 | 374 | 1,15 |
| H05 | 端拱元年 | V024–025 | Năm Đoan Củng nguyên niên (988) | 103 | 91 | 0,88 |
| H06–H09 | 去歲秋末抵交州境 (4 đoạn trích) | V026–034 | Năm sau (991), tháng 6… | 560 | 585 | 1,04 |
| H10 | 四年，進封桓交阯郡王 | V035–038 | Năm thứ 4 (993) | 250 | 310 | 1,24 |
| H11 | 先是，欽州如洪 | V039–045 | Trước đó, ba trấn ở Khâm Châu… | 477 | 520 | 1,09 |
| H12 | 真宗即位 | V046–049 | Chân Tông lên ngôi… | 288 | 347 | 1,20 |
| H13 | 三年，桓卒 | V050–053 | Năm thứ 3 (1006) | 276 | 320 | 1,16 |
| H14 | 四年，龍廷稱權 | V054–058 | Năm thứ 4 (1007) | 428 | 456 | 1,07 |
| H15 | 至忠纔年二十六 | V059–065 | Năm thứ 4 (1011), Chí Trung… | 604 | 642 | 1,06 |
| H16 | 其子德政自稱權知留後事 | V066–071 | Con của Lý Công Uẩn là Đức Chính… | 400 | 431 | 1,08 |
| H17 | 初，德政發兵取占城 | V072–074 | Ban đầu, Đức Chính phát binh… | 143 | 176 | 1,23 |
| H18 | 其子日尊遣人告哀 | V075–080 | Con của Đức Chính là Nhật Tôn… | 491 | 556 | 1,13 |
| H19 | 五年三月，日尊卒 | V081–082 | Năm thứ 5, tháng 3 (1072) | 278 | 312 | 1,12 |
| H20 | 元豐五年 | V083–086 | Năm Nguyên Phong thứ 5 (1082) | 296 | 338 | 1,14 |
| H21 | 紹興二年，乾德卒 | V087–094 | Năm Thiệu Hưng thứ 2 (1132) | 453 | 526 | 1,16 |
| H22 | 明年，子龍𣉙嗣位 | V095–097 | Năm sau (1177), con là Long Trát… | 168 | 193 | 1,15 |
| H23 | 嘉定五年，龍𣉙卒 | V098 | Năm Gia Định thứ 5 (1212) | 68 | 80 | 1,18 |
| H24 | 昊旵卒，無子 | V099–104 | Hạo Sảm mất, không có con… | 196 | 231 | 1,18 |
| **大理** | 大理國，即唐南詔也 (6 đoạn) | **không có** | — | 601 | 0 | — |

#### HCB_14

| Vị trí | Hán | Việt |
|---|---|---|
| Đầu (1333) | ○諭曰、福康安等奏、阮惠即阮光平。 | Dụ rằng: Phúc Khang An (福康安) tấu: Nguyễn Huệ tức Nguyễn Quang Bình (阮惠即阮光平) |
| Giữa (1339) | ○又諭曰、福康安奏、黎維祁之弟黎維祇、潛匿安南保樂地方。 | Lại dụ rằng: Phúc Khang An tâu, em của Lê Duy Kỳ là Lê Duy Chỉ 潛匿 ở địa phương Bảo Lạc 保樂 của An Nam |
| Cuối (1438) | 不必再行懇請也。 | không cần tiếp tục khẩn cầu nữa. |

Trong bản Việt, 3 bài của quyển 1333 và 2 bài của quyển 1339 nằm chung dưới một đề mục ngày, nên phải tách theo ranh giới ghi ở bảng dưới.

| Quyển | Ngày (Càn Long) | Đuôi mã bài sillok | Phần Việt tương ứng | Chữ Hán | Âm tiết Việt | r |
|---|---|---|---|---|---|---|
| 1333 | 54/6/22 | `…0060_0030` | "Dụ rằng: Phúc Khang An…" đến "…quy phục giáo hóa vậy." | 536 | 495 | 0,92 |
| 1333 | 54/6/22 | `…0060_0040` | "Chiếu dụ cho An Nam Nguyễn Quang Bình…" | 323 | 311 | 0,96 |
| 1333 | 54/6/22 | `…0060_0050` | "Sách phong Nguyễn Quang Bình…" | 391 | 373 | 0,95 |
| 1339 | 54/9/23 | `…0080_0040` | "Lại dụ rằng: Phúc Khang An… Tôn Vĩnh Thanh…" | 209 | 224 | 1,07 |
| 1339 | 54/9/23 | `…0080_0050` | "Lại dụ rằng: Phúc Khang An tâu, em của Lê Duy Kỳ…" | 421 | 427 | 1,01 |
| 1357 | 55/6/25 | `…0090_0020` | "Lại dụ rằng: Phúc Khang An… tâu rằng, việc cung ứng…" | 511 | 562 | 1,10 |
| 1357 | 55/6/27 | `…0110_0030` | "Lại dụ rằng: Quốc vương An Nam…" | 287 | 310 | 1,08 |
| 1438 | 58/10/3 | `…0020_0070` | "Lại dụ rằng: Trần Dụng Phu tâu…" | 231 | 228 | 0,99 |

### 3.3. Phương pháp và giới hạn

**Đã làm:**
- Đối chiếu từng tệp với manifest (SHA-256, kích thước) và với máy chủ nguồn (`sha1` từng phiên bản, tải lại bài sillok).
- Đo từng trang PDF: số ký tự, ảnh, trang trùng.
- So chuỗi can chi (HCB_01) và mốc chữ Hán (HCB_05, 07, 11, 13) giữa hai bản.
- Dóng thô theo độ dài đoạn để tìm chỗ bất thường, rồi đọc lại bằng mắt những chỗ quan trọng. Nhờ vậy đã loại 3 cảnh báo sai: can chi Q2, đoạn Q6, đoạn Q15.

**Chưa làm:**
- Không đánh giá chất lượng dịch từng câu. Lỗi dịch ghi ở đây chỉ là những lỗi bắt gặp khi đọc.
- Với HCB_01, HCB_07, HCB_11 và HCB_13, tôi chỉ đọc mẫu và những chỗ bất thường, không đọc toàn văn. Có thể vẫn còn câu bị lược lẻ tẻ chưa phát hiện.
- Không tải lại PDF, vì PDF sinh lại có thể khác byte. PDF được kiểm tra qua `oldid` và độ phủ nội dung.
- Không so Wikisource với bản in gốc. Lỗi có sẵn trên Wikisource (như mã `[BD77]`) không phải lỗi tải.
- Các số chữ, âm tiết, câu chỉ để đo đạc, chưa qua làm sạch Bước 5, nên có thể lệch nhẹ so với số cuối.
