# Công cụ kiểm tra toàn bộ

Chạy tại thư mục `Lab/GK`. Trên Windows, đặt trước `PYTHONUTF8=1 PYTHONIOENCODING=utf-8`.

| Lệnh | Việc làm |
|---|---|
| `PYTHONPATH=. python Docs/kiem_tra_toan_bo/cong_cu/dump.py HCB_13 1 80` | In các cặp 1–80, đúng thứ tự dòng trong TSV nộp, kèm mã câu, cờ máy và ghi chú. Số cặp là số **sau** hiệu đính. |
| `PYTHONPATH=. python Docs/kiem_tra_toan_bo/cong_cu/hd.py HCB_13 Kien 22 gop "ghi chú"` | Gộp cặp 22 với cặp ngay sau, ghi vào `hieu_dinh/HCB_13__Kien.tsv`. Các quyết định khác: `sai` (bỏ cặp), `dung` (xác nhận đúng, ghi chú viết tay vào cột Ghi chú), `sua "ghi chú" "<Hán>" "<Việt>"`. |
| `PYTHONPATH=. python Docs/kiem_tra_toan_bo/cong_cu/dumpq.py HCB_14 1358 [1421 …]` | In các cặp của từng quyển (số # như TSV nộp) kèm câu máy để không ghép của quyển đó. |
| `PYTHONPATH=. python Docs/kiem_tra_toan_bo/cong_cu/chia_lai.py HCB_14 Tai 371 432 khuc.txt [--thu] [--khong-ghep]` | Chia lại ranh giới khúc cặp #371–#432. `khuc.txt`: dòng `HB: <Hán, '|' ở ranh giới>` (vế Việt giữ nguyên từng cặp) hoặc các cặp `H:`/`V:`. Bắt buộc nối chữ Hán/Việt giống hệt bản cũ; số cặp mới ≤ cũ (cặp thừa ghi `sai`). `--khong-ghep` cho đưa thêm đúng các câu máy để không ghép. |
| `PYTHONPATH=. python Docs/kiem_tra_toan_bo/cong_cu/dumpc.py HCB_01 4286 4400` | In gọn các cặp #a–#b (2 dòng mỗi cặp, không mã câu) để đọc nhanh khối lớn. |
| `PYTHONPATH=. python Docs/kiem_tra_toan_bo/cong_cu/mkkhuc.py HCB_01 4516 4519 khuc.txt "ghi chú" --h 朕於臣下 宋琪曰 --v "Trẫm đối với" "Tống Kỳ nói"` | Dựng tệp khúc `HB:`/`VB:` cho `chia_lai.py` từ chữ hiện có của #a–#b: chỉ cần cho đoạn chữ mở đầu cặp mới thứ 2, 3… ở mỗi bên, nên không phải chép tay chữ nào. |

Lưu ý:
- Sau mỗi lần gộp, số thứ tự các cặp phía sau giảm đi. Khi sửa nhiều chỗ, làm từ cuối lên.
- Sau khi sửa: chạy `python -m hvalign run --work HCB_xx`, rồi kiểm `khong_khop = 0` (dòng thống kê `hd.py` in ra).
