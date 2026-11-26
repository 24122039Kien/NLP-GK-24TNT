# Hướng dẫn thực hành `hvalign`

**Dành cho:** cả nhóm CV02 (Kiên, Huy, Tài, Đăng). **Phiên bản chương trình:** 0.3.2, ngày 2026-11-26.
**Liên quan:** [phan_viec_hvalign.md](phan_viec_hvalign.md) (việc của từng người) · [implementation_plan.md](implementation_plan.md) (thiết kế).

Mọi ví dụ đầu ra trong tài liệu này đều chép từ lần chạy thật trên dữ liệu của nhóm.

---

## 0. Tóm tắt một phút

**Cách dễ nhất: dùng app.** Nhấp đúp `Mo_hvalign.bat` ở thư mục gốc repo, hoặc gõ `python -m hvalign app`. Trình duyệt sẽ mở `http://127.0.0.1:8765`. App chỉ chạy trên máy bạn, không cần mạng.

Trang chính của app chỉ có 3 bước:

1. **Làm tự động:** bấm **▶ Làm tự động tất cả**. Máy đọc nguồn, làm sạch, tách câu, dóng hàng, **tự viết ghi chú** cho cặp dịch rút gọn hoặc có thêm diễn giải, rồi kiểm định định dạng.
2. **Nhìn qua (không bắt buộc):** bấm **Xem nhanh** ở một tác phẩm để lướt các cặp máy đã ghi chú. Thấy cặp sai rõ ràng thì bấm **Bỏ** (mục 6).
3. **Tải về:** bấm **⬇ Tải về** (một tác phẩm) hoặc **⬇ Tải tất cả**. Bạn nhận một tệp `.zip` đúng cấu trúc nộp: `CV02_<MA>/01_nguon`, `03_text_sach`, `04_dong_hang/` + `bao_cao.md` (mục 7).

Hiệu đính từng cặp bằng phím, chấm mẫu §8 và ghi vào `04_dong_hang` trong repo vẫn có, ở trang **Công cụ nâng cao** (góc phải trên).

Trước đó vẫn phải đưa nguồn vào và khai báo phân công (mục 2). Muốn dùng dòng lệnh thì vẫn chạy được như cũ, mở terminal **tại thư mục gốc của repo**:

```
python -m hvalign inventory --work HCB_xx      # nguồn đã đủ và đúng chưa
python -m hvalign run --work HCB_xx            # chạy hết Bước 4 → 7, xuất file, kiểm định, báo cáo
python -m hvalign status                       # số cặp của từng người
```

Sửa cấu hình xong thì bấm **Chạy** trong app, hoặc chạy lại lệnh `run`. Mỗi tác phẩm chỉ mất vài giây.

---

## 1. Chuẩn bị lần đầu

1. **Kiểm tra Python** (cần 3.10 trở lên):
   ```
   python --version
   ```
   Nếu máy báo không nhận lệnh `python`, dùng `py` thay cho `python` ở mọi lệnh trong tài liệu này.
2. **Lấy code và cài đặt:**
   ```
   git clone https://github.com/24122039Kien/NLP-GK-24TNT.git
   cd NLP-GK-24TNT
   pip install -r requirements.txt
   ```
3. **Chạy kiểm thử.** Kết quả phải là `18 passed`:
   ```
   python -m pytest -q
   ```
4. **Chạy thử trên dữ liệu có sẵn của Kiên:**
   ```
   python -m hvalign run --work HCB_04
   ```
   Lệnh chạy xong trong chưa đầy 1 giây và dòng cuối ghi `Kiểm định HCB_04: ĐẠT` là cài đặt đã ổn.

---

## 2. Đưa nguồn của bạn vào

### 2.1. Chép tệp

Chép tệp nguồn vào `CV02_<MA>/01_nguon/`. **Giữ nguyên tên và định dạng.** Cả hai cách sắp xếp sau đều được:

```
CV02_HCB_01/01_nguon/                      CV02_HCB_01/01_nguon/
├── han/                                   ├── TTTTG_q03_han.txt
│   └── 續資治通鑑_卷002.wikitext           ├── TTTTG_q03_viet.txt
└── viet/                                  ├── TTTTG_q05_han.txt
    └── Tục_tư_trị_thông_giám_Quyển_2.wikitext   └── …
        (kiểu của Kiên)                         (kiểu của Huy)
```

Chương trình tự xác định bốn thứ sau:

| Thông tin | Xác định bằng | Nếu xác định sai |
|---|---|---|
| Định dạng | **Nội dung tệp.** `.txt` có `{{…}}`, `== … ==`, `[[…]]` thì đọc như wikitext; `.txt` không có markup thì mỗi dòng là một đoạn; `.html` của sillok có bộ đọc riêng | Ép định dạng (mục 5F) |
| Hán hay Việt | Thư mục `han/` / `viet/`. Nếu không có thư mục thì xem hậu tố `_han` / `_viet` trong tên. Nếu vẫn không có thì xem tỷ lệ chữ Hán trong nội dung | Đổi tên hoặc chuyển vào thư mục `han/`, `viet/` |
| Số quyển | Tên tệp: `卷002`, `Quyển_2`, `_q03_`, `qsilok_007_1333_…` | Khai báo tay (mục 5G) |
| Mã hóa | UTF-8 (có hoặc không BOM) hoặc UTF-16 | Lưu lại tệp ở dạng UTF-8 (mục 8) |

**Lưu ý:**
- PDF không được dùng để trích text, cứ để trong thư mục.
- Nếu cùng một tài liệu có cả `.wikitext` lẫn `.txt` (cùng tên gốc), chương trình dùng `.wikitext`.
- **Không sửa tệp trong `01_nguon/`.** Muốn bỏ bớt nội dung thì dùng cấu hình (mục 5).

### 2.2. Khai báo phân công

Thêm dòng của bạn vào `config/phan_cong.tsv`. Các cột cách nhau bằng **TAB**, không phải dấu cách:

```
ma_tac_pham	quyen	thanh_vien
HCB_01	3	Huy
HCB_06	*	Huy
```

- `*` nghĩa là cả tác phẩm.
- Thiếu dòng phân công thì số cặp của bạn sẽ hiện dưới tên `chua_phan_cong`.

### 2.3. Manifest

Chép manifest của bạn thành `Docs/nguon_manifest_<ten>.tsv`. Cột `tep` phải ghi đường dẫn tính từ gốc repo, ví dụ `CV02_HCB_01/01_nguon/han/x.wikitext`. Nhờ đó:
- `inventory` so được SHA-256 để biết tệp có bị sửa không;
- báo cáo tự ghi được link nguồn.

---

## 3. Chạy

### 3.1. Kiểm kê nguồn

```
> python -m hvalign inventory --work HCB_04
  HCB_04: 1 quyển
    quyển     1 [Kien]: han 1 tệp (.wikitext); viet 1 tệp (.wikitext)
  Kiểm kê xong: 0 vấn đề
```

Phải ra **0 vấn đề** rồi mới chạy tiếp. Các dòng `!` hay gặp:

| Dòng | Nghĩa |
|---|---|
| `! quyển 1: thiếu bản Việt` | Quyển này chỉ có một bản, hoặc hai bản bị nhận ra số quyển khác nhau |
| `✗ …: SHA-256 KHÁC manifest` | Tệp nguồn đã bị sửa so với lúc tải. Hãy lấy lại bản gốc |
| `! Bài sillok … xuất hiện ở nhiều quyển` | Cùng một bài nằm ở hai quyển hoặc hai người (ví dụ nghi trùng Q1381/Q1384) |

### 3.2. Chạy cả pipeline

```
> python -m hvalign run --work HCB_04
== HCB_04
  B4 HCB_04: 1 quyển, 2 tệp text thô, 17 dòng; định dạng nguồn: han:wikitext×1, viet:wikitext×1; …
  B5 HCB_04: han.txt 8 dòng, viet.txt 9 dòng; loại trừ 0 khối; 0 cảnh báo; …
  B6 HCB_04: Kien: câu Hán 66, câu Việt 70 (đơn vị mịn 69/76)
  B7 HCB_04: 68 cặp (Kien 68); kiểu ghép: 1-1×61, 1-2×5, 1-3×1, 2-2×1; không ghép: 0 câu; …
  Xuất HCB_04: 68 cặp → work/HCB_04/xuat (xem trước); sổ hiệu đính: work/HCB_04/hieu_dinh/
  Kiểm định HCB_04: ĐẠT
  Báo cáo HCB_04: work/HCB_04/bao_cao.md
```

**Đọc từng dòng:**

| Dòng | Xem gì | Dấu hiệu bất thường |
|---|---|---|
| B4 | `định dạng nguồn` đúng như bạn nghĩ chưa | Một tệp `.txt` có markup mà lại ra `plain` |
| B5 | Số dòng `han.txt` và `viet.txt`; số cảnh báo | Có cảnh báo thì mở `work/<MA>/canh_bao.tsv` (mục 4.2) |
| B6 | Số câu Hán và Việt | Hai số chênh nhau rất xa, thường là do bản dịch thiếu phạm vi |
| B7 | Số cặp; số câu không ghép; tầng 1 ghép theo mục ở bao nhiêu quyển | Nhiều câu không ghép, hoặc `0/1` dù hai bản có cùng đề mục (xem ví dụ 5A) |
| Kiểm định | `ĐẠT` | `LỖI`: đọc dòng `✗` ngay bên dưới |

Không ghi `--work` thì chương trình chạy **mọi** tác phẩm có trên máy.

### 3.3. Xem số cặp

```
> python -m hvalign status
  Mã       B4 thô  han.txt viet.txt    cặp  theo thành viên
  HCB_01       10      676      747   1961  Kien 1961
  …
  Tổng theo thành viên: Kien 3490 cặp  (mục tiêu ≥ 2.000 cặp/người, sau hiệu đính)
```

---

## 4. Kiểm tra kết quả, theo đúng thứ tự các bước

### 4.1. Bước 4 – text thô: `work/<MA>/02_ocr_tho/{han,viet}/<quyển>.tsv`

Đây là tệp trung gian, **không nộp**. Nguồn của nhóm là text số (wikitext/HTML/txt), không phải ảnh hay PDF scan, nên theo nhận xét của giảng viên (18/11) thư mục nộp không cần `02_ocr_tho`. Từ bản 0.3.1, chạy `extract` sẽ tự dọn `CV02_<MA>/02_ocr_tho` cũ.

```
HCB_01/q002/han/s01/h	h2	建隆二年⟪*:遼應歴十一年。⟫⟪ref:建隆二年︰辛酉，公元九六一年⟫
HCB_01/q002/han/s01/p001	para	§春，正月，丙申朔，御崇元殿受朝，𨓆，羣臣詣皇太后宮門稱賀。
```

- **Cột 1 là mã truy vết:** tác phẩm / quyển / ngôn ngữ / mục `s` / đoạn `p`. Mọi cặp về sau đều lần ngược được về đây.
- **Cột 2 là loại dòng:** `h2`, `h3` (đề mục), `para` (đoạn), `item` (khoản `*`), `indent` (dòng `:`), `title` (dòng tiêu đề in đậm).
- **`⟪*:…⟫`, `⟪ref:…⟫`, `⟪注:…⟫` là chú thích được giữ tạm.** Bước 5 sẽ xóa chúng, nên ở đây có là bình thường.
- **Không được còn** `{{`, `[[`, `<ref`. Nếu còn, chương trình báo khi chạy B4.

### 4.2. Bước 5 – làm sạch

| Tệp | Xem gì |
|---|---|
| `CV02_<MA>/03_text_sach/han.txt`, `viet.txt` | Text sạch, mỗi dòng một đoạn: không còn chú thích, chữ Hán xen trong bản Việt, năm dương lịch |
| `work/<MA>/canh_bao.tsv` | **Đọc hết.** Mỗi dòng là một chỗ chương trình không tự quyết được |
| `work/<MA>/loai_tru.tsv` | Các khối bị loại theo cấu hình, kèm lý do. Kiểm tra không loại nhầm chính văn |
| `work/<MA>/clean_log.tsv` | Số lần áp dụng từng luật R01–R12 trên từng quyển |

**Ví dụ thật** trong `work/HCB_11/canh_bao.tsv`:

```
HCB_11/q086/han/s01/p023	R09 mã chữ chưa tra được	[BD77]
HCB_11/q086/han/s01/p023	bản Hán còn chữ Latin	板楯蠻夷者，秦昭襄王時，…
```

Nghĩa là nguồn có mã chữ lỗi `[BD77]`, cách sửa ở mục 5C. Các cảnh báo hay gặp:

| Cảnh báo | Làm gì |
|---|---|
| `R09 mã chữ chưa tra được` | Thêm vào bảng mã chữ (mục 5C) |
| `R06 chữ Hán không đứng sau âm tương ứng – giữ lại, cần xem` | Chữ Hán trong bản Việt không đứng sau phần phiên âm của nó, nên chương trình không dám xóa. Nếu là chú thích thì sửa khi hiệu đính; nếu là thơ nguyên tác thì xem luật R11 |
| `bản Việt còn chữ Hán` / `bản Hán còn chữ Latin` | Hệ quả của hai dòng trên |
| `template chưa biết, đã giữ chữ` | Nguồn có template lạ. Chương trình giữ chữ bên trong; báo Kiên để thêm vào bộ đọc |

### 4.3. Bước 7 – dóng hàng

| Tệp | Xem gì |
|---|---|
| `work/<MA>/xuat/<MA>_parallel.tsv`, `.xlsx` | Bản **xem trước**, đúng định dạng Guideline |
| `work/<MA>/khong_ghep.tsv` | Câu không tìm được cặp, không đưa vào TSV. Ví dụ thật ở HCB_14: `Lại dụ rằng:` |
| `work/<MA>/bao_cao.md` | Báo cáo tự sinh, đủ 5 mục tối thiểu của Guideline |

### 4.4. Chấm mẫu (Guideline §8)

Guideline tính `Tỷ lệ lỗi = số cặp lỗi / số cặp được kiểm tra`: **≤ 30% là đạt**, mục tiêu nội bộ **≤ 20%**. Người chấm nên là **một bạn khác**, không phải người làm phần đó.

Trong app, mở tab **Chấm mẫu** và chọn tên bạn được chấm. App lấy **100 cặp ngẫu nhiên** trên mọi tác phẩm của bạn đó. Mỗi cặp bấm một phím:

| Phím | Nghĩa |
|---|---|
| `1` | Đúng |
| `2` `OMISSION` | Vế Việt thiếu ý của vế Hán |
| `3` `ADDITION` | Vế Việt thêm ý không có ở vế Hán |
| `4` `MISSING` | Hai vế không phải bản dịch của nhau |
| `5` `RANH_GIOI` | Cắt câu sai chỗ (thiếu hoặc thừa nửa câu) |
| `U` | Hoàn tác |

Tỷ lệ lỗi hiện ngay trên thanh công cụ. Báo cáo tự sinh (`work/<MA>/bao_cao.md`) cũng tự ghi tỷ lệ này. Kết quả lưu ở `hieu_dinh/cham_mau__<người chấm>.tsv`.

Một số điểm cần biết:
- **Mẫu cố định.** Mọi người chạy cùng code và cùng nguồn sẽ thấy cùng 100 cặp. Hiệu đính làm mất vài cặp thì các cặp còn lại vẫn giữ nguyên trong mẫu.
- **Đổi cỡ mẫu** bằng `cham_mau: so_cap:` trong `config/project.yaml`.
- **Cặp chấm sai phải được sửa** (Guideline yêu cầu). Báo người làm phần đó tìm theo mã cặp trong tab Hiệu đính (chế độ "Tìm trong mọi cặp").
- **Thích dùng Excel** thì `python -m hvalign mau --work HCB_xx` vẫn xuất mẫu ra Excel, nhưng kết quả chấm trên Excel không được tính tự động.

---

## 5. Sửa bằng cấu hình

Vấn đề riêng của một tác phẩm thì sửa trong `config/works/<MA>.yaml`, **không sửa code**. Chưa có tệp thì tạo mới; có thể chép mẫu từ các tệp `HCB_05`, `HCB_11`, `HCB_13`, `HCB_14.yaml` sẵn có. Sửa xong thì chạy lại `python -m hvalign run --work <MA>`.

Viết YAML cần nhớ:
- thụt lề bằng **dấu cách**, không dùng TAB;
- chuỗi có `:` hoặc ký tự đặc biệt thì đặt trong ngoặc kép.

### 5A. Bản Việt không dịch một mục hoặc một nhân vật

```yaml
loai_tru:
  - {lang: han, muc: 大理, ly_do: "Bản Việt không dịch mục 大理"}
```

- `muc` là một phần chữ của **đề mục**. Cả đề mục lẫn mọi đoạn bên dưới nó đều bị loại.
- Thêm `den_het_quyen: true` để loại từ chỗ khớp đến hết quyển, ví dụ phần 校勘記 cuối quyển.

**Hiệu quả thật ở HCB_13:**

| | Không có cấu hình | Có cấu hình |
|---|---|---|
| Dòng `han.txt` | 30 | 25 (loại 7 khối của mục 大理) |
| Tầng 1 ghép theo mục | 0/1 quyển (số đề mục hai bản lệch) | 1/1 quyển |
| Cặp chứa câu của mục 大理 | 6, ví dụ một cặp `10-1` ghép đoạn về nước Đại Lý với câu Việt về Nhật Cảnh | 0 |
| Câu không ghép | 3 | 0 |

### 5B. Ghi chú của người biên tập hoặc người dịch nằm thành dòng riêng

```yaml
loai_tru:
  - {lang: han, loai: indent, muc: 交洲記卷一, ly_do: "Ghi chú khảo chứng 按"}
  - {lang: viet, regex: "^(Theo |Chú:)", ly_do: "Bản dịch ghi chú 按"}
```

Các điều kiện có thể kết hợp:

| Điều kiện | Nghĩa |
|---|---|
| `loai` | Kiểu dòng ở cột 2 của text thô |
| `muc` | Nằm trong mục có đề mục chứa chữ này |
| `regex` | Nội dung khớp biểu thức chính quy |
| `id` | Mã truy vết bắt đầu bằng chuỗi này |
| `quyen` | Chỉ áp cho quyển này |

**Kiểm tra lại `loai_tru.tsv`** sau khi thêm luật. Ở HCB_05, dòng `:` bên Việt có khi là chính văn, nên không thể loại hết dòng `:`.

### 5C. Mã chữ lỗi: `[BD77]`, `<曷毛>`, `{{SKchar|…}}`

Thêm dòng vào `resources/char_fix.tsv`. Cột 1 là chuỗi đúng như trong `canh_bao.tsv`, cột 2 là chữ thay vào:

```
ma	thay_bang	ghi_chu
[BD77]	…	tra ở bản PDF trang …
SKchar|2652	…
```

### 5D. Đoạn đã biết là dịch rút gọn

Gắn cờ cho đoạn đó để ưu tiên khi hiệu đính:

```yaml
co_rui_ro:
  - {lang: han, regex: "^若荆、楊無事", co: rut_gon}
```

### 5E. Văn bản sillok, hoặc một câu Việt ứng với nhiều vế Hán

```yaml
tach_cau:
  han_cham_la_ranh_gioi_mem: true   # 。 của sillok chỉ là ngắt nhỏ
  viet_tach_sau_hai_cham: true      # sillok: giữ tách câu Việt sau ':' để bám vế Hán chia mịn
dong_hang:
  gop_toi_da: 10                    # cho phép ghép đến 10–1
```

Từ bản 0.3.2, mặc định bên Việt **không** tách câu sau dấu hai chấm. Bên Hán 曰：「…」 vốn là một câu, nên bên Việt "X nói: «…»" cũng phải là một câu. Nếu tách, "X nói:" hay bị ghép nhầm vào câu đứng trước (kiểm tra ngày 26/11 tìm thấy khoảng 90 chỗ như vậy ở HCB_01). Chỉ HCB_14 (sillok) bật lại tùy chọn này.

### 5F. Chương trình nhận sai định dạng tệp

```yaml
dinh_dang_nguon: {han: plain, viet: wikitext}   # các giá trị: wikitext / plain / html
```

### 5G. Tên tệp không có số quyển, hoặc muốn tự chỉ định tệp

```yaml
sources:
  - volume: "130"
    member: Huy
    han:  CV02_HCB_03/01_nguon/DongDoSuLuoc_q130_han.txt
    viet: CV02_HCB_03/01_nguon/DongDoSuLuoc_q130_viet.txt
```

Đường dẫn tính từ gốc repo. Với HCB_14, nếu một quyển có nhiều bài sillok thì `han:` có thể là một danh sách.

### 5H. Bật hoặc tắt một luật làm sạch

```yaml
lam_sach:
  R05_viet_dan_nguon_cuoi_khoan: true   # bỏ "(Ngự Lãm 829)" cuối mỗi khoản
  R07_bo_nam_duong_lich: false
```

Danh sách luật và giá trị mặc định nằm ở `config/project.yaml`.

---

## 6. Hiệu đính

### 6.1. Cách nhanh: Xem nhanh trên trang chính

Bấm **Xem nhanh** ở thẻ tác phẩm. Tab **Cặp có ghi chú** chỉ hiện các cặp máy đã tự ghi chú. Với dữ liệu của Kiên là 39/3.490 cặp, phần lớn ở HCB_11. Ghi chú đã nằm sẵn trong tệp tải về, nên bạn **không phải sửa gì**. Chỉ bấm **Bỏ** khi hai vế rõ ràng không nói cùng một việc; bấm **Hoàn tác** hoặc **Lấy lại** nếu bấm nhầm. Cần chọn tên ở ô **Bạn là** trước khi bấm Bỏ.

Máy tự ghi chú khi:

| Ghi chú | Khi nào |
|---|---|
| `Dịch rút gọn: vế Việt chỉ dài khoảng X% mức thường gặp; bản Việt không nhắc tới: …` | Vế Việt ngắn hơn một nửa mức thường gặp của chính tác phẩm (trong đoạn đã biết là rút gọn: ngắn hơn 70%). Kèm tên riêng, can chi chỉ có ở vế Hán |
| `Vế Việt dài gấp khoảng X lần mức thường gặp…` | Vế Việt dài hơn 2 lần mức thường gặp: có thể có diễn giải của dịch giả |
| `Vế Việt có chú thích của dịch giả: «(…)»` | Vế Việt có đoạn trong ngoặc dài từ 40 ký tự |
| `Câu Hán ngay sau không có bản dịch, không đưa vào dữ liệu: «…»` | Có câu không ghép được ngay sau cặp này (cũng có dạng cho câu Việt) |

Ghi chú nằm ở cột `Ghi chú` của sheet `TRUY_VET`. Riêng tác phẩm có `cot_ghi_chu: true` trong cấu hình (hiện là HCB_11, theo yêu cầu của giảng viên) thì sheet `DONG_HANG` có thêm cột thứ ba `Ghi chú`; TSV vẫn đúng 2 cột.

### 6.2. Hiệu đính kỹ từng cặp (công cụ nâng cao)

Mở **Công cụ nâng cao → Hiệu đính** và chọn tác phẩm. App chỉ hiện các cặp **máy gắn cờ**, cặp rủi ro cao nhất ở trên cùng: với dữ liệu của Kiên là 203/3.490 cặp, khoảng 6%. Ví dụ, mục đầu hàng đợi của HCB_11 là 5 câu Hán bị ghép với một câu Việt tóm tắt. **Cặp không ai xem thì giữ nguyên kết quả máy**, nên xem được đến đâu hay đến đó, không bắt buộc xem hết.

Mỗi cặp hiện ba thứ: lý do máy nghi ngờ (ví dụ `Chỉ vế Việt có: 邵曄 (Thiệu Diệp)`), cặp ngay trên và cặp ngay dưới để đối chiếu ranh giới. Thao tác:

| Phím | Nút | Khi nào dùng |
|---|---|---|
| `1` | ✓ Đúng | Cặp đúng; máy nghi oan |
| `2` | ✗ Sai, bỏ | Hai vế không khớp, không sửa được; cặp bị bỏ khỏi bản xuất |
| `3` | ⤒ Gộp với cặp trên | Cặp này thực ra là phần tiếp của cặp trên |
| `4` | ⤓ Gộp với cặp dưới | Cặp này thiếu phần nằm ở cặp dưới |
| `5` | ✎ Sửa chữ | Cắt bớt hoặc sửa chữ; lưu bằng `Ctrl+Enter` |
| `→` / `←` | Bỏ qua / quay lại | |
| `U` | ↶ Hoàn tác | |

Muốn rà các lỗi giống nhau trên toàn tác phẩm (Guideline §8 yêu cầu), đổi sang chế độ **"Tìm trong mọi cặp"** rồi tìm theo chữ Hán, chữ Việt hoặc mã cặp.

**Quyết định được lưu và tự áp ra sao:**
- Mỗi thao tác được ghi ngay vào `hieu_dinh/<MA>__<tên bạn>.tsv`. Mỗi người một tệp nên không xung đột git. **Nhớ commit thư mục `hieu_dinh/`.**
- Quyết định gắn với mã câu, không gắn với số thứ tự cặp. Vì vậy **chạy lại chương trình không mất công hiệu đính.** Nếu sửa cấu hình làm một cặp bị ghép khác đi, quyết định cũ của cặp đó tự bị bỏ qua; dòng xuất sẽ ghi số quyết định không còn khớp.
- Quyết định được áp mỗi lần xuất. Sau khi xem xong, bấm **Cập nhật bản xuất** (vài giây, không cần chạy lại từ đầu).
- Sheet `TRUY_VET` trong file Excel có thêm cột `Hiệu đính`. Sheet `THONG_KE` ghi số cặp đã xác nhận, sửa, gộp và bỏ.

Ý nghĩa các cờ:

| Cờ | Nghĩa |
|---|---|
| `lech_do_dai` | Độ dài hai vế lệch nhiều so với tỷ lệ chung của quyển |
| `lech_moc` | Có can chi hoặc tên riêng ở một vế mà vế kia không có |
| `rut_gon` | Thuộc đoạn đã biết là dịch rút gọn |
| `n-m` | Gộp nhiều câu ở cả hai vế |

**Không sửa tay** tệp trong `work/<MA>/xuat/` hay `04_dong_hang/`, vì lần xuất sau sẽ ghi đè.

---

## 7. Bàn giao

**Cách dễ nhất: tải về.** Trên trang chính, bấm **⬇ Tải về** ở thẻ tác phẩm hoặc **⬇ Tải tất cả**. Máy tự cập nhật bản xuất, kiểm định, rồi trình duyệt tải tệp `.zip` về thư mục Downloads. Trong `.zip`, mỗi tác phẩm là một thư mục theo Guideline mục 2 và nhận xét của giảng viên (18/11):

```
CV02_HCB_11/
├── 01_nguon/            dữ liệu đã tải/crawl (nguyên bản; .pdf là bản in trang nguồn để đối chiếu)
├── 03_text_sach/        han.txt, viet.txt – text Hán và Việt đã trích xuất và làm sạch
├── 04_dong_hang/        HCB_11_parallel.tsv, HCB_11_parallel.xlsx
└── bao_cao.md           số cặp, phạm vi và độ phủ, số dòng, kết quả tự kiểm tra, nguồn, công cụ
```

Không có `02_ocr_tho`: nguồn là text số, không phải ảnh/PDF scan, nên không có bước OCR. Trong `03_text_sach` chỉ có hai tệp `han.txt` và `viet.txt` do chương trình sinh ra; không đặt thêm tệp text tự làm vào đây.

Tải về **không ghi gì vào repo**. Nếu tác phẩm chưa đạt kiểm định, app báo lỗi và không tải.

**Ghi thẳng vào `04_dong_hang` trong repo** (khi nhóm muốn commit bản nộp): vào **Công cụ nâng cao**, bấm **Bàn giao** ở dòng tác phẩm. App hỏi xác nhận và báo còn bao nhiêu cặp gắn cờ chưa xem. Dùng dòng lệnh thì gõ:

```
python -m hvalign run --work HCB_xx --ban-giao
```

Cả hai cách đều áp quyết định hiệu đính, rồi ghi `<MA>_parallel.tsv` và `.xlsx` vào `CV02_<MA>/04_dong_hang/` (thư mục nộp), và kiểm định ngay tại đó. Báo cáo nộp lấy số liệu từ `work/<MA>/bao_cao.md`.

---

## 8. Báo lỗi thường gặp và cách xử lý

| Bạn thấy | Nguyên nhân | Cách xử lý |
|---|---|---|
| `No module named hvalign` | Đang không đứng ở thư mục gốc repo | `cd` vào thư mục có `hvalign/` |
| `No module named yaml` | Chưa cài thư viện | `pip install -r requirements.txt` |
| `✗ X.txt: không phải UTF-8 (byte lỗi ở vị trí 0). Mở tệp bằng Notepad / VS Code rồi lưu lại với mã hóa UTF-8.` | Tệp lưu bằng mã hóa cũ (Big5, GBK, VNI…) | Notepad: *File → Save as → Encoding: UTF-8*. Lưu ý: việc này làm đổi SHA-256 trong manifest |
| `! quyển 1: thiếu bản Việt` rồi `✗ không có cặp nào …` | Thiếu một bản, hoặc hai bản bị nhận ra số quyển khác nhau | Chạy `inventory`, xem cột `quyển`. Đổi chỗ tệp hoặc khai báo tay (5G) |
| `✗ Thiếu tệp …segments.jsonl. Hãy chạy các bước trước đó…` | Chạy một bước lẻ (ví dụ `align`) khi chưa chạy các bước trước | Dùng `run --work <MA>` |
| `✗ Không ghi được tệp ([Errno 13] Permission denied): tệp đang mở, thường là trong Excel.` | File Excel kết quả hoặc sổ hiệu đính đang mở | Đóng Excel rồi chạy lại |
| Số cặp hiện dưới tên `chua_phan_cong` | Thiếu dòng trong `config/phan_cong.tsv` | Thêm dòng (mục 2.2), cột ngăn bằng TAB |
| `tầng 1 ghép theo mục ở 0/1 quyển` | Số đề mục hai bản khác nhau, nên tầng 1 phải dóng cả quyển một lần | Bình thường với tác phẩm không có đề mục (HCB_04). Nếu là do một bản thừa mục thì dùng `loai_tru` (5A) |
| Lỗi YAML (`ScannerError`, `mapping values are not allowed`) | Thụt lề bằng TAB, hoặc chuỗi có `:` mà không có ngoặc kép | Sửa theo lưu ý đầu mục 5 |
| `✗ Cổng 8765 đang bận` | App đã mở ở một cửa sổ khác | Mở `http://127.0.0.1:8765` trên trình duyệt, hoặc chạy `python -m hvalign app --cong 8766` |
| App báo `chọn tên của bạn` | Chưa chọn tên ở góc trên bên phải | Chọn tên; chưa có thì chọn "+ tên khác…" (viết không dấu) |
| App báo `không ghi được … tệp đang mở` | Tệp trong `hieu_dinh/` đang mở ở Excel | Đóng Excel |
| App ghi `✗ Lỗi chương trình (hãy báo cho nhóm)` hoặc lỗi khác có `Traceback` | Lỗi của chương trình | Ghi lệnh, mã tác phẩm và 5 dòng cuối của lỗi vào `Docs/kiem_tra_hvalign_<ten>.md`, báo Kiên |

---

## 9. Làm việc với git

**Mỗi buổi làm việc:**

```
git pull                                   # lấy bản mới của cả nhóm
python -m hvalign run --work <các mã của bạn>     # hoặc bấm Chạy trong app
git add config/ Docs/ CV02_<MA>/ hieu_dinh/  # chỉ thêm phần mình sửa
git commit -m "HCB_06: loại trừ phần chưa dịch"
git push
```

**Quy tắc:**
- `work/` không đưa lên git (đã có trong `.gitignore`), vì chạy lại là có.
- **Không** dùng `git push --force`.
- **Xung đột ở tệp sinh ra** (`03_text_sach/`, `04_dong_hang/`, `bao_cao.md`): không sửa tay. Chọn một bên rồi chạy lại `run`, rồi commit kết quả.
- **Xung đột ở `config/phan_cong.tsv`:** giữ dòng của cả hai bên.
- Sửa code trong `hvalign/` thì phải chạy `python -m pytest -q` và chạy lại `run` cho mọi tác phẩm trước khi push (xem [phan_viec_hvalign.md](phan_viec_hvalign.md), mục 4).

---

## 10. Bảng lệnh

| Lệnh | Làm gì |
|---|---|
| `inventory` | Kiểm kê nguồn: đủ cặp Hán–Việt, SHA-256, trùng bài sillok |
| `run` | Chạy tất cả: `extract → clean → segment → align → export → validate → report` |
| `extract` / `clean` / `segment` / `align` | Chạy riêng Bước 4 / 5 / 6 / 7 |
| `export` / `validate` / `report` | Xuất TSV + XLSX và sổ hiệu đính / kiểm định / báo cáo |
| `status` | Số cặp theo tác phẩm và thành viên |
| `app` | Mở giao diện web (`--cong 8766` để đổi cổng; `--khong-mo-trinh-duyet`) |
| `mau` | Xuất mẫu ngẫu nhiên ra Excel (`--so-cap N`, mặc định 30); chấm trong app thì không cần lệnh này |

Tùy chọn chung:
- `--work HCB_01 HCB_04`: chỉ chạy các tác phẩm này.
- `--ban-giao`: xuất vào `04_dong_hang/`.
- `--help`: xem trợ giúp.

---

## 11. Giới hạn hiện tại

- **Ghi chú tự động dựa trên độ dài và tên riêng**, không hiểu nghĩa câu. Nó bắt được chỗ dịch rút gọn rõ rệt, nhưng một cặp lệch ranh giới mà độ dài vẫn bình thường thì không có ghi chú. Trong vùng dịch rút gọn của HCB_11 có vài cặp lệch ranh giới như vậy (ví dụ `政不施焉，則君子不臣其人。` ↔ `Sứ giả nói:`); nên lướt tab **Cặp có ghi chú** của HCB_11 và bấm **Bỏ** những cặp đó.
- **Hàng đợi hiệu đính (nâng cao) chỉ gồm cặp có cờ.** Lỗi mà máy không gắn cờ chỉ lộ ra khi chấm mẫu; khi đó dùng "Tìm trong mọi cặp" để rà các cặp tương tự.
- **Câu không ghép** (`khong_ghep.tsv`) chưa ghép tay được trong app; xem bằng *Mở… → Câu không ghép*.
- **Trọng số dóng hàng đặt tay**, chưa chỉnh trên bộ mẫu chuẩn. Tỷ lệ lỗi phải tự đo bằng chấm mẫu.
- **Mốc dóng hàng:** chỉ dùng can chi và các cặp tên riêng thu từ chính bản Việt, chưa dùng từ điển Unihan hay embedding.
- **Chưa có:** lệnh tải bài sillok (Tài), chấm câu HCB_03 (Huy), luật thơ 4 phần R11 (Đăng). Xem [phan_viec_hvalign.md](phan_viec_hvalign.md).
