# HCB_03 – 東都事略 卷130 附録八 交趾 / Đông Đô sự lược quyển 130 (Huy)

**Trạng thái:** XONG (đợt 2, 2026-11-26). Trước khi sửa có 8 cặp, phần lớn sai. Sau khi sửa tận gốc có **59 cặp**, đã đọc hết 59/59, tất cả đúng. Độ phủ 100% / 100%. Không còn câu không ghép.

| Bước | Kết quả |
|---|---|
| 1. Tài liệu | Đủ `01_nguon`, `03_text_sach`, `04_dong_hang` (.tsv, .xlsx), `bao_cao.md`; có trong `phan_cong.tsv` (`*`, Huy) |
| 2. Nguồn | Hán: zh.wikisource 東都事略/卷130 (bản Tứ khố). Việt: vi.wikisource Biên dịch:Đông Đô sự lược/Quyển 130. 2/2 tệp khớp SHA-256 với `nguon_manifest_Huy.tsv`. Bản Việt dịch trọn bài, kể cả lời bàn 臣稱曰 |
| 3. Bản text | Có 2 lỗi, đã sửa (xem dưới): 2 mã chữ chưa tra, và bản Hán không có dấu câu |
| 4. Dóng hàng | 59 cặp: 1-1×54, 2-1×2, 3-1×1, 4-1×2. Đã đọc hết, đúng |

## Lỗi đã sửa (tận gốc, chạy lại ra cùng kết quả)

| Lỗi | Hậu quả trước khi sửa | Cách sửa |
|---|---|---|
| Mã chữ `{{SKchar|2652}}`, `{{SKchar|1440}}` chưa có trong bảng R09 | Còn `[？SKchar|2652]` trong text sạch; dấu `？` trong mã còn làm cắt câu sai chỗ | Tra bằng API zh.wikisource: 2652 = 𫝊 (U+2B74A, dị thể 傳), 1440 = 𤋮 (U+242EE, dị thể 熙; bản Việt cũng ghi 𤋮寧). Thêm vào `resources/char_fix.tsv` |
| Bản Hán (Tứ khố) không có dấu câu: cả bài là một khối khoảng 1.450 chữ | Chỉ tách được 1 câu Hán cho mỗi đoạn, nên các cặp là cả khối dài ghép với 9–10 đoạn Việt | Thêm tính năng **chấm câu thủ công** (R13, khóa `cham_cau_thu_cong`, đúng đặc tả ở `phan_viec_hvalign.md` 3.1): `resources/cham_cau/HCB_03_q130.txt`. Chương trình chỉ thay khi bỏ hết dấu câu thì giống hệt khối Hán từng chữ. Lệch thì không thay và ghi cảnh báo R13. Có kiểm thử `test_r13_manual_punctuation_only_when_same_chars` |
| Tầng 2 chỉ cho một đoạn ứng tối đa 8 đoạn bên kia (`tang2_max: 8`) | Đoạn Hán duy nhất ứng với 16 đoạn Việt, nên 8 đoạn Việt cuối bị dồn sang đoạn 臣稱曰 | `dong_hang.tang2_max: 20` trong `config/works/HCB_03.yaml`, giống HCB_02 và HCB_12 |
| Dòng tên sách / tên quyển / lạc khoản (欽定四庫全書, 東都事略卷一百三十…) và phần "Chú thích" của trang Việt | Bị ghép thành cặp, ví dụ "Đông Đô sự lược, quyển 130. Nguồn bổ sung:" | `loai_tru` (3 khối Hán, 3 khối Việt, mục Chú thích) |

**Cách chấm câu:** `。` đặt ở chỗ hết câu, theo cách ngắt câu của bản dịch. Các vế liền ý dùng `，` hoặc `；`, lời nói dùng 「」. Không thêm, bớt hay đổi chữ nào; chương trình tự kiểm điều này.

## Ghi chú viết tay (`hieu_dinh/HCB_03__Huy.tsv`, quyết định `dung`)

- **Cặp 39** (儂智髙反…): bản dịch ghi "Lý Càn Đức" đem quân, nhưng theo bản Hán người đem quân là Đức Chính (徳政). Cặp vẫn dóng đúng.
- **Cặp 45** (…遂謀入冦): bản dịch gắn 𤋮寧 vào cuối câu ("mưu vào cướp Hy Ninh"). Đúng ra 𤋮寧八年 là năm Hy Ninh thứ 8, mở đầu câu sau. Cặp vẫn dóng đúng.

## Ghi chú khi đọc

- Cặp 5: bản Việt có thêm "(Trung Quốc)" là lời dịch giả, chấp nhận được.
- Cặp 20, 49 (4-1) và 21 (3-1): bản Việt dịch cả chuỗi sự việc trong một câu. Bên Hán là các vế nối bằng `；`, nên ghép như vậy là đúng.
