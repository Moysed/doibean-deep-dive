"""
Build DoiBean Boardroom Summary PDF.
Uses reportlab + Tahoma (system font, supports Thai).
"""
import sys, io, os
from datetime import date
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, KeepTogether, HRFlowable
)

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ── Thai font registration ─────────────────────────────
pdfmetrics.registerFont(TTFont('Tahoma',   'C:/Windows/Fonts/tahoma.ttf'))
pdfmetrics.registerFont(TTFont('Tahoma-B', 'C:/Windows/Fonts/tahomabd.ttf'))
pdfmetrics.registerFontFamily(
    'Tahoma',
    normal='Tahoma', bold='Tahoma-B',
    italic='Tahoma', boldItalic='Tahoma-B'
)

# ── Palette (matches doibean editorial system) ─────────
BONE      = HexColor('#F4EFE6')
PAPER     = HexColor('#FBF7EE')
ESPRESSO  = HexColor('#2A1810')
INK       = HexColor('#1A0F08')
CREMA     = HexColor('#C8A268')
BRICK     = HexColor('#B8543A')
MOSS      = HexColor('#5C6B3F')
STONE     = HexColor('#C9C0B0')
SLATE     = HexColor('#5A4D3F')

# ── Styles ─────────────────────────────────────────────
styles = getSampleStyleSheet()

def style(name, parent=None, **kw):
    base = parent or styles['Normal']
    kw.setdefault('fontName', 'Tahoma')
    return ParagraphStyle(name=name, parent=base, **kw)

S_COVER_TITLE   = style('CoverTitle', fontName='Tahoma-B', fontSize=42, leading=48, textColor=ESPRESSO, alignment=TA_LEFT, spaceAfter=10)
S_COVER_SUBTITLE= style('CoverSub',   fontSize=16, leading=22, textColor=SLATE, spaceAfter=24)
S_COVER_META    = style('CoverMeta',  fontSize=10, leading=14, textColor=SLATE, spaceAfter=6)
S_LABEL         = style('Label',      fontName='Tahoma-B', fontSize=8, leading=12, textColor=BRICK, spaceAfter=4)
S_H1            = style('H1', fontName='Tahoma-B', fontSize=22, leading=28, textColor=ESPRESSO, spaceBefore=18, spaceAfter=10)
S_H2            = style('H2', fontName='Tahoma-B', fontSize=15, leading=22, textColor=INK, spaceBefore=14, spaceAfter=6)
S_H3            = style('H3', fontName='Tahoma-B', fontSize=12, leading=18, textColor=BRICK, spaceBefore=10, spaceAfter=4)
S_BODY          = style('Body', fontSize=10.5, leading=16, textColor=INK, alignment=TA_JUSTIFY, spaceAfter=6)
S_BODY_TIGHT    = style('BodyTight', fontSize=10, leading=14, textColor=INK, spaceAfter=4)
S_QUOTE         = style('Quote', fontName='Tahoma', fontSize=11, leading=17, textColor=SLATE, leftIndent=14, rightIndent=14, spaceBefore=6, spaceAfter=6, borderPadding=8)
S_BULLET        = style('Bullet', fontSize=10.5, leading=15, textColor=INK, leftIndent=14, bulletIndent=4, spaceAfter=3)
S_CAPTION       = style('Caption', fontSize=9, leading=12, textColor=SLATE, alignment=TA_LEFT)
S_CALLOUT_BODY  = style('Callout', fontSize=10.5, leading=15, textColor=INK, alignment=TA_LEFT)
S_TABLE         = style('Table', fontSize=9.5, leading=13, textColor=INK, alignment=TA_LEFT, wordWrap='LTR')
S_TABLE_KEY     = style('TableKey', fontName='Tahoma-B', fontSize=9.5, leading=13, textColor=SLATE, alignment=TA_LEFT, wordWrap='LTR')
S_TABLE_HEAD    = style('TableHead', fontName='Tahoma-B', fontSize=9, leading=12, textColor=BONE, alignment=TA_LEFT, wordWrap='LTR')


def P(text, st=S_TABLE):
    """Wrap a cell value in a Paragraph so it word-wraps within column width."""
    if hasattr(text, 'wrap'):  # already a flowable
        return text
    return Paragraph(str(text), st)


def hr(color=STONE, thickness=0.5, space_before=4, space_after=4):
    return HRFlowable(width="100%", thickness=thickness, color=color,
                      spaceBefore=space_before, spaceAfter=space_after)

def thick_hr():
    return hr(color=INK, thickness=1.4, space_before=8, space_after=10)


# ── Page frame: header + footer ────────────────────────
def page_frame(canvas, doc):
    canvas.saveState()
    canvas.setFont('Tahoma', 8)
    canvas.setFillColor(SLATE)
    # header
    canvas.drawString(20*mm, A4[1] - 12*mm, 'DOIBEAN  ·  BOARDROOM SUMMARY')
    canvas.drawRightString(A4[0] - 20*mm, A4[1] - 12*mm, 'Vol. 01  ·  พฤษภาคม 2026')
    canvas.setStrokeColor(STONE)
    canvas.setLineWidth(0.4)
    canvas.line(20*mm, A4[1] - 14*mm, A4[0] - 20*mm, A4[1] - 14*mm)
    # footer
    canvas.setFillColor(SLATE)
    canvas.drawString(20*mm, 10*mm, 'สำหรับท่านประธาน · มอนด์ @Moysed')
    canvas.drawRightString(A4[0] - 20*mm, 10*mm, f'หน้า {doc.page}')
    canvas.line(20*mm, 13*mm, A4[0] - 20*mm, 13*mm)
    canvas.restoreState()


# ── Tables helper ──────────────────────────────────────
def kv_table(rows, col_widths=None, header_row=False):
    """All cell values are auto-wrapped in Paragraphs so long Thai text breaks across lines."""
    cw = col_widths or [40*mm, 120*mm]
    wrapped = []
    for r_idx, row in enumerate(rows):
        new_row = []
        for c_idx, cell in enumerate(row):
            if header_row and r_idx == 0:
                new_row.append(P(cell, S_TABLE_HEAD))
            elif c_idx == 0 and not (header_row and r_idx == 0):
                new_row.append(P(cell, S_TABLE_KEY))
            else:
                new_row.append(P(cell, S_TABLE))
        wrapped.append(new_row)
    t = Table(wrapped, colWidths=cw, hAlign='LEFT', repeatRows=1 if header_row else 0)
    style_cmds = [
        ('VALIGN',   (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING',  (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING',   (0,0), (-1,-1), 5),
        ('BOTTOMPADDING',(0,0), (-1,-1), 5),
        ('LINEBELOW', (0,0), (-1,-2), 0.3, STONE),
    ]
    if header_row:
        style_cmds.extend([
            ('BACKGROUND', (0,0), (-1,0), INK),
            ('TOPPADDING', (0,0), (-1,0), 8),
            ('BOTTOMPADDING', (0,0), (-1,0), 8),
            ('LINEBELOW', (0,0), (-1,0), 0, INK),
        ])
    t.setStyle(TableStyle(style_cmds))
    return t


def callout_box(label, body_html, fill=PAPER, border=STONE, label_color=BRICK):
    p_label = Paragraph(label, ParagraphStyle('cl', parent=S_LABEL, textColor=label_color))
    p_body  = Paragraph(body_html, S_CALLOUT_BODY)
    inner = [[p_label],[p_body]]
    t = Table(inner, colWidths=[160*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), fill),
        ('BOX',        (0,0), (-1,-1), 0.5, border),
        ('LEFTPADDING',  (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING',   (0,0), (-1,-1), 10),
        ('BOTTOMPADDING',(0,0), (-1,-1), 10),
    ]))
    return t


# ── Build story ────────────────────────────────────────
story = []

# ──── COVER ────────────────────────────────────────────
story.append(Spacer(1, 28*mm))
story.append(Paragraph('<font color="#B8543A">DoiBean</font>', S_COVER_TITLE))
story.append(Paragraph('สรุปการประชุมบอร์ดที่ปรึกษา', S_COVER_SUBTITLE))
story.append(thick_hr())
story.append(Spacer(1, 4*mm))
story.append(Paragraph('<b>เรื่อง</b>  วิเคราะห์ขอบเขตโครงการ &nbsp;&middot;&nbsp; สิ่งที่ขาด &nbsp;&middot;&nbsp; การจับมูลค่า &nbsp;&middot;&nbsp; เชียงใหม่กับ Digital Economy', S_COVER_META))
story.append(Paragraph('<b>ประเภท</b> &nbsp; รายงานสรุป 3 รอบประชุมจากที่ปรึกษา 8 ท่าน', S_COVER_META))
story.append(Paragraph(f'<b>วันที่</b> &nbsp; พฤษภาคม 2026', S_COVER_META))
story.append(Paragraph('<b>ผู้บริหาร</b> &nbsp; มอนด์ &middot; @Moysed', S_COVER_META))
story.append(Spacer(1, 16*mm))

# advisors panel
_adv_head = style('AdvHead', fontName='Tahoma-B', fontSize=9, leading=12, textColor=BRICK, wordWrap='LTR')
_adv_cell = style('AdvCell', fontSize=10, leading=14, textColor=INK, wordWrap='LTR')
advisor_grid = [
    [P('รอบที่ 1 — ธุรกิจ', _adv_head), P('รอบที่ 2 — Sovereignty', _adv_head), P('รอบที่ 3 — เทคโนโลยี', _adv_head)],
    [P('ธนินท์ เจียรวนนท์', _adv_cell),    P('Top Jirayut (เพิ่ม)', _adv_cell),       P('Andrej Karpathy', _adv_cell)],
    [P('กระทิง พูนผล', _adv_cell),         P('Srettha Thavisin (เพิ่ม)', _adv_cell),  P('John Carmack', _adv_cell)],
    [P('Charlie Munger', _adv_cell),       P('', _adv_cell),                          P('George Hotz', _adv_cell)],
    [P('Jeff Bezos', _adv_cell),           P('', _adv_cell),                          P('9arm (อาร์ม)', _adv_cell)],
]
t = Table(advisor_grid, colWidths=[55*mm, 55*mm, 55*mm])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), PAPER),
    ('LINEBELOW', (0,0), (-1,0), 1, INK),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING',  (0,0), (-1,-1), 10),
    ('TOPPADDING',   (0,0), (-1,-1), 7),
    ('BOTTOMPADDING',(0,0), (-1,-1), 7),
]))
story.append(t)

story.append(PageBreak())

# ──── EXEC SUMMARY ─────────────────────────────────────
story.append(Paragraph('บทสรุปผู้บริหาร', S_H1))
story.append(thick_hr())

story.append(Paragraph('DoiBean คืออะไร', S_H3))
story.append(Paragraph(
    'AI co-pilot สำหรับชาวสวนกาแฟ specialty บนดอยช้าง จังหวัดเชียงราย '
    'ปิดช่องว่างราคา 25 เท่าระหว่างหน้าฟาร์ม (฿100/กก.) และร้านคาเฟ่ (฿2,500/กก.) '
    'โดยเป็นเจ้าของวงจรเต็มรูปแบบ ตั้งแต่เลือกสายพันธุ์ที่จะปลูก สแกนคุณภาพเมล็ดด้วย CV '
    'ไปจนถึงตลาดขายตรงให้ roaster ต่างประเทศ', S_BODY))

story.append(Paragraph('คำถามตั้งต้น 4 ข้อ', S_H3))
story.append(Paragraph('1) ขอบเขตโครงการเป็นอย่างไร', S_BULLET, bulletText='•'))
story.append(Paragraph('2) ขาดอะไร', S_BULLET, bulletText='•'))
story.append(Paragraph('3) จะได้ประโยชน์อย่างไร', S_BULLET, bulletText='•'))
story.append(Paragraph('4) ส่งผลต่อเชียงใหม่ในการเป็นเมืองแอปมูลค่าสูงอย่างไร', S_BULLET, bulletText='•'))

story.append(Paragraph('สรุปข้อค้นพบหลัก (ใน 5 บรรทัด)', S_H3))

story.append(callout_box(
    'KEY FINDINGS',
    '<b>1.</b> แนวคิดถูก — สามความล้มเหลว (information asymmetry / no direct channel / wrong crop) แก้ได้ด้วยการรวม CV + LLM + marketplace<br/>'
    '<b>2.</b> ขาดทีม &middot; ขาดลำดับลูกค้า &middot; ขาดแผน physical infrastructure &middot; ขาดประกาศ kill modes<br/>'
    '<b>3.</b> Tech stack ใหญ่เกิน — ตัด Mapbox / Stripe ปี 1 / S3 และเปลี่ยนจาก Anthropic API → THaLLE local เพื่อ sovereignty<br/>'
    '<b>4.</b> Data training 500 ภาพไม่พอ — ต้องเก็บอีก 2,000+ ก่อน train จริง<br/>'
    '<b>5.</b> NDEA Chiang Mai Digital Economy = ลูกค้าใหม่ + พันธมิตรรัฐ — เปลี่ยน HQ จากกรุงเทพ → เชียงใหม่ '
    'แต่เชียงใหม่เป็น brand origin ไม่ใช่ tech HQ ระยะยาว',
    fill=PAPER, border=BRICK, label_color=BRICK
))

story.append(PageBreak())

# ──── ROUND 1: BUSINESS BOARD ─────────────────────────
story.append(Paragraph('รอบที่ 1 &middot; บอร์ดธุรกิจ', S_H1))
story.append(Paragraph('ธนินท์ เจียรวนนท์ &middot; กระทิง พูนผล &middot; Charlie Munger &middot; Jeff Bezos', S_CAPTION))
story.append(thick_hr())

story.append(Paragraph('สิ่งที่ดี (ห้องเห็นตรงกัน)', S_H2))
good_rows = [
    ['Wedge ถูก',      'Quality verification เป็นความเจ็บปวดที่มีจริง — ชาวสวนเป็น price-taker เพราะไม่มีคะแนน SCA ของตัวเอง'],
    ['Lifecycle ถูก',   '6 โมดูลครอบคลุมทั้งปีของชาวสวน — แอป touch-เดียวจะ churn แอปทั้งปีจะถูกใช้ 100 ครั้ง/ปี'],
    ['Scope discipline','60-day MVP ตัด 3 โมดูล เก็บ 3 — founder ส่วนใหญ่ทำไม่ได้ การรู้ว่าจะไม่ทำอะไรคือสิ่งที่ทำให้ ship ได้'],
    ['3 Failures',     'Information asymmetry / no direct channel / wrong crop — ทั้งสาม solvable เทคโนโลยีพร้อมและตรงปัญหา'],
]
story.append(kv_table(good_rows))

story.append(Paragraph('สิ่งที่ขาด (ห้องเห็นตรงกัน)', S_H2))
lack_rows = [
    ['ลำดับลูกค้า',      'มี 2 customers (farmer + roaster) ยังไม่ตัดสินใจว่า v1 ตอบใครก่อน — Bezos: roaster เป็น economic customer'],
    ['Physical infra',  'แอปไม่ใช่ธุรกิจ — โกดัง cold chain financial bridging ชาวสวนรอเงิน export ทั้งหมดยังไม่มีแผน'],
    ['ทีม',              'Solo founder + ไม่มี co-founder + ไม่มี CTO + ไม่มี ASEAN narrative + ยังไม่ระดม pre-seed'],
    ['Defect declaration','คูเมืองความสัมพันธ์ Tokyo roaster ใช้เวลา 30 ปี ไม่ใช่ 30 วัน — deep-dive treats roaster trust เป็น marketing'],
]
story.append(kv_table(lack_rows))

story.append(Paragraph('คำแนะนำ (ห้องแตก แล้วบรรจบ)', S_H2))
adv_rows = [
    ['ธนินท์',  'ปี 1-3 แคบ ดอยช้าง 20 ครอบครัว วางทับสหกรณ์ premium 5% lane ความสัมพันธ์เป็นของใครยังอยู่ปีที่ 10'],
    ['กระทิง',  'Pre-seed hackathon ใช้ dtac/KXVC scale ASEAN ปีที่ 4 — Specialty Agriculture OS ไม่ใช่แค่กาแฟไทย'],
    ['Bezos',  'เลือก customer ก่อน — เขียน PR/FAQ 2-3 ฉบับ Type 1 decisions ใช้ 6-page memo'],
    ['Munger', 'Invert — ตั้งชื่อ kill modes 5 ข้อใน deep-dive ก่อตั้งบนความล้มเหลว ไม่ใช่ความสำเร็จ'],
]
story.append(kv_table(adv_rows, col_widths=[30*mm, 130*mm]))

story.append(Spacer(1, 6*mm))
story.append(callout_box(
    'SYNTHESIS',
    'ธนินท์ถูกในปีที่ 1-3 &nbsp;&middot;&nbsp; กระทิงถูกตั้งแต่ปีที่ 4 เป็นต้นไป &nbsp;&middot;&nbsp; '
    'Bezos ถูกเรื่อง operating discipline &nbsp;&middot;&nbsp; Munger ถูกเรื่องสิ่งที่ขาด<br/>'
    '<b>เลือกลำดับ ไม่ใช่เลือกข้าง</b>',
    fill=BONE, border=INK, label_color=INK
))

story.append(PageBreak())

# ──── ROUND 2: SOVEREIGNTY + GOV PARTNERSHIP ──────────
story.append(Paragraph('รอบที่ 2 &middot; เพิ่ม Sovereignty + รัฐพันธมิตร', S_H1))
story.append(Paragraph('Top Jirayut (เพิ่ม) &middot; Srettha Thavisin (เพิ่ม) &middot; ห้องเดิมยังอยู่', S_CAPTION))
story.append(thick_hr())

story.append(Paragraph('Frame เปลี่ยน — DoiBean เป็นแอปพัฒนาจังหวัดเชียงใหม่', S_H2))
story.append(Paragraph(
    'NDEA + Decentrix + สำนักงานอุตสาหกรรมเชียงใหม่ run โครงการ Chiang Mai Global Digital Economy City '
    '— DoiBean เป็น flagship ใน sector AgriTech (1 ใน 8 sector) เปลี่ยนจาก private startup เป็น public-private initiative',
    S_BODY))

story.append(Paragraph('Top Jirayut: 5-Layer Cake — DoiBean อยู่ชั้นไหน?', S_H2))
_st_safe   = style('LSafe',   fontName='Tahoma-B', fontSize=9, leading=12, textColor=MOSS,  wordWrap='LTR')
_st_warn   = style('LWarn',   fontName='Tahoma-B', fontSize=9, leading=12, textColor=BRICK, wordWrap='LTR')
layer_rows = [
    [P('Layer', S_TABLE_HEAD),       P('ใครเป็นเจ้าของของคุณ', S_TABLE_HEAD), P('สถานะ Sovereignty', S_TABLE_HEAD)],
    [P('1. Energy', S_TABLE_KEY),    P('ไทย (กฟผ)', S_TABLE),                  P('ปลอดภัย', _st_safe)],
    [P('2. Chips', S_TABLE_KEY),     P('TSMC / Nvidia (US-Taiwan)', S_TABLE),  P('เมืองขึ้น', _st_warn)],
    [P('3. Cloud', S_TABLE_KEY),     P('AWS / GCP (US)', S_TABLE),             P('เมืองขึ้น', _st_warn)],
    [P('4. AI Models', S_TABLE_KEY), P('Anthropic Claude Haiku (US)', S_TABLE),P('เมืองขึ้นชัดเจน', _st_warn)],
    [P('5. AI Apps', S_TABLE_KEY),   P('DoiBean (Thai)', S_TABLE),             P('ของเรา', _st_safe)],
]
t = Table(layer_rows, colWidths=[35*mm, 80*mm, 45*mm])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), INK),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING',  (0,0), (-1,-1), 8),
    ('TOPPADDING',   (0,0), (-1,-1), 6),
    ('BOTTOMPADDING',(0,0), (-1,-1), 6),
    ('LINEBELOW', (0,1), (-1,-2), 0.3, STONE),
]))
story.append(t)

story.append(Paragraph('Top: 4 ข้อแนะนำ', S_H3))
story.append(Paragraph('1. <b>เปลี่ยน LLM</b> — Claude Haiku → THaLLE ของ KBTG (open-source, Thai-trained) data ชาวสวนต้องไม่ไหลออกประเทศ', S_BULLET, bulletText='•'))
story.append(Paragraph('2. <b>กฎหมายมาก่อน</b> — คุย กรมเจรจาการค้า / กรมส่งเสริมการเกษตร / PDPA / SEC ก่อนทำ', S_BULLET, bulletText='•'))
story.append(Paragraph('3. <b>Sustainability ก่อน growth</b> — Top เสีย 37M ปีแรกเพราะวิ่งหา growth ปีแรก unit economics ของ 20 ฟาร์มก่อน', S_BULLET, bulletText='•'))
story.append(Paragraph('4. <b>Tokenize lot</b> — Phase 2 RWA บน Bitkub Chain ระดมทุน fractional ownership "1 ต้นกาแฟ"', S_BULLET, bulletText='•'))

story.append(Paragraph('Srettha: 3 อย่างเปลี่ยนเพราะรัฐหนุน', S_H3))
story.append(Paragraph('1. Customer ใหม่ = ราชการ + จังหวัด (NDEA, Industrial Office) จ่าย grant + showcase + ทุน', S_BULLET, bulletText='•'))
story.append(Paragraph('2. Distribution ใหม่ = extension services — สหกรณ์ที่ Munger เตือนจะ lobby ฆ่า กลายเป็นพันธมิตร', S_BULLET, bulletText='•'))
story.append(Paragraph('3. Brand ใหม่ = "Made in Chiang Mai" — verified-origin ของ Smart Province', S_BULLET, bulletText='•'))

story.append(Paragraph('ธนินท์แก้คำแนะนำ', S_H3))
story.append(callout_box(
    'HQ ย้ายไปเชียงใหม่',
    'ก่อนหน้านี้แนะกรุงเทพ — แต่เพราะรัฐสนับสนุน Three Benefits เปลี่ยน: '
    'จังหวัดได้ branding, ชาวสวนได้รายได้, DoiBean ได้ทุนรัฐ + impact fund &nbsp;&middot;&nbsp; '
    '<b>HQ เชียงใหม่ &middot; field office เชียงราย &middot; กรุงเทพคือ legal / banking</b>',
    fill=PAPER, border=BRICK
))

story.append(PageBreak())

# ──── ROUND 3: TECH BOARD ─────────────────────────────
story.append(Paragraph('รอบที่ 3 &middot; บอร์ดเทคโนโลยี', S_H1))
story.append(Paragraph('Andrej Karpathy &middot; John Carmack &middot; George Hotz &middot; 9arm', S_CAPTION))
story.append(thick_hr())

story.append(Paragraph('Karpathy: Have you looked at your data?', S_H2))
story.append(Paragraph(
    '500 ภาพ training สำหรับ defect taxonomy 30+ class = ~16 ตัวอย่าง/class &nbsp;&middot;&nbsp; '
    'underfit ก่อน train ด้วยซ้ำ',
    S_BODY))
story.append(Paragraph('6 phases ที่ต้องทำตามลำดับ', S_H3))
phase_rows = [
    ['1. Become one with data',  'ใช้ HOURS เปิดดูภาพทุกใบ — duplicate? corrupted label? light condition กระจายเท่าไหร่?'],
    ['2. Dumb baseline',         'ก่อน MobileNet — logistic regression บน color histogram เป็น floor'],
    ['3. Overfit one batch',     'ถ้า overfit ไม่ได้ = bug ใน loop ไม่ใช่ data'],
    ['4. Regularize',            'more data > augmentation > pretrain — เก็บภาพอีก 2,000+ ภาพ defect-balanced'],
    ['5. Tune',                  'random search ไม่ใช่ grid'],
    ['6. Squeeze juice',         'ensemble +2% ถ้าจริงจังต้องการ accuracy สุดท้าย'],
]
story.append(kv_table(phase_rows, col_widths=[55*mm, 105*mm]))

story.append(Paragraph('Carmack: ตัด stack ที่เกินจำเป็น', S_H2))
cut_rows = [
    ['ตัด',    'Mapbox &nbsp;&middot;&nbsp; ใช้ OpenStreetMap + leaflet ฟรีไม่ผูก subscription'],
    ['ตัด',    'Stripe Connect ปี 1 &nbsp;&middot;&nbsp; ใช้ PromptPay + manual roaster invoice ก่อน automate'],
    ['ตัด',    'S3 &nbsp;&middot;&nbsp; Postgres + filesystem ก่อน 100GB ไม่ต้องการ object storage'],
    ['เหลือ',  'Flutter app + Postgres + on-device TFLite (3 ชิ้น)'],
    ['เพิ่ม',   'Static analysis ตั้งแต่ commit แรก (mypy + dart analyze)'],
]
story.append(kv_table(cut_rows, col_widths=[20*mm, 140*mm]))

story.append(Paragraph('Hotz: 3 features เท่านั้น', S_H2))
story.append(callout_box(
    'MVP จริงๆ',
    '<b>1.</b> ถ่ายภาพเมล็ด → score<br/>'
    '<b>2.</b> Score post ลง list<br/>'
    '<b>3.</b> Buyer จ่ายเงินให้ farmer<br/><br/>'
    '<b>3 features end-to-end ไม่ใช่ 6</b> &nbsp;&middot;&nbsp; "you have never refactored enough" '
    '— ลบ Variety advisor ปี 1 (rules-based hardcoded หรือไม่ทำเลย) ปี 2 ค่อยเพิ่ม',
    fill=BONE, border=INK
))

story.append(Paragraph('9arm: ใช้ Thai infrastructure', S_H2))
infra_rows = [
    [P('ส่วน', S_TABLE_HEAD),             P('เปลี่ยนจาก', S_TABLE_HEAD),         P('ใช้แทนด้วย', S_TABLE_HEAD)],
    [P('LLM translation', S_TABLE_KEY),   P('Anthropic Claude Haiku', S_TABLE),   P('THaLLE 8B local (KBTG open-source)', S_TABLE)],
    [P('Image inference', S_TABLE_KEY),   P('Cloud', S_TABLE),                    P('TFLite on-device (privacy + offline + free)', S_TABLE)],
    [P('Cloud', S_TABLE_KEY),             P('AWS US-East', S_TABLE),              P('NIPA / CAT / AWS bkk-region', S_TABLE)],
    [P('HPC training', S_TABLE_KEY),      P('AWS GPU instances', S_TABLE),        P('LANTA (NSTDA) — applied funding ฟรี ถ้าเป็น Thai research', S_TABLE)],
]
t = Table(infra_rows, colWidths=[35*mm, 50*mm, 75*mm])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), MOSS),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING',  (0,0), (-1,-1), 8),
    ('TOPPADDING',   (0,0), (-1,-1), 6),
    ('BOTTOMPADDING',(0,0), (-1,-1), 6),
    ('LINEBELOW', (0,1), (-1,-2), 0.3, STONE),
]))
story.append(t)

story.append(PageBreak())

# ──── 60-DAY ACTION PLAN ──────────────────────────────
story.append(Paragraph('แผนปฏิบัติ 60 วันแรก', S_H1))
story.append(thick_hr())

_st_priority = style('Pri', fontName='Tahoma-B', fontSize=8.5, leading=12, textColor=BRICK, wordWrap='LTR')
plan_rows = [
    [P('สัปดาห์', S_TABLE_HEAD), P('ภารกิจ', S_TABLE_HEAD), P('ความสำคัญ', S_TABLE_HEAD)],
    [P('สัปดาห์ที่ 1-2', S_TABLE_KEY),
     P('เลือกลูกค้า v1 (roaster หรือ farmer) เขียน PR/FAQ 3 ฉบับ (จังหวัด + roaster + farmer) เพิ่มบทที่ 17 kill modes 5 ข้อใน deep-dive', S_TABLE),
     P('Type 1 Decision', _st_priority)],
    [P('สัปดาห์ที่ 3-4', S_TABLE_KEY),
     P('หา co-founder Chiang Rai (farmer relations) + CTO มี TFLite shipping experience + Designer ที่ทำ farmer UX ได้', S_TABLE),
     P('ทีมก่อนทุน', _st_priority)],
    [P('สัปดาห์ที่ 3-4', S_TABLE_KEY),
     P('สมัคร NDEA cohort ถัดไป · MOU กับ Decentrix — IP เป็นของ DoiBean ไม่ใช่ของเขา', S_TABLE),
     P('รัฐหนุน', _st_priority)],
    [P('สัปดาห์ที่ 5-6', S_TABLE_KEY),
     P('เก็บ Thai green-bean photos อีก 2,000+ ภาพ defect-balanced · ลบ Mapbox + Stripe + S3 จาก stack · ติดตั้ง THaLLE local inference', S_TABLE),
     P('Tech foundation', _st_priority)],
    [P('สัปดาห์ที่ 5-6', S_TABLE_KEY),
     P('Pre-seed ระดม $200K-$500K (500 TukTuks / KXVC / dtac Accelerate) กฎหมาย: คุย กรมเกษตร / กรมพาณิชย์ / PDPA', S_TABLE),
     P('ทุน + กฎ', _st_priority)],
    [P('สัปดาห์ที่ 7-8', S_TABLE_KEY),
     P('Pilot 3 farmers Doi Chang ผ่าน Doi Tung · ปิด 1 transaction กับ Bangkok roaster', S_TABLE),
     P('Proof of concept', _st_priority)],
    [P('สัปดาห์ที่ 9', S_TABLE_KEY),
     P('Polish: 90-second demo video + 10-slide deck + ซ้อมพรีเซ้นต์ 20 รอบ · pre-test failure modes', S_TABLE),
     P('Showcase', _st_priority)],
]
t = Table(plan_rows, colWidths=[28*mm, 98*mm, 34*mm])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), INK),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING',  (0,0), (-1,-1), 7),
    ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ('TOPPADDING',   (0,0), (-1,-1), 6),
    ('BOTTOMPADDING',(0,0), (-1,-1), 6),
    ('LINEBELOW', (0,1), (-1,-2), 0.3, STONE),
]))
story.append(t)

story.append(PageBreak())

# ──── KILL MODES + RISK ───────────────────────────────
story.append(Paragraph('ความเสี่ยง — 5 Kill Modes', S_H1))
story.append(Paragraph('สิ่งที่ Munger บอกว่าต้องเขียนเข้าไปใน deep-dive ตรงๆ', S_CAPTION))
story.append(thick_hr())

_st_kill_name = style('KillName', fontName='Tahoma-B', fontSize=9, leading=12, textColor=BRICK, wordWrap='LTR')
_st_kill = style('Kill', fontSize=8.5, leading=12, textColor=INK, alignment=TA_LEFT, wordWrap='LTR')
kill_rows = [
    [P('1. กฎหมาย certified-export', _st_kill_name),
     P('สหกรณ์ lobby ออกกฎ "export quality certification" ที่ออกได้เฉพาะหน่วยงานรับรอง — แอปกลายเป็นใช้เชิงพาณิชย์ผิดกฎหมาย', _st_kill),
     P('คุย กรมเกษตร + กรมพาณิชย์ตั้งแต่สัปดาห์แรก หา ally ในระดับนโยบาย', _st_kill)],
    [P('2. Variety advisor ผิด', _st_kill_name),
     P('IPCC RCP scenarios ไม่แม่น แนะปลูก Catimor 1,200m → ปีที่ 3 climate model ผิด → ลูกค้าฟ้อง', _st_kill),
     P('เพิ่ม disclaimer + uncertainty band + SHAP ให้ farmer ตัดสินใจเอง ปี 1 rules-based ปี 2 ขยับ XGBoost', _st_kill)],
    [P('3. Two-sided cold start', _st_kill_name),
     P('Roaster Tokyo ไม่เชื่อคะแนน CV จากแอปไทยใหม่ — chicken-and-egg ฆ่า marketplace 18 เดือนแรก', _st_kill),
     P('Roaster ก่อน farmer — anchor 1 trusted Thai/Japanese specialty buyer ก่อน scale farmer side', _st_kill)],
    [P('4. Solo founder burn out', _st_kill_name),
     P('Mond ทำ 4 บทบาทคนเดียว — ครั้งแรกที่ป่วย/เหนื่อย = บริษัทหยุด', _st_kill),
     P('Co-founder Chiang Rai + CTO ภายใน 60 วัน ไม่งั้นไม่ขยับต่อ', _st_kill)],
    [P('5. Relationship moat 30 ปี', _st_kill_name),
     P('Premium roaster ซื้อความสัมพันธ์ ไม่ใช่กาแฟ — แอปทดแทนความสัมพันธ์ 30 ปีไม่ได้', _st_kill),
     P('แพลตฟอร์ม "carry the relationship" ไม่ใช่ "replace" — store Q-grader notes / video calls / annual visits', _st_kill)],
]
header_kill = [P('Kill mode', S_TABLE_HEAD), P('ทำไมจะตาย', S_TABLE_HEAD), P('การ mitigate', S_TABLE_HEAD)]
t = Table([header_kill] + kill_rows,
          colWidths=[42*mm, 60*mm, 58*mm])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), BRICK),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING',  (0,0), (-1,-1), 7),
    ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ('TOPPADDING',   (0,0), (-1,-1), 6),
    ('BOTTOMPADDING',(0,0), (-1,-1), 6),
    ('LINEBELOW', (0,1), (-1,-2), 0.3, STONE),
]))
story.append(t)

story.append(PageBreak())

# ──── CHIANG MAI ANGLE ────────────────────────────────
story.append(Paragraph('เชียงใหม่ในฐานะเมืองแอปมูลค่าสูง', S_H1))
story.append(Paragraph('คำตอบจาก 4 ที่ปรึกษา (ห้องแตกชัดเจน)', S_CAPTION))
story.append(thick_hr())

cm_rows = [
    ['กระทิง',  'เชียงใหม่ = launch city + case study + farm-to-Tokyo proof point ถ้า 100 ดอยช้าง farmers รายได้เพิ่ม 3× ใน 24 เดือน → ASEAN ทุก coffee region อยากได้บ้าง'],
    ['ธนินท์',  'เชียงใหม่ผลิตกาแฟ กรุงเทพผลิตบริษัท อย่าสับสนระหว่างที่ปลูกเมล็ดกับที่บริษัทควรอยู่ &mdash; แต่ Frame เปลี่ยนเพราะรัฐ NDEA หนุน → HQ เชียงใหม่ผ่อนได้'],
    ['Bezos',  'โลกไม่อยากได้กาแฟเชียงใหม่ — โลกอยากได้ origin เชียงใหม่ TAM ใหญ่กว่า: ทุก verified-origin export ของจังหวัด (ชา / สมุนไพร / น้ำผึ้ง / ข้าวหมู่บ้าน / งานคราฟต์)'],
    ['Munger', 'เชียงใหม่เป็น lifestyle city — Bangalore / Bangkok / Singapore เป็น tech city เพราะมี Infosys / KBTG / sovereign infra อย่าหลอกตัวเอง — แอปอาจ launch จากเชียงใหม่แต่ scale จากกรุงเทพ'],
]
story.append(kv_table(cm_rows, col_widths=[30*mm, 130*mm]))

story.append(Spacer(1, 6*mm))
story.append(callout_box(
    'POSITION ที่ห้องบรรจบ',
    'เชียงใหม่ = <b>brand origin city</b> &nbsp;&middot;&nbsp; <b>HQ</b> &nbsp;&middot;&nbsp; <b>field office จริง field เชียงราย</b> &nbsp;&middot;&nbsp; '
    '<b>กรุงเทพ = legal + banking + capital</b> &nbsp;&middot;&nbsp; '
    '<b>Singapore = IPO ปลายทาง</b> (ปี 4-5)<br/><br/>'
    'คำว่า "high-value app" คือ <b>verified-origin platform</b> ที่ทำให้ทุก export ของเชียงใหม่ '
    'มีราคา premium ไม่ใช่แค่กาแฟ — TAM ขยายจาก ฿XB → ฿XXB',
    fill=PAPER, border=BRICK
))

story.append(PageBreak())

# ──── FINAL SUMMARY ───────────────────────────────────
story.append(Paragraph('สรุปสุดท้าย — Action Items', S_H1))
story.append(thick_hr())

story.append(Paragraph('5 ข้อต้องทำทันทีใน 14 วัน', S_H2))
story.append(Paragraph('1. <b>เลือกลูกค้า v1</b> &nbsp;&mdash;&nbsp; เขียน PR/FAQ 3 ฉบับ (roaster / farmer / จังหวัด)', S_BULLET, bulletText='•'))
story.append(Paragraph('2. <b>หา co-founder + CTO</b> &nbsp;&mdash;&nbsp; โพสต์ที่ 500 TukTuks / dtac / KBTG ภายใน 7 วัน', S_BULLET, bulletText='•'))
story.append(Paragraph('3. <b>เพิ่มบทที่ 17 ใน deep-dive</b> &nbsp;&mdash;&nbsp; 5 kill modes + mitigations (สำหรับนักลงทุน + ตัวเอง)', S_BULLET, bulletText='•'))
story.append(Paragraph('4. <b>สมัคร NDEA cohort + MOU Decentrix</b> &nbsp;&mdash;&nbsp; IP เป็นของ DoiBean ระบุชัดในสัญญา', S_BULLET, bulletText='•'))
story.append(Paragraph('5. <b>เปลี่ยน LLM</b> &nbsp;&mdash;&nbsp; Anthropic API → THaLLE local (sovereignty)', S_BULLET, bulletText='•'))

story.append(Paragraph('Decisions Needed (ท่านประธานต้องตอบ)', S_H2))
dec_rows = [
    ['ลูกค้า v1',           'roaster หรือ farmer? (Bezos: roaster — เป็น economic customer)'],
    ['HQ',                'เชียงใหม่ (รัฐหนุน) หรือกรุงเทพ (capital + talent)?'],
    ['Speed',             'ASEAN ปี 2 (กระทิง) หรือ Doi Chang ปี 3 ก่อน (ธนินท์)?'],
    ['LLM',               'THaLLE local หรือ keep Claude (sovereignty trade-off)?'],
    ['Variety advisor v1','rules-based hardcoded (Hotz) หรือ XGBoost ตั้งแต่ปี 1 (Karpathy)?'],
    ['ความสามารถทน',         '15 ปี pain ทนได้ไหม? (Top — ถ้าตอบไม่ได้ ไม่พร้อม)'],
]
story.append(kv_table(dec_rows, col_widths=[40*mm, 120*mm]))

story.append(Spacer(1, 8*mm))
story.append(callout_box(
    'CLOSING — จากบอร์ดถึงท่านประธาน',
    'แนวคิดถูก สิ่งที่ขาดมีชื่อ สิ่งที่ต้องทำมีลำดับ &nbsp;&middot;&nbsp; '
    'ความเสี่ยงสูงสุดไม่ใช่ AI accuracy &mdash; <b>คือคูเมืองความสัมพันธ์ + ความเร็ว + ทีม</b><br/><br/>'
    '<b>ปิดประชุม</b> &nbsp;&middot;&nbsp; การตัดสินใจอยู่ที่ท่านประธาน',
    fill=INK, border=INK, label_color=CREMA
))
# override callout text color for dark variant
# (visible because body uses INK foreground; on dark fill we need light text)
# Reportlab callout already styled — for dark version, manually override via Paragraph

story.append(Spacer(1, 4*mm))
story.append(Paragraph(
    f'<para alignment="right"><font size="8" color="#5A4D3F"><i>Generated by Almondo-local Boardroom &middot; '
    f'พฤษภาคม 2026 &middot; for ม.มอนด์</i></font></para>',
    S_CAPTION
))


# ── Build doc ──────────────────────────────────────────
OUT = "D:/Folder Project/doibean-deep-dive/docs/DoiBean-Boardroom-Summary.pdf"
doc = SimpleDocTemplate(
    OUT, pagesize=A4,
    leftMargin=20*mm, rightMargin=20*mm,
    topMargin=20*mm,  bottomMargin=18*mm,
    title='DoiBean — สรุปการประชุมบอร์ดที่ปรึกษา',
    author='Almondo-local Boardroom',
)
doc.build(story, onFirstPage=page_frame, onLaterPages=page_frame)
print(f'OK: {OUT} ({os.path.getsize(OUT)} bytes)')
