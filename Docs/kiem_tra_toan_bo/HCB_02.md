# HCB_02 – 平安南詔 / Bình An Nam chiếu (Tài)

**Trạng thái:** XONG (đợt 3, 2026-11-26). Trước khi sửa có 27 cặp, trong đó cặp 9 là một câu Hán dài ~500 chữ ghép với 15 câu Việt (2-15), và có 2 quyết định gộp. Sau khi sửa có **49 cặp, tất cả 1-1**. Đã đọc hết 49/49, tất cả đúng. Không còn câu nào chưa ghép.

| Bước | Kết quả |
|---|---|
| 1. Tài liệu | Đủ `01_nguon` (.wikitext + .pdf mỗi bên), `03_text_sach`, `04_dong_hang` (.tsv, .xlsx), `bao_cao.md`; có trong `phan_cong.tsv` (`*`, Tai). **Manifest chưa có**, đã thêm 4 dòng vào `Docs/nguon_manifest_Tai.tsv` |
| 2. Nguồn | Cả 2 tệp .wikitext giống hệt bản hiện hành tải qua API: 平安南詔 revid 1808602, Biên dịch:Bình An Nam chiếu revid 195870. Bản Hán đủ toàn văn chiếu; bản Việt có đủ phần Dịch nghĩa |
| 3. Bản text | Không cảnh báo, không sót markup |
| 4. Dóng hàng | 49 cặp, đọc hết, đúng |

**Phạm vi song ngữ:** giữ phần "Dịch nghĩa" bên Việt. Loại bảng "Nguyên văn chữ Hán | Phiên âm" (không phải bản dịch) và "Phụ ghi" (trích Minh thực lục, bản Hán không có). Cấu hình cũ đã đúng.

## Lỗi đã sửa

| Lỗi | Hậu quả trước khi sửa | Cách sửa |
|---|---|---|
| Nguồn Hán nối cả chiếu văn bằng ，/；. Đoạn 「興言至此…慰其幽冥；」 chỉ là một câu | Cặp 2-15 rất dài; thêm 4 cặp 1-2/1-3; cần 2 quyết định `gop` | Chấm câu thủ công (R13) `resources/cham_cau/HCB_02.txt`: chỉ đổi 20 dấu ，→。 (1 dấu →；) ở chỗ bản Việt hết câu, chữ giữ nguyên (R13 tự kiểm tra). Cấu hình `cham_cau_thu_cong` trong `config/works/HCB_02.yaml` |
| 2 quyết định `gop` cũ trong `hieu_dinh/HCB_02__Tai.tsv` | Gắn với mã câu cũ, sau khi chấm câu lại thì không còn cần | Xóa tệp (sau khi chấm câu, mọi cặp đã là 1-1 đúng) |

## Ghi chú khi đọc

- Cặp 6: 胡𡗨 là cách viết của nguồn cho tên Hồ Hán Thương (胡漢蒼); giữ nguyên.
- Cặp 25: bản Việt thêm ngoặc kép cho lời của quan lại, bên Hán là lời gián tiếp; nội dung khớp.
