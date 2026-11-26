# HCB_06 – 漢書 卷028 地理志 / Hán thư quyển 28, Địa lý chí (Huy)

**Trạng thái:** XONG (đợt 2, 2026-11-26). Trước khi sửa có 360 cặp và 270 câu không ghép. Sau khi sửa có **454 cặp** (1-1×449), đã đọc hết 454/454, tất cả đúng. Không còn câu không ghép.

| Bước | Kết quả |
|---|---|
| 1. Tài liệu | Đủ `01_nguon`, `03_text_sach`, `04_dong_hang` (.tsv, .xlsx), `bao_cao.md`; có trong `phan_cong.tsv` (`*`, Huy) |
| 2. Nguồn | Hán: khớp SHA với manifest, trùng với trang zh.wikisource 漢書/卷028 (revid 2605705). **Bản Việt tải thiếu**, đã tải lại (xem dưới) |
| 3. Bản text | Template `{{quote|…}}` chưa được đọc, đã sửa; không còn cảnh báo |
| 4. Dóng hàng | 454 cặp, đọc hết, đúng |

## Lỗi đã sửa (tận gốc)

| Lỗi | Hậu quả trước khi sửa | Cách sửa |
|---|---|---|
| Bản Việt trong `01_nguon` là bản chép tay từ trang hiển thị, **mất toàn bộ phần dịch 禹貢** nằm trong `{{quote|…}}` (~94 câu). Manifest ghi URL `…Quyển_028_thượng`, trang này không tồn tại | Bên Hán, 禹貢 bị ghép 10-1 vào các câu khác hoặc không có cặp | Tải lại wikitext từ trang đúng **Biên dịch:Hán thư/Quyển 028** (revid 204272, 2026-03-10). Cập nhật `Docs/nguon_manifest_Huy.tsv`: URL, revid, SHA-256 `93e1e2a6…`, ngày tải 26/11. Sửa URL bên Hán thành 漢書/卷028 (revid 2605705) |
| `hvalign/readers.py` chưa biết template `quote`, nên còn dính `⟪？quote：` trong text sạch | Cảnh báo "bản Hán còn chữ Latin"; câu đầu 禹貢 dính mã | Thêm `quote` vào `_KEEP_FIRST` (giữ nội dung). Chỉ HCB_06 có template này, nên tác phẩm khác không đổi |
| Bản Việt chỉ có tiêu đề cho 10 mục Đất Tần → Đất Vệ (chưa dịch) | 270 câu Hán không có cặp | `loai_tru` 10 mục bên Hán (chỉ dóng phần có song ngữ, theo yêu cầu của giảng viên) |
| Nguồn Hán, dòng 244: mảnh lặp dở dang 「廣陽國，戶二萬七百四」 | Bị dính vào cặp 膠東國 (2-1) | `loai_tru` theo regex đúng dòng này |

## Ghi chú khi đọc

- Các cặp "trùng hoàn toàn" mà kiểm định cảnh báo (厥土塗泥, 民二男三女, 其利蒲、魚…) là câu lặp thật trong 禹貢 và 職方, không phải lỗi.
- Cặp 5 「曰：」↔ "Rằng:" ngắn nhưng đúng: lời dẫn trước đoạn trích 禹貢.
- Cặp 261 (2-1): nguồn Hán ngắt dòng giữa danh sách 16 huyện của 天水郡, nên gộp là đúng.
- Một số danh sách huyện bên Hán ít hơn số ghi (ví dụ 左馮翊 ghi 24 huyện, liệt kê 23). Đây là lỗi của nguồn wikisource; hai bên vẫn khớp nhau từng tên.
