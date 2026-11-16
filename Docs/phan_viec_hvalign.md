# Phân việc: kiểm tra và hoàn thiện `hvalign`

**Dành cho:** Huy, Tài, Đăng (và Kiên điều phối). **Ngày:** 2026-11-14.
**Mục tiêu:** `hvalign` chạy đúng trên **toàn bộ tác phẩm được giao của cả 4 người**, và mỗi người có đủ ≥ 2.000 cặp.
**Đọc trước:** [huong_dan_hvalign.md](huong_dan_hvalign.md) (cách dùng), [implementation_plan.md](implementation_plan.md) (thiết kế).

---

## 1. Hiện trạng

| | Tình trạng |
|---|---|
| Đã chạy ổn | 7 tác phẩm của Kiên: 3.490 cặp tự động; 18/18 kiểm thử đạt; 7/7 qua kiểm định TSV/XLSX |
| **App (0.3.0)** | `Mo_hvalign.bat` hoặc `python -m hvalign app`: **Làm tự động → Nhìn qua (không bắt buộc) → Tải về .zip** đúng cấu trúc nộp. Máy tự ghi chú cặp dịch rút gọn. Hiệu đính từng cặp, chấm mẫu §8 nằm ở *Công cụ nâng cao* |
| **Giảng viên đã trả lời (QA 16/11)** | Chỉ dóng hàng phần có song ngữ; phần không có bản dịch thì không cần dóng. Bản dịch rút gọn vẫn dùng được nhưng phải đánh dấu: HCB_11 thêm cột `Ghi chú` vào `.xlsx` (máy tự điền). HCB_14: chỉ làm phần có song ngữ, được lấy bản Hán từ sillok.history.go.kr |
| **Chưa chạy trên dữ liệu thật của Huy, Tài, Đăng** | Máy Kiên chưa có nguồn của các bạn. Kiểu tên tệp `.txt` của Huy mới được thử bằng bản giả lập |
| Chương trình còn thiếu | (1) tải bài sillok; (2) chấm câu cho văn bản Hán không dấu (HCB_03); (3) luật bỏ phiên âm trong thơ 4 phần (HCB_14); (4) bộ mẫu chuẩn và chỉnh trọng số |

Mỗi phần còn thiếu được giao cho người có dữ liệu cần đến phần đó (mục 3).

---

## 2. Đợt 1 – Ai cũng làm: chạy chương trình trên tác phẩm của mình

Làm trước tiên, vì đợt này lộ ra lỗi sớm nhất.

1. **Lấy code:** clone kho chung https://github.com/24122039Kien/NLP-GK-24TNT.git. Chạy `pip install -r requirements.txt`, rồi `python -m pytest -q` phải ra 18 passed.
2. **Chép nguồn:** chép vào `CV02_<MA>/01_nguon/` và **giữ nguyên tên và định dạng** (`.wikitext`, `.txt`, `.html` đều được). PDF cứ để đó, chương trình không đọc PDF.
3. **Khai báo phân công:** thêm dòng của mình vào `config/phan_cong.tsv`.
4. **Manifest:** chép manifest của mình thành `Docs/nguon_manifest_<ten>.tsv`. Cột `tep` phải là đường dẫn tính từ `Lab/GK`, ví dụ `CV02_HCB_01/01_nguon/han/x.wikitext`.
5. **Chạy:** `python -m hvalign inventory --work <các mã của bạn>` để kiểm kê nguồn. Sau đó mở app (`Mo_hvalign.bat`), chọn tên mình và bấm **▶ Làm tự động tất cả**.
6. **Nhìn qua** (không bắt buộc): bấm **Xem nhanh**, lướt tab *Cặp có ghi chú*, bấm **Bỏ** cặp sai rõ ràng ([hướng dẫn mục 6.1](huong_dan_hvalign.md#61-cách-nhanh-xem-nhanh-trên-trang-chính)). Có bấm Bỏ thì commit thư mục `hieu_dinh/`. Sau đó bấm **⬇ Tải về** để lấy `.zip` nộp.
7. **Chấm chéo** (không bắt buộc, nên làm nếu còn thời gian) 100 cặp trong *Công cụ nâng cao → Chấm mẫu*, theo vòng: **Kiên chấm Huy → Huy chấm Tài → Tài chấm Đăng → Đăng chấm Kiên.** Người chấm cần `git pull` và chạy tác phẩm của bạn mình để có cùng dữ liệu. Cặp sai thì báo người làm sửa.
8. **Ghi kết quả** vào `Docs/kiem_tra_hvalign_<ten>.md` theo mẫu ở mục 5.

**Tiêu chí xong Đợt 1** (cho từng tác phẩm của mình):

- [ ] `inventory`: không còn "thiếu bản Hán/Việt", không trùng bài (hoặc đã ghi rõ lý do)
- [ ] `run` không có `Traceback`; kiểm định **ĐẠT**
- [ ] `02_ocr_tho/*.tsv`: đề mục nhận đúng, không còn markup `{{ }}`, `[[ ]]`, `<ref>`
- [ ] Đã đọc hết `work/<MA>/canh_bao.tsv` và `loai_tru.tsv`
- [ ] Chấm 30 cặp mỗi tác phẩm; ghi tỷ lệ đúng
- [ ] `status`: ghi số cặp của mình (mục tiêu ≥ 2.000)

---

## 3. Đợt 2 – Việc riêng từng người

### 3.1. Huy

**Tác phẩm:** HCB_01 Q3, 5, 7, 11, 16 · HCB_03 Q130 · HCB_06 Q28 · HCB_08 Q24 · HCB_09 Q76 · HCB_14 Q1327, 1361, 1363, 1381, 1419, 1429.

**Kiểm tra dữ liệu và viết cấu hình:**

| Việc | Cách làm | Xong khi |
|---|---|---|
| Kiểm chứng bộ đọc `.txt` trên dữ liệu thật (cả nhóm chỉ Huy có nguồn `.txt`) | Xem cột `dinh_dang` trong `work/<MA>/extract_log.tsv`: tệp có markup wiki phải ra `wikitext`, tệp chép thuần ra `plain`. Nếu tệp `.txt` đã mất đề mục thì ghi lại | Mọi tệp `.txt` nhận đúng định dạng, đúng Hán/Việt, đúng số quyển |
| HCB_06: bản Việt chỉ bằng ~½ bản Hán | Xác định phần chưa dịch, ghi `loai_tru` vào `config/works/HCB_06.yaml` (xem mẫu ở `HCB_13.yaml`) | Tỷ lệ độ dài trong `bao_cao.md` về khoảng 1,0–1,3 |
| HCB_09: chỉ dịch 3 nhân vật | `loai_tru` cho các nhân vật còn lại, theo đề mục (`muc:`) | `khong_ghep.tsv` gần như rỗng |
| HCB_14: bản Hán `.txt` gộp nhiều bài | Chấm mẫu kỹ hơn ở các quyển nhiều bài | Không có cặp nối giữa hai bài khác nhau |

**Phần chương trình – Bước 5: mã chữ và văn bản không dấu câu**

1. **Bảng mã chữ (R09):**
   - Tra chữ đúng cho `{{SKchar|…}}` ở HCB_03, HCB_06 và 6 mã của HCB_11 (`[BD77]`, `[B258]`, `[E8E6]`, `[CF3D]`, `<曷毛>`, `<名頁>`).
   - Ghi vào `resources/char_fix.tsv`. Khóa là chuỗi đúng như trong text thô, ví dụ `SKchar|2652`.
   - **Xong khi:** `canh_bao.tsv` không còn dòng "R09 mã chữ chưa tra được".
2. **Chấm câu thủ công cho HCB_03** (kế hoạch mục 5.3). Hiện bản Hán là một khối khoảng 1.400 chữ không dấu, nên gần như không dóng được theo câu. Làm như sau:
   - Thêm khóa cấu hình `cham_cau_thu_cong` trỏ tới tệp `resources/cham_cau/HCB_03_q130.txt`, trong đó bản Hán đã được chấm câu (bằng tay, hoặc thử mô hình guwen-punc).
   - Ở `hvalign/clean.py`, thay text Hán bằng bản đã chấm, **chỉ khi bỏ hết dấu câu thì hai bản giống hệt nhau từng chữ**. Nếu không giống, báo lỗi và không thay.
   - Thêm kiểm thử: một ca khớp và một ca lệch chữ.
   - **Xong khi:** HCB_03 dóng ra phần lớn là kiểu `1-1` / `1-2`.

### 3.2. Tài

**Tác phẩm:** HCB_01 Q1, 8, 17, 19 · HCB_02 · HCB_12 Q113 · HCB_14 Q1335, 1337, 1358, 1360, 1362, 1410, 1421, 1445.

> ⚠ Tài có rủi ro thiếu 2.000 cặp cao nhất nhóm (HCB_02, HCB_12 ngắn; HCB_14 đang thiếu nguồn). Làm 3.2 **trước** rồi báo số cặp cho nhóm sớm.

**Phần chương trình – lệnh tải bài sillok (`fetch-sillok`).** Bản Hán HCB_14 của Tài hiện chỉ có PDF từ zh.wikisource, mà chương trình không đọc PDF. Thêm nữa Q1358 và Q1410 bị sai bài, Q1360 thiếu 3 ngày. Vì vậy cần một lệnh tải đúng bài từ sillok:

| Yêu cầu | Chi tiết |
|---|---|
| Đầu vào | Danh sách link sillok ở mục "Nguồn:" cuối bản Việt. `readers.py` đã gom sẵn các link này vào `doc.meta["source_urls"]` |
| Đầu ra | `01_nguon/han/清實錄_高宗純皇帝實錄_卷<quyển>_<mã bài>.html`, đặt tên giống phần của Kiên; thêm dòng vào manifest (url, sha256, ngày tải) |
| Lịch sự với máy chủ | User-Agent chung của nhóm (xem `Docs/tai_nguon.py`), giãn cách ≥ 3 giây, tôn trọng `Retry-After` khi gặp lỗi 429. Tệp đã có thì bỏ qua, không tải lại |
| Kiểm thử | Không gọi mạng trong kiểm thử: dùng một trang HTML mẫu lưu sẵn |
| Xong khi | 8 quyển HCB_14 của Tài đều có bản Hán `.html`; `inventory` hết "thiếu bản Hán"; mẫu 30 cặp HCB_14 đạt |

Đăng và Huy cũng dùng được lệnh này nếu thiếu bài.

**Kiểm tra dữ liệu và viết cấu hình:**

| Việc | Cách làm |
|---|---|
| HCB_02: bản Việt thừa phiên âm và đoạn trích Minh Thực Lục | `loai_tru` bên Việt theo đề mục; chỉ giữ phần **dịch nghĩa** của chiếu văn |
| HCB_12: bản Hán thiếu 三家注 (kế hoạch mục 11, câu 5) | Thử tìm bản Hán có chú. Nếu không có: `loai_tru` các đoạn chú giải bên Việt, chỉ dóng chính văn |

### 3.3. Đăng

**Tác phẩm:** HCB_01 Q4, 9, 12, 13, 14, 18 · HCB_10 Q81 · HCB_14 Q1328, 1331, 1346, 1359, 1384, 1420, 1428, 1463.

**Kiểm tra dữ liệu và viết cấu hình:**

| Việc | Cách làm |
|---|---|
| HCB_10: bản Việt chỉ có lời tựa, truyện Lý Thiện, lời tán | `loai_tru` bên Hán cho 23 truyện còn lại, theo đề mục. Kiểm tra chữ giản thể trong ngoặc như `(独行篇)` đã bị R06 xóa hết chưa |
| Q1384 (Đăng) ghi tiêu đề 1381, trùng số với Q1381 của Huy | Sau khi cả hai chép nguồn, chạy `inventory`: dòng "Bài sillok … xuất hiện ở nhiều quyển" cho biết có trùng thật không. Thống nhất với Huy ai giữ bài |
| "1 quyển dư" trong phân công | Xác nhận với nhóm, sửa `config/phan_cong.tsv` |

**Phần chương trình – luật R11 cho thơ 4 phần (HCB_14, ví dụ Q1359).** Bản Việt có thơ ngự chế gồm 4 phần: *nguyên tác chữ Hán, phiên âm, dịch nghĩa, dịch thơ*. Chỉ được giữ **dịch nghĩa** (nếu không có thì giữ dịch thơ), vì phiên âm không phải bản dịch và nguyên tác thì lặp bản Hán.

1. Xem các phần này được đánh dấu thế nào trong wikitext: đề mục, chữ in đậm "Phiên âm:", hay `<poem>`.
2. Viết luật có cấu trúc trong `hvalign/clean.py` (bật bằng cấu hình), không chỉ là một regex. Các dòng bị bỏ phải được ghi vào `loai_tru.tsv` kèm lý do.
3. Kiểm thử: một bài thơ đủ 4 phần, một bài thiếu dịch nghĩa, và một đoạn văn xuôi không bị đụng tới.
4. **Xong khi:** các cặp thơ trong HCB_14 chỉ chứa phần dịch nghĩa.

### 3.4. Kiên (điều phối)

| Việc | Ghi chú |
|---|---|
| ~~Tạo kho git~~ (đã xong: https://github.com/24122039Kien/NLP-GK-24TNT); mời 3 bạn làm collaborator | Cần làm trước Đợt 1 |
| Gộp thay đổi của các bạn; chạy lại `pytest` và `run --work` toàn bộ sau mỗi lần gộp | |
| ~~Lệnh `review apply`~~ (đã xong, thay bằng app: quyết định lưu ở `hieu_dinh/` và tự áp mỗi lần xuất) | Kế hoạch mục 7.1 |
| Bộ mẫu chuẩn khoảng 120 câu/người và đánh giá cấu hình A/B/C | Kế hoạch mục 6.4. Cần cả nhóm dóng tay phần mẫu của mình |

---

## 4. Quy tắc khi sửa chương trình

1. **Ưu tiên cấu hình hơn sửa code.** Vấn đề riêng của một tác phẩm thì giải quyết trong `config/works/<MA>.yaml` (`loai_tru`, `co_rui_ro`, bật/tắt luật). Chỉ sửa `hvalign/` khi cần một khả năng mới.
2. **Mọi thay đổi code phải kèm kiểm thử** trong `tests/`, và `python -m pytest -q` phải đạt hết.
3. **Sửa xong chạy lại phần của mọi người, không chỉ phần mình.** Chạy `python -m hvalign run` và so số cặp trong `status` trước/sau. Nếu số cặp của người khác thay đổi bất thường, ghi rõ khi gửi thay đổi.
4. **Không sửa tệp trong `01_nguon/`** (Guideline Bước 3); không dùng `--ban-giao` khi chưa hiệu đính.
5. **Báo lỗi** trong `Docs/kiem_tra_hvalign_<ten>.md`, ghi đủ:
   - lệnh đã chạy;
   - mã tác phẩm;
   - mã truy vết (ví dụ `HCB_09/q076/viet/s02/p004`);
   - kết quả mong đợi và kết quả thực tế.

---

## 5. Mẫu báo cáo kiểm tra (`Docs/kiem_tra_hvalign_<ten>.md`)

```markdown
# Kiểm tra hvalign – <tên> – <ngày>

## Kết quả chạy
| Mã | inventory | run / kiểm định | Cặp | Cặp gắn cờ đã xem | Ghi chú |
|---|---|---|---|---|---|
| HCB_xx | 0 vấn đề | ĐẠT | 412 | 21/21 | |

Tổng số cặp của tôi (status): ….
Tỷ lệ lỗi mẫu do <tên bạn chấm> chấm trong app: …% (… / 100 cặp).

## Lỗi chương trình
| # | Lệnh | Mã truy vết | Mong đợi | Thực tế | Đã sửa? |
|---|---|---|---|---|---|

## Cấu hình đã thêm
- config/works/HCB_xx.yaml: …

## Việc riêng (mục 3)
- …
```

---

## 6. Thứ tự và phụ thuộc

| Thứ tự | Việc | Ai | Chặn việc gì |
|---|---|---|---|
| 1 | Kho git chung (đã có), mời 3 bạn vào repo | Kiên | Mọi việc |
| 2 | Đợt 1 (mục 2) | Cả 4 | Lộ lỗi sớm; số cặp thật của từng người |
| 3 | `fetch-sillok` | Tài | HCB_14 của Tài; kiểm tra trùng Q1381/Q1384 |
| 3 | Bảng mã chữ, chấm câu HCB_03 | Huy | HCB_03, HCB_06, HCB_11 |
| 3 | Luật R11 thơ | Đăng | HCB_14 của Đăng (và của người khác nếu có thơ) |
| 4 | Cấu hình `loai_tru` các tác phẩm dịch thiếu | Người giữ tác phẩm | Số cặp chính xác |
| 5 | Hiệu đính + chấm chéo trong app (đã có công cụ); bộ mẫu chuẩn | Cả 4; bộ mẫu chuẩn: Kiên | Bàn giao (G6) |

**Điều kiện coi là "chạy được tất cả tác phẩm của từng người":** cả 4 file `kiem_tra_hvalign_<ten>.md` đều có:
- mọi tác phẩm **ĐẠT** kiểm định;
- tỷ lệ lỗi mẫu ≤ 20%, do bạn khác chấm trong app (ngưỡng đạt của Guideline là ≤ 30%);
- số cặp ≥ 2.000.

Tác phẩm nào chưa đạt thì ghi lý do và người xử lý.
