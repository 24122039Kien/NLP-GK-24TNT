# HCB_01 – 續資治通鑑 / Tục tư trị thông giám, quyển 1–20 (cả 4 người)

**Trạng thái:** quyển 1–10 XONG (đợt 5, 26–27/11). Quyển 11–20 để đợt 6.

Sau đợt 5, HCB_01 có **8.092 cặp** (trước đó 8.094). Quyển 1–10 có 4.285 cặp (#1–#4285), đã đọc hết 4.285/4.285. Sau khi sửa, tất cả đều đúng.

| Quyển | Người | Số cặp | # | Kết quả |
|---|---|---|---|---|
| 1 | Tài | 419 | 1–419 | Sửa #15–17, #95–97 (khúc `q1_a`, `q1_b`); bỏ ngoặc dịch lời chú ở #97, #415 |
| 2 | Kiên | 451 | 420–870 | Bỏ ngoặc dịch lời chú ở #428, #444, #631, #749 |
| 3 | Huy | 394 | 871–1264 | Sửa #1229–1230 (khúc `q3_a`); chữ PUA #1014 (渾瑊), #1027 (踰) |
| 4 | Đăng | 398 | 1265–1662 | Đúng hết |
| 5 | Huy | 495 | 1663–2157 | Bỏ 2 cặp lặp; bỏ chữ rác #1886, #1948, #1959; ghi chú #1891 |
| 6 | Kiên | 371 | 2158–2528 | Sửa #2210–2211, #2372–2374, #2421–2422, #2454–2455 (khúc `q6_a`…`q6_d`) |
| 7 | Huy | 454 | 2529–2982 | Chữ ghép bộ #2663 (扌晉 → 搢) |
| 8 | Tài | 438 | 2983–3420 | Chữ ghép bộ #3315 (衤復 → 複) |
| 9 | Đăng | 405 | 3421–3825 | Sửa #3421–3425 (khúc `q9_a`), #3772–3773 (khúc `q9_b`) |
| 10 | Kiên | 460 | 3826–4285 | Chữ ghép bộ #4049 (钅句 → 鉤) |

Số # là số thứ tự trong `CV02_HCB_01/04_dong_hang/HCB_01_parallel.tsv` sau khi sửa.

## Bước 1–3: tài liệu, nguồn, bản text

- **Đủ tài liệu:** có `01_nguon`, `03_text_sach`, `04_dong_hang` (.tsv, .xlsx) và `bao_cao.md`. Cả 20 quyển có trong `phan_cong.tsv`.
- **Nguồn:** tải lại 20 trang (10 quyển × Hán/Việt) qua API wikisource để đối chiếu.
  - Tệp `.wikitext` giống hệt bản hiện hành.
  - Tệp `.txt` của Huy (q3, 5, 7, cả Hán lẫn Việt) là wikitext lưu với đuôi .txt, đủ chữ.
- **Manifest:** thêm q1, q8 (Tài) vào `nguon_manifest_Tai.tsv` và q4, q9 (Đăng) vào `nguon_manifest_Dang.tsv`; điền revid cho q3, 5, 7 (Huy). 30/30 tệp khớp SHA.
- **Bản text:** không sót markup. Lỗi chữ của nguồn zh được xử lý ở bước 4 (xem dưới).

## Lỗi hệ thống đã sửa

| Lỗi | Hậu quả | Cách sửa |
|---|---|---|
| Bản Việt q1 mở đầu bằng đoạn tiểu sử Thái Tổ. Đây là bản dịch của lời chú nhỏ `{{*|帝諱匡胤…}}`, mà bên Hán đã bỏ (R04) | Câu Việt thừa, không có vế Hán | `loai_tru` bên Việt `HCB_01/q001/viet/s00/p001` trong `config/works/HCB_01.yaml`. Không cặp máy nào thay đổi |
| Trang zh và vi của quyển 5 đều chép trùng đoạn 「戊申，北漢主殂…」 | 2 cặp lặp (#1875–1876 cũ) | `sai` 2 cặp lặp (Huy). Từ đó số # lùi 2 |

## Sửa tay (human in the loop)

Hiệu đính ghi ở `hieu_dinh/HCB_01__<người>.tsv`, gồm 40 quyết định: 37 `sua`, 2 `sai`, 1 `dung`. Tệp khúc lưu ở `Docs/kiem_tra_toan_bo/khuc/HCB_01/`.

**Chia lại ranh giới** (`cong_cu/chia_lai.py`; chữ Hán và chữ Việt của khúc giữ nguyên tuyệt đối):
- q1 #15–17, #95–97; q3 #1229–1230; q6 #2210–2211, #2372–2374, #2421–2422, #2454–2455: máy trượt 1 vế, vì bản Việt gộp hoặc tách câu khác bản Hán.
- q9 #3421–3425: nguồn zh đặt tiêu đề 太宗至仁應運…皇帝 **sau** đoạn tiểu sử, còn bản Việt đưa tên hiệu lên đầu câu, nên cả 5 cặp trượt 1 vế.
- q9 #3772–3773: vế Việt "Bân đáp" (彬對曰) bị ghép vào cặp trước.

**Bỏ ngoặc dịch lời chú nhỏ:** bên Hán, R04 đã bỏ lời chú `{{*|…}}`, nhưng bản Việt dịch cả lời chú này trong ngoặc. Phần ngoặc đã được bỏ bằng `sua` ở #97, #415 (Tài) và #428, #444, #631, #749 (Kiên). Ngoặc giải thích ngắn của người dịch ("tức …", "(môn hạ)") thì giữ.

**Lỗi chữ của nguồn zh** (sửa bằng `sua`, chỉ đổi đúng chữ lỗi):
- Chữ PUA, tức bộ thủ ghép với chữ sau: #1014 渾瑊, #1027 踰 (Huy).
- Chữ ghép bộ, tức một chữ bị viết thành bộ thủ + chữ khác: #2663 扌晉 → 搢 (Huy), #3315 衤復 → 複 (Tài), #4049 钅句 → 鉤 (Kiên).
- Ký tự rác: #1886, #1948, #1959 (Huy). #1891 có ghi chú rằng nguồn thiếu tên 霸榮 (`dung`).

## Ghi chú

- Lỗi chữ có nghĩa của nguồn được giữ nguyên, ví dụ 「餘斌」 (thay cho 全斌) ở #3366 và ngày can chi sai thứ tự 「丙子…丁卯」 ở #3321–3322. Bản Việt thiếu dấu ở vài chữ ("nuoc", "Bon", "duong", #3836–3839) cũng giữ nguyên, vì là lỗi của bản dịch.
- Còn 4 chỗ chữ ghép bộ ở q17–19 (#6686 钅屈, #7157 và #7358 鹿阝, #7451 扌捲). Để sửa ở đợt 6.
- Cảnh báo kiểm định: 13 cặp trùng lặp và 38 câu Hán lặp. Đây là câu lặp thật (帝曰, 不許…) ở các chỗ khác nhau.
