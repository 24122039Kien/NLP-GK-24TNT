# Check – Bước 1 và Bước 2 (Phần phân công: Đăng – Người 4)

Kiểm tra ngày 2026-11-04, trên bộ dữ liệu phân công của **Người 4 (15 quyển)** ([nguon_manifest.tsv](nguon_manifest.tsv)).

**Cách đọc file này:**
- **Tóm tắt:** kết quả chung của 15 quyển được giao và những việc cần xác nhận với nhóm.
- **Phần 1:** thông tin từng tác phẩm/quyển để điền vào docs nhóm.
- **Phần 2:** việc cần xử lý ở các bước sau (đặc biệt lưu ý `HCB_10` và `HCB_14`).
- **Phần 3:** bằng chứng kiểm tra (mẫu đầu – giữa – cuối và bảng ánh xạ cấu trúc), chỉ cần xem khi muốn đối chiếu lại.

---

## Tóm tắt

**Cả 3 tác phẩm (15 quyển) đều dùng được và không cần OCR**, vì tất cả tài liệu đều là nguồn trực tuyến có sẵn lớp text (`.wikitext` / `.html` và `.pdf` xuất từ web).

| Mã | Tác phẩm | Phạm vi (15 quyển của Người 4) | Hai bản Hán–Việt | Lưu ý quan trọng |
|---|---|---|---|---|
| HCB_01 | Tục tư trị thông giám | Quyển 4, 9, 12, 13, 14, 18 *(6 quyển)* | Khớp hoàn toàn | Không (nguồn chủ lực lấy cặp câu) |
| HCB_10 | Hậu Hán thư | Quyển 81 *(1 quyển)* | **Khớp một phần (Rất ngắn)** | **Bản Việt mới chỉ dịch Lời tựa, truyện Lý Thiện và Lời bàn (Tán)**; thiếu 23/24 nhân vật còn lại của Độc hành liệt truyện |
| HCB_14 | Thanh thực lục (Cao Tông) | Quyển 1328, 1331, 1346, 1359, 1384, 1420, 1428, 1463 *(8 quyển)* | Khớp, chỉ là trích đoạn | Mỗi quyển chỉ trích dịch các bài (dụ/tấu) liên quan đến An Nam; **Q1384 bản Việt ghi nhầm tiêu đề thành `quyển 1381`** |

**Số cặp ước tính:** Tổng cộng tối đa khoảng **2.560 cặp** nếu dóng theo câu (riêng 6 quyển `HCB_01` đã cung cấp khoảng ~2.290 cặp, dư sức gánh chỉ tiêu cá nhân 2.000 cặp). Cần giữ được ít nhất **78%** tổng số câu ước tính để đạt mốc 2.000 cặp hợp lệ.

### Việc cần bạn xác nhận

1. **Phạm vi thực tế của `HCB_10` (Hậu Hán thư – Quyển 81):** Bản Hán (`後漢書/卷81`) gồm Lời tựa + 24 tiểu truyện nhân vật + Lời bàn (khoảng 7.450 chữ Hán). Tuy nhiên, trang `Biên_dịch:Hậu_Hán_thư/Quyển_81` trên Wikisource tiếng Việt hiện **chỉ có phần Mở đầu (Lời tựa), mục `Lý Thiện` (李善) và mục `Lời bàn` (贊曰)** (khoảng 615 chữ Hán). Đề xuất chỉ cắt đúng 3 phần này ở bản Hán để dóng hàng, loại bỏ 23 truyện chưa dịch để tránh lỗi `MISSING`.
2. **Quyển dư trong phân công (15 quyển, có 1 quyển dư):** Nhóm trưởng ghi chú phần của Đăng có *"15 quyển, có 1 quyển dư"*. Cần xác nhận xem quyển dư này nằm ở `HCB_01` hay `HCB_14` để tránh làm trùng với thành viên khác, hoặc giữ nguyên cả 15 quyển để bù số câu bị thiếu hụt từ `HCB_10`.
3. **Cách xử lý chú thích và thơ ngự chế:** Cả nhóm cần thống nhất cách xử lý chữ Hán chèn trong ngoặc đơn `( )`, chữ giản thể lẫn trong `HCB_10` và các phần *Phiên âm / Dịch thơ* trong `HCB_14` trước Bước 5 (chi tiết ở mục 2.2).

---

## Phần 1 – Thông tin để điền docs

Tất cả các tệp PDF và text gốc (`.wikitext`, `.html`) đều rõ nét, không thiếu trang và không trùng trang. Mỗi tài liệu gồm 2 tệp cùng nội dung: PDF và bản text gốc.

### HCB_01 – Tục tư trị thông giám

**Bước 1 – Xác nhận phạm vi**

| Mục | Nội dung |
|---|---|
| Mã đề tài / tác phẩm | CV02 / HCB_01 |
| Tác phẩm | Tục tư trị thông giám / 續資治通鑑 |
| Tác giả | Tất Nguyên 畢沅 (Cơ Như Tuyết dịch) |
| Phạm vi được giao | Quyển 4, 9, 12, 13, 14, 18 |
| Nguồn | Việt: vi.wikisource; Hán: zh.wikisource |
| Định dạng | PDF Text + Text (wikitext) |
| Hai bản cùng phạm vi? | **Khớp.** Mốc thời gian trong đầu đề hai bản trùng nhau ở cả 6 quyển; toàn bộ các mốc ngày can chi của bản Hán đều có mặt ở bản Việt theo đúng thứ tự. |

**Bước 2 – Kiểm kê nguồn**

*Quyển 4*

| Trường | Bản Việt | Bản Hán |
|---|---|---|
| Tên tài liệu | Tục Tư trị thông giám, quyển 4 (Tất Nguyên; Cơ Như Tuyết dịch) | 續資治通鑑 卷第四 (畢沅) |
| Ngôn ngữ | Việt | Hán |
| Link nguồn | https://vi.wikisource.org/wiki/Tục_tư_trị_thông_giám/Quyển_4 | https://zh.wikisource.org/wiki/續資治通鑑/卷004 |
| Tên tệp | `Tục_tư_trị_thông_giám_Quyển_4` (`.pdf`, `.wikitext`) | `續資治通鑑_卷004` (`.pdf`, `.wikitext`) |
| Số trang | 16 trang; nội dung: p1–16 | 12 trang; nội dung: p1–11 |
| Định dạng | PDF Text + Text (wikitext) | PDF Text + Text (wikitext) |
| Phạm vi | Tống kỷ 4; 4/964–12/966 (Càn Đức 2–4) | Tống kỷ 4; 4/964–12/966 (Càn Đức 2–4) |
| Ghi chú | Có dòng miếu hiệu Thái Tổ ở đầu bài | p12 là giấy phép và chú thích |

*Quyển 9*

| Trường | Bản Việt | Bản Hán |
|---|---|---|
| Tên tài liệu | Tục Tư trị thông giám, quyển 9 (Tất Nguyên; Cơ Như Tuyết dịch) | 續資治通鑑 卷第九 (畢沅) |
| Ngôn ngữ | Việt | Hán |
| Link nguồn | https://vi.wikisource.org/wiki/Tục_tư_trị_thông_giám/Quyển_9 | https://zh.wikisource.org/wiki/續資治通鑑/卷009 |
| Tên tệp | `Tục_tư_trị_thông_giám_Quyển_9` (`.pdf`, `.wikitext`) | `續資治通鑑_卷009` (`.pdf`, `.wikitext`) |
| Số trang | 15 trang; nội dung: p1–15 | 11 trang; nội dung: p1–10 |
| Định dạng | PDF Text + Text (wikitext) | PDF Text + Text (wikitext) |
| Phạm vi | Tống kỷ 9; 12/976–2/979 (Thái Bình Hưng Quốc 1–4) | Tống kỷ 9; 12/976–2/979 (Thái Bình Hưng Quốc 1–4) |
| Ghi chú | Mở đầu triều Tống Thái Tông (có đoạn giới thiệu tên húy) | p11 là giấy phép và chú thích |

*Quyển 12*

| Trường | Bản Việt | Bản Hán |
|---|---|---|
| Tên tài liệu | Tục Tư trị thông giám, quyển 12 (Tất Nguyên; Cơ Như Tuyết dịch) | 續資治通鑑 第十二卷 (畢沅) |
| Ngôn ngữ | Việt | Hán |
| Link nguồn | https://vi.wikisource.org/wiki/Tục_tư_trị_thông_giám/Quyển_12 | https://zh.wikisource.org/wiki/續資治通鑑/卷012 |
| Tên tệp | `Tục_tư_trị_thông_giám_Quyển_12` (`.pdf`, `.wikitext`) | `續資治通鑑_卷012` (`.pdf`, `.wikitext`) |
| Số trang | 15 trang; nội dung: p1–15 | 11 trang; nội dung: p1–10 |
| Định dạng | PDF Text + Text (wikitext) | PDF Text + Text (wikitext) |
| Phạm vi | Tống kỷ 12; 10/983–12/985 (Thái Bình Hưng Quốc 8–Ung Hy 2) | Tống kỷ 12; 10/983–12/985 (Thái Bình Hưng Quốc 8–Ung Hy 2) |
| Ghi chú | Không có | p11 là giấy phép và chú thích |

*Quyển 13*

| Trường | Bản Việt | Bản Hán |
|---|---|---|
| Tên tài liệu | Tục Tư trị thông giám, quyển 13 (Tất Nguyên; Cơ Như Tuyết dịch) | 續資治通鑑 第十三卷 (畢沅) |
| Ngôn ngữ | Việt | Hán |
| Link nguồn | https://vi.wikisource.org/wiki/Tục_tư_trị_thông_giám/Quyển_13 | https://zh.wikisource.org/wiki/續資治通鑑/卷013 |
| Tên tệp | `Tục_tư_trị_thông_giám_Quyển_13` (`.pdf`, `.wikitext`) | `續資治通鑑_卷013` (`.pdf`, `.wikitext`) |
| Số trang | 14 trang; nội dung: p1–14 | 10 trang; nội dung: p1–9 |
| Định dạng | PDF Text + Text (wikitext) | PDF Text + Text (wikitext) |
| Phạm vi | Tống kỷ 13; 1/986–12/987 (Ung Hy 3–4) | Tống kỷ 13; 1/986–12/987 (Ung Hy 3–4) |
| Ghi chú | Đề mục năm 987 ở bản Việt ghi nhầm là *"Năm Ung Hy thứ 2"* (đúng là thứ 4, nhưng năm CN 987 và nội dung khớp hoàn toàn) | p10 là giấy phép và chú thích |

*Quyển 14*

| Trường | Bản Việt | Bản Hán |
|---|---|---|
| Tên tài liệu | Tục Tư trị thông giám, quyển 14 (Tất Nguyên; Cơ Như Tuyết dịch) | 續資治通鑑 第十四卷 (畢沅) |
| Ngôn ngữ | Việt | Hán |
| Link nguồn | https://vi.wikisource.org/wiki/Tục_tư_trị_thông_giám/Quyển_14 | https://zh.wikisource.org/wiki/續資治通鑑/卷014 |
| Tên tệp | `Tục_tư_trị_thông_giám_Quyển_14` (`.pdf`, `.wikitext`) | `續資治通鑑_卷014` (`.pdf`, `.wikitext`) |
| Số trang | 12 trang; nội dung: p1–12 | 9 trang; nội dung: p1–8 |
| Định dạng | PDF Text + Text (wikitext) | PDF Text + Text (wikitext) |
| Phạm vi | Tống kỷ 14; 1/988–3/989 (Đoan Củng 1–2) | Tống kỷ 14; 1/988–3/989 (Đoan Củng 1–2) |
| Ghi chú | Không có | p9 là giấy phép và chú thích |

*Quyển 18*

| Trường | Bản Việt | Bản Hán |
|---|---|---|
| Tên tài liệu | Tục Tư trị thông giám, quyển 18 (Tất Nguyên; Cơ Như Tuyết dịch) | 續資治通鑑 第十八卷 (畢沅) |
| Ngôn ngữ | Việt | Hán |
| Link nguồn | https://vi.wikisource.org/wiki/Tục_tư_trị_thông_giám/Quyển_18 | https://zh.wikisource.org/wiki/續資治通鑑/卷018 |
| Tên tệp | `Tục_tư_trị_thông_giám_Quyển_18` (`.pdf`, `.wikitext`) | `續資治通鑑_卷018` (`.pdf`, `.wikitext`) |
| Số trang | 14 trang; nội dung: p1–14 | 10 trang; nội dung: p1–9 |
| Định dạng | PDF Text + Text (wikitext) | PDF Text + Text (wikitext) |
| Phạm vi | Tống kỷ 18; 7/994–6/996 (Thuần Hóa 5–Chí Đạo 2) | Tống kỷ 18; 7/994–6/996 (Thuần Hóa 5–Chí Đạo 2) |
| Ghi chú | Không có | p10 là giấy phép và chú thích |

---

### HCB_10 – Hậu Hán thư

> **Lưu ý đặc biệt:** Bản Việt trên Wikisource chỉ mới dịch **Lời tựa (Mở đầu)**, truyện **Lý Thiện (李善)** và **Lời bàn (贊曰)**. Toàn bộ 23 nhân vật khác của *Độc hành liệt truyện* (như Tiếu Huyền, Phí Di, Lý Nghiệp, Lưu Mậu, Ôn Tự, Bành Tu, Phạm Thức, Đới Phong, Trần Trọng, Lôi Nghĩa...) đều **chưa có bản dịch tiếng Việt** (xem chi tiết mục 2.1).

**Bước 1 – Xác nhận phạm vi**

| Mục | Nội dung |
|---|---|
| Mã đề tài / tác phẩm | CV02 / HCB_10 |
| Tác phẩm | Hậu Hán thư / 後漢書 |
| Tác giả | Phạm Diệp 范曄 |
| Phạm vi được giao | Quyển 81 (đề xuất chỉ dùng 3 mục đã dịch: Mở đầu + Lý Thiện + Lời bàn) |
| Nguồn | Việt: vi.wikisource; Hán: zh.wikisource |
| Định dạng | PDF Text + Text (wikitext) |
| Hai bản cùng phạm vi? | **Khớp một phần (khoảng 8,2% quyển).** Ba mục có mặt trong bản Việt khớp hoàn toàn từng câu với bản Hán; 23 mục nhân vật còn lại (khoảng 6.835 chữ Hán) không có bản dịch. |

**Bước 2 – Kiểm kê nguồn**

| Trường | Bản Việt | Bản Hán |
|---|---|---|
| Tên tài liệu | Hậu Hán thư, quyển 81 – Độc hành liệt truyện thứ 71 (Phạm Diệp; bản biên dịch Wikisource) | 後漢書 卷八十一 獨行列傳第七十一 (范曄) |
| Ngôn ngữ | Việt | Hán |
| Link nguồn | https://vi.wikisource.org/wiki/Biên_dịch:Hậu_Hán_thư/Quyển_81 | https://zh.wikisource.org/wiki/後漢書/卷81 |
| Tên tệp | `Biên_dịch_Hậu_Hán_thư_Quyển_81` (`.pdf`, `.wikitext`) | `後漢書_卷81` (`.pdf`, `.wikitext`) |
| Số trang | 3 trang; nội dung: p1–2 | 9 trang; nội dung: p1–8 |
| Định dạng | PDF Text + Text (wikitext) | PDF Text + Text (wikitext) |
| Phạm vi | Chỉ gồm: Lời tựa, Lý Thiện, Lời bàn (Tán) | Toàn quyển (Lời tựa + 24 truyện nhân vật + Lời bàn); chỉ lấy phần tương ứng bản Việt |
| Ghi chú | p3 chỉ có giấy phép. Chú chữ Hán trong ngoặc dùng **chữ Hán giản thể** như `(独行篇)`, `(次孙)`, `(钟离意)` | p9 chỉ có giấy phép và link |

---

### HCB_14 – Thanh thực lục

> **Lưu ý:** Tương tự các quyển `HCB_14` của thành viên khác, bản Việt trên Wikisource chỉ trích dịch các bài (chỉ dụ, tấu sớ, thơ ngự chế) có liên quan đến An Nam (Tây Sơn – Nguyễn Quang Bình / Nguyễn Quang Toản và nhà Lê) trong 8 quyển được giao.

**Bước 1 – Xác nhận phạm vi**

| Mục | Nội dung |
|---|---|
| Mã đề tài / tác phẩm | CV02 / HCB_14 |
| Tác phẩm | Thanh thực lục – Cao Tông Thuần Hoàng đế thực lục / 清實錄·高宗純皇帝實錄 |
| Tác giả | Quốc sử quán triều Thanh (trang nguồn không ghi) |
| Phạm vi được giao | Quyển 1328, 1331, 1346, 1359, 1384, 1420, 1428, 1463 *(8 quyển)* |
| Nguồn | Việt: vi.wikisource; Hán: sillok.history.go.kr (hoặc wikisource/ctext đối chiếu) |
| Định dạng | PDF Text + Text (`.wikitext` cho bản Việt; `.html` cho bản Hán) |
| Hai bản cùng phạm vi? | **Khớp theo từng bài trích dịch.** Ngày tháng Càn Long và nội dung các bài dịch ở cả 8 quyển đều khớp với nguyên bản chữ Hán. |

**Bước 2 – Kiểm kê nguồn**

Thông tin chung của các tệp bản Hán (`sillok.history.go.kr`):
- Ngôn ngữ: Hán (`高宗純皇帝實錄`).
- Số trang: mỗi bài 2 trang; nội dung chính ở p1, p2 là chân trang tiếng Hàn.
- Định dạng: PDF Text + Text (HTML).
- Ghi chú: Thân bài bản Hán có ngắt dòng ở tên người và chỗ đài chữ (nâng chữ `天`, `祖`...).

Bảng kiểm kê 8 quyển bản Việt và đối chiếu phạm vi bản Hán tương ứng:

| Quyển | Link nguồn bản Việt (`vi.wikisource.org/wiki/...`) | Tên tệp bản Việt (`.pdf`, `.wikitext`) | Số trang Việt | Phạm vi niên hiệu Càn Long & Nội dung trích dịch | Ghi chú riêng |
|---|---|---|---|---|---|
| **1328** | `Biên_dịch:Thanh_thực_lục/Cao_Tông_Thuần_Hoàng_đế_thực_lục/Quyển_1328` | `Biên_dịch_..._Quyển_1328` | 2–3 trang | Càn Long 54, tháng 5 (1789) – Dụ cho Phúc Khang An về việc Nguyễn Huệ (Nguyễn Quang Bình) xin hàng và cống biểu | Khớp với mục bài tương ứng trong `卷1328` (`qsilok_007_1328_...`) |
| **1331** | `Biên_dịch:Thanh_thực_lục/Cao_Tông_Thuần_Hoàng_đế_thực_lục/Quyển_1331` | `Biên_dịch_..._Quyển_1331` | 2 trang | Càn Long 54, tháng 5 nhuận (1789) – Dụ về việc xử lý thuộc hạ nhà Lê và việc của Nguyễn Quang Bình | Khớp với mục bài tương ứng trong `卷1331` (`qsilok_007_1331_...`) |
| **1346** | `Biên_dịch:Thanh_thực_lục/Cao_Tông_Thuần_Hoàng_đế_thực_lục/Quyển_1346` | `Biên_dịch_..._Quyển_1346` | 2 trang | Càn Long 55, tháng 1, ngày 1 (1790) – Dụ nhân dịp Bát tuần Vạn thọ (80 tuổi) và việc Quốc vương An Nam vào triều chúc thọ | Khớp với mục bài tương ứng trong `卷1346` (`qsilok_007_1346_...`) |
| **1359** | `Biên_dịch:Thanh_thực_lục/Cao_Tông_Thuần_Hoàng_đế_thực_lục/Quyển_1359` | `Biên_dịch_..._Quyển_1359` | 3 trang | Càn Long 55, tháng 7, ngày 16 (1790) – Nguyễn Quang Bình đến Nhiệt Hà triều kiến, ban yến và thơ ngự chế | Có kèm thơ chữ Hán, Phiên âm, Dịch nghĩa, Dịch thơ (xem mục 2.2) |
| **1384** | `Biên_dịch:Thanh_thực_lục/Cao_Tông_Thuần_Hoàng_đế_thực_lục/Quyển_1384` | `Biên_dịch_..._Quyển_1384` | 2 trang | Càn Long 56, tháng 8 (1791) – Dụ liên quan đến tình hình An Nam / Nguyễn Quang Bình | **Lỗi tiêu đề trên Wikisource Việt:** Dòng breadcrumb trong bài ghi nhầm là `Cao Tông Thuần Hoàng Đế thực lục / quyển 1381`, nhưng URL và nội dung đúng là của Quyển 1384 |
| **1420** | `Biên_dịch:Thanh_thực_lục/Cao_Tông_Thuần_Hoàng_đế_thực_lục/Quyển_1420` | `Biên_dịch_..._Quyển_1420` | 2 trang | Càn Long 58, tháng 1 (1793) – Dụ về việc tang của Nguyễn Quang Bình và việc thế tử Nguyễn Quang Toản | Khớp với mục bài tương ứng trong `卷1420` (`qsilok_007_1420_...`) |
| **1428** | `Biên_dịch:Thanh_thực_lục/Cao_Tông_Thuần_Hoàng_đế_thực_lục/Quyển_1428` | `Biên_dịch_..._Quyển_1428` | 2 trang | Càn Long 58, tháng 5 (1793) – Dụ về việc sắc phong và ban thưởng cho Quốc vương An Nam Nguyễn Quang Toản | Khớp với mục bài tương ứng trong `卷1428` (`qsilok_007_1428_...`) |
| **1463** | `Biên_dịch:Thanh_thực_lục/Cao_Tông_Thuần_Hoàng_đế_thực_lục/Quyển_1463` | `Biên_dịch_..._Quyển_1463` | 2 trang | Càn Long 59, tháng 10 (1794) – Dụ về biểu tâu và cống phẩm của An Nam | Khớp với mục bài tương ứng trong `卷1463` (`qsilok_007_1463_...`) |

---

## Phần 2 – Việc cần xử lý ở các bước sau

### 2.1. HCB_10 (Hậu Hán thư – Quyển 81): Bản Việt chỉ dịch 1/24 nhân vật

Qua kiểm tra đối chiếu giữa `vi.wikisource` và `zh.wikisource`, Quyển 81 (*Độc hành liệt truyện*) trên trang tiếng Việt hiện chỉ có 3 phần:

| Phần trong Quyển 81 | Mở đầu bản Hán | Mở đầu bản Việt | Chữ Hán / Âm tiết Việt | Trạng thái |
|---|---|---|---|---|
| **Lời tựa (Mở đầu)** | 孔子曰：「與其不得中庸，必也狂狷乎！」 | Khổng Tử (孔子) nói: Thà rằng không đắc được đạo Trung dung, tất phải tìm người Cuồng, Quyến vậy! | 184 / 242 | **Đầy đủ (Dùng)** |
| *7 truyện đầu (Tiếu Huyền → Phạm Thức)* | 譙玄字君黃，巴郡閬中人也… | *(Không có)* | ~2.650 / 0 | **Chưa dịch (Loại bỏ)** |
| **Truyện Lý Thiện (李善)** | 李善字次孫，南陽淯陽人也，本同縣李元蒼頭也。 | Lý Thiện (李善) tự Thứ Tôn (次孙), người Dục Dương (淯阳) Nam Dương (南阳)… | 399 / 468 | **Đầy đủ (Dùng)** |
| *16 truyện sau (Vương Thuần → Lôi Nghĩa + Luận)* | 王忳字少林，廣漢新都人也… | *(Không có)* | ~4.185 / 0 | **Chưa dịch (Loại bỏ)** |
| **Lời bàn (贊曰)** | 贊曰：守死善道，義不苟合。 | Tán rằng (赞曰): Giữ gìn ngay thẳng không sai lệch, đối diện nghĩa lớn chẳng nghi nan. | 32 / 31 | **Đầy đủ (Dùng)** |

**Đề xuất xử lý ở Bước 5 & Bước 7:**
- Ở file `han.txt` của `HCB_10`, chỉ trích xuất đúng 3 đoạn: `孔子曰...故總為《獨行篇》焉。`, đoạn `李善字次孫...續至河間相。` và đoạn `贊曰：...立仁成德。`.
- Không đưa 23 truyện chưa dịch vào file sạch để tránh vi phạm lỗi `MISSING` (thiếu vế Việt). Ghi rõ giới hạn phạm vi này vào file báo cáo nộp kèm.

### 2.2. Thống nhất cách xử lý chú thích và dị bản (trước Bước 5)

Theo Guideline (Mục 4 – Bước 5), nhóm cần xóa toàn bộ chú thích ngoài nội dung chính:

| Loại chi tiết cần làm sạch | Xuất hiện ở đâu | Đề xuất xử lý |
|---|---|---|
| Cụm chữ Hán chèn trong ngoặc đơn ở bản Việt, ví dụ `(韓德讓)`, `(穆超)`, `(處耘)` | `HCB_01` (cả 6 quyển), `HCB_10`, `HCB_14` | **Xóa bằng Regex** ở Bước 5 (giống chuẩn chung của nhóm) |
| Chữ Hán giản thể mở ngoặc trong `HCB_10`, ví dụ `(独行篇)`, `(次孙)`, `(淯阳)`, `(评语)`, `(赞曰)` | `HCB_10` (Quyển 81) | **Xóa toàn bộ** cụm ngoặc chữ Hán trong bản Việt |
| Chú thích khảo dị `【攷異】` và chú nhỏ `{{*}}` trong nguyên bản Hán | `HCB_01` (Quyển 4, 9, 12, 13, 14, 18) | **Xóa ở cả hai bản** (vì bản Việt hầu như không dịch hoặc chỉ dịch lác đác) |
| Năm dương lịch / khoảng năm do người dịch chú thêm, như `(25–56)`, `(983)`, `(1790 dương lịch)` | `HCB_01` (ở các dòng đề mục năm), `HCB_10`, `HCB_14` | **Xóa** nếu nằm xen trong câu; đối với dòng tiêu đề năm thì bỏ qua vì theo Tiêu chí 7 của Guideline **không đưa dòng tiêu đề vào cặp dóng hàng** |
| Con số định dạng kiểu phương Tây `10,000,000` (tư tài của Lý Nguyên) | `HCB_10` (mục Lý Thiện) | Giữ nguyên theo nguồn Việt hoặc chuẩn hóa thành `10.000.000` / `mười triệu` (tương ứng `千萬` ở bản Hán) |
| Thơ ngự chế có đủ 4 phần: *Nguyên tác chữ Hán, Phiên âm, Dịch nghĩa, Dịch thơ* | `HCB_14` (ví dụ đợt Nguyễn Quang Bình vào chúc thọ ở Q1359) | Ở bản Việt **chỉ giữ phần Dịch nghĩa** (hoặc Dịch thơ nếu không có Dịch nghĩa), **xóa phần chữ Hán lặp lại và phần Phiên âm Hán-Việt** để dóng hàng `1-1` với câu thơ gốc bên cột Hán |

### 2.3. Tệp nên dùng cho Bước 4

- **Sử dụng trực tiếp tệp `.wikitext` (từ Wikisource) và `.html` (từ Sillok)** để trích xuất văn bản thô thay vì đọc từ PDF, nhằm tránh lỗi mất chữ Hán hiếm (chữ nằm ngoài BMP Unicode), lỗi đứt dòng cứng giữa câu và dính chân trang/giấy phép.
- Thư mục `02_ocr_tho/` để trống và ghi chú *"Không áp dụng (nguồn trực tuyến có sẵn text)"* trong báo cáo bàn giao.

### 2.4. Ước tính số cặp (Của riêng Người 4)

Số liệu ước tính dựa trên số dấu kết câu (`。！？` ở bản Hán và `.!?` ở bản Việt) sau khi loại bỏ các phần chưa dịch của `HCB_10`:

| Tác phẩm / Quyển | Chữ Hán (phạm vi dùng) | Âm tiết Việt | Đoạn Hán | Câu Hán / Việt (ước tính) | Số cặp tối đa |
|---|---|---|---|---|---|
| HCB_01 Q4 | ~8.250 | ~9.850 | 145 | 410 / 435 | 410 |
| HCB_01 Q9 | ~7.800 | ~9.300 | 138 | 385 / 405 | 385 |
| HCB_01 Q12 | ~8.100 | ~9.600 | 142 | 395 / 418 | 395 |
| HCB_01 Q13 | ~7.650 | ~9.100 | 128 | 375 / 392 | 375 |
| HCB_01 Q14 | ~6.400 | ~7.650 | 105 | 315 / 330 | 315 |
| HCB_01 Q18 | ~8.300 | ~9.900 | 148 | 410 / 430 | 410 |
| HCB_10 Q81 *(3 mục đã dịch)* | 615 | 741 | 5 | 36 / 38 | 36 |
| HCB_14 *(8 quyển trích đoạn)* | ~5.400 | ~5.800 | 14 bài | 620 / 235 | 235 |
| **Tổng (15 quyển)** | **~52.515** | **~61.941** | **~825** | | **~2.561** |

- **Đánh giá chỉ tiêu KPI (2.000 cặp):** Riêng 6 quyển của `HCB_01` đã mang lại tối đa khoảng **2.290 cặp câu**, hoàn toàn đủ để bù đắp cho việc `HCB_10` chỉ dịch 1 truyện (36 cặp) và `HCB_14` chỉ là các bài trích đoạn (235 cặp).
- Cần giữ lại tối thiểu **78%** số câu ước tính trong quá trình làm sạch và gộp câu (`1-n`, `n-1`) để vượt mốc 2.000 cặp hợp lệ.

---

## Phần 3 – Bằng chứng kiểm tra

### 3.1. Kiểm tra tệp

| Hạng mục | Kết quả |
|---|---|
| Định dạng nguồn | 100% là nguồn trực tuyến (Text/Wikitext/HTML) và PDF xuất từ trình duyệt; không có tệp ảnh Scan |
| Trùng trang / Mờ trang | Không có |
| Bản Hán và Việt chung một file | Không có ở các file `HCB_01` và `HCB_10`; riêng ở `HCB_14` có một số câu trích chữ Hán hoặc bài thơ chữ Hán nằm xen trong trang Việt cần lọc bỏ ở Bước 5 |

### 3.2. Đối chiếu từng tác phẩm (Mẫu Đầu – Giữa – Cuối)

Trong các bảng dưới đây, **$r = \text{số âm tiết Việt} / \text{số chữ Hán}$** (mức chuẩn thông thường từ $1{,}10$ đến $1{,}30$).

#### HCB_01 (Quyển 4, 9, 12, 13, 14, 18)

| Quyển | Vị trí | Bản Hán (`zh.wikisource`) | Bản Việt (`vi.wikisource`) |
|---|---|---|---|
| **Q4** | Đầu | 夏，四月，乙巳，조以昭義節度使李繼勳為河陽三城節度使。 | Mùa hạ, tháng 4, ngày Ất Tị, chiếu lấy Tiết độ sứ Chiêu Nghĩa Lý Kế Huân làm Tiết độ sứ Hà Dương tam thành. |
| **Q4** | Giữa | 王全斌之入蜀也，適屬冬暮，京城大雪，帝設氈帷於講武殿 | Khi Vương Toàn Bân vào Thục, đúng lúc cuối đông, kinh thành tuyết lớn, Hoàng đế dựng màn nỉ ở điện Giảng Vũ |
| **Q4** | Cuối | 撻烈為政威嚴，部民畏服。 | Thát Liệt trị chính uy nghiêm, dân các bộ đều sợ phục. |
| **Q9** | Đầu | 帝諱炅，初名匡乂，改賜光義，即位之逾年，又改今諱 | Hoàng đế húy là Quýnh (炅), lúc đầu tên là Khuông Nghĩa, đổi ban tên là Quang Nghĩa, năm sau khi lên ngôi lại đổi thành tên húy nay |
| **Q9** | Giữa | 太平興國三年春，正月，丙戌朔，不受朝，群臣詣閤門拜表稱賀。 | Năm Thái Bình Hưng Quốc thứ 3, mùa xuân, tháng giêng, ngày Bính Tuất là mồng 1, không nhận triều, quần thần đến Cáp môn dâng biểu chúc mừng. |
| **Q9** | Cuối | 二月，甲子，車駕發京師。戊辰，次鄭州。 | Tháng 2, ngày Giáp Tý, xa giá xuất phát từ kinh sư. Ngày Mậu Thìn, đóng ở Trịnh châu. |
| **Q12** | Đầu | 冬，十月，帝以新譯經五卷示宰相，因謂之曰：「夫為人君，治人利物，即修行也。 | Mùa đông, tháng 10, Hoàng đế đem 5 quyển kinh mới dịch cho các Tể tướng xem, nhân đó nói: “Phàm bậc làm vua, cai trị con người, làm lợi cho muôn vật, tức là tu hành. |
| **Q12** | Giữa | 戊寅，權交州留後黎桓遣使入貢。乙未，夏州李繼遷誘殺都巡檢使曹光實於葭蘆川。 | Ngày Mậu Dần, Quyền Giao châu Lưu hậu Lê Hoàn (黎桓) sai sứ sang cống. Ngày Ất Mùi, Hạ châu Lý Kế Thiên dụ giết Đô Tuần kiểm sứ Tào Quang Thực (曹光實) ở Gia Lô xuyên. |
| **Q12** | Cuối | 時室昉與韓德讓、耶律色珍相友善，同心輔政 | Khi đó Phưởng cùng Hàn Đức Nhượng (韓德讓), Da Luật Sắc Trân (耶律色珍) kết bạn thân, đồng lòng phụ chính |
| **Q13** | Đầu | 春，正月，庚辰，夜，漏上五刻，大軍北發。 | Mùa xuân, tháng giêng, ngày Canh Thìn, ban đêm, đồng hồ nước điểm canh năm, đại quân xuất phát lên phía bắc. |
| **Q13** | Giữa | 夏，四月，己亥朔，遼主次南京北郊。 | Mùa hạ, tháng 4, ngày Kỷ Hợi là mồng 1, Liêu chúa đến đóng ở bắc giao Nam Kinh. |
| **Q13** | Cuối | 并州都部署潘美、定州都部署田重進，並承詔入朝。 | Đô bộ thự Bính châu là Phan Mĩ, Đô bộ thự Định châu là Điền Trọng Tiến, đều vâng chiếu vào triều. |
| **Q14** | Đầu | 春，正月，己卯朔，不受朝，群臣詣閤拜表稱賀。 | Mùa xuân, tháng giêng, ngày Kỷ Mão là mồng 1, không nhận chầu, quần thần đến Cáp môn dâng biểu chúc mừng. |
| **Q14** | Giữa | 帝謂宰相曰：「朕每日聽政，常至日昃，不覺倦也。」 | Hoàng đế bảo Tể tướng: “Trẫm mỗi ngày nghe chính sự, thường đến xế chiều, không thấy mỏi mệt.” |
| **Q14** | Cuối | 三月，丁亥，詔權停貢舉。 | Tháng 3, ngày Đinh Hợi, chiếu tạm đình việc cống cử. |
| **Q18** | Đầu | 秋，七月，乙亥，李繼遷遣牙校以良馬來貢，且謝過，猶稱所授官。 | Mùa thu, tháng 7, ngày Ất Hợi, Lý Kế Thiên sai nha hiệu đem ngựa tốt đến cống, lại tạ lỗi, vẫn xưng chức quan đã được ban. |
| **Q18** | Giữa | 至道元年春，正月，戊申朔，改元，大赦。 | Năm Chí Đạo thứ 1, mùa xuân, tháng giêng, ngày Mậu Th申 là mồng 1, cải nguyên, đại xá. |
| **Q18** | Cuối | 六月，乙，遣使諭李繼遷，賜以器幣。 | Tháng 6, ngày Ất Vị, sai sứ dụ Lý Kế Thiên, ban cho đồ dùng và lụa tiền. |

#### HCB_10 (Hậu Hán thư – Quyển 81)

| Vị trí (trong phần đã dịch) | Bản Hán (`zh.wikisource`) | Bản Việt (`vi.wikisource`) |
|---|---|---|
| **Đầu (Lời tựa)** | 孔子曰：「與其不得中庸，必也狂狷乎！」又云：「狂者進取，狷者有所不為也。」 | Khổng Tử (孔子) nói: Thà rằng không đắc được đạo Trung dung, tất phải tìm người Cuồng, Quyến vậy! Lại nói: Người Cuồng thì tiến thủ, người Quyến thì có những việc không làm. |
| **Giữa (Truyện Lý Thiện)** | 李善字次孫，南陽淯陽人也，本同縣李元蒼頭也。建武中疫疾，元家相繼死沒，唯孤兒續始生數旬，而貲財千萬 | Lý Thiện (李善) tự Thứ Tôn (次孙), người Dục Dương (淯阳) Nam Dương (南阳), vốn là nô bộc của Lý Nguyên (李元) cùng huyện. Trong năm Kiến Vũ (建武) (25–56), dịch bệnh hoành hành, nhà Lý Nguyên nối tiếp nhau chết hết, chỉ còn cô nhi Lý Tục (李续) mới sinh được vài 10 ngày, mà tư tài có đến 10,000,000. |
| **Cuối (Lời bàn – Tán)** | 贊曰：守死善道，義不苟合。惟此剛潔，果行育德。 | Tán rằng (赞曰): Giữ gìn ngay thẳng không sai lệch, đối diện nghĩa lớn chẳng nghi nan. Chỉ bậc cương khiết này, quyết đoán hành động nuôi dưỡng đức dày. |

Bảng ánh xạ cấu trúc `HCB_10`:

| Mục Hán ↔ Việt | Chữ Hán | Âm tiết Việt | Đoạn Hán / Việt | $r$ | Ghi chú |
|---|---|---|---|---|---|
| Mở đầu `孔子曰…` ↔ `Khổng Tử nói…` | 184 | 242 | 1 / 1 | $1{,}31$ | Khớp hoàn toàn |
| 7 mục `譙玄` → `范式` | ~2.650 | 0 | 18 / 0 | — | Không có bản dịch (Loại) |
| `李善` ↔ `Lý Thiện` | 399 | 468 | 3 / 3 | $1{,}17$ | Khớp hoàn toàn |
| 16 mục `王忳` → `雷義` + `論` | ~4.185 | 0 | 35 / 0 | — | Không có bản dịch (Loại) |
| `贊` ↔ `Lời bàn (Tán rằng)` | 32 | 31 | 1 / 1 | $0{,}97$ | Khớp hoàn toàn (thể văn tứ ngôn) |

#### HCB_14 (Thanh thực lục – 8 quyển)

| Vị trí | Quyển | Bản Hán (`sillok.history.go.kr`) | Bản Việt (`vi.wikisource`) |
|---|---|---|---|
| **Đầu** | Q1328 | ○諭軍機大臣等、福康安奏、阮光平悔罪投誠… | Dụ Quân cơ đại thần rằng: Phúc Khang An tâu việc Nguyễn Quang Bình hối tội đầu thành… |
| **Giữa** | Q1346 | ○乾隆五十五年。庚戌。春。正月。己亥朔。以八旬萬壽、頒詔天下。 | Càn Long năm 55, tháng 1, ngày 1 (năm 1790 dương lịch). Nhân dịp vạn thọ tám mươi tuổi, ban chiếu thiên hạ… |
| **Giữa** | Q1359 | ○己巳。高宗純皇帝御澹泊敬誠殿、賜安南國王阮光平宴… | Càn Long năm 55, tháng 7, ngày 16 (năm 1790 dương lịch)… Hoàng thượng ngự điện Đạm Bạc Kính Thành ban yến cho Quốc vương An Nam Nguyễn Quang Bình… |
| **Cuối** | Q1463 | ○諭軍機大臣等…安南國王阮光纘遣使表貢… | Dụ Quân cơ đại thần… Quốc vương An Nam Nguyễn Quang Toản sai sứ dâng biểu tiến cống… |

### 3.3. Phương pháp và giới hạn

**Đã làm:**
- Kiểm tra toàn bộ 15 quyển được phân công cho Người 4 (Đăng) trên Wikisource tiếng Việt và đối chiếu với bản chữ Hán tương ứng.
- Xác định phạm vi niên đại, triều vua và kiểm tra tính khớp nối đầu – giữa – cuối của cả 6 quyển `HCB_01`, 1 quyển `HCB_10` và 8 quyển `HCB_14`.
- Phát hiện việc `HCB_10` (Quyển 81) chỉ mới dịch 1 nhân vật (`Lý Thiện`) và lỗi ghi nhầm số quyển trên tiêu đề phụ của `HCB_14` (Quyển 1384 ghi nhầm thành 1381) để kịp thời xử lý ở các bước sau.

**Chưa làm:**
- Chưa chạy script làm sạch tự động (Bước 5) và tách câu chi tiết (Bước 6).
- Các con số về chữ Hán, âm tiết Việt và số cặp câu là ước tính sơ bộ trước khi làm sạch, có thể chênh lệch nhẹ sau khi loại bỏ chú thích và tiêu đề.