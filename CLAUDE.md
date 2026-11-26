# CLAUDE.md – Đồ án GK dóng hàng Hán–Việt (CV02)

Hướng dẫn cho Claude khi làm việc trong thư mục `Lab/GK`. Đọc hết tệp này trước khi làm gì.

## 0. Việc đầu tiên mỗi phiên

1. Đọc `Docs/kiem_tra_toan_bo/TIEN_DO.md`. Nếu có việc dở dang thì làm tiếp **đúng chỗ đã dừng**: không đọc lại phần đã xong, không bỏ sót phần chưa đọc. Chi tiết từng tác phẩm nằm ở `Docs/kiem_tra_toan_bo/<MA>.md`.
2. `git status` và `git log --oneline -5`: xem có thay đổi chưa commit hay commit mới của bạn trong nhóm không.

## 1. Sắp hết quota hoặc context: ghi bàn giao NGAY

Khi thấy quota hoặc context sắp hết, hoặc phải dừng giữa chừng, **trước khi dừng** phải cập nhật `Docs/kiem_tra_toan_bo/TIEN_DO.md`:

- **Đang làm:** đợt nào, tác phẩm nào, quyển nào, đã đọc tới cặp số mấy (theo thứ tự trong `work/<MA>/xuat/<MA>_parallel.tsv`).
- **Đã sửa:** tệp cấu hình hoặc tệp hiệu đính nào. Đã chạy lại và kiểm chứng chưa, đã commit chưa.
- **Bước tiếp theo:** ghi cụ thể, để phiên sau làm được ngay mà không phải đoán.
- Lỗi hoặc nghi vấn còn mở.

Ghi tiến độ thường xuyên (sau mỗi khúc cặp đọc xong), không đợi tới cuối. Phiên sau bắt đầu bằng mục 0.

## 2. Nhóm và repo

- Nhóm 4 người: **Kiên** (người dùng), Huy, Tài, Đăng. Mỗi người cần **≥ 2.000 cặp** sau hiệu đính.
- Đề tài CV02, 14 tác phẩm HCB_01 → HCB_14. Phân công ở `config/phan_cong.tsv` (HCB_01 và HCB_14 chia quyển cho cả 4 người).
- Repo: https://github.com/24122039Kien/NLP-GK-24TNT, nhánh `main`.
- Chương trình: `hvalign` (Bước 4 → 7, xuất, kiểm định, báo cáo). Hướng dẫn ở `Docs/huong_dan_hvalign.md`.
- Mỗi phiên làm việc có báo cáo `Docs/reportN.md` (phiên mới nhất là số lớn nhất).

## 3. Quy tắc bắt buộc

- **Commit và push chỉ khi người dùng yêu cầu.** Người dùng bảo "commit" thì chỉ commit; bảo push mới push.
- **Không thêm** dòng `Co-Authored-By: Claude …` hay "Generated with Claude Code" vào commit hoặc PR.
- Email cá nhân của người dùng là thông tin riêng. Repo dùng email noreply của GitHub.
- **Không sửa tay nội dung `01_nguon/`.** Nguồn thiếu hoặc sai thì tải lại bản đúng:
  - User-Agent chung `HanVietAlignStudentProject/1.0 (university NLP course project)`, giãn cách 3 giây, không đưa email hay thông tin cá nhân vào yêu cầu;
  - ghi vào manifest `Docs/nguon_manifest*.tsv`.
- Tác phẩm của Huy, Tài, Đăng: được tự sửa. Quyết định hiệu đính ghi vào `hieu_dinh/<MA>__<tên người làm>.tsv`.
- Sửa code trong `hvalign/`:
  1. chạy `python -m pytest -q`;
  2. chạy lại `python -m hvalign run` cho cả 14 tác phẩm;
  3. so dấu vân tay các tệp nộp. Chỉ được đổi đúng những gì cố ý sửa.
- Thử app hoặc thử nghiệm thì làm trên bản sao trong scratchpad, không ghi vào `hieu_dinh/` thật.
- Mọi tệp sinh ra phải **giống hệt nhau giữa các máy và giữa các lần chạy**: không đưa ngày giờ, đường dẫn máy hay số phiên bản vào nội dung tệp. Riêng dòng ngày trong `bao_cao.md` là ngoại lệ đã biết.
- Lệnh trên Windows: đặt `PYTHONUTF8=1 PYTHONIOENCODING=utf-8`. Script nằm ngoài repo cần `PYTHONPATH=.`.

## 4. Yêu cầu của giảng viên (bắt buộc theo)

**Trả lời Q&A ngày 16/11** (ảnh ở `QA/`):
- Chỉ dóng phần **có song ngữ**. Phần chỉ một bản có thì loại trừ (cấu hình `loai_tru` trong `config/works/<MA>.yaml`).
- HCB_11 là bản dịch rút gọn: vẫn dùng được, nhưng .xlsx phải có cột **"Ghi chú"** nêu rõ phần bị lược hoặc không được dịch (`cot_ghi_chu: true`). TSV vẫn giữ 2 cột.
- HCB_14: được lấy bản Hán từ sillok (sillok.history.go.kr).

**Nhận xét bản demo ngày 18/11:**
- "Kết quả dóng hàng tốt, có ghi chú rõ ràng."
- "Cần xác nhận cuốn HCB_11 chỉ mới thực hiện 1 phần, chưa đủ toàn bộ."
  - Bản demo chỉ trích 49 cặp đầu của HCB_11.
  - Bản đầy đủ dóng **toàn bộ Hậu Hán thư quyển 86** (cả phạm vi được giao), 512 cặp, độ phủ 100% chữ Hán và 100% âm tiết Việt. Số liệu này ghi ở `CV02_HCB_11/bao_cao.md` mục 1.
  - Mọi `bao_cao.md` đều có dòng "Phạm vi được giao / đã dóng / độ phủ".
- "File output cuối cùng nên có thêm folder **03_text_sach** chứa text Hán và Việt sau khi đã trích xuất và làm sạch. Với nguồn không phải ảnh/PDF scan thì **không cần folder 02**. Có thể bổ sung **folder 01** (dữ liệu đã tải/crawl)."

Cấu trúc nộp hiện tại (từ hvalign 0.3.1):

```
CV02_HCB_xx/
├── 01_nguon/        dữ liệu đã tải/crawl (.pdf = bản in trang nguồn để đối chiếu, không phải scan)
├── 03_text_sach/    CHỈ có han.txt, viet.txt do hvalign sinh ra
├── 04_dong_hang/    HCB_xx_parallel.tsv, HCB_xx_parallel.xlsx
└── bao_cao.md
```

- Không có `02_ocr_tho`. Text thô trung gian nằm ở `work/<MA>/02_ocr_tho` và không nộp.
- Mốc tên riêng cho dóng hàng lấy thẳng từ `01_nguon`, nên mọi máy ra cùng kết quả.

**Còn chưa chốt:** Guideline ghi sheet `DONG_HANG`, tiêu đề `Hán`/`Việt`, nhưng `example.xlsx` của giảng viên dùng `Sheet1`, tiêu đề `han`/`vi`, TSV CRLF. Chương trình đang theo Guideline. Nhắc người dùng hỏi lại giảng viên nếu chưa hỏi.

## 5. Nhiệm vụ đang làm: kiểm tra toàn bộ (người dùng giao ngày 26/11)

Kiểm **từng tác phẩm, từng quyển, đọc MỌI cặp**, không bỏ cặp nào. Đọc theo khúc khoảng 150–200 cặp mỗi lượt để tiết kiệm context.

**6 đợt (sau mỗi đợt thì dừng, báo người dùng và chờ người dùng đồng ý mới sang đợt sau):**

| Đợt | Tác phẩm |
|---|---|
| 1 | HCB_04, 05, 07, 11, 13 (Kiên) |
| 2 | HCB_03, 06, 08, 09 (Huy; HCB_03 bản Hán không có dấu câu) |
| 3 | HCB_02, 10, 12 (Tài, Đăng) |
| 4 | HCB_14 |
| 5 | HCB_01 quyển 1–10 |
| 6 | HCB_01 quyển 11–20 |

**Mỗi tác phẩm kiểm 4 bước:**

1. **Đủ tài liệu:** có `01_nguon`, `03_text_sach` (han.txt, viet.txt), `04_dong_hang` (.tsv và .xlsx), `bao_cao.md`. Tác phẩm có trong `phan_cong.tsv` và manifest.
2. **Nguồn đã tải đủ:** mỗi quyển được giao có cả bản Hán lẫn bản Việt. SHA-256 khớp manifest. Bản Việt không thiếu trang, không bị cắt, và đúng là bản dịch của bản Hán đó. Thiếu hoặc sai thì tự tải về.
3. **Đã có bản text:** text thô và `03_text_sach` không rỗng, không sót markup, không lỗi mã hóa, số đoạn hợp lý so với nguồn.
4. **Dóng hàng đúng:** đọc đối chiếu Hán ↔ Việt từng cặp của từng quyển. Ghi kết quả vào `Docs/kiem_tra_toan_bo/<MA>.md`: đã đọc khúc nào, cặp nào sai, kiểu sai, cách sửa.

**Thứ tự sửa, để chạy lại vẫn ra đúng:**

1. Lỗi có hệ thống trước: lệch cả đoạn, thiếu dấu câu, phần không song ngữ. Sửa tận gốc bằng cấu hình `config/works/<MA>.yaml` (`loai_tru`, `dong_hang`…), chấm câu, hoặc sửa `hvalign`.
2. Sau đó mới sửa từng cặp lẻ bằng `hieu_dinh/<MA>__<người>.tsv` (`gop` / `sai` / `sua` / `dung` / `xoa`). Quyết định gắn với mã câu, nên phải làm **sau** khi cách tách câu đã ổn định.
3. Lỗi đã sửa ở mức chương trình thì thêm kiểm thử vào `tests/`.

**Kiểm chứng trước khi coi một đợt là xong:**

1. Chạy hvalign từ đầu trên **bản sao sạch** (clone từ git vào scratchpad).
2. Rà lại đúng các cặp đã sửa.
3. Hai lần chạy cho cùng dấu vân tay.
4. Bản trong `04_dong_hang` khớp với lần chạy lại.
5. Kiểm định ĐẠT.

Sau đó: ghi bản nộp vào `04_dong_hang` + `bao_cao.md`, cập nhật `Docs/report7.md` và `TIEN_DO.md`, commit (khi được bảo), rồi báo người dùng.

**Điểm đã biết, cần xem kỹ:**
- ~~HCB_03: chỉ 8 cặp là đoạn dài~~ → đã sửa ở đợt 2 (chấm câu thủ công R13, 59 cặp).
- Bản Việt do thành viên chép tay (`.txt` không có `{{đầu đề…}}`) có thể mất khối `<div>`, `<poem>`, `{{quote}}`; đợt 2 gặp ở HCB_06, 08, 09. Mỗi đợt phải so với wikitext tải qua API (xem `TIEN_DO.md`).
- Nguồn Hán chấm câu thưa (cả đoạn nối bằng ，) làm cặp rất dài: dùng chấm câu thủ công R13 như HCB_02 (đợt 3), chỉ đổi dấu ở chỗ bản Việt hết câu.
- Manifest: HCB_02, 10, 12 đã bổ sung ở đợt 3; nguồn của Đăng (HCB_01, HCB_14) hầu như chưa có trong manifest, thêm vào `Docs/nguon_manifest_Dang.tsv` khi kiểm.
- HCB_10: bản Hán zh.wikisource là giản thể, không có bản phồn thể dùng được; đã ghi hạn chế, không chuyển bằng máy.
- HCB_14 Q1421, Q1445: vài cặp lệch ranh giới, ví dụ `批、所見是。` ↔ `Lại tâu:`.
- HCB_01 phần của Kiên là 1.958 cặp (< 2.000 nếu tính riêng HCB_01; tổng của Kiên là 3.483).

## 6. Lệnh hay dùng

```
python -m hvalign run [--work HCB_xx ...]   # chạy đủ các bước; xuất vào work/<MA>/xuat
python -m hvalign status                    # bảng số cặp theo tác phẩm / thành viên
python -m pytest -q                         # kiểm thử
python -m hvalign app                       # app web cục bộ (cổng 8765)
```

Ghi bản nộp vào repo: dùng `app.build_zip` rồi giải nén chỉ `04_dong_hang` và `bao_cao.md` vào `CV02_<MA>/`, hoặc chạy `run --ban-giao` (chỉ ghi `04_dong_hang`).
