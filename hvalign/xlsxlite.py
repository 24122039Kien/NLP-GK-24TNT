"""Ghi / đọc .xlsx tối giản bằng thư viện chuẩn (không cần openpyxl).

Ghi: mọi ô văn bản là chuỗi (inlineStr) → một câu bắt đầu bằng '=' không thành công thức;
     không gộp ô; dòng đầu in đậm và cố định.
Đọc: hiểu cả chuỗi dùng chung (sharedStrings) để đọc được tệp đã mở và lưu lại bằng Excel.
"""
from __future__ import annotations

import re
import zipfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from xml.sax.saxutils import escape

_ILLEGAL = re.compile("[\x00-\x08\x0b\x0c\x0e-\x1f￾￿]")
NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
NS_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS_PKG = "http://schemas.openxmlformats.org/package/2006/relationships"

_STYLES = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="{NS}"><fonts count="2"><font><sz val="11"/><name val="Calibri"/></font>\
<font><b/><sz val="11"/><name val="Calibri"/></font></fonts><fills count="2"><fill><patternFill patternType="none"/>\
</fill><fill><patternFill patternType="gray125"/></fill></fills><borders count="1"><border><left/><right/><top/>\
<bottom/><diagonal/></border></borders><cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/>\
</cellStyleXfs><cellXfs count="3"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>\
<xf numFmtId="0" fontId="1" fillId="0" borderId="0" xfId="0" applyFont="1"/>\
<xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0" applyAlignment="1"><alignment wrapText="1" \
vertical="top"/></xf></cellXfs><cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>\
</styleSheet>"""


def col_letter(i: int) -> str:
    s, i = "", i + 1
    while i:
        i, r = divmod(i - 1, 26)
        s = chr(65 + r) + s
    return s


@dataclass
class Sheet:
    name: str
    rows: list[list]
    widths: list[float] = field(default_factory=list)
    wrap: bool = False


def _cell(ref: str, v, style: int) -> str:
    s = f' s="{style}"' if style else ""
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        return f'<c r="{ref}"{s}><v>{v}</v></c>'
    text = escape(_ILLEGAL.sub("", "" if v is None else str(v)))
    return f'<c r="{ref}"{s} t="inlineStr"><is><t xml:space="preserve">{text}</t></is></c>'


def _sheet_xml(sh: Sheet) -> str:
    out = [f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><worksheet xmlns="{NS}">',
           '<sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" '
           'state="frozen"/></sheetView></sheetViews>']
    if sh.widths:
        out.append("<cols>" + "".join(f'<col min="{i}" max="{i}" width="{w}" customWidth="1"/>'
                                      for i, w in enumerate(sh.widths, start=1)) + "</cols>")
    out.append("<sheetData>")
    for r, row in enumerate(sh.rows, start=1):
        style = 1 if r == 1 else (2 if sh.wrap else 0)
        out.append(f'<row r="{r}">' + "".join(_cell(f"{col_letter(c)}{r}", v, style)
                                              for c, v in enumerate(row)) + "</row>")
    out.append("</sheetData></worksheet>")
    return "".join(out)


def write_xlsx(path: Path, sheets: list[Sheet]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    ct = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
          '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
          '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
          '<Default Extension="xml" ContentType="application/xml"/>'
          '<Override PartName="/xl/workbook.xml" '
          'ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
          '<Override PartName="/xl/styles.xml" '
          'ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>']
    wb = [f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><workbook xmlns="{NS}" xmlns:r="{NS_R}"><sheets>']
    rels = [f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="{NS_PKG}">']
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for i, sh in enumerate(sheets, start=1):
            z.writestr(f"xl/worksheets/sheet{i}.xml", _sheet_xml(sh))
            ct.append(f'<Override PartName="/xl/worksheets/sheet{i}.xml" '
                      'ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>')
            wb.append(f'<sheet name="{escape(sh.name)}" sheetId="{i}" r:id="rId{i}"/>')
            rels.append(f'<Relationship Id="rId{i}" Type="{NS_R}/worksheet" Target="worksheets/sheet{i}.xml"/>')
        rels.append(f'<Relationship Id="rId{len(sheets) + 1}" Type="{NS_R}/styles" Target="styles.xml"/>')
        z.writestr("[Content_Types].xml", "".join(ct) + "</Types>")
        z.writestr("_rels/.rels", f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                                  f'<Relationships xmlns="{NS_PKG}"><Relationship Id="rId1" '
                                  f'Type="{NS_R}/officeDocument" Target="xl/workbook.xml"/></Relationships>')
        z.writestr("xl/workbook.xml", "".join(wb) + "</sheets></workbook>")
        z.writestr("xl/_rels/workbook.xml.rels", "".join(rels) + "</Relationships>")
        z.writestr("xl/styles.xml", _STYLES)


@dataclass
class Workbook:
    sheets: dict[str, list[list[str]]]
    formulas: dict[str, int]
    merged: dict[str, int]


def _ref_col(ref: str) -> int:
    n = 0
    for ch in re.match(r"[A-Z]+", ref).group(0):
        n = n * 26 + ord(ch) - 64
    return n - 1


def read_xlsx(path: Path) -> Workbook:
    q = lambda t: f"{{{NS}}}{t}"  # noqa: E731
    with zipfile.ZipFile(path) as z:
        names = set(z.namelist())
        shared = []
        if "xl/sharedStrings.xml" in names:
            for si in ET.fromstring(z.read("xl/sharedStrings.xml")).iter(q("si")):
                shared.append("".join(t.text or "" for t in si.iter(q("t"))))
        rels = {r.get("Id"): r.get("Target") for r in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
        wb = ET.fromstring(z.read("xl/workbook.xml"))
        out = Workbook({}, {}, {})
        for sh in wb.iter(q("sheet")):
            target = rels[sh.get(f"{{{NS_R}}}id")].lstrip("/")
            target = target if target.startswith("xl/") else "xl/" + target
            root = ET.fromstring(z.read(target))
            rows = []
            for row in root.iter(q("row")):
                vals: dict[int, str] = {}
                for c in row.iter(q("c")):
                    t, v = c.get("t"), c.find(q("v"))
                    if t == "inlineStr":
                        val = "".join(x.text or "" for x in c.iter(q("t")))
                    elif t == "s":
                        val = shared[int(v.text)] if v is not None else ""
                    else:
                        val = v.text if v is not None and v.text is not None else ""
                    vals[_ref_col(c.get("r"))] = val
                width = max(vals) + 1 if vals else 0
                rows.append([vals.get(i, "") for i in range(width)])
            name = sh.get("name")
            out.sheets[name] = rows
            out.formulas[name] = sum(1 for _ in root.iter(q("f")))
            out.merged[name] = sum(1 for _ in root.iter(q("mergeCell")))
        return out
