# HCB_09 – 後漢書 卷76 循吏列傳 / Hậu Hán thư quyển 76, Tuần lại liệt truyện (Huy)

**Trạng thái:** XONG (đợt 2, 2026-11-26). Trước khi sửa có 132 cặp, trong đó có các cặp lệch 10-1, 9-1, 1-10. Sau khi sửa có **159 cặp** (1-1×158), đã đọc hết 159/159, tất cả đúng. Không còn câu không ghép.

| Bước | Kết quả |
|---|---|
| 1. Tài liệu | Đủ `01_nguon`, `03_text_sach`, `04_dong_hang` (.tsv, .xlsx), `bao_cao.md`; có trong `phan_cong.tsv` (`*`, Huy) |
| 2. Nguồn | Hán: khớp SHA với manifest; chữ trùng với trang 後漢書/卷76 hiện tại (chỉ khác thẻ `<onlyinclude>`). **Bản Việt tải thiếu**, đã tải lại |
| 3. Bản text | Không cảnh báo |
| 4. Dóng hàng | 159 cặp, đọc hết, đúng |

**Phạm vi song ngữ:** bản Việt chỉ dịch lời tựa, 衛颯 (Vệ Táp), 任延 (Nhâm Diên), 孟嘗 (Mạnh Thường) và bài Tán. 9 truyện còn lại đã có `loai_tru` từ trước (王景 … 童恢), đúng với yêu cầu chỉ dóng phần song ngữ.

## Lỗi đã sửa

| Lỗi | Hậu quả trước khi sửa | Cách sửa |
|---|---|---|
| Bản Việt trong `01_nguon` mất khối `<div style="background-color:pink">`: 4 đoạn Nhâm Diên làm Thái thú Cửu Chân (dạy cày bừa, cưới hỏi của dân Lạc Việt) và Tích Quang ở Giao Chỉ (~20 câu) | Các câu Hán này ghép 10-1, 9-1 vào câu Việt khác | Tải lại wikitext **Biên dịch:Hậu Hán thư/Quyển 76** (revid 204344, 2026-03-16). Cập nhật `Docs/nguon_manifest_Huy.tsv`: SHA-256 `7ee7b584…` |
| Bài Tán bên Việt có kèm "Chú thích từ văn bản", tức bản dịch các lời chú nhỏ `{{*|…}}` mà bên Hán đã bỏ theo R04 | Cặp Tán ghép 1-10 | `loai_tru` (regex, `den_het_quyen`). Các số chú thích "(1)…(4)" trong câu Tán đã được R07 bỏ sẵn |

## Ghi chú khi đọc

- Cặp 106 (2-1) 「章句既通。悉顯拔榮進之。」: nguồn Hán chấm câu ở giữa, bản Việt gộp làm một câu. Ghép như vậy là đúng.
- Cặp 138: nguồn Hán có 2 chữ thừa 「榧齔」 trước 桓帝時. Đây là lỗi của bản wikisource, giữ nguyên vì không sửa nguồn.
