# -*- coding: utf-8 -*-
"""رندر تصویری برچسب‌ها (۳۰۰ DPI) — خروجی PNG برای پیش‌نمایش و بازبینی.

    pip install pillow arabic_reshaper python-bidi fonttools brotli
    python3 render_preview.py

طرح دقیقاً از همان مقادیر میلی‌متری label_template.html پیروی می‌کند.
"""
import base64, io, json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display

HERE = Path(__file__).resolve().parent
FONTS_JSON = HERE.parent / 'workspace-01a04268-60f1-7e19-bce0-e27eb41243db' / 'ui' / 'selim-vand' / 'fonts_b64.json'
OUT = HERE / 'preview'
OUT.mkdir(exist_ok=True)

SCALE = 12          # پیکسل بر میلی‌متر  ≈ ۳۰۵ DPI
STORE = 'فروشگاه سلیم‌وند'


def fa_num(t: str) -> str:
    return ''.join('۰۱۲۳۴۵۶۷۸۹'[int(c)] if c.isdigit() else c for c in t)
SITE = 'salimvand.ir'

NAVY, ACCENT, TEXT, TEXT2, TEXT3 = '#0d2b4b', '#3f8ede', '#0b1c2f', '#4a5f79', '#8095ad'
CHIP_BG, CHIP_BD, CHIP_FG, BORDER = '#f1f6fd', '#e0ecfa', '#124270', '#c8d4e3'

# ----------------------------------------------------------------- فونت‌ها
_TTF: dict[str, bytes] = {}


def _load_fonts():
    from fontTools.ttLib import TTFont
    data = json.loads(FONTS_JSON.read_text(encoding='utf-8'))
    for w, b64 in data.items():
        f = TTFont(io.BytesIO(base64.b64decode(b64)))
        f.flavor = None
        buf = io.BytesIO()
        f.save(buf)
        _TTF[w] = buf.getvalue()


_load_fonts()
_CACHE: dict = {}


def fa_font(mm: float, weight: str = '400'):
    key = ('fa', round(mm, 3), weight)
    if key not in _CACHE:
        _CACHE[key] = ImageFont.truetype(io.BytesIO(_TTF[weight]), int(round(mm * SCALE)))
    return _CACHE[key]


def mono_font(mm: float, weight: str = '600'):
    key = ('mono', round(mm, 3), weight)
    if key not in _CACHE:
        for p in ('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',
                  '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'):
            if Path(p).exists():
                _CACHE[key] = ImageFont.truetype(p, int(round(mm * SCALE)))
                break
        else:
            _CACHE[key] = fa_font(mm, weight)
    return _CACHE[key]


def shape(t: str) -> str:
    """شکل‌دهی حروف فارسی + الگوریتم دوسویه (چون PIL بدون raqm ساخته شده)."""
    return get_display(arabic_reshaper.reshape(t))


# ----------------------------------------------------------------- بارکد
EAN_L = ['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
EAN_G = ['0100111','0110011','0011011','0100001','0011101','0111001','0000101','0010001','0001001','0010111']
EAN_R = ['1110010','1100110','1101100','1000010','1011100','1001110','1010000','1000100','1001000','1110100']
EAN_P = ['LLLLLL','LLGLGG','LLGGLG','LLGGGL','LGLLGG','LGGLLG','LGGGLL','LGLGLG','LGLGGL','LGGLGL']


def ean_check(b12: str) -> str:
    s = sum(int(d) * (3 if i % 2 else 1) for i, d in enumerate(b12[:12]))
    return str((10 - s % 10) % 10)


def ean13_from_sku(sku: str) -> str:
    h = 0
    for ch in sku:
        h = (h * 31 + ord(ch)) % 1_000_000_000
    body = ('626' + str(h).zfill(9))[:12]
    return body + ean_check(body)


def ean13_bits(code: str) -> str:
    p = EAN_P[int(code[0])]
    bits = '101'
    for i in range(1, 7):
        bits += (EAN_L if p[i - 1] == 'L' else EAN_G)[int(code[i])]
    bits += '01010'
    for i in range(7, 13):
        bits += EAN_R[int(code[i])]
    return bits + '101'


C128 = ["11011001100","11001101100","11001100110","10010011000","10010001100","10001001100","10011001000","10011000100","10001100100","11001001000","11001000100","11000100100","10110011100","10011011100","10011001110","10111001100","10011101100","10011100110","11001110010","11001011100","11001001110","11011100100","11001110100","11101101110","11101001100","11100101100","11100100110","11101100100","11100110100","11100110010","11011011000","11011000110","11000110110","10100011000","10001011000","10001000110","10110001000","10001101000","10001100010","11010001000","11000101000","11000100010","10110111000","10110001110","10001101110","10111011000","10111000110","10001110110","11101110110","11010001110","11000101110","11011101000","11011100010","11011101110","11101011000","11101000110","11100010110","11101101000","11101100010","11100011010","11101111010","11001000010","11110001010","10100110000","10100001100","10010110000","10010000110","10000101100","10000100110","10110010000","10110000100","10011010000","10011000010","10000110100","10000110010","11000010010","11001010000","11110111010","11000010100","10001111010","10100111100","10010111100","10010011110","10111100100","10011110100","10011110010","11110100100","11110010100","11110010010","11011011110","11011110110","11110110110","10101111000","10100011110","10001011110","10111101000","10111100010","11110101000","11110100010","10111011110","10111101110","11101011110","11110101110","11010000100","11010010000","11010011100","11000111010"]


def code128_bits(text: str) -> str:
    codes = [104] + [max(0, ord(c) - 32) for c in text]
    chk = (104 + sum(c * i for i, c in enumerate(codes) if i)) % 103
    return ''.join(C128[c] for c in codes) + C128[chk] + '1100011101011'


def draw_bars(d: ImageDraw.ImageDraw, bits: str, x: float, y: float, w: float, h: float, color='#000'):
    mw = w / len(bits)
    i = 0
    while i < len(bits):
        if bits[i] == '1':
            j = i
            while j < len(bits) and bits[j] == '1':
                j += 1
            d.rectangle([round(x + i * mw), round(y), round(x + j * mw) - 1, round(y + h)], fill=color)
            i = j
        else:
            i += 1


# ----------------------------------------------------------------- برچسب
SIZES = {
    '50x30': dict(w=50, h=30, hh=5.6, hpad=1.6, mk=3.8, f_store=2.1, f_url=1.8, bpad=(1.4, 1.8, 1.0),
                  f_name=2.5, f_meta=1.85, f_dig=2.1, f_foot=1.6, bc=6.4, gap=.62),
    '60x40': dict(w=60, h=40, hh=6.6, hpad=1.9, mk=4.4, f_store=2.5, f_url=2.0, bpad=(1.8, 2.2, 1.2),
                  f_name=3.0, f_meta=2.1, f_dig=2.4, f_foot=1.9, bc=8.0, gap=.85),
    '38x22': dict(w=38, h=22, hh=4.2, hpad=1.1, mk=2.9, f_store=1.75, f_url=1.45, bpad=(.9, 1.2, .7),
                  f_name=1.95, f_meta=1.5, f_dig=1.7, f_foot=0, bc=5.0, gap=.34),
}


def _pal(style):
    if style == 'mono':
        return dict(bg='#ffffff', bd='#000000', head='#000000', head_fg='#ffffff', mk_bg='#ffffff',
                    mk_fg='#000000', url='#ffffff', name='#000000', meta='#333333', sku='#000000',
                    chip_bg='#ffffff', chip_bd='#000000', chip_fg='#000000', dig='#000000',
                    foot='#333333', foot_ln='#666666', bar_bg=None, accent='#ffffff', dot='#666666')
    if style == 'navy':
        return dict(bg=NAVY, bd='#0a2440', head=None, head_fg='#ffffff', mk_bg='#ffffff', mk_fg=NAVY,
                    url='#bcd7f5', name='#ffffff', meta='#bcd7f5', sku='#ffffff',
                    chip_bg='#1b3d61', chip_bd='#3a5a80', chip_fg='#e0ecfa', dig='#0b1c2f',
                    foot='#7fb5ea', foot_ln='#2c4b६f'.replace('६', '6'), bar_bg='#ffffff',
                    accent=ACCENT, dot='#7fb5ea')
    return dict(bg='#ffffff', bd=BORDER, head=NAVY, head_fg='#ffffff', mk_bg='#ffffff', mk_fg=NAVY,
                url='#bcd7f5', name=TEXT, meta=TEXT2, sku=NAVY, chip_bg=CHIP_BG, chip_bd=CHIP_BD,
                chip_fg=CHIP_FG, dig=TEXT, foot=TEXT3, foot_ln='#dce4ee', bar_bg=None,
                accent=ACCENT, dot='#bcd7f5')


def label(prod, size='50x30', style='', bctype='ean13', show_sku=True, show_meta=True, show_foot=True):
    S, P = SIZES[size], _pal(style)
    px = lambda mm: int(round(mm * SCALE))
    W, H = px(S['w']), px(S['h'])
    img = Image.new('RGB', (W, H), '#ffffff')
    d = ImageDraw.Draw(img)
    r = px(1.6)
    d.rounded_rectangle([0, 0, W - 1, H - 1], r, fill=P['bg'], outline=P['bd'], width=max(1, px(.25)))

    # ---- سربرگ
    hh = px(S['hh'])
    if P['head']:
        d.rounded_rectangle([0, 0, W - 1, hh], r, fill=P['head'])
        d.rectangle([0, hh - r, W - 1, hh], fill=P['head'])
    else:
        d.line([px(.6), hh, W - px(.6), hh], fill='#33557a', width=max(1, px(.2)))
    d.rectangle([W - px(1.2), 1, W - 2, hh - 1], fill=P['accent'])      # نوار لهجه سمت راست (RTL)

    hp, mk = px(S['hpad']), px(S['mk'])
    x_r = W - hp - px(.5)
    d.rounded_rectangle([x_r - mk, (hh - mk) // 2, x_r, (hh - mk) // 2 + mk], px(1), fill=P['mk_bg'])
    f = fa_font(S['mk'] * .62, '700')
    t = shape('س')
    bb = d.textbbox((0, 0), t, font=f)
    d.text((x_r - mk / 2 - (bb[2] - bb[0]) / 2 - bb[0], hh / 2 - (bb[3] + bb[1]) / 2), t, font=f, fill=P['mk_fg'])

    f = fa_font(S['f_store'], '700')
    t = shape(STORE)
    tw = d.textlength(t, font=f)
    d.text((x_r - mk - px(1) - tw, hh / 2), t, font=f, fill=P['head_fg'], anchor='lm')

    f = mono_font(S['f_url'] * .95, '600')
    d.text((hp, hh / 2), SITE, font=f, fill=P['url'], anchor='lm')

    # ---- بدنه
    pt, pr, pb = px(S['bpad'][0]), px(S['bpad'][1]), px(S['bpad'][2])
    right, left = W - pr, pr
    y = hh + pt

    f = fa_font(S['f_name'], '700')
    name = shape(prod['name'])
    d.text((right, y), name, font=f, fill=P['name'], anchor='ra')
    y += px(S['f_name'] * 1.38)

    fm = fa_font(S['f_meta'], '400')
    if show_meta:
        y += px(S['gap'])
        ch = fa_font(S['f_meta'] * .95, '600')
        ct = shape(prod['cat'])
        cw = d.textlength(ct, font=ch) + px(1.8)
        chh = px(S['f_meta'] * 1.7)
        d.rounded_rectangle([right - cw, y, right, y + chh], px(.9), fill=P['chip_bg'], outline=P['chip_bd'])
        d.text((right - cw / 2, y + chh / 2), ct, font=ch, fill=P['chip_fg'], anchor='mm')
        dot = px(.35)
        cx = right - cw - px(1.2)
        d.ellipse([cx - dot, y + chh / 2 - dot, cx + dot, y + chh / 2 + dot], fill=P['dot'])
        d.text((cx - px(1.2), y + chh / 2), shape(prod['cars']), font=fm, fill=P['meta'], anchor='rm')
        y += chh + px(S['gap'] * .6)

    if show_sku:
        y += px(S['gap'] * .4)
        d.text((right, y), shape('کد کالا'), font=fa_font(S['f_meta'], '600'), fill=P['meta'], anchor='ra')
        d.text((left, y), prod['sku'], font=mono_font(S['f_meta'] * 1.05, '700'), fill=P['sku'], anchor='la')
        y += px(S['f_meta'] * 1.45)

    # ---- بارکد (چسبیده به پایین)
    foot_h = px(S['f_foot'] * 2.2) if (show_foot and S['f_foot']) else 0
    dig_h = px(S['f_dig'] * 1.5)
    avail = H - pb - foot_h - dig_h - y - px(.4)          # فضای باقی‌مانده تا پایین
    bc_h = max(px(3.2), min(px(S['bc']), avail))          # ارتفاع میله‌ها با محتوا تطبیق می‌یابد
    bc_y = H - pb - foot_h - dig_h - bc_h
    bx0, bx1 = left, right
    if P['bar_bg']:
        pad = px(.7)
        d.rounded_rectangle([bx0 - pad, bc_y - pad, bx1 + pad, bc_y + bc_h + dig_h + px(.2)],
                            px(1), fill=P['bar_bg'])

    if bctype == 'ean13':
        code = prod.get('ean') or ean13_from_sku(prod['sku'])
        bits = ean13_bits(code)
        digits = f'{code[0]} {code[1:7]} {code[7:]}'
    else:
        code = prod['sku'].upper()
        bits = code128_bits(code)
        digits = code
    draw_bars(d, bits, bx0, bc_y, bx1 - bx0, bc_h, '#000000')
    fd = mono_font(S['f_dig'], '600')
    d.text(((bx0 + bx1) / 2, bc_y + bc_h + px(.15)), digits, font=fd, fill=P['dig'], anchor='ma')

    # ---- پانویس
    if foot_h:
        fy = H - pb - foot_h
        for i in range(0, W - 2 * left, px(1.0)):        # خط‌چین
            d.line([left + i, fy, left + i + px(.5), fy], fill=P['foot_ln'], width=max(1, px(.15)))
        ff = fa_font(S['f_foot'], '400')
        d.text((right, fy + px(.4)), shape('اصالت و گارانتی کالا'), font=ff, fill=P['foot'], anchor='ra')
        d.text((left, fy + px(.4)), SITE, font=mono_font(S['f_foot'] * .95, '600'), fill=P['foot'], anchor='la')
    return img


# ----------------------------------------------------------------- صحنه
PRODUCTS = [
    dict(sku='BRK-00452', name='لنت ترمز جلو پژو ۲۰۶', cat='ترمز', cars='۲۰۶ تیپ ۲ و ۵ · ۲۰۷'),
    dict(sku='ELE-00640', name='باتری ۶۰ آمپر اتمی', cat='برقی و روشنایی', cars='عمومی — همه خودروها'),
    dict(sku='ENG-00377', name='شمع موتور سمند EF7', cat='موتور', cars='سمند EF7 · دنا'),
    dict(sku='FLT-00203', name='فیلتر روغن پراید و تیبا', cat='فیلتراسیون', cars='پراید · تیبا · ساینا'),
]

BG, CARD, GRID = '#f3f6fa', '#ffffff', '#eef3f9'


def board(items, title, sub, cols=None, pad=54, gap=44, path='board.png'):
    """چیدن چند برچسب روی یک بوم با سربرگ، شبیه صحنهٔ پیش‌نمایش سایت."""
    cols = cols or len(items)
    rows = (len(items) + cols - 1) // cols
    cw = max(im.width for im, _ in items)
    ch = max(im.height for im, _ in items)
    cap_h = 46
    head_h = 132
    W = pad * 2 + cols * cw + (cols - 1) * gap
    H = head_h + pad + rows * (ch + cap_h) + (rows - 1) * gap + pad
    img = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(img)
    for x in range(0, W, 26):
        d.line([x, head_h, x, H], fill=GRID)
    for y in range(head_h, H, 26):
        d.line([0, y, W, y], fill=GRID)

    d.rectangle([0, 0, W, head_h], fill=CARD)
    d.line([0, head_h, W, head_h], fill='#dce4ee')
    mk = 56
    d.rounded_rectangle([W - pad - mk, 38, W - pad, 38 + mk], 16, fill=NAVY)
    f = fa_font(2.6, '700')
    d.text((W - pad - mk / 2, 38 + mk / 2), shape('س'), font=f, fill='#fff', anchor='mm')
    d.text((W - pad - mk - 18, 46), shape(title), font=fa_font(2.1, '700'), fill=TEXT, anchor='ra')
    d.text((W - pad - mk - 18, 80), shape(sub), font=fa_font(1.55, '400'), fill=TEXT3, anchor='ra')
    d.text((pad, 62), SITE, font=mono_font(1.7, '600'), fill='#175894', anchor='lm')

    for i, (im, cap) in enumerate(items):
        r, c = divmod(i, cols)
        x = pad + c * (cw + gap) + (cw - im.width) // 2
        y = head_h + pad + r * (ch + cap_h + gap) + (ch - im.height) // 2
        sh = Image.new('RGB', (im.width + 8, im.height + 8), '#dde5ef')
        img.paste(sh, (x - 4, y - 2))
        img.paste(im, (x, y))
        d.text((pad + c * (cw + gap) + cw / 2, y + im.height + 16), shape(cap),
               font=fa_font(1.5, '600'), fill=TEXT2, anchor='ma')
    img.save(OUT / path)
    print(f'✓ {path}  {W}×{H}')
    return img


def main():
    p = PRODUCTS[0]
    board([(label(p, s), 'میلی‌متر ' + fa_num(s.split('x')[1] + '×' + s.split('x')[0])) for s in ('60x40', '50x30', '38x22')],
          'برچسب محصول — فروشگاه سلیم‌وند', 'سه اندازهٔ استاندارد · مقیاس ۱:۱ در ۳۰۵ DPI',
          path='01-sizes.png')

    board([(label(p, '50x30', st), cap) for st, cap in
           (('', 'سبک برند (چاپ رنگی)'), ('mono', 'تک‌رنگ (چاپگر حرارتی)'), ('navy', 'ناوی (پریمیوم)'))],
          'سه سبک چاپ', 'یک محصول، سه پرداخت بصری — اندازهٔ ۵۰×۳۰',
          path='02-styles.png')

    board([(label(p, '50x30', '', 'ean13'), 'EAN-13 — پیشوند ۶۲۶ ایران'),
           (label(p, '50x30', '', 'code128'), 'Code 128 — کد داخلی انبار')],
          'دو نوع بارکد', 'عدد بارکد زیر خطوط چاپ می‌شود',
          path='03-barcodes.png')

    board([(label(q, '50x30'), q['name']) for q in PRODUCTS], 'چند محصول از انبار',
          'همان قالب، چهار کالای واقعی از دادهٔ پروژه', cols=2, path='04-products.png')

    im = label(p, '60x40')
    im = im.resize((im.width * 3, im.height * 3), Image.LANCZOS)
    board([(im, 'بزرگ‌نمایی ۳× — جزئیات چاپ')], 'نمای نزدیک', '۶۰×۴۰ میلی‌متر · سربرگ، چیپ دسته، SKU، بارکد، پانویس',
          path='05-zoom.png')


if __name__ == '__main__':
    main()
