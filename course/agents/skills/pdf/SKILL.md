# PDF Generation Skill

> Reference for any mode that needs to generate PDF documents. Use Python reportlab to create professional, styled PDFs.

---

## Setup

```bash
pip install reportlab
```

## Quick Start — Generate a PDF

Write a Python script and execute it. Example pattern:

```python
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.graphics.shapes import Drawing, Rect, String
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.barcharts import VerticalBarChart

def generate_pdf(output_path, data):
    doc = SimpleDocTemplate(output_path, pagesize=letter,
                            leftMargin=0.75*inch, rightMargin=0.75*inch,
                            topMargin=0.75*inch, bottomMargin=0.75*inch)
    styles = getSampleStyleSheet()
    elements = []

    # Title
    title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=24, spaceAfter=20)
    elements.append(Paragraph(data['title'], title_style))

    # Body
    elements.append(Paragraph(data['body'], styles['Normal']))

    # Table
    table_data = [['Header 1', 'Header 2', 'Header 3']] + data['rows']
    table = Table(table_data, colWidths=[2*inch, 2*inch, 2*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a365d')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8fafc')]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e2e8f0')),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    elements.append(table)

    doc.build(elements)
```

## Charts

### Donut/Pie Chart
```python
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing

d = Drawing(200, 200)
pie = Pie()
pie.x = 50; pie.y = 50; pie.width = 100; pie.height = 100
pie.data = [65, 5]  # pass, fail
pie.slices[0].fillColor = colors.HexColor('#16a34a')
pie.slices[1].fillColor = colors.HexColor('#dc2626')
pie.innerRadiusFraction = 0.5  # donut
d.add(pie)
elements.append(d)
```

### Bar Chart
```python
from reportlab.graphics.charts.barcharts import VerticalBarChart

d = Drawing(400, 200)
bc = VerticalBarChart()
bc.x = 50; bc.y = 50; bc.width = 300; bc.height = 125
bc.data = [[12, 7, 5, 8, 6, 3]]
bc.categoryAxis.categoryNames = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6']
bc.bars[0].fillColor = colors.HexColor('#3b82f6')
d.add(bc)
elements.append(d)
```

## Color-Coded Status Rows

```python
# Color rows based on severity/status
for i, row in enumerate(data_rows, start=1):
    severity = row[1]
    if severity == 'Critical':
        bg = colors.HexColor('#fef2f2')  # red tint
    elif severity == 'High':
        bg = colors.HexColor('#fff7ed')  # orange tint
    elif severity == 'Pass':
        bg = colors.HexColor('#f0fdf4')  # green tint
    else:
        bg = colors.white
    table_style.add('BACKGROUND', (0, i), (-1, i), bg)
```

## Header/Footer on Every Page

```python
def header_footer(canvas, doc):
    canvas.saveState()
    # Header bar
    canvas.setFillColor(colors.HexColor('#1a365d'))
    canvas.rect(0, letter[1] - 40, letter[0], 40, fill=True)
    canvas.setFillColor(colors.white)
    canvas.setFont('Helvetica-Bold', 10)
    canvas.drawString(54, letter[1] - 26, 'Product Name — Report Title')
    canvas.drawRightString(letter[0] - 54, letter[1] - 26, '2026-03-15')
    # Footer
    canvas.setFillColor(colors.HexColor('#6b7280'))
    canvas.setFont('Helvetica', 8)
    canvas.drawCentredString(letter[0]/2, 30, f'Page {doc.page}')
    canvas.restoreState()

doc.build(elements, onFirstPage=header_footer, onLaterPages=header_footer)
```

## Unicode Symbols for Status

Use these in table cells for visual indicators:
- Pass: ✅ or ✓ (use Paragraph with UTF-8 font)
- Fail: ❌ or ✗
- Warning: ⚠️
- Info: ℹ️

```python
# For Unicode in reportlab, use Paragraph instead of plain strings
from reportlab.platypus import Paragraph
pass_cell = Paragraph('✅ Pass', ParagraphStyle('status', fontSize=10))
```

## Best Practices

- Always use `Helvetica` (built-in, no font files needed)
- Use `HexColor` for precise brand colors
- Keep margins at 0.75 inch
- Header bar on every page for professional look
- Alternating row colors in all tables
- Color-code severity/status (red/orange/yellow/green)
- Include page numbers in footer
- Generate to `.onemillion/assets/` directory
