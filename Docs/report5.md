# Report 5 – App giao diện cho `hvalign`

**Ngày:** 2026-11-14

**Yêu cầu:** làm `hvalign` thành dạng app có giao diện cho cả nhóm dễ dùng, nhưng giữ phần việc tay của con người ở mức vừa phải hoặc ít.

**Sản phẩm:** `hvalign` 0.2.0, thêm lệnh `python -m hvalign app` và tệp `Mo_hvalign.bat` (nhấp đúp để mở).

## Cách giữ phần việc tay ở mức ít

Máy tự làm mọi bước, từ đọc nguồn đến xuất file, kiểm định và báo cáo. Người chỉ làm 3 việc, và trang Tổng quan luôn ghi rõ việc tiếp theo:

| Việc của người | Khối lượng với dữ liệu của Kiên |
|---|---|
| Xem các cặp máy gắn cờ, rủi ro cao trước | 203/3.490 cặp (khoảng 6%), ước tính khoảng 50 phút cho cả 7 tác phẩm |
| Chấm chéo mẫu ngẫu nhiên (§8 Guideline) | 100 cặp mỗi người |
| Bấm Bàn giao | 1 lần mỗi tác phẩm |

Một số nguyên tắc thiết kế:
- **Cặp không ai xem thì giữ kết quả máy**, nên dừng giữa chừng vẫn bàn giao được.
- **Mỗi cặp một phím** (`1` đúng, `2` sai, `3`/`4` gộp, `5` sửa, `U` hoàn tác) rồi tự sang cặp kế tiếp.
- **App hiện lý do máy nghi ngờ** bằng lời, ví dụ `Chỉ vế Việt có: 邵曄 (Thiệu Diệp)`, kèm cặp trên và cặp dưới để đối chiếu.
- **Cỡ mẫu chấm là 100 cặp.** Kế hoạch cũ ghi "100 hoặc 10%", tức 349 cặp với Kiên. Guideline §8 chỉ đặt ngưỡng tỷ lệ lỗi chứ không đặt cỡ mẫu, và 100 cặp đủ để kết luận đạt/không đạt (sai số khoảng ±8% quanh mức 20%). Đổi được trong `config/project.yaml`.

## Hiệu đính tự áp

Việc này hoàn thành phần "`review apply`" vốn giao cho Kiên.

- Quyết định được ghi vào `hieu_dinh/<MA>__<người>.tsv`. Mỗi người một tệp nên không xung đột git. Thư mục này cần commit.
- Kết quả chấm mẫu ghi vào `hieu_dinh/cham_mau__<người chấm>.tsv`.
- Mỗi quyết định gắn với **mã câu**, không gắn với số thứ tự cặp. Chạy lại chương trình không mất công sửa. Nếu cấu hình đổi làm một cặp bị ghép khác đi, quyết định cũ của cặp đó tự bị bỏ qua và được báo lại.
- Quyết định được áp ở bước xuất, cả bản xem trước lẫn bản bàn giao. Sheet `TRUY_VET` có thêm cột `Hiệu đính`; `THONG_KE` có số cặp đã xác nhận, sửa, gộp và bỏ.
- Báo cáo tự sinh ghi trạng thái hiệu đính và **tỷ lệ lỗi mẫu** thay cho dòng "chưa đo" trước đây.

## Kỹ thuật

- **Chỉ dùng thư viện chuẩn của Python** (`http.server`), không cần cài thêm. Giao diện là một tệp HTML, không cần mạng.
- **An toàn:**
  - máy chủ chỉ nghe trên `127.0.0.1`;
  - lệnh ghi phải có header riêng, để trang web khác không gửi lệnh tới được;
  - kiểm tra `Host` để chặn DNS rebinding;
  - nút "Mở tệp" chỉ mở được tệp trong thư mục đồ án.
- **Chạy nền:** mỗi lúc chỉ một việc, nhật ký hiện trực tiếp. Lỗi quen thuộc (tệp đang mở trong Excel, nguồn không phải UTF-8…) được báo bằng câu dễ hiểu, dùng chung một hàm với dòng lệnh.

## Kiểm tra đã làm

- **Kiểm thử tự động:** 16/16 đạt. Có thêm kiểm thử cho áp quyết định (đúng / sai / sửa / gộp chuỗi / quyết định cũ không khớp) và cho lưu tệp, hoàn tác, tỷ lệ lỗi.
- **API, thử trên bản sao:**
  - lưu và áp quyết định;
  - chặn yêu cầu thiếu header (403), Host lạ (403), đường dẫn ra ngoài đồ án (400);
  - khóa khi đang chạy việc khác (409);
  - cập nhật bản xuất sau hiệu đính: 340 → 339 cặp, kiểm định vẫn ĐẠT.
- **Giao diện, chạy trên Chrome:** bấm phím Đúng, Sai, quay lại, hoàn tác, sửa chữ (`Ctrl+Enter`), gộp với cặp trên rồi hoàn tác, chấm mẫu. Không có lỗi JavaScript. Ở bề rộng điện thoại (390px) trang không bị tràn ngang.
- **Chạy lại toàn bộ dữ liệu của Kiên:** vẫn 3.490 cặp, 7/7 tác phẩm ĐẠT. Thư mục `hieu_dinh/` trên repo thật chưa có quyết định nào, vì các thao tác thử chỉ làm trên bản sao.

## Việc bạn cần làm

1. Mở app và thử. Khi bạn đồng ý thì commit và push, để các bạn trong nhóm dùng được.
2. Báo nhóm vòng chấm chéo đã ghi trong `phan_viec_hvalign.md`: **Kiên → Huy → Tài → Đăng → Kiên**.

## Tệp đã thay đổi (chưa commit, cộng dồn với report4)

- **Mới:**
  - `hvalign/app.py`;
  - `hvalign/app_static/index.html`;
  - `hvalign/review.py`;
  - `Mo_hvalign.bat`;
  - `Docs/report5.md`.
- **Sửa:**
  - `hvalign/__main__.py` (lệnh `app`, hàm báo lỗi dùng chung);
  - `export.py` và `report.py` (áp hiệu đính, tỷ lệ lỗi);
  - `__init__.py` (phiên bản 0.2.0);
  - `config/project.yaml` (`cham_mau.so_cap`);
  - `.gitattributes` (`.bat` giữ CRLF);
  - `tests/test_pipeline.py` (+2 kiểm thử);
  - `README.md`, `Docs/huong_dan_hvalign.md` (mục 0, 4.4, 6, 7, 8, 9, 10, 11), `Docs/phan_viec_hvalign.md`.
