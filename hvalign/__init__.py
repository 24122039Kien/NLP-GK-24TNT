"""hvalign – chương trình dóng hàng Hán–Việt dùng chung của nhóm CV02.

Các bước (theo Guideline):
  B4 extract  : đọc nguồn (.wikitext / .txt / .html), chuẩn hóa về một dạng, ghi work/<MA>/02_ocr_tho/ (không nộp)
  B5 clean    : bộ luật làm sạch R01–R12, ghi 03_text_sach/ và log
  B6 segment  : tách câu, đánh dấu ranh giới cứng/mềm
  B7 align    : dóng 3 tầng (mục → đoạn → câu)
  export      : xuất TSV + XLSX, kiểm định, báo cáo

Chạy: python -m hvalign --help
"""

__version__ = "0.3.5"
