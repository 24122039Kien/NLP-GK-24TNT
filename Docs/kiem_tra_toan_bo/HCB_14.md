# HCB_14 – 清實錄 高宗純皇帝實錄 / Thanh thực lục, Cao Tông Thuần Hoàng đế thực lục (cả 4 người)

**Trạng thái:** XONG (đợt 4, 2026-11-26). 26 quyển (Kiên 4, Tài 8, Huy 6, Đăng 8). Trước khi sửa có 868 cặp: 58 câu không ghép, phần lớn các quyển trượt 1 vế suốt quyển. Sau khi sửa có **912 cặp**. Đã đọc hết 912/912, tất cả đúng. Không còn câu nào bị bỏ ngoài.

| Bước | Kết quả |
|---|---|
| 1. Tài liệu | Đủ `01_nguon`, `03_text_sach`, `04_dong_hang`, `bao_cao.md`; 26 quyển có trong `phan_cong.tsv` |
| 2. Nguồn | 20 tệp Việt `.wikitext` giống hệt bản hiện hành tải qua API. 6 tệp Việt `.txt` của Huy đủ nội dung, chỉ thiếu dòng liên kết nguồn, nên giữ. Bản Hán: xem các lỗi bên dưới. 141 tệp, tất cả có trong manifest và khớp SHA |
| 3. Bản text | Đã sửa lỗi chữ ngoài BMP thành `��` (xem dưới); không còn sót markup |
| 4. Dóng hàng | 912 cặp, đọc hết, đúng |

## Lỗi hệ thống đã sửa

| Lỗi | Hậu quả | Cách sửa |
|---|---|---|
| **Bản Hán `.txt` của Huy** (Q1327, 1361, 1363, 1381, 1419, 1429) là bản chép tay, bị ngắt đoạn ở mỗi chữ tôn kính nâng đầu dòng (天, 上, 皇…), ví dụ 「是蓋奉」 xuống dòng 「天道也」 | Câu Hán bị cắt giữa chừng, nên dóng lệch | Thay bằng **15 bài sillok HTML gốc** (đã so: chữ trùng khớp). Bộ đọc sillok nối liền các đoạn này. Manifest Huy ghi URL từng bài |
| **Thiếu bài sillok**: bản Việt có dịch nhưng chưa tải bản Hán. Q1358: 御製詩「瀛藩入祝…」 (0110_0020), dụ tông thất 「今歲因朕八旬…宗人府」 (0110_0030). Q1360: 「遣官告祭天地太廟社稷」 (0120_0030), 「御重華宮張樂進宴」 (0120_0050) | Câu Việt không có cặp, hoặc bị ghép nhầm | Tải 4 bài (kèm PDF), ghi manifest Tài. Không tải 0120_0040 (遣官告祭奉先殿) vì bản Việt không dịch |
| Sillok viết chữ ngoài BMP bằng **cặp thực thể surrogate** (`&#55360;&#56822;` = 𠇶, `&#55381;&#56916;` = 𥙔) | 黎𠇶, 黎維𥙔 bị thành `黎��` (Q1346, 1362, 1463) | **hvalign 0.3.4**: `readers._unescape` ghép cặp surrogate; có kiểm thử `test_sillok_html_surrogate_pair_entities` |
| Trang Việt chép lại thơ ngự chế gồm nguyên văn chữ Hán, phiên âm, dịch nghĩa, dịch thơ (Q1358, 1421, 1428) | Phiên âm và chữ Hán bị ghép như bản dịch | `loai_tru` bên Việt: Q1358 giữ Dịch nghĩa; Q1421, Q1428 không có dịch nghĩa nên giữ Dịch thơ. Mỗi câu thơ Hán giờ ứng với 1 câu dịch |
| Q1346: chiếu ân xá 22 điều, 1 đoạn Hán ứng với 24 đoạn Việt, vượt `tang2_max` (8) | Ghép 1-10 / 10-1, 6 câu Việt không ghép | `dong_hang.tang2_max: 30` trong `config/works/HCB_14.yaml`. Chỉ ảnh hưởng tới Q1346, 1358, 1363, 1421, 1428, các quyển này được đọc sau khi đổi |

## Sửa tay (human in the loop) – `hieu_dinh/HCB_14__<người>.tsv`

Bản Việt ngắt câu khác hẳn dấu 。 của sillok (sillok dùng 。 cả ở chỗ ngắt nhỏ). Vì vậy máy thường trượt 1 vế suốt quyển. Mọi quyển đều được chia lại ranh giới bằng `cong_cu/chia_lai.py`, với ràng buộc nối toàn bộ chữ Hán và toàn bộ chữ Việt của khúc phải **giống hệt** bản gốc. Tệp khúc lưu ở `Docs/kiem_tra_toan_bo/khuc/HCB_14/q<quyển>*.txt`. Tổng cộng 544 `sua`, 22 `sai`. 22 cặp `sai` đều thuộc Q1346, là các cặp số thứ tự "1.", "2."… đã ghép vào nội dung điều tương ứng.

| Người | Quyển (số cặp sau sửa) |
|---|---|
| Kiên | 1333 (62), 1339 (23), 1357 (30), 1438 (9) = 124 |
| Tài | 1335 (23), 1337 (21), 1358 (63), 1360 (22), 1362 (42), 1410 (11), 1421 (86), 1445 (11) = 279 |
| Huy | 1327 (26), 1361 (66), 1363 (70), 1381 (38), 1419 (6), 1429 (19) = 225 |
| Đăng | 1328 (86), 1331 (14), 1346 (85), 1359 (3), 1384 (12), 1420 (17), 1428 (46), 1463 (21) = 284 |

Sửa thêm ngoài phần chia lại ranh giới:
- Đưa vào cặp 3 câu máy để không ghép: "Lại dụ rằng:" (Q1339, Q1357), 「○庚申。」 (Q1360).
- Bỏ chữ Hán sót trong vế Việt: 「元閔鶚」 (Q1358), 「阮光平」 (Q1359).
- Ghi chú lỗi của người dịch, vẫn giữ lời dịch:
  - Q1410: 省河 bị dịch thành "tỉnh Hà Nội".
  - Q1445: 緦服族叔 bị dịch thành "đang chịu tang thúc phụ".

## Ghi chú

- Q1428 cặp "示依北闕誌心親似茲亂命同治命。" gồm 2 câu thơ, vì nguồn Hán thiếu dấu giữa hai câu. Nội dung đúng.
- Các cặp trùng nhau (欽哉, 特諭, danh sách ban yến…) là công thức lặp thật ở các bài khác nhau.
- **Bài học:** quyết định `sua` gắn với cặp máy. Nếu sửa code hoặc cấu hình làm máy dóng lại, phải kiểm `khong_khop`; nếu lệch thì xóa quyết định của quyển đó và áp lại tệp khúc (đã gặp ở Q1346 sau bản sửa 0.3.4).
