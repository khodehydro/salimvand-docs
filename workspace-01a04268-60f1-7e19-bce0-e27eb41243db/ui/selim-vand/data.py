# -*- coding: utf-8 -*-
"""Mock data + shared render helpers for the سليم‌وند UI concept."""

from icons import ico, part

# ---------------------------------------------------------------- products
# status: ok | low | out | soon | disc
PRODUCTS = [
    dict(code='BRK-00452', name='لنت ترمز جلو پژو ۲۰۶', part='9653514180', cat='ترمز', icon='brake-pad',
         cars='۲۰۶ تیپ ۲ و ۵ · ۲۰۷', status='ok',
         brands=[('ایساکو', 5), ('پارس لنت', 4), ('مهر', 0)]),
    dict(code='FLT-00118', name='فیلتر هوای پژو ۴۰۵ و پارس', part='1444R8', cat='فیلتراسیون', icon='air-filter',
         cars='۴۰۵ · پارس · سمند LX', status='low',
         brands=[('سرکان', 2), ('بوش', 7)]),
    dict(code='FLT-00203', name='فیلتر روغن پراید و تیبا', part='1R0709', cat='فیلتراسیون', icon='oil-filter',
         cars='پراید · تیبا · ساینا', status='ok',
         brands=[('بوش', 24), ('سرکان', 11), ('مان', 6)]),
    dict(code='ENG-00377', name='شمع موتور سمند EF7', part='ILZKAR7A11', cat='موتور', icon='spark-plug',
         cars='سمند EF7 · دنا', status='ok',
         brands=[('NGK', 18), ('بوش', 9)]),
    dict(code='SUS-00290', name='کمک فنر عقب پژو پارس', part='56210N7', cat='جلوبندی', icon='shock',
         cars='پارس · ۴۰۵', status='out',
         brands=[('کی‌بی‌ای', 0), ('مونرو', 0)]),
    dict(code='ELE-00512', name='چراغ جلو راست پژو ۲۰۶', part='6205E9', cat='برقی و روشنایی', icon='headlight',
         cars='۲۰۶ تیپ ۲', status='ok',
         brands=[('اصلی', 2), ('عقاب', 5)]),
    dict(code='ELE-00640', name='باتری ۶۰ آمپر اتمی', part='BAT-60Ah', cat='برقی و روشنایی', icon='battery',
         cars='عمومی — همه خودروها', status='low',
         brands=[('سپاهان', 3), ('صبا', 1)]),
    dict(code='ENG-00188', name='تسمه تایم پژو XU7', part='1249K7', cat='موتور', icon='belt',
         cars='۴۰۵ · پارس · سمند', status='soon',
         brands=[('گیتس', 0), ('دایکو', 0)]),
    dict(code='BRK-00311', name='دیسک و صفحه کلاچ پراید', part='KK15411', cat='انتقال قدرت', icon='clutch',
         cars='پراید ۱۳۱ · ۱۳۲', status='ok',
         brands=[('واله', 8), ('سایپا یدک', 3)]),
    dict(code='CLG-00072', name='رادیاتور آب پژو ۲۰۶ تیپ ۵', part='1330K4', cat='خنک‌کاری', icon='radiator',
         cars='۲۰۶ تیپ ۵', status='out',
         brands=[('کوشش', 0)]),
    dict(code='ELE-00905', name='سنسور اکسیژن دنا پلاس', part='0258010052', cat='برقی و روشنایی', icon='sensor',
         cars='دنا پلاس · دنا', status='ok',
         brands=[('بوش', 4)]),
    dict(code='ENG-00241', name='پمپ بنزین کامل تیبا', part='TBA-FL-22', cat='موتور', icon='fuel-pump',
         cars='تیبا · ساینا · کوییک', status='ok',
         brands=[('عقاب', 6), ('سایپا یدک', 2)]),
]

STATUS = {
    'ok':    dict(label='موجود', cls='b-ok', ic='check'),
    'low':   dict(label='موجود (کم)', cls='b-warn', ic='alert'),
    'out':   dict(label='ناموجود', cls='b-danger', ic='x'),
    'soon':  dict(label='به‌زودی', cls='b-warn', ic='clock'),
    'disc':  dict(label='توقف تولید', cls='b-line', ic='x'),
}

CATS = ['ترمز', 'فیلتراسیون', 'موتور', 'جلوبندی', 'برقی و روشنایی', 'انتقال قدرت', 'خنک‌کاری', 'بدنه']
MODELS = ['پژو ۲۰۶', 'پژو پارس', 'پراید', 'سمند', 'تیبا', 'دنا', 'کوییک']
BRANDS_ALL = ['ایساکو', 'بوش', 'سرکان', 'پارس لنت', 'واله', 'NGK', 'سپاهان', 'کوشش']


def brand_chips(brands):
    out = []
    for n, q in brands:
        if q > 0:
            out.append(f'<span class="brd in">{ico("check")}{n}</span>')
        else:
            out.append(f'<span class="brd out">{ico("x")}{n}</span>')
    return '<div class="brands">' + ''.join(out) + '</div>'


def status_badge(p):
    s = STATUS[p['status']]
    return f'<span class="badge {s["cls"]} st">{ico(s["ic"])}{s["label"]}</span>'


def product_card(p, compact=False):
    imgs = f'''<div class="imgs"><i>{ico('image')}</i><i>{ico('play')}</i></div>'''
    footer = f'''
      <div class="pcard-f">
        <button class="btn btn-sm btn-p">{ico('phone')}تماس</button>
        <button class="btn btn-sm btn-soft">{ico('telegram')}تلگرام</button>
      </div>''' if compact else f'''
      <div class="pcard-f">
        <button class="btn btn-sm btn-p">{ico('phone')}استعلام قیمت</button>
        <button class="btn btn-sm btn-o">{ico('bale')}بله</button>
      </div>
      <div class="icon-btns">
        <button title="گالری تصاویر">{ico('image')}</button>
        <button title="ویدئوی آپارات">{ico('play')}</button>
        <button class="tg" title="تلگرام">{ico('telegram')}</button>
        <button class="call" title="تماس تلفنی">{ico('phone')}</button>
        <button title="کپی کد قطعه">{ico('copy')}</button>
      </div>'''
    return f'''<article class="pcard">
      <div class="pcard-img">
        <span class="badge b-dark cat">{p['cat']}</span>
        {status_badge(p)}
        {part(p['icon'], 'part')}
        {imgs}
      </div>
      <div class="pcard-b">
        <h4 class="pcard-t">{p['name']}</h4>
        <div class="pcard-cars">{ico('car')}<span>مناسب: {p['cars']}</span></div>
        {brand_chips(p['brands'])}
        <span class="pcard-code">{p['code']} · {p['part']}</span>
      </div>
      {footer}
    </article>'''


# ---------------------------------------------------------------- helpers
def money(v):
    s = f'{v:,}'
    return s.translate(str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹'))


def bars(vals, labels, today_idx=None):
    mx = max(vals) or 1
    cols = []
    for i, v in enumerate(vals):
        h = max(4, round(v / mx * 100))
        t = ' today' if i == today_idx else ''
        cols.append(f'<div class="bcol{t}" title="{labels[i]}"><i style="height:{h}%" data-v="{money(v*1000)}"></i>'
                    f'<span>{labels[i]}</span></div>')
    return '<div class="bars">' + ''.join(cols) + '</div>'


def donut(parts):
    """parts: list of (label, value, color)"""
    total = sum(p[1] for p in parts) or 1
    import math
    r, cx, cy, sw = 42, 56, 56, 15
    circ = 2 * math.pi * r
    off = 0
    segs = []
    for lab, val, col in parts:
        frac = val / total
        segs.append(f'<circle r="{r}" cx="{cx}" cy="{cy}" fill="none" stroke="{col}" stroke-width="{sw}" '
                    f'stroke-dasharray="{frac*circ:.2f} {circ:.2f}" stroke-dashoffset="{-off:.2f}" '
                    f'transform="rotate(-90 {cx} {cy})" stroke-linecap="butt"/>')
        off += frac * circ
    leg = ''.join(f'<div class="r"><i style="background:{c}"></i>{l}'
                  f'<span class="v">{money(v)}</span></div>' for l, v, c in parts)
    return (f'<div class="donut"><svg viewBox="0 0 112 112">{"".join(segs)}'
            f'<text x="56" y="54" text-anchor="middle" font-size="15" font-weight="700" fill="currentColor">'
            f'{money(total)}<tspan font-size="8" fill="currentColor" opacity=".6"> قلم</tspan></text>'
            f'<text x="56" y="68" text-anchor="middle" font-size="8" fill="currentColor" opacity=".55">موجودی انبار</text>'
            f'</svg><div class="dlegend">{leg}</div></div>')
