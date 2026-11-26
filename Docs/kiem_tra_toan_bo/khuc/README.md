# Tệp khúc sửa tay (human in the loop)

Mỗi tệp `HCB_xx/q<quyển>*.txt` ghi ranh giới cặp đúng của một khúc đã được người đọc chia lại. Tệp dùng với `../cong_cu/chia_lai.py`:
- dòng `HB:` chứa toàn bộ chữ Hán của khúc, `|` đánh dấu ranh giới cặp;
- hoặc từng cặp `H:` / `V:`.

Các quyết định `sua`/`sai` trong `hieu_dinh/` gắn với cặp máy. Nếu sửa code hoặc cấu hình làm máy dóng lại, `khong_khop` sẽ lớn hơn 0. Khi đó:
1. xóa các dòng quyết định của quyển đó trong `hieu_dinh/<MA>__<người>.tsv`;
2. tìm số thứ tự cặp mới của khúc (`dumpq.py`);
3. chạy lại `chia_lai.py` với đúng tệp khúc.

Nội dung chữ trong tệp khúc không đổi, nên kết quả giống hệt lần trước.

Chú ý: một số khúc được làm theo thứ tự (khúc sau trước, khúc có `--khong-ghep` sau). Số `#` trong lệnh phụ thuộc vào lần chạy, xem `Docs/kiem_tra_toan_bo/HCB_xx.md` và `TIEN_DO.md`.
