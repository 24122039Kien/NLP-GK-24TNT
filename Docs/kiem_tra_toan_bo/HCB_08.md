# HCB_08 – 後漢書 卷24 馬援列傳 / Hậu Hán thư quyển 24, Mã Viện liệt truyện (Huy)

**Trạng thái:** XONG (đợt 2, 2026-11-26). Trước khi sửa có 411 cặp, 20 câu không ghép và nhiều vùng lệch hẳn (cặp 10-1). Sau khi sửa có **481 cặp**, đã đọc hết, tất cả đúng. Không còn câu không ghép.

| Bước | Kết quả |
|---|---|
| 1. Tài liệu | Đủ `01_nguon`, `03_text_sach`, `04_dong_hang` (.tsv, .xlsx), `bao_cao.md`; có trong `phan_cong.tsv` (`*`, Huy) |
| 2. Nguồn | Hán: khớp SHA với manifest; chữ trùng với trang zh.wikisource 後漢書/卷24 hiện tại (chỉ khác 2 thẻ `<onlyinclude>`). **Bản Việt tải thiếu**, đã tải lại (xem dưới) |
| 3. Bản text | Còn markup `-{徵}-`, `-{后}-`, `-{松}-` (67 chỗ) trong text Hán sạch, đã sửa |
| 4. Dóng hàng | 481 cặp, đọc hết, đúng |

## Lỗi đã sửa

| Lỗi | Hậu quả trước khi sửa | Cách sửa |
|---|---|---|
| Bản Việt trong `01_nguon` là bản chép từ trang hiển thị, **mất các khối nằm trong `<div style="background-color:pink">` và `<poem>`**: cả đoạn Trưng Trắc – Trưng Nhị và chiến dịch Giao Chỉ, trống đồng, Mạnh Ký, thư gửi Dương Quảng (~70 câu) | Các đoạn Hán này ghép 10-1 vào câu Việt khác, ví dụ 「又交阯女子徵側…」 ↔ "Về chưa đầy một tháng, gặp lúc Hung Nô…" | Tải lại wikitext **Biên dịch:Hậu Hán thư/Quyển 24** (revid 204355, 2026-03-17). Cập nhật `Docs/nguon_manifest_Huy.tsv`: SHA-256 `50be15cc…`, ngày tải 26/11 |
| `readers.py` chưa xử lý markup chuyển đổi phồn/giản `-{…}-` của MediaWiki | Text Hán sạch còn `-{徵}-側`, `皇-{后}-` (HCB_08 có 67 chỗ, HCB_01 có 3 chỗ) | Thêm `_lang_conv`: `-{X}-` → X; `-{zh-hans:…;zh-hant:…}-` → bản phồn thể; `-{H|…}-` → bỏ. Có kiểm thử `test_wikitext_language_conversion_and_quote` |
| Bản Việt chia đoạn khác hẳn bản Hán (thư răn cháu: 1 đoạn Hán ↔ 7 đoạn Việt, ranh giới lệch 1 câu) | Tầng 2 (ghép đoạn) ghép sai, nên trượt 1 câu suốt vùng 「帝乃使…梁松」 → 「詔免保官」 | Thêm tùy chọn `dong_hang.tang2_doan: false` (`align.py`): bỏ ghép đoạn, dóng câu trên cả mục. Chỉ HCB_08 bật; tác phẩm khác giữ mặc định |
| Tên 龍伯高 / 杜季良 không có trong bộ mốc, vì bản Việt không chú chữ Hán | Câu "Long Bá Cao…" bị ghép với 杜季良…, trượt 1 câu | Thêm `resources/han_viet_extra.tsv`: Bá Cao ↔ 伯高, Kế Lương ↔ 季良. Hai tên này chỉ có trong HCB_08 |
| Lời giải thích "Chú thích ý nghĩa:" của dịch giả sau bài Tán | Bị ghép 1-7 vào câu cuối 「廖乏三趣，防遂驕陵。」 | `loai_tru` (regex, `den_het_quyen`) |

## Hiệu đính (`hieu_dinh/HCB_08__Huy.tsv`)

| Cặp | Lỗi | Sửa |
|---|---|---|
| 69 | Câu mở thư "Xuân Khanh bình an chứ?" (春卿無恙) bị kéo lên câu dẫn | `gop` 69 + 70 → 2-3 |
| 244 | Bản Việt dịch rút gọn 4 câu Hán (季良名保 … 詔免保官) thành 2 câu, ranh giới không trùng | `gop` → 4-2, có ghi chú phần không dịch |
| 472 | "Sau khi Đậu Hiến bị giết, Lăng cũng bị liên lụy mà chịu tội" (憲誅，坐抵罪) nằm ở cặp sau | `gop` → 2-3 |

## Ghi chú khi đọc

- 「{{-|臣}}」: template chữ nhỏ trong nguồn Hán, giữ chữ 臣. Có 3 cảnh báo "template chưa biết", vô hại.
- Lời dịch giả trong ngoặc, ví dụ "(Quắc thước tai thị ông dã)" ở cặp 216, nằm trong vế Việt; ghi chú tự động đã nêu.
