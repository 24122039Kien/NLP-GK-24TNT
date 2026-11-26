# HCB_12 – 史記 卷113 南越列傳 / Sử ký tam gia chú quyển 113, Nam Việt liệt truyện (Tài)

**Trạng thái:** XONG (đợt 3, 2026-11-26). **149 cặp** (1-1×136, 1-2×13), đã đọc hết 149/149. 3 cặp do máy bỏ tiêu đề nên thiếu nhãn ở một vế, đã sửa tay (`sua`); giờ tất cả đúng, không còn câu nào chưa ghép.

| Bước | Kết quả |
|---|---|
| 1. Tài liệu | Đủ `01_nguon` (.wikitext + .pdf mỗi bên), `03_text_sach`, `04_dong_hang` (.tsv, .xlsx), `bao_cao.md`; có trong `phan_cong.tsv` (113, Tai). **Manifest chưa có**, đã thêm 4 dòng vào `Docs/nguon_manifest_Tai.tsv` |
| 2. Nguồn | Bản Việt giống hệt bản hiện hành (Biên dịch:Sử ký tam gia chú/Quyển 113, revid 204266). Bản Hán: ngày 24/11/2026 trang 史記/卷113 được **đổi tên** thành 史記 (維基文庫點校本)/卷113, tên cũ thành trang đổi hướng; nội dung không đổi (revid nội dung 8735632, giống hệt tệp đang có). Manifest ghi tên cũ (đúng lúc tải) |
| 3. Bản text | Không cảnh báo, không sót markup |
| 4. Dóng hàng | 149 cặp, đọc hết, đúng |

**Phạm vi song ngữ:** bỏ 67 dòng lời chú Tam gia chú (Tập giải, Sách ẩn, Chính nghĩa) bên Việt, vì bản Hán chỉ có chính văn. Giữ bài Thái sử công và "Sách Ẩn thuật tán" vì bản Hán có mục 太史公曰 và 索隱述贊. Cấu hình cũ đã đúng.

## Hiệu đính (`hieu_dinh/HCB_12__Tai.tsv`, sửa tay theo yêu cầu "human in the loop")

| Cặp | Lỗi | Sửa |
|---|---|---|
| 1 | Bản Việt viết "Nam Việt Vương (南越王)" thành dòng tiêu đề riêng, máy bỏ như tiêu đề, nên vế Việt thiếu 南越王 | `sua` vế Việt: "Nam Việt Vương Úy Đà là người Chân Định, họ Triệu." |
| 135 | Bên Hán 太史公曰 là tiêu đề mục (bị bỏ), bên Việt nhãn "Thái Sử Công nói:" nằm trong câu | `sua` vế Hán: 「太史公曰：尉佗之王，本由任囂。」 |
| 145 | Tương tự với 索隱述贊 ↔ "Sách Ẩn thuật tán:" | `sua` vế Hán: 「索隱述贊：中原鹿走，群雄莫制。」 |

## Ghi chú khi đọc

- Lỗi chữ của nguồn Hán, giữ nguyên vì không sửa nguồn: 高後 / 太後 (đúng là 后) ở cặp 15, 17, 64, 97; 嫪後 (đúng là 樛后) ở cặp 148.
- Bản Việt thêm năm dương lịch và giải thích trong ngoặc, ví dụ "(Nguyên Đỉnh năm thứ 4)", "(Lê đán)"; ghi chú tự động đã nêu.
