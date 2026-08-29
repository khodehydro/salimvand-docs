# -*- coding: utf-8 -*-
"""Assemble the single-file UI concept for فروشگاه سلیم‌وند."""

import json
import pathlib

from icons import svg_defs, ico
import screens_site as S
import screens_admin as A
import screens_ds as DS

HERE = pathlib.Path(__file__).parent


# ------------------------------------------------------------------ frame
def frame(url, inner, cls='w-desk', cap=''):
    bar = (f'<div class="frame-bar"><i></i><i></i><i></i>'
           f'<span class="url">{ico("shield")}<span>{url}</span></span></div>')
    c = f'<div class="phone-cap">{cap}</div>' if cap else ''
    return f'<div class="frame {cls}">{bar}<div class="frame-body">{inner}</div></div>{c}'


def note(title, items):
    lis = ''.join(f'<li>{ico("check")}<span>{t}</span></li>' for t in items)
    return f'''<div class="note"><div class="card"><div class="card-b">
      <h4>{title}</h4><ul>{lis}</ul></div></div></div>'''


def stage(*cols):
    return f'<div class="stage">{"".join(cols)}</div>'


def section(sid, eyebrow, title, desc, body):
    return f'''<section class="sec" id="{sid}">
      <div class="sec-h"><div><div class="eyebrow">{eyebrow}</div><h2>{title}</h2>
        <p>{desc}</p></div></div>
      {body}</section>'''


# ------------------------------------------------------------------ views
def view_site():
    nav = ''.join(f'<a href="#s{i}"><span class="k">{i}</span>{t}</a>'
                  for i, t in [(1, 'کاتالوگ دسکتاپ'), (2, 'نمای موبایل'), (3, 'فاکتور آنلاین')])
    s1 = section('s1', 'سایت عمومی · مسیر /', 'کاتالوگ تک‌صفحه‌ای',
                 'تنها صفحهٔ اصلی سایت: هیرو، ویدئوی اعتماد آپارات، کاتالوگ با فیلتر چسبان، تماس و فوتر. '
                 'بدون سبد خرید و بدون قیمت.',
                 stage(frame('selimvand.ir', S.site_home()),
                       note('نکته‌های این صفحه', [
                           '<span class="k">بدون قیمت:</span> هیچ فیلد قیمتی از API عمومی نمی‌آید؛ پیام ثابت «قیمت فقط با استعلام» در هیرو، کارت‌ها و فوتر.',
                           '<span class="k">فیلتر چسبان:</span> خودرو (برند/مدل/تیپ) + دستهٔ درختی + جست‌وجو + «فقط موجود».',
                           '<span class="k">وضعیت فیلتر در URL:</span> قابل اشتراک و ایندکس‌پذیر.',
                           '<span class="k">کارت محصول:</span> تصویر، بج دسته، وضعیت رنگی، برندهای موجود/ناموجود، خودروهای سازگار.',
                           '<span class="k">ویدئو:</span> فقط با کلیک کاربر iframe آپارات لود می‌شود.',
                           '<span class="k">هدایت به تماس:</span> دکمه‌های تماس/تلگرام/بله در هر کارت و در نوار چسبان موبایل.',
                       ])))
    s2 = section('s2', 'سایت عمومی · موبایل', 'نمای موبایل سایت',
                 'بیشتر مشتری‌ها با موبایل می‌آیند: هدر فشرده، هیرو کوتاه، فیلتر جمع‌شونده و نوار تماس چسبان پایین.',
                 stage(frame('selimvand.ir', S.site_mobile(), 'w-phone', '۳۷۸px — نمای موبایل'),
                       note('نکته‌های موبایل', [
                           'فیلترها به یک ردیف جمع‌شونده تبدیل می‌شوند (دکمهٔ فیلتر → شیت پایین).',
                           'کارت‌ها تک‌ستونه با دکمه‌های فشردهٔ تماس/تلگرام.',
                           'نوار چسبان پایین همیشه سه راه ارتباطی را در دسترس نگه می‌دارد.',
                           'صفحهٔ فاکتور پیامک‌شده هم همین زبان بصری را دارد.',
                       ])))
    s3 = section('s3', 'سایت عمومی · مسیر /invoice/[token]', 'فاکتور آنلاین مشتری',
                 'صفحهٔ عمومی فاکتور که فقط با توکن امن باز می‌شود؛ اقلام با برند، مبالغ، وضعیت پرداخت، QR و دانلود PDF.',
                 stage(frame('selimvand.ir/invoice/9f2c…b71e', S.invoice_page()),
                       frame('selimvand.ir/invoice/9f2c…b71e', S.invoice_mobile(), 'w-phone', 'لینک پیامک‌شده'),
                       note('نکته‌های فاکتور', [
                           'تاریخ شمسی، مبلغ به ریال و توضیح تومان در کنار آن.',
                           'وضعیت پرداخت: تسویه / پرداخت بخشی / بدهی — با رنگ معنایی.',
                           'QR برای بازکردن سریع همان فاکتور روی گوشی دیگر.',
                           'دکمهٔ PDF (تولید در لحظه روی سرور) و چاپ.',
                           'هیچ دادهٔ داخلی (قفسه، قیمت خرید، موجودی) نمایش داده نمی‌شود.',
                       ])))
    return f'<div class="sec-nav">{nav}</div>{s1}{s2}{s3}'


def view_admin():
    nav = ''.join(f'<a href="#a{i}"><span class="k">{i}</span>{t}</a>'
                  for i, t in [(1, 'ورود'), (2, 'داشبورد'), (3, 'صدور فاکتور'), (4, 'محصول'),
                               (5, 'انبار'), (6, 'فاکتورها'), (7, 'گزارش‌ها'), (8, 'تنظیمات'),
                               (9, 'جست‌وجوی سراسری'), (10, 'موبایل')])
    secs = [
        section('a1', 'پنل مدیریت · ورود', 'ورود به پنل',
                'ورود با نام کاربری و رمز، با محدودسازی نرخ و انقضای نشست. پس‌زمینه از همان پالت سرمه‌ای برند.',
                stage(frame('admin.selimvand.ir/login', A.login(), 'w-tab'),
                      note('نکته‌های ورود', [
                          'بدون بازیابی رمز خودکار عمومی — ریست توسط مدیر کل.',
                          'نمایش وضعیت امنیت (نرخ ورود، انقضای نشست) برای اطمینان کاربر.',
                      ]))),
        section('a2', 'پنل مدیریت · داشبورد', 'داشبورد',
                'چهار کارت شاخص، نمودار فروش ۳۰ روز، ترکیب موجودی، فاکتورهای پرداخت‌نشده، کمبودها، '
                'دفتر تراکنش‌ها و سلامت یکپارچه‌سازی‌ها.',
                stage(frame('admin.selimvand.ir', A.dashboard(), 'w-admin'),
                      note('نکته‌های داشبورد', [
                          'شاخص‌ها بر اساس نقش فیلتر می‌شوند (فروشنده سود را نمی‌بیند).',
                          '«کمبود موجودی» مستقیماً به فرم ورود کالا وصل است.',
                          'دفتر تراکنش‌ها فقط خواندنی است — موجودی از آن مشتق می‌شود.',
                          'کارت سلامت: پیامک، تلگرام، بکاپ درایو، فضای دیسک VPS.',
                      ]))),
        section('a3', 'پنل مدیریت · مهم‌ترین صفحه', 'صدور فاکتور',
                'انتخاب مشتری، جست‌وجوی زندهٔ قطعه با ورودی بارکدخوان، انتخاب برند و تعداد، '
                'محاسبهٔ مبلغ و پرداخت، و صدور با پیامک خودکار.',
                stage(frame('admin.selimvand.ir/sales/invoices/new', A.invoice_create(), 'w-admin'),
                      note('نکته‌های صدور فاکتور', [
                          'فیلد جست‌وجو همزمان ورودی بارکدخوان کیبوردی است (Enter = اسکن).',
                          'هر برند یک ردیف موجودی مستقل است؛ قیمت و قفسه همان لحظه دیده می‌شود.',
                          'برند ناموجود غیرفعال نمایش داده می‌شود تا فروشنده اشتباه انتخاب نکند.',
                          'باقی‌ماندهٔ پرداخت به‌صورت خودکار بدهی مشتری می‌شود.',
                          'مودال موفقیت: شمارهٔ فاکتور، وضعیت پیامک، لینک فاکتور، «فاکتور بعدی».',
                      ]))),
        section('a4', 'پنل مدیریت · کاتالوگ', 'فرم محصول (تب‌دار)',
                'یک فرم با پنج تب: اطلاعات پایه، تصاویر، ویدئوی آپارات، خودروهای سازگار (درختی) '
                'و اقلام موجودی به تفکیک برند.',
                stage(frame('admin.selimvand.ir/catalog/products/edit', A.product_edit(), 'w-admin'),
                      note('نکته‌های فرم محصول', [
                          'کد محصول خودکار از پیشوند دسته ساخته می‌شود (BRK-00452).',
                          'تصاویر به WebP تبدیل و فقط دو اندازه نگه داشته می‌شوند.',
                          'ویدئو فقط با شناسهٔ آپارات ذخیره می‌شود — بدون فایل روی سرور.',
                          'تب اقلام موجودی: برند، تعداد، قیمت خرید/فروش، قفسه، بارکد، آستانهٔ هشدار.',
                          'حذف نرم با امکان بازیابی.',
                      ]))),
        section('a5', 'پنل مدیریت · انبار', 'اقلام موجودی و اصلاح',
                'لیست قلم‌های موجودی (محصول × برند) با قفسه و آستانه، و شیت کناری اصلاح موجودی با دلیل اجباری '
                'و تاریخچهٔ تراکنش‌ها.',
                stage(frame('admin.selimvand.ir/warehouse/items', A.inventory(), 'w-admin'),
                      note('نکته‌های انبار', [
                          'موجودی فقط با تراکنش تغییر می‌کند؛ اصلاح = تراکنش adjustment با دلیل اجباری.',
                          'مسیر قفسه از ریشه نمایش داده می‌شود (انبار › راهرو › قفسه › طبقه › باکس).',
                          'چاپ دسته‌ای بارکد EAN-13 برای قفسه و کالا.',
                          'فیلتر سریع: کمبود / صفر / بدون قفسه.',
                      ]))),
        section('a6', 'پنل مدیریت · فروش', 'لیست فاکتورها',
                'جدول فاکتورها با فیلتر وضعیت، بدهی، تاریخ و دسترسی سریع به PDF، پیامک مجدد و جزئیات.',
                stage(frame('admin.selimvand.ir/sales/invoices', A.invoices(), 'w-admin'),
                      note('نکته‌های لیست', [
                          'فاکتور هرگز حذف فیزیکی نمی‌شود — فقط ابطال با ثبت دلیل.',
                          'مرجوعی، فاکتور اصلی را دست نمی‌زند.',
                          'ارسال مجدد لینک فاکتور با یک کلیک.',
                      ]))),
        section('a7', 'پنل مدیریت · گزارش‌ها', 'گزارش سود و فروش',
                'نمودار فروش ماهانه، سهم برندها و جدول سود به تفکیک برند با خروجی اکسل.',
                stage(frame('admin.selimvand.ir/reports', A.reports(), 'w-admin'),
                      note('نکته‌های گزارش', [
                          'سود واقعی از تفاوت قیمت خرید و فروش همان قلم برندمحور محاسبه می‌شود.',
                          'دسترسی گزارش سود فقط برای مدیر و مدیر کل.',
                          'خروجی Excel/CSV سمت سرور تولید می‌شود.',
                      ]))),
        section('a8', 'پنل مدیریت · تنظیمات', 'تنظیمات سیستم',
                'اطلاعات فروشگاه (خوراک سایت)، قالب پیامک، تلگرام/بله/کانال، آستانهٔ هشدارها و بکاپ.',
                stage(frame('admin.selimvand.ir/settings', A.settings(), 'w-admin'),
                      note('نکته‌های تنظیمات', [
                          'هرچه در «اطلاعات فروشگاه» است، مستقیماً در سایت عمومی نمایش داده می‌شود.',
                          'قالب پیامک با متغیرهای قابل درج و پیش‌نمایش.',
                          'قانون «بدون فایل دائمی روی VPS» در همین صفحه قابل رصد است.',
                      ]))),
        section('a9', 'پنل مدیریت · بهره‌وری', 'جست‌وجوی سراسری (Ctrl+K)',
                'پالت مرکزی با گروه‌بندی نتایج: محصولات (با موجودی)، مشتریان، فاکتورها، قفسه‌ها.',
                stage(frame('admin.selimvand.ir', A.shell('<div style="height:340px"></div>', 'داشبورد', A.palette()), 'w-tab'),
                      note('نکته‌های پالت', [
                          'کلیدهای ۱..۵ برای پرش بین گروه‌ها.',
                          'نتایج محصول همراه با موجودی هر برند.',
                          'بدون ماوس: کامل با کیبورد قابل استفاده است.',
                      ]))),
        section('a10', 'پنل مدیریت · موبایل', 'پنل روی موبایل',
                'فروشنده و انباردار با گوشی کار می‌کنند: نوار پایین، دکمهٔ شناور صدور فاکتور، کارت‌های فشرده.',
                stage(frame('admin.selimvand.ir', A.mobile_admin(), 'w-phone', '۳۷۸px — فروشنده/انباردار'),
                      note('نکته‌های موبایل پنل', [
                          'سایدبار به نوار پایین تبدیل می‌شود؛ منوها بر اساس نقش فیلتر می‌شوند.',
                          'دکمهٔ شناور = صدور فاکتور سریع با بارکدخوان دوربین.',
                          'همهٔ جدول‌ها ستون‌های کم‌اهمیت را در موبایل پنهان می‌کنند.',
                      ]))),
    ]
    return f'<div class="sec-nav">{nav}</div>' + ''.join(secs)


def view_ds():
    return section('ds', 'مبانی طراحی', 'سیستم طراحی',
                   'توکن‌های رنگ، تایپوگرافی، فاصله، اجزای پایه و حالت‌ها. پایهٔ پالت: آبی تیره و سفید '
                   'با سه رنگ معنایی برای وضعیت موجودی.',
                   DS.design_system())


# ------------------------------------------------------------------ page
def topbar():
    return f'''<header class="topbar"><div class="topbar-in">
      <div class="brandmark">
        <div class="logo"><span>س</span></div>
        <div><div class="t1">فروشگاه سلیم‌وند</div><div class="t2">مفهوم رابط کاربری · نسخهٔ ۱</div></div>
      </div>
      <div class="tabsbar">
        <button class="on" data-view="site">{ico('home')}سایت عمومی</button>
        <button data-view="admin">{ico('grid')}پنل مدیریت</button>
        <button data-view="ds">{ico('layers')}سیستم طراحی</button>
      </div>
      <span class="grow"></span>
      <div class="pals" title="پالت رنگ برند">
        <button class="pal pal-p1 on" data-pal="" title="سرمه‌ای کلاسیک"></button>
        <button class="pal pal-p2" data-pal="slate" title="سرمه‌ای خاکستری"></button>
        <button class="pal pal-p3" data-pal="petrol" title="آبی نفتی"></button>
        <button class="pal pal-p4" data-pal="indigo" title="سرمه‌ای نیلی"></button>
      </div>
      <button class="btn btn-sm btn-soft" data-theme-btn>{ico('moon')}<span data-theme-label>دارک مود</span></button>
    </div></header>'''


JS = r'''
(function(){
  var root=document.documentElement;
  function setTheme(t){root.setAttribute('data-theme',t);
    document.querySelectorAll('[data-theme-label]').forEach(function(e){e.textContent=t==='dark'?'لایت مود':'دارک مود';});
    document.querySelectorAll('[data-theme-btn] svg use').forEach(function(u){
      u.setAttribute('href', t==='dark'?'#i-sun':'#i-moon');});
  }
  document.addEventListener('click',function(e){
    var tb=e.target.closest('[data-theme-btn]');
    if(tb){setTheme(root.getAttribute('data-theme')==='dark'?'light':'dark');return;}
    var pal=e.target.closest('[data-pal]');
    if(pal){root.setAttribute('data-palette',pal.getAttribute('data-pal'));
      document.querySelectorAll('[data-pal]').forEach(function(p){p.classList.remove('on');});
      pal.classList.add('on');return;}
    var v=e.target.closest('[data-view]');
    if(v){document.querySelectorAll('[data-view]').forEach(function(b){b.classList.remove('on');});
      v.classList.add('on');
      document.querySelectorAll('[data-viewpane]').forEach(function(p){
        p.style.display=p.getAttribute('data-viewpane')===v.getAttribute('data-view')?'block':'none';});
      try{window.scrollTo({top:0,behavior:'smooth'});}catch(err){window.scrollTo(0,0);}
      return;}
    var cp=e.target.closest('[data-copy]');
    if(cp){var hex=cp.getAttribute('data-copy');
      if(navigator.clipboard){navigator.clipboard.writeText(hex).catch(function(){});}
      var b=cp.querySelector('b'),old=b.textContent;b.textContent='کپی شد!';
      setTimeout(function(){b.textContent=old;},900);return;}
    var sw=e.target.closest('.sw');
    if(sw){sw.classList.toggle('on');return;}
    var ck=e.target.closest('.chk');
    if(ck){ck.classList.toggle('on');return;}
    var sg=e.target.closest('.seg button, .pill-tabs button, .tabs button');
    if(sg){var p=sg.parentElement;
      p.querySelectorAll('button').forEach(function(b){b.classList.remove('on');});
      sg.classList.add('on');}
  });
  setTheme('light');
})();
'''


def build():
    fonts = json.loads((HERE / 'fonts_b64.json').read_text())
    faces = ''.join(
        f"@font-face{{font-family:'Vazirmatn UI FD';font-style:normal;font-weight:{w};"
        f"font-display:swap;src:url(data:font/woff2;base64,{b}) format('woff2')}}"
        for w, b in sorted(fonts.items(), key=lambda x: int(x[0])))

    css = ''.join((HERE / f).read_text(encoding='utf-8') for f in
                  ['css_base.css', 'css_screens.css', 'css_site.css', 'css_admin.css'])

    intro = f'''<div class="sec" id="intro" style="padding-top:26px">
      <div class="card" style="border-color:var(--brand-200);overflow:hidden">
        <div class="card-b pad-lg" style="display:grid;grid-template-columns:1.4fr 1fr;gap:26px;align-items:start">
          <div>
            <span class="badge b-brand">{ico('layers')}مفهوم رابط کاربری — بر پایهٔ سند معماری پروژه</span>
            <h2 style="font-size:25px;margin:12px 0 10px">فروشگاه سلیم‌وند</h2>
            <p class="mut fs13" style="line-height:2.1">یک کانسپت بصری کامل برای دو محصول:
              <b style="color:var(--text)">سایت کاتالوگ عمومی</b> (بدون قیمت، بدون سبد خرید، هدایت به تماس)
              و <b style="color:var(--text)">پنل مدیریت</b> (کاتالوگ، انبار چندبرندی، فروش و فاکتور، گزارش‌ها).
              پالت پایه آبی تیره و سفید است و هر دو پوستهٔ روشن و تاریک در سراسر صفحات طراحی شده‌اند.</p>
            <div class="row" style="gap:8px;margin-top:16px;flex-wrap:wrap">
              <button class="btn btn-sm btn-p" data-view="site">{ico('home')}دیدن سایت</button>
              <button class="btn btn-sm btn-o" data-view="admin">{ico('grid')}دیدن پنل</button>
              <button class="btn btn-sm btn-ghost" data-view="ds">{ico('layers')}سیستم طراحی</button>
            </div>
          </div>
          <div class="col" style="gap:9px">
            <div class="kv"><span class="k">صفحه‌های طراحی‌شده</span><span class="v">۱۴ نما</span></div>
            <div class="kv"><span class="k">پوسته</span><span class="v">لایت + دارک (کلیهٔ صفحات)</span></div>
            <div class="kv"><span class="k">پالت‌های پیشنهادی</span><span class="v">۴ طیف آبی تیره</span></div>
            <div class="kv"><span class="k">فونت</span><span class="v">وزیرمتن (اعداد فارسی)</span></div>
            <div class="kv"><span class="k">جهت</span><span class="v">RTL کامل</span></div>
            <div class="kv"><span class="k">وضعیت</span><span class="v" style="color:var(--warn)">کانسپت — بدون پیاده‌سازی</span></div>
          </div>
        </div>
      </div>
    </div>'''

    panes = (f'<div data-viewpane="site">{view_site()}</div>'
             f'<div data-viewpane="admin" style="display:none">{view_admin()}</div>'
             f'<div data-viewpane="ds" style="display:none">{view_ds()}</div>')

    html = f'''<!DOCTYPE html>
<html lang="fa" dir="rtl" data-theme="light" data-palette="">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>فروشگاه سلیم‌وند — مفهوم رابط کاربری</title>
<style>{faces}</style>
<style>{css}</style>
</head>
<body>
{svg_defs()}
{topbar()}
<main class="shell">{intro}{panes}</main>
<footer style="text-align:center;padding:20px;color:var(--text-3);font-size:11.5px">
  مفهوم رابط کاربری فروشگاه سلیم‌وند — طراحی‌شده بر پایهٔ سند معماری پروژه · داده‌ها نمونه هستند
</footer>
<script>{JS}</script>
</body>
</html>'''

    out = HERE / 'selimvand-ui.html'
    out.write_text(html, encoding='utf-8')
    return out, len(html)


if __name__ == '__main__':
    p, n = build()
    print(f'{p} — {n:,} bytes')
