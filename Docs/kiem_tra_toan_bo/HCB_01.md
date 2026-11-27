# HCB_01 – 續資治通鑑 / Tục tư trị thông giám, quyển 1–20 (cả 4 người)

**Trạng thái:** XONG cả 20 quyển. Quyển 1–10 ở đợt 5 (26–27/11), quyển 11–20 ở đợt 6 (27/11).

HCB_01 có **8.092 cặp**; đã đọc hết 8.092/8.092 cặp. Sau khi sửa, tất cả đều đúng, trừ 4 chữ của nguồn zh không xác định được (xem "Còn để nguyên" bên dưới).

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
| 9 | Đăng | 405 | 3421–3825 | Sửa #3421–3425 (khúc `q9_a`), #3772–3773 (khúc `q9_b`); #3386 乙太 → 以太 (bổ sung ở đợt 6) |
| 10 | Kiên | 460 | 3826–4285 | Chữ ghép bộ #4049 (钅句 → 鉤) |
| 11 | Huy | 403 | 4286–4688 | Sửa #4516–4519 (khúc `q11_a`) |
| 12 | Đăng | 412 | 4689–5100 | Chữ PUA #5019 (巇); #4855 乙太 → 以太; #4869 thừa dấu 。 |
| 13 | Đăng | 374 | 5101–5474 | #5373 備位元 → 備位; #5385 thừa dấu 」 |
| 14 | Đăng | 337 | 5475–5811 | Sửa #5705–5706 (khúc `q14_a`); chữ ghép bộ #5667 (牜字 → 牸); PUA #5723 để nguyên, có ghi chú |
| 15 | Kiên | 352 | 5812–6163 | Sửa #6113–6114 (khúc `q15_a`); PUA #6109 để nguyên, có ghi chú |
| 16 | Huy | 378 | 6164–6541 | Sửa #6386–6387 (khúc `q16_a`); chữ PUA #6179 (棲), #6314 (穡); #6288 lặp chữ 俶 |
| 17 | Tài | 351 | 6542–6892 | #6583 dấu 』 → 「; PUA #6625 và chữ ghép bộ #6686 để nguyên, có ghi chú |
| 18 | Đăng | 415 | 6893–7307 | Sửa #6913–6914 (khúc `q18_a`); chữ PUA #6998 (楊礪); chữ ghép bộ #7157 (鹿阝 → 鄜); #7135 thừa dấu ， |
| 19 | Tài | 464 | 7308–7771 | Sửa #7326–7327, #7344–7345 (khúc `q19_a`, `q19_b`); chữ PUA #7316 (秕); chữ ghép bộ #7358 (鄜), #7451 (扌捲 → 捲); #7657 乙太 → 以太 |
| 20 | Kiên | 321 | 7772–8092 | Sửa #7866–7868 (khúc `q20_a`) |

Số # là số thứ tự trong `CV02_HCB_01/04_dong_hang/HCB_01_parallel.tsv`.

## Bước 1–3: tài liệu, nguồn, bản text

- **Đủ tài liệu:** có `01_nguon`, `03_text_sach`, `04_dong_hang` (.tsv, .xlsx) và `bao_cao.md`. Cả 20 quyển có trong `phan_cong.tsv`.
- **Nguồn:** đã tải lại cả 40 trang (20 quyển × Hán/Việt) qua API wikisource để đối chiếu (đợt 5: `GK_tam/dot5_live`, đợt 6: `GK_tam/dot6_live`).
  - Tệp `.wikitext` giống hệt bản hiện hành.
  - Tệp `.txt` của Huy (q3, 5, 7, 11, 16; cả Hán lẫn Việt) là wikitext lưu đuôi .txt, đủ chữ, không lệch chữ nào.
- **Manifest:** mọi tệp nguồn của 20 quyển đều có trong manifest, kèm revid và SHA khớp.
  - Đợt 5: Tài q1, q8; Đăng q4, q9; Huy điền revid q3, 5, 7.
  - Đợt 6: Tài q17, q19; Đăng q12, 13, 14, 18; Huy điền revid q11, q16. Kiên (q15, q20) đã có sẵn trong `nguon_manifest.tsv`.
- **Bản text:** không sót markup. Lỗi chữ của nguồn zh được xử lý ở bước 4 (xem dưới).

## Lỗi hệ thống đã sửa

| Lỗi | Hậu quả | Cách sửa |
|---|---|---|
| Bản Việt q1 mở đầu bằng đoạn tiểu sử Thái Tổ. Đây là bản dịch của lời chú nhỏ `{{*|帝諱匡胤…}}`, mà bên Hán đã bỏ (R04) | Câu Việt thừa, không có vế Hán | `loai_tru` bên Việt `HCB_01/q001/viet/s00/p001` trong `config/works/HCB_01.yaml`. Không cặp máy nào thay đổi |
| Trang zh và vi của quyển 5 đều chép trùng đoạn 「戊申，北漢主殂…」 | 2 cặp lặp (#1875–1876 cũ) | `sai` 2 cặp lặp (Huy). Từ đó số # lùi 2 |

## Sửa tay (human in the loop)

Hiệu đính ghi ở `hieu_dinh/HCB_01__<người>.tsv`, gồm **81 quyết định**: 74 `sua`, 2 `sai`, 5 `dung`. Đợt 5 có 40, đợt 6 có 41. Tệp khúc lưu ở `Docs/kiem_tra_toan_bo/khuc/HCB_01/`.

**Chia lại ranh giới** (`cong_cu/chia_lai.py`; chữ Hán và chữ Việt của khúc giữ nguyên tuyệt đối; tệp khúc dựng bằng `cong_cu/mkkhuc.py`):
- q1 #15–17, #95–97; q3 #1229–1230; q6 #2210–2211, #2372–2374, #2421–2422, #2454–2455: máy trượt 1 vế, vì bản Việt gộp hoặc tách câu khác bản Hán.
- q9 #3421–3425: nguồn zh đặt tiêu đề 太宗至仁應運…皇帝 **sau** đoạn tiểu sử, còn bản Việt đưa tên hiệu lên đầu câu, nên cả 5 cặp trượt 1 vế.
- q9 #3772–3773: vế Việt "Bân đáp" (彬對曰) bị ghép vào cặp trước.
- Đợt 6 có 8 khúc, đều là một vế Việt ngắn ở ranh giới bị dính sang cặp bên cạnh:
  - q11 #4516–4519: vế "nếu là đế vương nóng nảy…" và câu 宋琪曰;
  - q14 #5705–5706: vế "Sách Quân chí nói" (軍志曰);
  - q15 #6113–6114: vế "Hoằng tính nhút nhát…" (宏性懦謹);
  - q16 #6386–6387: vế "Hoàng đế đặc biệt yêu thương" (帝尤所鍾愛);
  - q18 #6913–6914: vế "Hoàng đế vui, phê ở cuối tờ giấy" (帝悅，批紙尾曰);
  - q19 #7326–7327: vế "Đạt Lan nghe theo lời ấy…" (達蘭從其言);
  - q19 #7344–7345: vế "Hoàng đế nổi giận, triệu Đoan…" (帝大怒，召責端等);
  - q20 #7866–7868: các vế 詔禮官詳定 / 禮官引《春秋》.
- q20 #7772 **không** phải sửa. Tiêu đề 真宗膺符稽古…皇帝 trong nguồn zh là dòng đề mục `== … ==` nên bị bỏ như mọi đề mục khác. Bản Việt viết tên hiệu liền trong câu "…, húy là Hằng", không tách được.

**Bỏ ngoặc dịch lời chú nhỏ:** bên Hán, R04 đã bỏ lời chú `{{*|…}}`, nhưng bản Việt dịch cả lời chú này trong ngoặc. Phần ngoặc đã được bỏ bằng `sua` ở #97, #415 (Tài) và #428, #444, #631, #749 (Kiên). Ngoặc giải thích ngắn của người dịch ("tức …", "(môn hạ)") thì giữ.

**Lỗi chữ của nguồn zh** (sửa bằng `sua`, chỉ đổi đúng chữ lỗi):
- **Chữ PUA:** wikisource ghi chữ hiếm bằng `{{PUA|…}}`, tức một bộ thủ ở vùng ký tự riêng, rồi đến phần còn lại của chữ. Đã ghép lại thành chữ đúng:
  - #1014 渾瑊, #1027 踰 (Huy);
  - #5019 嶮巇 (山 + 戲), #6998 楊礪, tên người làm Thôi quan phủ Khai Phong năm 994 (Đăng);
  - #6179 窮棲 (木 + 妻), #6314 稼穡 (禾 + 嗇) (Huy);
  - #7316 糠秕 (禾 + 比) (Tài).
- **Chữ ghép bộ:** một chữ bị viết thành bộ thủ + chữ khác.
  - Đợt 5: #2663 扌晉 → 搢 (Huy), #3315 衤復 → 複 (Tài), #4049 钅句 → 鉤 (Kiên).
  - Đợt 6: #5667 牜字 → 牸 (Đăng), #7157 鹿阝 → 鄜 (Đăng), #7358 鹿阝 → 鄜 (Tài), #7451 扌捲 → 捲 (Tài).
- **Rác do bộ chuyển phồn–giản:** 備位元 → 備位 (#5373); 乙太 → 以太 (#3386, #4855, #7657).
- **Dấu và chữ thừa:**
  - #4869 「。。」, #7135 「，，」, #5385 thừa 」, #6583 dấu mở 』 → 「 (Đăng, Tài);
  - #6288 「錢俶俶日」 lặp chữ (Huy);
  - #1886, #1948, #1959 ký tự rác (Huy).
- #1891 có ghi chú rằng nguồn thiếu tên 霸榮 (`dung`).

**Còn để nguyên (có ghi chú `dung`):** 4 chữ không xác định được chữ gốc. Không đoán, để giữ nguyên vẹn văn bản nguồn:

| # | Người | Chữ trong nguồn | Nghĩa theo bản Việt |
|---|---|---|---|
| 5723 | Đăng | 慰{{PUA|U+E491}}庶 | "an ủi trăm họ" |
| 6109 | Kiên | 亢 U+E789 之咎 | "tai họa khô hạn" (có thể là 亢旱 / 亢陽) |
| 6625 | Tài | 民{{PUA|U+E407}}朁滅 | "bị giết sạch" |
| 6686 | Tài | 槍钅屈 | "thương, kích" |

## Ghi chú

- Lỗi chữ có nghĩa của nguồn được giữ nguyên, ví dụ:
  - 「餘斌」 (thay cho 全斌) ở #3366;
  - ngày can chi sai thứ tự 「丙子…丁卯」 ở #3321–3322;
  - 國了博士, 南鄰 (南郊), 知制浩, 謂埠, 這，御乾元門, 吾賦.
- Lỗi của bản Việt cũng giữ nguyên: thiếu dấu ở vài chữ ("nuoc", "Bon", "duong", #3836–3839), hiểu sai nghĩa (#6072 "ở Phúc Kiến"), phiên âm tên chưa thống nhất.
- Chữ PUA và chữ ghép bộ được quét bằng regex các bộ thủ đứng riêng `[衤礻扌氵亻犭忄阝钅牜糹訁釒飠讠纟饣]` cộng vùng `U+E000–U+F8FF` trên vế Hán. Chữ rác do bộ chuyển phồn–giản được quét bằng các cụm `乙太`, `位元`, `資訊`, `軟體`, `網路` trên cả 14 tác phẩm: chỉ HCB_01 có.
- Cảnh báo kiểm định: 13 cặp trùng lặp và 38 câu Hán lặp. Đây là câu lặp thật (帝曰, 不許…) ở các chỗ khác nhau.
