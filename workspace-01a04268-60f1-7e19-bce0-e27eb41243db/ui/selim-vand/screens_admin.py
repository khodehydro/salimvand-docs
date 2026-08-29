# -*- coding: utf-8 -*-
"""Admin panel screens — shell, sidebar, dashboard."""

from icons import ico, part
from data import PRODUCTS, money, bars, donut

MENU = [
    ('grp', 'اصلی'),
    ('it', 'home', 'داشبورد', 'on', None, None),
    ('grp', 'فروشگاه'),
    ('it', 'box', 'محصولات', '', '۱۲۴', None),
    ('it', 'layers', 'انبار', '', None, ['اقلام موجودی', 'ورود کالا', 'اصلاح موجودی', 'جابه‌جایی قفسه', 'تاریخچهٔ تراکنش‌ها']),
    ('it', 'money', 'فروش', '', None, ['صدور فاکتور', 'لیست فاکتورها', 'مرجوعی‌ها']),
    ('it', 'users', 'مشتریان', '', '۴', None),
    ('it', 'truck', 'تأمین‌کنندگان', '', None, None),
    ('grp', 'مدیریت'),
    ('it', 'chart', 'گزارش‌ها', '', None, None),
    ('it', 'gear', 'تنظیمات', '', None, None),
    ('it', 'shield', 'سیستم', '', None, None),
]


def sidebar(active='داشبورد'):
    out = ['<aside class="adm-side">',
           '<div class="s-logo"><div class="logo" style="width:34px;height:34px"><span>س</span></div>'
           '<div><div class="n1">سلیم‌وند</div><div class="n2">پنل مدیریت</div></div></div>']
    for m in MENU:
        if m[0] == 'grp':
            out.append(f'<div class="grp">{m[1]}</div>')
            continue
        _, icon, name, on, cnt, subs = m
        cls = 'on' if name == active else ''
        badge = f'<span class="cnt">{cnt}</span>' if cnt else ''
        ar = f'<span class="ar">{ico("chevron")}</span>' if subs else ''
        out.append(f'<a class="ni {cls}">{ico(icon)}<span class="wrap">{name}</span>{badge}{ar}</a>')
        if subs and name == active:
            out.append('<div style="padding-inline-start:14px;margin:2px 0 6px">')
            for i, s in enumerate(subs):
                c = 'on' if i == 0 else ''
                out.append(f'<a class="ni {c}" style="font-size:12px;padding:6px 10px">{s}</a>')
            out.append('</div>')
    out.append(f'<div class="foot">{ico("db")}<span>بکاپ امروز ۰۳:۰۰ ✓ · درایو</span></div></aside>')
    return ''.join(out)


def topbar():
    return f'''<header class="adm-top">
      <button class="btn btn-sm btn-ghost btn-icon">{ico('menu')}</button>
      <div class="gsearch">{ico('search')}<input class="inp" placeholder="جست‌وجوی سراسری: قطعه، مشتری، فاکتور، قفسه…"><kbd>Ctrl K</kbd></div>
      <span class="grow"></span>
      <button class="btn btn-sm btn-p">{ico('plus')}فاکتور جدید</button>
      <button class="icb" title="اعلان‌ها">{ico('bell')}<i class="bdg"></i></button>
      <button class="icb" data-theme-btn title="پوسته">{ico('moon')}</button>
      <div class="uchip"><div class="av">مس</div>
        <div><div class="nm">مهدی سلیمانی</div><div class="rl">مدیر کل</div></div>{ico('chevron')}</div>
    </header>'''


def shell(body, active='داشبورد', overlay=''):
    return (f'<div class="adm">{sidebar(active)}'
            f'<div class="adm-main">{topbar()}<div class="adm-body">{body}</div></div>{overlay}</div>')


# ============================================================ DASHBOARD
def dashboard():
    days = ['۱', '۴', '۷', '۱۰', '۱۳', '۱۶', '۱۹', '۲۲', '۲۵', '۲۸', '۳۱', '۳', '۶', '۹', '۱۲']
    vals = [42, 61, 38, 77, 95, 54, 68, 88, 120, 71, 63, 102, 138, 91, 116]
    low = [
        ('لنت ترمز جلو پژو ۲۰۶', 'ایساکو · قفسهٔ A-03-2', 2, 10, 'brake-pad'),
        ('فیلتر هوای پژو ۴۰۵', 'سرکان · قفسهٔ B-11-1', 2, 15, 'air-filter'),
        ('باتری ۶۰ آمپر اتمی', 'صبا · قفسهٔ C-02-4', 1, 6, 'battery'),
        ('کمک فنر عقب پارس', 'کی‌بی‌ای · قفسهٔ D-07-3', 0, 4, 'shock'),
    ]
    lowrows = ''.join(f'''<div class="list-row">
        <span class="thumb">{part(ic)}</span>
        <div class="wrap"><div class="nm">{n}</div><div class="sub">{b}</div>
          <div class="stockbar {'mid' if q else ''}"><i style="width:{max(6, q/m*100):.0f}%"></i></div></div>
        <div class="val"><span class="badge {'b-danger' if q == 0 else 'b-warn'}">{money(q)} از {money(m)}</span></div>
      </div>''' for n, b, q, m, ic in low)

    unpaid = [
        ('۱۴۰۵/۰۰۳۴۷', 'علی محمدی', 78700000, '۲ روز'),
        ('۱۴۰۵/۰۰۳۴۴', 'تعمیرگاه برادران نوری', 215000000, '۵ روز'),
        ('۱۴۰۵/۰۰۳۳۹', 'رضا کریمی', 12400000, '۹ روز'),
        ('۱۴۰۵/۰۰۳۳۱', 'مکانیکی صدف', 96500000, '۱۴ روز'),
    ]
    urows = ''.join(f'''<tr><td class="mono b">{n}</td><td>{c}</td>
      <td class="num b" style="color:var(--danger)">{money(v)}</td>
      <td><span class="badge {'b-danger' if d in ('۹ روز','۱۴ روز') else 'b-warn'}">{d}</span></td>
      <td><button class="btn btn-sm btn-ghost btn-icon">{ico('sms')}</button></td></tr>'''
                    for n, c, v, d in unpaid)

    body = f'''
    <div class="page-h">
      <div><h2>داشبورد</h2>
        <div class="crumb">{ico('home')} خانه {ico('chevronL')} امروز، سه‌شنبه ۳ شهریور ۱۴۰۵</div></div>
      <span class="grow"></span>
      <div class="seg"><button>امروز</button><button class="on">۷ روز</button><button>۳۰ روز</button><button>ماهانه</button></div>
      <button class="btn btn-sm btn-o">{ico('download')}خروجی</button>
      <button class="btn btn-sm btn-ghost btn-icon">{ico('refresh')}</button>
    </div>

    <div class="kpis">
      <div class="kpi"><div class="hd"><span class="ic">{ico('money')}</span>فروش امروز</div>
        <div class="v">{money(48620)}<small>هزار ریال</small></div>
        <div class="f up">{ico('trend')}۱۸٪ نسبت به دیروز</div></div>
      <div class="kpi"><div class="hd"><span class="ic">{ico('file')}</span>فاکتورهای امروز</div>
        <div class="v">{money(23)}<small>فاکتور</small></div>
        <div class="f up">{ico('trend')}۴ فاکتور بیشتر</div></div>
      <div class="kpi"><div class="hd"><span class="ic">{ico('users')}</span>مشتری جدید (۷ روز)</div>
        <div class="v">{money(11)}<small>نفر</small></div>
        <div class="f fl">{ico('user')}میانگین خرید ۳.۲ قلم</div></div>
      <div class="kpi alert"><div class="hd"><span class="ic">{ico('alert')}</span>هشدار کمبود موجودی</div>
        <div class="v" style="color:var(--danger)">{money(7)}<small>قلم</small></div>
        <div class="f dn">{ico('down')}۲ قلم از دیروز بیشتر</div></div>
    </div>

    <div class="cols-2">
      <div class="card">
        <div class="card-h"><h3>روند فروش — ۳۰ روز گذشته</h3><span class="grow"></span>
          <div class="legend"><span><i style="background:var(--brand-500)"></i>فروش (میلیون ریال)</span>
            <span><i style="background:var(--brand-200)"></i>میانگین</span></div></div>
        <div class="chart-wrap">{bars(vals, days, today_idx=14)}
          <div class="axis"><span>۴ مرداد</span><span>۱۹ مرداد</span><span>۳ شهریور (امروز)</span></div></div>
      </div>
      <div class="card">
        <div class="card-h"><h3>ترکیب موجودی بر اساس دسته</h3><span class="grow"></span>
          <button class="btn btn-sm btn-ghost btn-icon">{ico('chevron')}</button></div>
        <div class="card-b">{donut([
            ('ترمز و جلوبندی', 3120, 'var(--brand-600)'),
            ('فیلتراسیون', 2480, 'var(--brand-400)'),
            ('موتور و انتقال', 2260, 'var(--brand-300)'),
            ('برقی و روشنایی', 1840, 'var(--ok)'),
            ('بدنه و سایر', 2780, 'var(--border-2)'),
        ])}</div>
      </div>
    </div>

    <div class="cols-2" style="margin-top:14px">
      <div class="card">
        <div class="card-h"><h3>فاکتورهای پرداخت‌نشده</h3><span class="grow"></span>
          <span class="badge b-danger">{money(4)} مورد</span>
          <button class="btn btn-sm btn-ghost">همه {ico('chevronL')}</button></div>
        <table class="tbl"><thead><tr><th>شماره</th><th>مشتری</th><th class="num">بدهی (ریال)</th>
          <th>گذشته</th><th></th></tr></thead><tbody>{urows}</tbody></table>
      </div>
      <div class="card">
        <div class="card-h"><h3>کمبود موجودی</h3><span class="grow"></span>
          <button class="btn btn-sm btn-soft">{ico('truck')}ثبت خرید</button></div>
        <div class="card-b" style="padding-top:6px;padding-bottom:6px">{lowrows}</div>
      </div>
    </div>

    <div class="cols-2b" style="margin-top:14px">
      <div class="card">
        <div class="card-h"><h3>آخرین تراکنش‌های انبار</h3><span class="grow"></span>
          <span class="fs11 mut3">دفتر کل — غیرقابل تغییر</span></div>
        <div class="card-b"><div class="tl">
          <div class="it neg"><b>فروش ۲ عدد — لنت ترمز ۲۰۶ (ایساکو)</b>
            <span>۱۴:۲۲ · فاکتور ۱۴۰۵/۰۰۳۴۷ · موجودی بعد: ۳</span></div>
          <div class="it pos"><b>ورود کالا ۲۰ عدد — فیلتر روغن پراید (بوش)</b>
            <span>۱۱:۰۵ · فاکتور خرید از «یدک گستر» · موجودی بعد: ۲۴</span></div>
          <div class="it"><b>جابه‌جایی قفسه — شمع EF7 (NGK)</b>
            <span>۱۰:۴۱ · از B-04-2 به B-04-5 · انباردار: ح. رحیمی</span></div>
          <div class="it pos"><b>مرجوعی ۱ عدد — فیلتر هوای ۴۰۵ (سرکان)</b>
            <span>دیروز ۱۸:۳۰ · مرجوعی از فاکتور ۱۴۰۵/۰۰۳۴۱ · موجودی بعد: ۲</span></div>
        </div></div>
      </div>
      <div class="card">
        <div class="card-h"><h3>یکپارچه‌سازی‌ها و سلامت سیستم</h3><span class="grow"></span>
          <span class="badge b-line">audit / logs</span></div>
        <div class="card-b" style="padding-top:8px">
          <div class="list-row"><span class="thumb">{ico('sms')}</span>
            <div class="wrap"><div class="nm">پیامک فاکتور</div><div class="sub">آخرین ارسال ۱۴:۲۲ — موفق</div></div>
            <span class="badge b-ok">{ico('check')}فعال</span></div>
          <div class="list-row"><span class="thumb">{ico('telegram')}</span>
            <div class="wrap"><div class="nm">ربات و کانال تلگرام</div><div class="sub">۳۸۴ عضو · آخرین پست دیروز</div></div>
            <span class="badge b-ok">{ico('check')}فعال</span></div>
          <div class="list-row"><span class="thumb">{ico('db')}</span>
            <div class="wrap"><div class="nm">بکاپ گوگل‌درایو</div><div class="sub">امروز ۰۳:۰۰ — ۱۲.۴ مگابایت</div></div>
            <span class="badge b-ok">{ico('check')}موفق</span></div>
          <div class="list-row"><span class="thumb">{ico('alert')}</span>
            <div class="wrap"><div class="nm">فضای دیسک VPS</div>
              <div class="sub">۸.۲ گیگ از ۳۰ گیگ مصرف‌شده</div>
              <div class="stockbar ok" style="width:100%"><i style="width:27%"></i></div></div>
            <span class="badge b-ok">۲۷٪</span></div>
        </div>
      </div>
    </div>'''
    return shell(body, 'داشبورد')


# ============================================================ INVOICE CREATE
def invoice_create():
    rows = [
        ('لنت ترمز جلو پژو ۲۰۶', 'BRK-00452', 'ایساکو', 'A-03-2', 2, 18500000, 0, 'brake-pad'),
        ('فیلتر روغن پراید و تیبا', 'FLT-00203', 'بوش', 'B-11-1', 1, 4200000, 0, 'oil-filter'),
        ('کمک فنر عقب پژو پارس', 'SUS-00290', 'مونرو', 'D-07-3', 2, 96000000, 3000000, 'shock'),
    ]
    body_rows = ''
    sub = 0
    for n, code, br, sh, q, p, d, ic in rows:
        tot = q * p - d
        sub += tot
        body_rows += f'''<div class="irow">
          <div><div class="pn">{n}</div><div class="ps">{code} · {sh}</div></div>
          <div><span class="badge b-brand">{br}</span></div>
          <div class="qty"><button>{ico('minus')}</button><span>{money(q)}</span><button>{ico('plus')}</button></div>
          <input class="money-in hd-hide" value="{money(p)}">
          <input class="money-in hd-hide" value="{money(d) if d else '۰'}">
          <div class="num b mono">{money(tot)}</div>
          <button class="btn btn-sm btn-ghost btn-icon">{ico('trash')}</button>
        </div>'''
    hd = ('<div class="irow hd"><div>محصول / قفسه</div><div>برند</div><div>تعداد</div>'
          '<div class="hd-hide num">فی (ریال)</div><div class="hd-hide num">تخفیف</div>'
          '<div class="num">جمع</div><div></div></div>')
    disc_total = 1500000
    total = sub - disc_total
    paid = 150000000
    debt = total - paid

    body = f'''
    <div class="page-h">
      <div><h2>صدور فاکتور</h2>
        <div class="crumb">{ico('money')} فروش {ico('chevronL')} فاکتور جدید · پیش‌نویس ۱۴۰۵/۰۰۳۴۸</div></div>
      <span class="grow"></span>
      <button class="btn btn-sm btn-ghost">{ico('refresh')}پاک کردن</button>
      <button class="btn btn-sm btn-o">{ico('file')}بازیابی پیش‌نویس</button>
    </div>

    <div class="cust-bar">
      <span class="lab">مشتری</span>
      <div class="cust">
        <div class="av">عم</div>
        <div class="wrap"><div class="nm">علی محمدی</div>
          <div class="sub"><span class="mono" style="direction:ltr">09123456789</span>
            <span>پژو ۲۰۶ تیپ ۵ — ۱۳۹۴</span>
            <span style="color:var(--danger)">بدهی: {money(78700000)} ریال</span>
            <span>۱۲ فاکتور قبلی</span></div></div>
      </div>
      <div class="search search-sm" style="width:250px">{ico('search')}
        <input class="inp" placeholder="نام یا موبایل مشتری…"></div>
      <button class="btn btn-sm btn-soft">{ico('plus')}مشتری جدید</button>
      <button class="btn btn-sm btn-ghost btn-icon">{ico('user')}</button>
    </div>

    <div class="inv-grid">
      <div>
        <div class="scan-box">
          <div class="scan-in">
            <div class="search grow">{ico('barcode')}
              <input class="inp" value="لنت" placeholder="جست‌وجوی قطعه یا اسکن بارکد (Enter = اسکن)…"></div>
            <button class="btn btn-o" style="width:44px;padding:0" title="اسکن دوربین">{ico('camera')}</button>
            <span class="badge b-line">{ico('qr')}بارکدخوان آماده</span>
          </div>
          <div class="scan-res">
            <div class="sr"><span class="thumb">{part('brake-pad')}</span>
              <div class="wrap"><div class="nm">لنت ترمز جلو پژو ۲۰۶ <span class="badge b-brand">BRK-00452</span></div>
                <div class="brs">
                  <button class="br sel">{ico('check')}ایساکو <b>{money(5)}</b> <span class="mut3">A-03-2</span></button>
                  <button class="br">پارس لنت <b>{money(4)}</b> <span class="mut3">A-03-4</span></button>
                  <button class="br" style="opacity:.5">{ico('x')}مهر <b>۰</b></button>
                </div></div>
              <div class="val"><span class="badge b-ok">موجود</span></div></div>
            <div class="sr"><span class="thumb">{part('brake-pad')}</span>
              <div class="wrap"><div class="nm">لنت ترمز عقب پژو پارس <span class="badge b-brand">BRK-00318</span></div>
                <div class="brs"><button class="br">{ico('check')}ایساکو <b>{money(9)}</b> <span class="mut3">A-04-1</span></button>
                  <button class="br">واله <b>{money(3)}</b> <span class="mut3">A-04-2</span></button></div></div>
              <div class="val"><span class="badge b-ok">موجود</span></div></div>
            <div class="sr"><span class="thumb">{part('clutch')}</span>
              <div class="wrap"><div class="nm">لنت ترمز ۴۰۵ GLX <span class="badge b-brand">BRK-00102</span></div>
                <div class="brs"><button class="br" style="opacity:.5">{ico('x')}پارس لنت <b>۰</b></button></div></div>
              <div class="val"><span class="badge b-danger">ناموجود</span></div></div>
          </div>
        </div>

        <div class="rows" style="margin-top:14px">
          {hd}{body_rows}
        </div>

        <div class="row" style="margin-top:12px;gap:9px;flex-wrap:wrap">
          <button class="btn btn-sm btn-ghost">{ico('plus')}افزودن ردیف دستی</button>
          <button class="btn btn-sm btn-ghost">{ico('scan')}اسکن پیوسته</button>
          <span class="grow"></span>
          <span class="fs11 mut3">{ico('alert')} پس از صدور، موجودی به‌صورت خودکار و با ثبت در دفتر تراکنش‌ها کسر می‌شود.</span>
        </div>
      </div>

      <div class="tot-panel">
        <div class="sec-h2">{ico('money')}مبالغ فاکتور</div>
        <div class="tot-b">
          <div class="ln"><span>جمع اقلام ({money(3)} قلم)</span><b>{money(sub)}</b></div>
          <div class="ln"><span>تخفیف ردیف‌ها</span><b>{money(3000000)}</b></div>
          <div class="field" style="margin:9px 0"><span class="lab">تخفیف کل فاکتور</span>
            <div class="row" style="gap:7px"><input class="money-in" style="height:34px" value="{money(disc_total)}">
              <button class="btn btn-sm btn-ghost btn-icon">{ico('edit')}</button></div></div>
          <div class="ln grand"><span>مبلغ نهایی</span><b>{money(total)}</b></div>

          <div class="paybox">
            <div class="pr"><span class="chk on">{ico('check')}</span>نقدی
              <input class="money-in" style="margin-inline-start:auto" value="{money(60000000)}"></div>
            <div class="pr"><span class="chk on">{ico('check')}</span>کارت‌خوان
              <input class="money-in" style="margin-inline-start:auto" value="{money(90000000)}"></div>
            <div class="pr"><span class="chk">{ico('check')}</span>نسیه / چک
              <input class="money-in" style="margin-inline-start:auto" value="۰"></div>
            <div class="hr" style="margin:9px 0"></div>
            <div class="pr"><span class="mut">پرداخت‌شده</span>
              <b style="margin-inline-start:auto" class="mono">{money(paid)}</b></div>
          </div>

          <div class="debt-note">{ico('alert')}<span>باقی‌مانده <b class="mono">{money(debt)}</b> ریال به‌صورت
            خودکار به بدهی مشتری منتقل می‌شود.</span></div>

          <div class="col" style="margin-top:12px;gap:8px">
            <button class="btn btn-p btn-block btn-lg">{ico('check')}صدور فاکتور + پیامک مشتری</button>
            <div class="row" style="gap:8px">
              <button class="btn btn-o btn-sm grow">{ico('save')}پیش‌نویس</button>
              <button class="btn btn-ghost btn-sm grow">{ico('print')}چاپ</button>
            </div>
            <label class="pr fs11 mut3" style="display:flex;gap:7px;align-items:center;justify-content:center">
              <span class="chk on" style="width:15px;height:15px">{ico('check')}</span>ارسال لینک فاکتور با پیامک</label>
          </div>
        </div>
      </div>
    </div>'''

    overlay = f'''<div class="modal-mask">
      <div class="palette" style="width:min(420px,92%)">
        <div class="tot-b" style="padding:22px">
          <div class="success-box">
            <div class="ok">{ico('check')}</div>
            <h3 style="font-size:17px">فاکتور صادر شد</h3>
            <p class="mut fs12" style="margin-top:6px">شمارهٔ فاکتور <b class="mono" style="color:var(--text)">۱۴۰۵/۰۰۳۴۸</b></p>
            <div class="kv" style="margin-top:14px"><span class="k">مبلغ</span><span class="v mono">{money(total)} ریال</span></div>
            <div class="kv"><span class="k">کسر از انبار</span><span class="v">۳ ردیف · ثبت در دفتر تراکنش‌ها ✓</span></div>
            <div class="kv"><span class="k">پیامک مشتری</span>
              <span class="v" style="color:var(--ok)">{ico('check')} ارسال شد — ۱۴:۳۱</span></div>
            <div class="kv"><span class="k">لینک فاکتور</span>
              <span class="v en" style="font-size:11px">selimvand.ir/invoice/9f2c…b71e</span></div>
          </div>
          <div class="row" style="gap:8px;margin-top:16px">
            <button class="btn btn-p grow">{ico('plus')}فاکتور بعدی</button>
            <button class="btn btn-o grow">{ico('download')}PDF</button>
            <button class="btn btn-ghost btn-icon">{ico('print')}</button>
          </div>
        </div>
      </div>
    </div>'''
    return shell(body, 'فروش', overlay)


# ============================================================ PRODUCTS
def product_edit():
    tabs = [('اطلاعات پایه', 'on', '۱'), ('تصاویر', '', '۲'), ('ویدئوی آپارات', '', ''),
            ('خودروهای سازگار', '', '۳'), ('اقلام موجودی (برندها)', '', '۵')]
    tabbar = ''
    for n, c, k in tabs:
        tag = f'<span class="n">{k}</span>' if k else ''
        tabbar += f'<button class="{c}">{n}{tag}</button>'
    inv_rows = [
        ('ایساکو', 5, 12800000, 18500000, 'A-03-2', '2000000452013', 4),
        ('پارس لنت', 4, 11900000, 17200000, 'A-03-4', '2000000452020', 4),
        ('مهر', 0, 10400000, 15800000, '—', '2000000452037', 3),
    ]
    irows = ''.join(f'''<tr>
        <td><div class="row" style="gap:8px"><span class="badge b-brand">{b}</span></div></td>
        <td class="num b">{money(q)}</td>
        <td class="num hd-hide">{money(pu)}</td>
        <td class="num">{money(ps)}</td>
        <td class="hd-hide"><span class="badge b-line">{ico('archive')}{lo}</span></td>
        <td class="hd-hide"><span class="en fs11">{bc}</span></td>
        <td class="num hd-hide">{money(ms)}</td>
        <td><div class="row" style="gap:5px">
          <button class="btn btn-sm btn-ghost btn-icon">{ico('edit')}</button>
          <button class="btn btn-sm btn-ghost btn-icon">{ico('barcode')}</button>
          <button class="btn btn-sm btn-ghost btn-icon">{ico('trash')}</button></div></td>
      </tr>''' for b, q, pu, ps, lo, bc, ms in inv_rows)

    body = f'''
    <div class="page-h">
      <div><h2>ویرایش محصول</h2>
        <div class="crumb">{ico('box')} محصولات {ico('chevronL')} لنت ترمز جلو پژو ۲۰۶</div></div>
      <span class="grow"></span>
      <span class="badge b-brand mono">BRK-00452</span>
      <span class="badge b-ok">{ico('check')}نمایش در سایت</span>
      <button class="btn btn-sm btn-ghost">{ico('eye')}نمایش عمومی</button>
      <button class="btn btn-sm btn-o">{ico('trash')}حذف نرم</button>
      <button class="btn btn-sm btn-p">{ico('save')}ذخیرهٔ تغییرات</button>
    </div>

    <div class="card" style="overflow:hidden">
      <div class="tabs" style="padding:0 14px">{tabbar}</div>

      <div style="display:grid;grid-template-columns:1fr 320px;gap:0">
        <div class="card-b" style="border-inline-end:1px solid var(--border)">
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:13px">
            <div class="field" style="grid-column:span 2"><span class="lab">نام محصول</span>
              <input class="inp" value="لنت ترمز جلو پژو ۲۰۶"></div>
            <div class="field"><span class="lab">دسته‌بندی</span>
              <div class="selwrap">{ico('chevron')}<select class="inp sel"><option>ترمز › لنت (BRK)</option></select></div></div>
            <div class="field"><span class="lab">کد محصول (خودکار)</span>
              <input class="inp mono" value="BRK-00452" style="direction:ltr"></div>
            <div class="field"><span class="lab">شماره فنی (Part Number)</span>
              <input class="inp mono" value="9653514180" style="direction:ltr"></div>
            <div class="field"><span class="lab">وضعیت</span>
              <div class="selwrap">{ico('chevron')}<select class="inp sel"><option>active — نمایش در سایت</option><option>hidden</option></select></div></div>
            <div class="field"><span class="lab">جایگزینی وضعیت موجودی (اختیاری)</span>
              <div class="selwrap">{ico('chevron')}<select class="inp sel"><option>محاسبهٔ خودکار از موجودی</option>
                <option>به‌زودی (coming_soon)</option><option>توقف تولید</option></select></div></div>
            <div class="field"><span class="lab">شناسهٔ ویدئوی آپارات</span>
              <input class="inp mono" value="a1b2c3d4" style="direction:ltr" placeholder="بدون فایل روی سرور"></div>
            <div class="field" style="grid-column:span 2"><span class="lab">توضیحات</span>
              <textarea class="inp" rows="3">لنت ترمز جلو مناسب پژو ۲۰۶ تیپ ۲ و ۵ و پژو ۲۰۷ — دارای نشان استاندارد.</textarea></div>
          </div>

          <div class="hr"></div>
          <div class="row" style="margin-bottom:9px"><h3 class="fs13">مشخصات فنی (specs)</h3>
            <span class="grow"></span><button class="btn btn-sm btn-ghost">{ico('plus')}ردیف جدید</button></div>
          <div class="row" style="gap:8px;flex-wrap:wrap">
            <span class="badge b-line">محل نصب: جلو</span>
            <span class="badge b-line">ضخامت: ۱۷.۵ میلی‌متر</span>
            <span class="badge b-line">سنسور سایش: دارد</span>
            <span class="badge b-line">کیت نصب: دارد</span>
            <button class="btn btn-sm btn-ghost">{ico('plus')}</button>
          </div>
        </div>

        <div class="card-b" style="background:var(--surface-2)">
          <div class="row" style="margin-bottom:10px"><h3 class="fs13">تصاویر (حداکثر ۲)</h3>
            <span class="grow"></span><span class="fs11 mut3">WebP · ۴۰۰px و ۹۰۰px</span></div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:9px">
            <div style="aspect-ratio:1;border-radius:11px;border:1px solid var(--border);background:var(--surface);
              display:grid;place-items:center;color:var(--brand-500);position:relative">
              {part('brake-pad', 'part')}
              <span class="badge b-dark" style="position:absolute;top:7px;inset-inline-start:7px">اصلی</span></div>
            <div style="aspect-ratio:1;border-radius:11px;border:1px dashed var(--border-2);display:grid;
              place-items:center;color:var(--text-3);flex-direction:column;gap:4px">
              <div style="text-align:center">{ico('plus')}<div class="fs11">افزودن تصویر</div></div></div>
          </div>
          <div class="hr"></div>
          <h3 class="fs13" style="margin-bottom:8px">خودروهای سازگار</h3>
          <div class="treebox">
            <div class="tnode on"><span class="c">{ico('check')}</span>{ico('car')} پژو</div>
            <div class="tlvl2 tnode on"><span class="c">{ico('check')}</span>۲۰۶</div>
            <div class="tlvl3 tnode on"><span class="c">{ico('check')}</span>تیپ ۲</div>
            <div class="tlvl3 tnode on"><span class="c">{ico('check')}</span>تیپ ۵</div>
            <div class="tlvl2 tnode half"><span class="c"></span>۲۰۷</div>
            <div class="tlvl3 tnode"><span class="c"></span>SD</div>
            <div class="tnode"><span class="c"></span>{ico('car')} سایپا</div>
          </div>
          <p class="fs11 mut3" style="margin-top:8px;line-height:1.9">خالی بودن تیپ = سازگاری با همهٔ تیپ‌های آن مدل.</p>
        </div>
      </div>
    </div>

    <div class="card" style="margin-top:14px;overflow:hidden">
      <div class="card-h"><h3>اقلام موجودی — هر برند یک قلم مستقل</h3><span class="grow"></span>
        <span class="badge b-line">{ico('box')}۳ برند</span>
        <span class="badge b-ok">موجودی کل: {money(9)}</span>
        <button class="btn btn-sm btn-p">{ico('plus')}افزودن برند</button></div>
      <table class="tbl">
        <thead><tr><th>برند</th><th class="num">موجودی</th><th class="num hd-hide">قیمت خرید</th>
          <th class="num">قیمت فروش</th><th class="hd-hide">قفسه</th><th class="hd-hide">بارکد EAN-13</th>
          <th class="num hd-hide">آستانهٔ هشدار</th><th></th></tr></thead>
        <tbody>{irows}
          <tr><td colspan="8">
            <div class="row" style="gap:8px;padding:4px 0">
              <button class="btn btn-sm btn-soft">{ico('plus')}افزودن برند جدید</button>
              <button class="btn btn-sm btn-ghost">{ico('archive')}ورود کالا (فاکتور خرید)</button>
              <span class="grow"></span>
              <span class="fs11 mut3">{ico('alert')} قیمت‌ها فقط در پنل دیده می‌شوند — هیچ‌گاه در API عمومی.</span>
            </div></td></tr>
        </tbody>
      </table>
    </div>'''
    return shell(body, 'محصولات')


# ============================================================ INVENTORY
def inventory():
    items = [
        ('لنت ترمز جلو پژو ۲۰۶', 'BRK-00452', 'ایساکو', 5, 10, 'A-03-2', '18,500,000', 'brake-pad', 'ok'),
        ('لنت ترمز جلو پژو ۲۰۶', 'BRK-00452', 'پارس لنت', 4, 4, 'A-03-4', '17,200,000', 'brake-pad', 'ok'),
        ('فیلتر هوای پژو ۴۰۵', 'FLT-00118', 'سرکان', 2, 15, 'B-11-1', '6,400,000', 'air-filter', 'low'),
        ('فیلتر روغن پراید و تیبا', 'FLT-00203', 'بوش', 24, 20, 'B-11-3', '4,200,000', 'oil-filter', 'ok'),
        ('کمک فنر عقب پژو پارس', 'SUS-00290', 'کی‌بی‌ای', 0, 4, 'D-07-3', '—', 'shock', 'out'),
        ('باتری ۶۰ آمپر اتمی', 'ELE-00640', 'صبا', 1, 6, 'C-02-4', '32,900,000', 'battery', 'low'),
        ('شمع موتور سمند EF7', 'ENG-00377', 'NGK', 18, 12, 'B-04-5', '9,800,000', 'spark-plug', 'ok'),
    ]
    badge = {'ok': '<span class="badge b-ok">سالم</span>',
             'low': '<span class="badge b-warn">کمبود</span>',
             'out': '<span class="badge b-danger">صفر</span>'}
    rows = ''
    for n, c, b, q, mn, lo, p, ic, st in items:
        pct = max(5, min(100, q / mn * 100)) if mn else 100
        cls = '' if st == 'ok' else 'mid'
        rows += f'''<tr>
          <td><div class="row" style="gap:9px"><span class="thumb">{part(ic)}</span>
            <div><div class="b fs12">{n}</div><div class="ps en" style="font-size:10px">{c}</div></div></div></td>
          <td><span class="badge b-brand">{b}</span></td>
          <td class="num"><b>{money(q)}</b>
            <div class="stockbar {cls}" style="margin-inline-start:auto"><i style="width:{pct:.0f}%"></i></div></td>
          <td class="num hd-hide">{money(mn)}</td>
          <td class="hd-hide"><span class="badge b-line">{ico('archive')}{lo}</span></td>
          <td class="num hd-hide">{p}</td>
          <td>{badge[st]}</td>
          <td><div class="row" style="gap:5px">
            <button class="btn btn-sm btn-ghost btn-icon" title="اصلاح موجودی">{ico('edit')}</button>
            <button class="btn btn-sm btn-ghost btn-icon" title="جابه‌جایی">{ico('swap')}</button>
            <button class="btn btn-sm btn-ghost btn-icon" title="تاریخچه">{ico('clock')}</button></div></td>
        </tr>'''

    body = f'''
    <div class="page-h">
      <div><h2>اقلام موجودی</h2>
        <div class="crumb">{ico('layers')} انبار {ico('chevronL')} اقلام موجودی · محصول × برند</div></div>
      <span class="grow"></span>
      <button class="btn btn-sm btn-o">{ico('archive')}ورود کالا</button>
      <button class="btn btn-sm btn-o">{ico('swap')}جابه‌جایی قفسه</button>
      <button class="btn btn-sm btn-p">{ico('edit')}اصلاح موجودی</button>
    </div>

    <div class="kpis" style="grid-template-columns:repeat(4,1fr)">
      <div class="kpi"><div class="hd"><span class="ic">{ico('box')}</span>اقلام فعال</div>
        <div class="v">{money(486)}</div><div class="f fl">{ico('layers')}در ۱۴۲ محصول</div></div>
      <div class="kpi"><div class="hd"><span class="ic">{ico('archive')}</span>ارزش انبار (خرید)</div>
        <div class="v">{money(2840)}<small>میلیون ریال</small></div><div class="f fl">بر پایهٔ آخرین قیمت خرید</div></div>
      <div class="kpi alert"><div class="hd"><span class="ic">{ico('alert')}</span>زیر آستانه</div>
        <div class="v" style="color:var(--warn)">{money(7)}</div><div class="f dn">نیاز به سفارش</div></div>
      <div class="kpi"><div class="hd"><span class="ic">{ico('x')}</span>موجودی صفر</div>
        <div class="v" style="color:var(--danger)">{money(12)}</div><div class="f fl">۳ مورد «به‌زودی» در سایت</div></div>
    </div>

    <div class="toolbar">
      <div class="pill-tabs">
        <button class="on">همه <span class="n">{money(486)}</span></button>
        <button>کمبود <span class="n">{money(7)}</span></button>
        <button>صفر <span class="n">{money(12)}</span></button>
        <button>بدون قفسه <span class="n">{money(3)}</span></button>
      </div>
      <div class="search search-sm" style="width:250px">{ico('search')}
        <input class="inp" placeholder="نام قطعه، برند یا بارکد…"></div>
      <div class="selwrap">{ico('chevron')}<select class="inp inp-s sel" style="width:130px">
        <option>همهٔ قفسه‌ها</option><option>راهروی A</option><option>راهروی B</option></select></div>
      <div class="selwrap">{ico('chevron')}<select class="inp inp-s sel" style="width:120px">
        <option>همهٔ برندها</option><option>ایساکو</option><option>بوش</option></select></div>
      <span class="spacer"></span>
      <button class="btn btn-sm btn-ghost">{ico('download')}خروجی اکسل</button>
      <button class="btn btn-sm btn-ghost">{ico('print')}چاپ بارکدها</button>
    </div>

    <div class="card" style="overflow:hidden">
      <table class="tbl">
        <thead><tr><th>محصول</th><th>برند</th><th class="num">موجودی</th><th class="num hd-hide">آستانه</th>
          <th class="hd-hide">قفسه</th><th class="num hd-hide">قیمت فروش (ریال)</th><th>وضعیت</th><th></th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
      <div class="row" style="padding:11px 14px;gap:9px">
        <span class="fs11 mut3">نمایش ۷ از ۴۸۶ قلم</span><span class="grow"></span>
        <button class="btn btn-sm btn-ghost btn-icon">{ico('chevronL')}</button>
        <span class="badge b-line">۱ / ۷۰</span>
        <button class="btn btn-sm btn-ghost btn-icon" style="transform:scaleX(-1)">{ico('chevronL')}</button>
      </div>
    </div>'''

    sheet = f'''<div class="sheet">
      <div class="sheet-h"><span class="thumb" style="width:34px;height:34px">{part('brake-pad')}</span>
        <div class="wrap"><h3 class="fs13">اصلاح موجودی</h3>
          <div class="fs11 mut3">لنت ترمز جلو پژو ۲۰۶ · ایساکو · A-03-2</div></div>
        <button class="btn btn-sm btn-ghost btn-icon">{ico('x')}</button></div>
      <div class="sheet-b">
        <div class="kv"><span class="k">موجودی فعلی</span><span class="v">{money(5)}</span></div>
        <div class="kv"><span class="k">آخرین تراکنش</span><span class="v">فروش −۲ · ۱۴:۲۲</span></div>
        <div class="field"><span class="lab">نوع اصلاح</span>
          <div class="seg" style="width:100%"><button class="on" style="flex:1">شمارش</button>
            <button style="flex:1">افزایش دستی</button><button style="flex:1">کاهش دستی</button></div></div>
        <div class="field"><span class="lab">تعداد شمارش‌شده</span>
          <input class="inp" value="۴"></div>
        <div class="field"><span class="lab">دلیل (اجباری)</span>
          <div class="selwrap">{ico('chevron')}<select class="inp sel"><option>مغایرت شمارش انبار</option>
            <option>کالای آسیب‌دیده</option><option>ثبت اشتباه فروش</option><option>سایر</option></select></div></div>
        <div class="field"><span class="lab">توضیح</span>
          <textarea class="inp" rows="2">شمارش دستی ۳ شهریور — یک عدد کسری.</textarea></div>
        <div class="debt-note">{ico('alert')}<span>این عملیات یک تراکنش <b>adjustment</b> در دفتر کل ثبت می‌کند
          و قابل ویرایش نیست؛ فقط با تراکنش جدید قابل جبران است.</span></div>
        <div class="tl">
          <div class="it neg"><b>فروش −۲</b><span>فاکتور ۱۴۰۵/۰۰۳۴۷ · ۱۴:۲۲ · بعد: ۵</span></div>
          <div class="it pos"><b>ورود کالا +۷</b><span>فاکتور خرید ۱۴۰۵/۰۰۰۸۸ · دیروز · بعد: ۷</span></div>
          <div class="it"><b>موجودی اولیه ۰</b><span>۱۲ مرداد · بعد: ۰</span></div>
        </div>
      </div>
      <div class="sheet-f">
        <button class="btn btn-p grow">{ico('check')}ثبت اصلاح (−۱)</button>
        <button class="btn btn-ghost">انصراف</button>
      </div>
    </div>'''
    return shell(body, 'انبار', sheet)


# ============================================================ INVOICES LIST
def invoices():
    rows = [
        ('۱۴۰۵/۰۰۳۴۷', 'علی محمدی', '۳ شهریور ۱۴:۲۲', 3, 228700000, 78700000, 'بدهی', 'danger'),
        ('۱۴۰۵/۰۰۳۴۶', 'مکانیکی صدف', '۳ شهریور ۱۲:۰۵', 8, 96500000, 0, 'تسویه', 'ok'),
        ('۱۴۰۵/۰۰۳۴۵', 'رضا کریمی', '۳ شهریور ۱۰:۴۱', 2, 12400000, 0, 'تسویه', 'ok'),
        ('۱۴۰۵/۰۰۳۴۴', 'تعمیرگاه برادران نوری', '۲ شهریور ۱۸:۳۰', 11, 215000000, 215000000, 'بدهی', 'danger'),
        ('۱۴۰۵/۰۰۳۴۳', 'حسین اکبری', '۲ شهریور ۱۶:۱۲', 1, 4200000, 0, 'تسویه', 'ok'),
        ('۱۴۰۵/۰۰۳۴۲', 'سمیرا نوری', '۲ شهریور ۱۱:۰۳', 4, 33800000, 8000000, 'پرداخت بخشی', 'warn'),
        ('۱۴۰۵/۰۰۳۴۱', 'مهدی توکلی', '۱ شهریور ۱۹:۴۵', 2, 19600000, 0, 'مرجوعی دارد', 'info'),
    ]
    cls = {'ok': 'b-ok', 'danger': 'b-danger', 'warn': 'b-warn', 'info': 'b-brand'}
    trs = ''.join(f'''<tr>
        <td class="mono b">{n}</td><td>{c}</td><td class="fs12 mut">{d}</td>
        <td class="num">{money(q)}</td><td class="num b">{money(t)}</td>
        <td class="num" style="color:{'var(--danger)' if db else 'var(--text-3)'}">{money(db) if db else '—'}</td>
        <td><span class="badge {cls[s]}">{ico('check') if s == 'ok' else ico('clock')}{st}</span></td>
        <td><div class="row" style="gap:4px">
          <button class="btn btn-sm btn-ghost btn-icon">{ico('eye')}</button>
          <button class="btn btn-sm btn-ghost btn-icon">{ico('download')}</button>
          <button class="btn btn-sm btn-ghost btn-icon">{ico('sms')}</button>
          <button class="btn btn-sm btn-ghost btn-icon">{ico('chevron')}</button></div></td>
      </tr>''' for n, c, d, q, t, db, st, s in rows)

    body = f'''
    <div class="page-h">
      <div><h2>فاکتورها</h2><div class="crumb">{ico('money')} فروش {ico('chevronL')} لیست فاکتورها</div></div>
      <span class="grow"></span>
      <button class="btn btn-sm btn-o">{ico('refresh')}به‌روزرسانی</button>
      <button class="btn btn-sm btn-p">{ico('plus')}فاکتور جدید</button>
    </div>
    <div class="toolbar">
      <div class="pill-tabs">
        <button class="on">همه <span class="n">{money(1248)}</span></button>
        <button>پرداخت‌نشده <span class="n">{money(4)}</span></button>
        <button>بدهی‌دار <span class="n">{money(19)}</span></button>
        <button>مرجوعی‌دار <span class="n">{money(3)}</span></button>
        <button>باطل‌شده <span class="n">{money(1)}</span></button>
      </div>
      <div class="search search-sm" style="width:230px">{ico('search')}
        <input class="inp" placeholder="شمارهٔ فاکتور، مشتری، موبایل…"></div>
      <div class="selwrap">{ico('chevron')}<select class="inp inp-s sel" style="width:150px">
        <option>۷ روز اخیر</option><option>این ماه</option><option>بازهٔ دلخواه</option></select></div>
      <span class="spacer"></span>
      <button class="btn btn-sm btn-ghost">{ico('download')}خروجی</button>
    </div>
    <div class="card" style="overflow:hidden">
      <table class="tbl"><thead><tr><th>شماره</th><th>مشتری</th><th>تاریخ</th><th class="num">قلم</th>
        <th class="num">مبلغ (ریال)</th><th class="num">بدهی</th><th>وضعیت</th><th></th></tr></thead>
        <tbody>{trs}</tbody></table>
      <div class="row" style="padding:11px 14px"><span class="fs11 mut3">۷ از ۱,۲۴۸ فاکتور</span>
        <span class="grow"></span><span class="badge b-line">۱ / ۱۷۹</span></div>
    </div>'''
    return shell(body, 'فروش')


# ============================================================ REPORTS
def reports():
    labels = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور']
    vals = [62, 74, 68, 91, 104, 48]
    brands = [('ایساکو', 412, 'var(--brand-600)'), ('بوش', 318, 'var(--brand-400)'),
              ('سرکان', 205, 'var(--ok)'), ('واله', 164, 'var(--brand-300)'),
              ('سایر', 341, 'var(--border-2)')]
    total = sum(b[1] for b in brands)
    legend = ''.join(f'''<tr><td><div class="row" style="gap:8px"><i style="width:9px;height:9px;border-radius:3px;
        background:{c};display:inline-block"></i>{n}</div></td>
      <td class="num b">{money(v)}<span class="fs11 mut3"> قلم</span></td>
      <td class="num hd-hide">{money(round(v/total*100))}٪</td>
      <td class="num hd-hide">{money(v*1820000)}</td></tr>''' for n, v, c in brands)

    body = f'''
    <div class="page-h">
      <div><h2>گزارش سود و فروش</h2>
        <div class="crumb">{ico('chart')} گزارش‌ها {ico('chevronL')} سود برندمحور</div></div>
      <span class="grow"></span>
      <div class="selwrap">{ico('chevron')}<select class="inp inp-s sel" style="width:140px"><option>۶ ماه اخیر</option></select></div>
      <button class="btn btn-sm btn-o">{ico('download')}خروجی Excel</button>
      <button class="btn btn-sm btn-ghost btn-icon">{ico('print')}</button>
    </div>
    <div class="kpis">
      <div class="kpi"><div class="hd"><span class="ic">{ico('money')}</span>فروش کل</div>
        <div class="v">{money(18420)}<small>میلیون ریال</small></div><div class="f up">{ico('trend')}۲۴٪ رشد</div></div>
      <div class="kpi"><div class="hd"><span class="ic">{ico('trend')}</span>سود ناخالص</div>
        <div class="v">{money(4680)}<small>میلیون ریال</small></div><div class="f up">{ico('trend')}حاشیهٔ ۲۵.۴٪</div></div>
      <div class="kpi"><div class="hd"><span class="ic">{ico('file')}</span>میانگین فاکتور</div>
        <div class="v">{money(14.8)}<small>میلیون ریال</small></div><div class="f fl">۴.۱ قلم در هر فاکتور</div></div>
      <div class="kpi"><div class="hd"><span class="ic">{ico('users')}</span>مشتریان فعال</div>
        <div class="v">{money(286)}</div><div class="f up">{ico('trend')}۳۱ مشتری جدید</div></div>
    </div>
    <div class="cols-2">
      <div class="card">
        <div class="card-h"><h3>فروش ماهانه (میلیون ریال)</h3><span class="grow"></span>
          <div class="legend"><span><i style="background:var(--brand-500)"></i>فروش</span>
            <span><i style="background:var(--ok)"></i>سود</span></div></div>
        <div class="chart-wrap">{bars(vals, labels, today_idx=5)}
          <div class="axis"><span>فروردین</span><span>خرداد</span><span>شهریور (ناقص)</span></div></div>
      </div>
      <div class="card">
        <div class="card-h"><h3>سهم برندها از فروش</h3><span class="grow"></span>
          <button class="btn btn-sm btn-ghost btn-icon">{ico('chevron')}</button></div>
        <div class="card-b">{donut([
            ('ایساکو', 412, 'var(--brand-600)'), ('بوش', 318, 'var(--brand-400)'),
            ('سرکان', 205, 'var(--ok)'), ('واله', 164, 'var(--brand-300)'),
            ('سایر', 341, 'var(--border-2)')])}</div>
      </div>
    </div>
    <div class="card" style="margin-top:14px;overflow:hidden">
      <div class="card-h"><h3>جدول سود به تفکیک برند</h3><span class="grow"></span>
        <div class="seg"><button class="on">سود</button><button>تعداد</button><button>گردش مالی</button></div></div>
      <table class="tbl"><thead><tr><th>برند</th><th class="num">اقلام فروخته‌شده</th>
        <th class="num hd-hide">سهم</th><th class="num hd-hide">سود تخمینی (ریال)</th></tr></thead>
        <tbody>{legend}</tbody></table>
    </div>'''
    return shell(body, 'گزارش‌ها')


# ============================================================ SETTINGS
def settings():
    body = f'''
    <div class="page-h">
      <div><h2>تنظیمات</h2><div class="crumb">{ico('gear')} مدیریت {ico('chevronL')} تنظیمات سیستم</div></div>
      <span class="grow"></span>
      <button class="btn btn-sm btn-p">{ico('save')}ذخیرهٔ تنظیمات</button>
    </div>
    <div class="cols-2b">
      <div class="card">
        <div class="card-h">{ico('shop' if False else 'home')}<h3>اطلاعات فروشگاه (نمایش در سایت)</h3></div>
        <div class="card-b col">
          <div class="field"><span class="lab">نام فروشگاه</span><input class="inp" value="فروشگاه قطعات یدکی سلیم‌وند"></div>
          <div class="field"><span class="lab">تلفن‌ها</span><input class="inp mono" value="021-33987654, 09123456789" style="direction:ltr"></div>
          <div class="field"><span class="lab">آدرس</span><textarea class="inp" rows="2">تهران، خیابان امام خمینی، پاساژ قطعات یدکی، پلاک ۱۲</textarea></div>
          <div class="row" style="gap:9px">
            <div class="field grow"><span class="lab">ساعت شروع</span><input class="inp" value="۰۹:۰۰"></div>
            <div class="field grow"><span class="lab">ساعت پایان</span><input class="inp" value="۲۰:۰۰"></div>
            <div class="field grow"><span class="lab">روزهای تعطیل</span><input class="inp" value="جمعه"></div>
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-h">{ico('sms')}<h3>قالب پیامک</h3>
          <span class="grow"></span><span class="badge b-ok">{ico('check')}پنل فعال</span></div>
        <div class="card-b col">
          <div class="field"><span class="lab">قالب فاکتور</span>
            <textarea class="inp" rows="3">سلیم‌وند: فاکتور {{"شماره"}} صادر شد. مبلغ {{"مبلغ"}} ریال.
مشاهده: {{"لینک"}}</textarea></div>
          <div class="row" style="gap:7px;flex-wrap:wrap">
            <span class="badge b-line mono">{"{{"}شماره{"}}"}</span>
            <span class="badge b-line mono">{"{{"}مبلغ{"}}"}</span>
            <span class="badge b-line mono">{"{{"}نام{"}}"}</span>
            <span class="badge b-line mono">{"{{"}لینک{"}}"}</span>
          </div>
          <div class="row" style="gap:9px;justify-content:space-between">
            <span class="fs12">ارسال خودکار پس از صدور فاکتور</span><span class="sw on"></span></div>
          <div class="row" style="gap:9px;justify-content:space-between">
            <span class="fs12">یادآوری بدهی (۷ روز)</span><span class="sw on"></span></div>
          <div class="row" style="gap:9px;justify-content:space-between">
            <span class="fs12">اعتبارسنجی شمارهٔ موبایل</span><span class="sw"></span></div>
        </div>
      </div>
      <div class="card">
        <div class="card-h">{ico('telegram')}<h3>تلگرام / بله / کانال</h3></div>
        <div class="card-b col">
          <div class="row" style="gap:9px;justify-content:space-between">
            <span class="fs12">ربات استعلام مشتری</span><span class="sw on"></span></div>
          <div class="row" style="gap:9px;justify-content:space-between">
            <span class="fs12">انتشار خودکار در کانال (کالاهای جدید)</span><span class="sw on"></span></div>
          <div class="row" style="gap:9px;justify-content:space-between">
            <span class="fs12">اعلان کمبود موجودی به چت مدیر</span><span class="sw on"></span></div>
          <div class="field"><span class="lab">شناسهٔ کانال</span><input class="inp mono" value="@selimvand_parts" style="direction:ltr"></div>
          <div class="field"><span class="lab">ربات بله</span><input class="inp mono" value="@selimvand_bot" style="direction:ltr"></div>
        </div>
      </div>
      <div class="card">
        <div class="card-h">{ico('alert')}<h3>آستانهٔ هشدارها و بکاپ</h3>
          <span class="grow"></span><span class="badge b-ok">{ico('db')}درایو متصل</span></div>
        <div class="card-b col">
          <div class="row" style="gap:9px;align-items:center">
            <span class="fs12 wrap">هشدار پیش‌فرض کمبود (min_stock)</span>
            <input class="money-in" style="width:76px" value="۵"></div>
          <div class="row" style="gap:9px;align-items:center">
            <span class="fs12 wrap">هشدار موجودی صفر در سایت</span><span class="sw on"></span></div>
          <div class="row" style="gap:9px;align-items:center">
            <span class="fs12 wrap">بکاپ خودکار روزانه — ساعت</span>
            <input class="money-in" style="width:76px" value="۰۳:۰۰"></div>
          <div class="row" style="gap:9px;align-items:center">
            <span class="fs12 wrap">حذف فایل‌های موقت پس از آپلود</span><span class="sw on"></span></div>
          <div class="debt-note">{ico('shield')}<span>هیچ فایل دائمی روی VPS نگهداری نمی‌شود؛
            PDF در لحظه تولید و ویدئوها روی آپارات میزبانی می‌شوند.</span></div>
        </div>
      </div>
    </div>'''
    return shell(body, 'تنظیمات')


# ============================================================ LOGIN + PALETTE + MOBILE
def login():
    return f'''<div class="login-wrap">
  <div class="login-card">
    <div class="row" style="gap:11px;margin-bottom:6px">
      <div class="logo" style="width:42px;height:42px"><span>س</span></div>
      <div><h3 style="font-size:16px">سلیم‌وند</h3><div class="fs11 mut3">پنل مدیریت فروشگاه</div></div>
    </div>
    <p class="mut fs12" style="margin-bottom:16px">برای ورود، نام کاربری و رمز عبور خود را وارد کنید.</p>
    <div class="col" style="gap:13px">
      <div class="field"><span class="lab">نام کاربری</span><input class="inp" value="m.salemi"></div>
      <div class="field"><span class="lab">رمز عبور</span><input class="inp" type="password" value="••••••••••"></div>
      <div class="row" style="justify-content:space-between">
        <span class="fs12 row" style="gap:7px"><span class="chk on">{ico('check')}</span>مرا به خاطر بسپار</span>
        <a class="fs12" style="color:var(--link)">فراموشی رمز؟</a>
      </div>
      <button class="btn btn-p btn-lg btn-block">{ico('key')}ورود به پنل</button>
    </div>
    <div class="hr"></div>
    <div class="row" style="justify-content:center;gap:8px">
      <span class="badge b-line">{ico('shield')}محدودسازی نرخ ورود</span>
      <span class="badge b-line">{ico('clock')}انقضای نشست ۸ ساعت</span>
    </div>
  </div>
</div>'''


def palette():
    groups = [
        ('محصولات', '۱', [
            ('box', 'لنت ترمز جلو پژو ۲۰۶', 'BRK-00452 · ایساکو ۵ · پارس لنت ۴', 'b-ok', 'موجود'),
            ('box', 'کمک فنر عقب پژو پارس', 'SUS-00290 · کی‌بی‌ای ۰', 'b-danger', 'ناموجود'),
        ]),
        ('مشتریان', '۲', [
            ('users', 'علی محمدی', '۰۹۱۲۳۴۵۶۷۸۹ · بدهی ۷۸,۷۰۰,۰۰۰', 'b-warn', 'بدهی'),
        ]),
        ('فاکتورها', '۳', [
            ('file', '۱۴۰۵/۰۰۳۴۷', 'علی محمدی · ۲۲۸,۷۰۰,۰۰۰ ریال', 'b-brand', 'باز'),
        ]),
        ('قفسه‌ها', '۴', [
            ('archive', 'انبار اصلی › A › قفسهٔ ۳ › طبقهٔ ۲', '۱۴ باکس · ۸۶ قلم', '', ''),
        ]),
    ]
    out = ''
    for title, key, items in groups:
        rows = ''
        for ic, nm, sub, bc, tag in items:
            t = f'<span class="badge {bc}">{tag}</span>' if bc else ''
            on = ' on' if title == 'محصولات' and 'لنت' in nm else ''
            rows += (f'<div class="pitem{on}"><span class="ic">{ico(ic)}</span>'
                     f'<div class="wrap"><div class="nm">{nm}</div><div class="sub">{sub}</div></div>'
                     f'<span class="rt">{t}</span></div>')
        out += f'<div class="pgroup"><div class="gt">{title}<kbd>{key}</kbd></div>{rows}</div>'
    return f'''<div class="modal-mask">
  <div class="palette">
    <div class="pi">{ico('search')}<input value="لنت" placeholder="جست‌وجوی سراسری…"><kbd>Esc</kbd></div>
    <div style="max-height:420px;overflow:auto">{out}</div>
    <div class="row" style="padding:9px 14px;border-top:1px solid var(--border);gap:12px">
      <span class="fs11 mut3">{ico('chevronL')} بالا/پایین</span>
      <span class="fs11 mut3">Enter — باز کردن</span>
      <span class="grow"></span>
      <span class="fs11 mut3">۱..۵ — پرش به بخش</span>
    </div>
  </div>
</div>'''


def mobile_admin():
    body = f'''
    <header class="adm-top" style="height:52px;padding:0 12px;gap:8px">
      <div class="row" style="gap:8px"><div class="logo" style="width:30px;height:30px"><span>س</span></div>
        <b class="fs13">داشبورد</b></div>
      <span class="grow"></span>
      <button class="icb" style="width:30px;height:30px">{ico('bell')}<i class="bdg"></i></button>
      <div class="av" style="width:28px;height:28px;border-radius:9px;background:var(--brand-800);color:#fff;
        display:grid;place-items:center;font-size:11px;font-weight:700">مس</div>
    </header>
    <div class="adm-body" style="padding:12px">
      <div class="search search-sm" style="margin-bottom:12px">{ico('search')}
        <input class="inp" placeholder="جست‌وجوی سریع…"><kbd></kbd></div>
      <div class="kpis" style="grid-template-columns:1fr 1fr;gap:9px">
        <div class="kpi" style="padding:11px 12px"><div class="hd" style="font-size:11px"><span class="ic" style="width:26px;height:26px">{ico('money')}</span>فروش امروز</div>
          <div class="v" style="font-size:17px;margin-top:6px">{money(48620)}</div>
          <div class="f up" style="font-size:10px">{ico('trend')}۱۸٪</div></div>
        <div class="kpi" style="padding:11px 12px"><div class="hd" style="font-size:11px"><span class="ic" style="width:26px;height:26px">{ico('file')}</span>فاکتورها</div>
          <div class="v" style="font-size:17px;margin-top:6px">{money(23)}</div>
          <div class="f up" style="font-size:10px">{ico('trend')}۴ بیشتر</div></div>
      </div>
      <div class="card" style="margin-top:11px">
        <div class="card-h" style="padding:11px 13px"><h3 class="fs13">کمبود موجودی</h3>
          <span class="grow"></span><span class="badge b-danger">{money(7)}</span></div>
        <div class="card-b" style="padding:6px 13px">
          <div class="list-row"><span class="thumb">{part('brake-pad')}</span>
            <div class="wrap"><div class="nm">لنت ترمز ۲۰۶</div><div class="sub">ایساکو · A-03-2</div></div>
            <span class="badge b-warn">{money(2)}/{money(10)}</span></div>
          <div class="list-row"><span class="thumb">{part('shock')}</span>
            <div class="wrap"><div class="nm">کمک فنر پارس</div><div class="sub">کی‌بی‌ای · D-07-3</div></div>
            <span class="badge b-danger">۰</span></div>
        </div>
      </div>
      <div class="card" style="margin-top:11px">
        <div class="card-h" style="padding:11px 13px"><h3 class="fs13">آخرین فاکتورها</h3></div>
        <div class="card-b" style="padding:6px 13px">
          <div class="list-row"><span class="thumb">{ico('file')}</span>
            <div class="wrap"><div class="nm">۱۴۰۵/۰۰۳۴۷ — علی محمدی</div>
              <div class="sub">۳ قلم · ۱۴:۲۲</div></div>
            <div class="val"><b class="fs12 mono">{money(228700000)}</b>
              <div class="fs11" style="color:var(--danger)">بدهی</div></div></div>
          <div class="list-row"><span class="thumb">{ico('file')}</span>
            <div class="wrap"><div class="nm">۱۴۰۵/۰۰۳۴۶ — مکانیکی صدف</div>
              <div class="sub">۸ قلم · ۱۲:۰۵</div></div>
            <div class="val"><b class="fs12 mono">{money(96500000)}</b>
              <div class="fs11" style="color:var(--ok)">تسویه</div></div></div>
        </div>
      </div>
    </div>
    <button class="fab">{ico('plus')}</button>
    <nav class="mnav">
      <a class="on">{ico('home')}داشبورد</a><a>{ico('money')}فروش</a><a>{ico('box')}محصولات</a>
      <a>{ico('layers')}انبار</a><a>{ico('users')}مشتریان</a><a>{ico('gear')}بیشتر</a>
    </nav>'''
    return f'<div class="adm" style="display:block;position:relative">{body}</div>'
