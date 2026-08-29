# -*- coding: utf-8 -*-
"""Design-system reference view."""

from icons import ico

PALETTE = [
    ('--brand-950', 'سرمه‌ای ۹۵۰', '#04121f', 'فوتر / پس‌زمینهٔ عمیق'),
    ('--brand-900', 'سرمه‌ای ۹۰۰', '#071c30', 'هدر سایت / سایدبار پنل'),
    ('--brand-800', 'آبی تیره ۸۰۰', '#0d2b4b', 'رنگ اصلی برند / دکمهٔ اصلی'),
    ('--brand-700', 'آبی تیره ۷۰۰', '#124270', 'هاور دکمه / هدینگ روی رنگ'),
    ('--brand-600', 'آبی ۶۰۰', '#175894', 'لینک‌ها / آیکن فعال'),
    ('--brand-500', 'آبی ۵۰۰', '#1f6fbe', 'تأکید / نمودار'),
    ('--brand-300', 'آبی روشن ۳۰۰', '#7fb5ea', 'متن تأکیدی روی تیره'),
    ('--brand-100', 'آبی ۱۰۰', '#e0ecfa', 'پس‌زمینهٔ بج و تگ'),
    ('--brand-50', 'آبی ۵۰', '#f1f6fd', 'هاور / انتخاب‌شده'),
    ('--ok', 'سبز — موجود', '#0f8f52', 'وضعیت «موجود»، موفقیت'),
    ('--warn', 'کهربایی — به‌زودی', '#b9770b', 'هشدار کمبود، «به‌زودی»'),
    ('--danger', 'قرمز — ناموجود', '#c8383c', 'ناموجودی، خطا، بدهی'),
]

SEMANTIC_LIGHT = [
    ('--bg', 'پس‌زمینهٔ صفحه', '#f3f6fa'),
    ('--surface', 'کارت / سطح', '#ffffff'),
    ('--surface-2', 'سطح ثانویه', '#f7fafd'),
    ('--border', 'خط جداکننده', '#dce4ee'),
    ('--text', 'متن اصلی', '#0b1c2f'),
    ('--text-2', 'متن ثانویه', '#4a5f79'),
]
SEMANTIC_DARK = [
    ('--bg', 'پس‌زمینهٔ صفحه', '#050b14'),
    ('--surface', 'کارت / سطح', '#0d1826'),
    ('--surface-2', 'سطح ثانویه', '#111f31'),
    ('--border', 'خط جداکننده', '#1d3049'),
    ('--text', 'متن اصلی', '#eaf1f9'),
    ('--text-2', 'متن ثانویه', '#9db1c8'),
]


def _chips(rows):
    out = ''
    for row in rows:
        if len(row) == 4:
            tok, name, hexv, use = row
        else:
            tok, name, hexv = row
            use = tok
        out += f'''<div class="sw-chip" data-copy="{hexv}"><i style="background:{hexv}"></i>
          <div><b>{name}</b><span>{hexv}</span><span style="color:var(--text-2);font-family:inherit">{use}</span></div></div>'''
    return f'<div class="swatches">{out}</div>'


def design_system():
    types = [
        ('۳۴ / ۷۰۰', 'عنوان هیرو — H1', 'font-size:34px;font-weight:700;line-height:1.5'),
        ('۲۲ / ۷۰۰', 'عنوان بخش — H2', 'font-size:22px;font-weight:700'),
        ('۱۷ / ۷۰۰', 'عنوان کارت — H3', 'font-size:17px;font-weight:700'),
        ('۱۴ / ۴۰۰', 'متن بدنه', 'font-size:14px'),
        ('۱۲ / ۶۰۰', 'برچسب فیلد', 'font-size:12px;font-weight:600'),
        ('۱۱ / ۶۰۰', 'بج و متادیتا', 'font-size:11px;font-weight:600'),
    ]
    type_rows = ''.join(f'<div class="type-row"><span class="m">{m}</span><span style="{s}">{t}</span></div>'
                        for m, t, s in types)
    spaces = [4, 8, 12, 16, 24, 32, 48]
    sp_rows = ''.join(f'<div class="sp-row"><i style="width:{v*3}px"></i><span>{v}px</span></div>' for v in spaces)

    return f'''
<div class="ds">
  <div class="card"><div class="card-h">{ico('layers')}<h3>پالت برند — آبی تیره / سفید</h3>
      <span class="grow"></span><span class="fs11 mut3">کلیک = کپی هگز</span></div>
    <div class="card-b">{_chips(PALETTE)}</div></div>

  <div class="card"><div class="card-h">{ico('sun')}<h3>توکن‌های معنایی — لایت</h3></div>
    <div class="card-b">{_chips(SEMANTIC_LIGHT)}</div></div>

  <div class="card"><div class="card-h">{ico('moon')}<h3>توکن‌های معنایی — دارک</h3>
      <span class="grow"></span><span class="badge b-line">data-theme="dark"</span></div>
    <div class="card-b">{_chips(SEMANTIC_DARK)}</div></div>

  <div class="card"><div class="card-h">{ico('edit')}<h3>مقیاس تایپوگرافی</h3>
      <span class="grow"></span><span class="badge b-line">Vazirmatn UI FD</span></div>
    <div class="card-b">{type_rows}
      <div class="fs11 mut3" style="margin-top:10px;line-height:2">اعداد فارسی در همهٔ سطوح؛ اعداد لاتین
        (بارکد، کد محصول، شماره فنی) با فونت مونو و جهت LTR.</div></div></div>

  <div class="card"><div class="card-h">{ico('grid')}<h3>فضا و گرید</h3></div>
    <div class="card-b">
      <div class="col" style="gap:7px;margin-bottom:14px">{sp_rows}</div>
      <div class="grid-demo"><div>کارت</div><div>کارت</div><div>کارت</div><div>کارت</div></div>
      <div class="fs11 mut3" style="margin-top:10px;line-height:2">گرید کاتالوگ: ۴ ستون دسکتاپ · ۲ ستون تبلت ·
        ۱ ستون موبایل. گاتر ۱۴px، شعاع کارت ۱۴px.</div></div></div>

  <div class="card"><div class="card-h">{ico('check')}<h3>دکمه‌ها</h3></div>
    <div class="card-b comp-stack">
      <div class="comp-line"><button class="btn btn-p">{ico('check')}اصلی</button>
        <button class="btn btn-o">ثانویه</button><button class="btn btn-soft">ملایم</button>
        <button class="btn">پیش‌فرض</button><button class="btn btn-ghost">متنی</button></div>
      <div class="comp-line"><button class="btn btn-p btn-sm">کوچک</button>
        <button class="btn btn-lg">بزرگ</button>
        <button class="btn btn-danger btn-sm">{ico('trash')}حذف</button>
        <button class="btn btn-icon btn-sm">{ico('plus')}</button></div>
      <div class="comp-line"><button class="btn btn-p btn-block">{ico('phone')}تمام‌عرض — فراخوان اصلی</button></div>
    </div></div>

  <div class="card"><div class="card-h">{ico('tag')}<h3>بج‌ها و وضعیت موجودی</h3></div>
    <div class="card-b comp-stack">
      <div class="comp-line">
        <span class="badge b-ok">{ico('check')}موجود</span>
        <span class="badge b-warn">{ico('alert')}موجود (کم)</span>
        <span class="badge b-warn">{ico('clock')}به‌زودی</span>
        <span class="badge b-danger">{ico('x')}ناموجود</span>
        <span class="badge b-line">توقف تولید</span></div>
      <div class="comp-line">
        <span class="badge b-brand">ایساکو</span><span class="badge b-dark">دسته</span>
        <span class="badge b-line mono">BRK-00452</span></div>
      <div class="comp-line"><span class="brd in">{ico('check')}برند موجود</span>
        <span class="brd out">{ico('x')}برند ناموجود</span></div>
      <div class="fs11 mut3" style="line-height:2">قاعدهٔ سایت: موجودی کل &gt; ۰ → سبز؛ صفر → قرمز؛
        <span class="en">coming_soon</span> → کهربایی.</div>
    </div></div>

  <div class="card"><div class="card-h">{ico('edit')}<h3>فرم‌ها</h3></div>
    <div class="card-b col">
      <div class="field"><span class="lab">ورودی متنی</span>
        <input class="inp" placeholder="نام قطعه…"></div>
      <div class="field"><span class="lab">انتخابگر</span>
        <div class="selwrap">{ico('chevron')}<select class="inp sel"><option>پژو ۲۰۶ · تیپ ۵</option></select></div></div>
      <div class="field"><span class="lab">جست‌وجو</span>
        <div class="search">{ico('search')}<input class="inp" placeholder="جست‌وجو…"></div></div>
      <div class="row" style="gap:16px;flex-wrap:wrap">
        <span class="row" style="gap:8px;font-size:12.5px"><span class="chk on">{ico('check')}</span>کلید فعال</span>
        <span class="row" style="gap:8px;font-size:12.5px"><span class="chk">{ico('check')}</span>کلید غیرفعال</span>
        <span class="row" style="gap:8px;font-size:12.5px">سوییچ <span class="sw on"></span></span>
        <span class="row" style="gap:8px;font-size:12.5px">سوییچ <span class="sw"></span></span>
      </div>
      <div class="seg"><button class="on">امروز</button><button>۷ روز</button><button>۳۰ روز</button></div>
    </div></div>

  <div class="card"><div class="card-h">{ico('file')}<h3>جدول و داده</h3></div>
    <div style="overflow:hidden">
      <table class="tbl"><thead><tr><th>محصول</th><th>برند</th><th class="num">موجودی</th><th>وضعیت</th></tr></thead>
        <tbody><tr><td>لنت ترمز ۲۰۶</td><td><span class="badge b-brand">ایساکو</span></td>
            <td class="num b">۵</td><td><span class="badge b-ok">سالم</span></td></tr>
          <tr><td>کمک فنر پارس</td><td><span class="badge b-brand">کی‌بی‌ای</span></td>
            <td class="num b">۰</td><td><span class="badge b-danger">صفر</span></td></tr>
        </tbody></table>
      <div class="card-b col">
        <div class="field"><span class="lab">نوار پیشرفت / موجودی</span>
          <div class="prog"><i style="width:62%"></i></div></div>
        <div class="kv"><span class="k">ردیف کلید/مقدار</span><span class="v mono">۲۲۸,۷۰۰,۰۰۰</span></div>
      </div>
    </div></div>

  <div class="card"><div class="card-h">{ico('clock')}<h3>حالت‌ها: بارگذاری، خالی، اعلان</h3></div>
    <div class="card-b comp-stack">
      <div class="row" style="gap:9px">
        <div class="sk" style="width:56px;height:56px;border-radius:11px"></div>
        <div class="col grow" style="gap:6px"><div class="sk" style="height:12px;width:70%"></div>
          <div class="sk" style="height:10px;width:45%"></div>
          <div class="sk" style="height:22px;width:90px;border-radius:99px"></div></div>
      </div>
      <div class="empty">{ico('box')}<div>قطعه‌ای با این فیلترها پیدا نشد.</div>
        <button class="btn btn-sm btn-ghost">{ico('refresh')}پاک کردن فیلترها</button></div>
      <div class="toast-demo">{ico('check')}<span>فاکتور ۱۴۰۵/۰۰۳۴۸ صادر و پیامک ارسال شد.</span>
        <button class="btn btn-sm btn-ghost" style="color:inherit">{ico('x')}</button></div>
    </div></div>

  <div class="card"><div class="card-h">{ico('car')}<h3>آیکون‌گرافی قطعات</h3>
      <span class="grow"></span><span class="fs11 mut3">خطی، تک‌رنگ، بدون تصویر خارجی</span></div>
    <div class="card-b">
      <div class="comp-line" style="gap:14px;color:var(--brand-500)">
        {''.join(f'<span style="display:inline-block;width:38px;height:38px">{ico_svg}</span>' for ico_svg in _part_grid())}
      </div>
      <div class="fs11 mut3" style="margin-top:10px;line-height:2">در پیاده‌سازی واقعی، تصویر محصول
        (WebP) جای این آیکون‌ها را می‌گیرد؛ آیکون به‌عنوان جای‌نما و fallback استفاده می‌شود.</div>
    </div></div>
</div>'''


def _part_grid():
    from icons import part
    names = ['brake-pad', 'air-filter', 'oil-filter', 'spark-plug', 'shock', 'headlight',
             'battery', 'belt', 'radiator', 'clutch', 'fuel-pump', 'sensor']
    return [part(n, 'part') for n in names]
