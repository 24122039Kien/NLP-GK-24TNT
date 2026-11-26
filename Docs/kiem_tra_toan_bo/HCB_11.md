# HCB_11 – 後漢書 卷86 / Hậu Hán thư quyển 86 (Kiên)

**Trạng thái:** XONG (đợt 1, 2026-11-26). Đã đọc hết; sau khi sửa còn **499 cặp**, tất cả đúng. Bản dịch Việt là bản rút gọn, nên cột "Ghi chú" trong .xlsx ghi rõ phần bị lược (theo trả lời của GV ngày 16/11).

| Bước | Kết quả |
|---|---|
| 1. Tài liệu | Đủ `01_nguon`, `03_text_sach`, `04_dong_hang` (.tsv, .xlsx có cột Ghi chú), `bao_cao.md`; có trong `phan_cong.tsv` (`*`, Kien) |
| 2. Nguồn | Hán: zh.wikisource 後漢書/卷86. Việt: vi.wikisource Biên dịch:Hậu Hán thư/Quyển 86. 4/4 tệp khớp SHA-256; đúng quyển; bản Việt dịch trọn quyển (có rút gọn) |
| 3. Bản text | Hán 59 dòng, Việt 60 dòng; không sót markup. Mã lỗi chữ [BD77], [B258], [E8E6], [CF3D] và thẻ <曷毛>, <名頁> có sẵn trong nguồn wikisource |
| 4. Dóng hàng | Có 5 chỗ lệch ranh giới, đã sửa bằng gộp kèm ghi chú phần bị lược. Độ phủ 100% / 100% |

## Lỗi và cách sửa (số cặp theo bản trước khi sửa)

| Cặp | Lỗi | Sửa |
|---|---|---|
| 148–150 | Lý do 2–4 của Lý Cố: câu kết 其不可二也 / 其不可三也 bị ghép vào cặp "Ba là" / "Bốn là" | `gop`, có ghi chú |
| 149–152 (sau lần gộp trên) | Lý do 5–7 bị lệch tương tự, cộng thêm 其不可七也 + chuyện Doãn Tựu | `gop`, có ghi chú |
| 155–156 | Câu Việt "treo thưởng phong Hầu…" là bản dịch của 有能反間致頭首者 ở cặp sau | `gop`, có ghi chú |
| 219–221 | Lời Trình Bao: vế Việt trượt đi một cặp ("Bao thưa: 7 họ…" ↔ 程包對曰「板楯七姓…」); câu 羌人畏忌…連摧破之 không được dịch | `gop`, có ghi chú phần bị lược |
| 377–378 | Sớ Chu Phủ: "Truyện nói: «Đường Kỳ…»" là bản dịch của 傳曰 ở cặp trước; 詩人誦詠，以爲符驗 không được dịch | `gop`, có ghi chú |

Nhờ Bước 6 không tách câu sau ':' nữa, máy tự ghép đúng thêm 4 chỗ mà trước đây sai: "hát rằng:" ↔ 歌曰, "nói:" ↔ 曰 (cặp 302, 363 theo số mới), "Bao thưa:", "Chu Phủ thượng sớ nói:".

Ba quyết định cũ bị đổi mã câu nên đã được ghi lại theo mã mới, các mã cũ rút bằng `xoa`: gộp Ngư Hủ (máy nay tự ghép 5-1), gộp lời Chu Công 95+96, và ghi chú của cặp 97.

## Ghi chú khi đọc

- Phần thơ Bạch Lang (三章): mỗi câu Hán gồm phần nghĩa và phần phiên âm, ứng với dạng "nghĩa (phiên âm)" bên Việt. Các cặp 2-1 ở đây là đúng.
- Cờ `rut_gon` / `lech_do_dai` ở phần lời tâu của Lý Cố và Trình Bao là đúng thực tế: bản Việt rút gọn, đã có ghi chú.
