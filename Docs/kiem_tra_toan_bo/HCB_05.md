# HCB_05 – 交州記 / Giao Châu ký (Kiên)

**Trạng thái:** XONG (đợt 1, 2026-11-26). Đã đọc 70/70 cặp máy; sau khi sửa còn **68 cặp**, tất cả đúng.

| Bước | Kết quả |
|---|---|
| 1. Tài liệu | Đủ `01_nguon`, `03_text_sach`, `04_dong_hang` (.tsv, .xlsx), `bao_cao.md`; có trong `phan_cong.tsv` (`*`, Kien) |
| 2. Nguồn | Hán: zh.wikisource 交州記 (嶺南遺書本). Việt: vi.wikisource Biên dịch:Giao Châu ký. 4/4 tệp khớp SHA-256 với manifest, đúng cùng một bài |
| 3. Bản text | Hán 72 dòng, Việt 74 dòng; không sót markup |
| 4. Dóng hàng | 2 chỗ lệch ranh giới đã sửa bằng gộp (xem dưới). Độ phủ 100% / 100% |

**Loại trừ:** 17 khối Hán và 16 khối Việt. Đây là ghi chú khảo chứng 按 và lời dẫn biến thể (引云…) của người biên tập. Cả hai bên đều có, và đã khớp nhau. Khối Hán dư ra là s02/p030 「章懷太子後漢書和帝紀注引同」: bản Việt không dịch câu này, nên loại là đúng.

## Lỗi đã sửa

| Cặp (trước khi sửa) | Lỗi | Sửa |
|---|---|---|
| 59–60 | Khoản Hán 「枕赤色堪作船作牀」 (s02/p027) bị ghép vào cặp 59. Bản dịch của nó, "Gối đá đỏ có màu đỏ…", lại nằm ở đầu cặp 60, vì người dịch gộp câu này chung một khoản với cây Cổ Độ | `gop` 59 + 60 thành một cặp 3-3, đúng trọn nghĩa (`hieu_dinh/HCB_05__Kien.tsv`) |
| 8–9 (sau khi bỏ tách sau ':') | Bỏ tách sau ':' làm câu "Phong tục thích đánh trống…" bị kéo lên cặp Bà Triệu, còn cặp 9 chỉ còn lời chú "(Ca Khúc nói về: …)" của dịch giả | `gop` 8 + 9 thành cặp 2-5, đúng trọn nghĩa |

## Ghi chú khi đọc

- Cặp 2: nguyên văn wikisource có 「…在湖之中國學」. "國學" có sẵn trong nguồn (đứng trước chú 初學記), không phải lỗi trích xuất, nên giữ nguyên.
- Hai cặp cuối (s03 – số 69, 70 theo cách đánh số cũ): bản Việt bỏ phần ghi xuất xứ 「劉澄之交州記曰」 / 「姚文咸交州記曰」. Chấp nhận được.
- Cặp 9: vế Việt có chú thích của dịch giả. Ghi chú tự động đã nêu.
