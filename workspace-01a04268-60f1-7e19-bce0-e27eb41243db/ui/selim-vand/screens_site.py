# -*- coding: utf-8 -*-
"""Public site screens (catalog single page + online invoice) + mobile views."""

from icons import ico, part
from data import PRODUCTS, product_card, money, CATS

SHOP = dict(
    name='سلیم‌وند', tag='قطعات یدکی خودرو', phone='۰۹۱۲ ۳۴۵ ۶۷۸۹', phone2='۰۲۱-۳۳۹۸۷۶۵۴',
    addr='تهران، خیابان امام خمینی، پاساژ قطعات یدکی، طبقهٔ همکف، پلاک ۱۲',
    hours='شنبه تا پنجشنبه ۹:۰۰ تا ۲۰:۰۰ · جمعه تعطیل',
)

MAP = ('<svg class="roads" viewBox="0 0 400 260" fill="none" stroke="currentColor" stroke-width="1.4">'
       '<path d="M0 60h400M0 140h400M0 210h400M70 0v260M180 0v260M290 0v260"/>'
       '<path d="M0 100h400M120 0v260M240 0v260M350 0v260" opacity=".45"/>'
       '<path d="M0 60 400 210" opacity=".3"/></svg>')


# ============================================================ SITE HEADER
def site_header(active='کاتالوگ', with_theme=True, sticky_note=True):
    items = ['کاتالوگ قطعات', 'ویدئوی فروشگاه', 'تماس و آدرس']
    nav = ''.join(
        f'<a class="{"on" if i == active else ""}">{i}</a>' for i in items)
    theme = f'<button class="btn btn-sm btn-ghost btn-icon" data-theme-btn title="تغییر پوسته">{ico("moon")}</button>' if with_theme else ''
    return f'''<header class="s-hd">
      <div class="s-logo">
        <div class="logo"><span>س</span></div>
        <div><div class="n1">{SHOP['name']}</div><div class="n2">{SHOP['tag']}</div></div>
      </div>
      <nav class="s-nav">{nav}</nav>
      <div class="grow"></div>
      <div class="s-cta">
        {theme}
        <button class="btn btn-sm btn-soft">{ico('telegram')}تلگرام</button>
        <button class="btn btn-sm btn-p">{ico('phone')}<span class="mono">{SHOP['phone']}</span></button>
      </div>
    </header>'''


# ============================================================ SITE: HOME
def site_home(products=None, show_all=True):
    products = products or PRODUCTS
    grid = ''.join(product_card(p) for p in products)
    return f'''<div class="site">
  {site_header()}

  <!-- 1. HERO -->
  <section class="s-hero">
    <div class="s-hero-in">
      <div>
        <span class="badge b-brand" style="background:rgba(255,255,255,.12);color:#fff;margin-bottom:14px">
          {ico('shield')}۱۸ سال سابقهٔ تأمین قطعات یدکی
        </span>
        <h1>قطعهٔ ماشینت رو <em>پیدا کن</em>،<br>بقیه‌اش با ماست.</h1>
        <p class="lead">کاتالوگ زندهٔ قطعات یدکی پژو، سایپا، ایران‌خودرو و ... — با اعلام لحظه‌ای
          <b>موجود / ناموجود</b> و برندهای موجود در انبار. قیمت به‌صورت روزانه اعلام می‌شود.</p>
        <div class="hero-chips">
          <button>{ico('car')}پژو ۲۰۶</button><button>{ico('car')}پارس</button>
          <button>{ico('car')}پراید</button><button>{ico('car')}سمند</button>
          <button>{ico('car')}تیبا</button><button>{ico('car')}دنا</button>
        </div>
        <div class="hero-btns">
          <button class="btn btn-lg">{ico('search')}جست‌وجوی قطعه</button>
          <button class="btn btn-lg btn-o">{ico('phone')}تماس سریع</button>
          <button class="btn btn-lg btn-o">{ico('telegram')}استعلام در تلگرام</button>
        </div>
        <div class="price-note">{ico('alert')}
          <span><b>بدون قیمت در سایت:</b> به‌دلیل نوسان روزانهٔ بازار، قیمت فقط با استعلام تلفنی یا پیام‌رسان اعلام می‌شود.</span>
        </div>
      </div>
      <aside class="hero-card">
        <div class="hs"><span class="ic">{ico('clock')}</span><div><b>ارسال و تحویل همان روز</b><span>برای سفارش‌های قبل از ساعت ۱۶</span></div></div>
        <div class="hs"><span class="ic">{ico('layers')}</span><div><b>۱۲,۴۸۰ قلم موجودی فعال</b><span>در ۸ دسته‌بندی و ۴۲ برند</span></div></div>
        <div class="hs"><span class="ic">{ico('shield')}</span><div><b>ضمانت اصالت قطعه</b><span>فقط برندهای تأییدشده و گارانتی‌دار</span></div></div>
        <div class="hs"><span class="ic">{ico('map')}</span><div><b>ارسال به شهرستان</b><span>باربری / تیپاکس / پست پیشتاز</span></div></div>
      </aside>
    </div>
  </section>

  <!-- 2. VIDEO (آپارات — lazy) -->
  <section class="s-vid">
    <div class="s-vid-in">
      <div>
        <div class="vid-thumb">
          <span class="lines"></span>
          <span class="lazy"><span>{ico('play')} فقط با کلیک کاربر بارگذاری می‌شود — iframe آپارات</span></span>
          <button class="vid-play">{ico('play')}</button>
          <div class="ph">{ico('camera')}<span>ویدئوی معرفی فروشگاه و انبار — میزبانی روی آپارات (بدون مصرف دیسک سرور)</span></div>
        </div>
      </div>
      <div>
        <span class="badge b-brand">{ico('star')}فروشگاه ما را ببینید</span>
        <h3 style="font-size:19px;margin:10px 0 8px">قبل از خرید، انبار را از نزدیک ببینید</h3>
        <p class="mut fs13" style="line-height:2">ویدئوی کوتاه از قفسه‌بندی انبار، بسته‌بندی و نحوهٔ ارسال.
          اعتماد، اولین قطعهٔ یدکی است.</p>
        <div class="row" style="margin-top:14px;gap:8px">
          <button class="btn btn-sm btn-o">{ico('play')}پخش ویدئو</button>
          <span class="fs11 mut3">۱:۴۲ دقیقه</span>
        </div>
      </div>
    </div>
  </section>

  <!-- 3. CATALOG -->
  <section class="s-cat" id="catalog">
    <div class="s-cat-in">
      <div class="page-h" style="margin:26px 0 12px">
        <h2 style="font-size:20px">کاتالوگ قطعات</h2>
        <span class="badge b-line">{ico('box')}۱۲۴ نتیجه</span>
        <span class="grow"></span>
        <span class="fs11 mut3">وضعیت فیلترها در آدرس صفحه ذخیره می‌شود و قابل اشتراک است</span>
      </div>

      <div class="filt">
        <div class="filt-top">
          <div class="search grow" style="max-width:340px">{ico('search')}
            <input class="inp" placeholder="نام قطعه یا شماره فنی را بنویسید…"></div>
          <div class="field"><span class="lab">برند خودرو</span>
            <div class="selwrap filt-sel">{ico('chevron')}<select class="inp inp-s sel"><option>پژو</option><option>سایپا</option></select></div></div>
          <div class="field"><span class="lab">مدل</span>
            <div class="selwrap filt-sel">{ico('chevron')}<select class="inp inp-s sel"><option>۲۰۶</option><option>پارس</option></select></div></div>
          <div class="field"><span class="lab">تیپ / موتور</span>
            <div class="selwrap filt-sel">{ico('chevron')}<select class="inp inp-s sel"><option>تیپ ۵</option><option>همهٔ تیپ‌ها</option></select></div></div>
          <div class="field"><span class="lab">دسته‌بندی</span>
            <div class="selwrap filt-sel">{ico('chevron')}<select class="inp inp-s sel"><option>ترمز › لنت</option><option>همهٔ دسته‌ها</option></select></div></div>
          <div class="field"><span class="lab">&nbsp;</span>
            <button class="btn btn-sm btn-p">{ico('check')}فقط موجود</button></div>
          <div class="field"><span class="lab">&nbsp;</span>
            <button class="btn btn-sm btn-ghost">{ico('x')}پاک کردن</button></div>
        </div>
        <div class="tree">
          <span class="node">{ico('folder')}ترمز</span><span class="sep">›</span>
          <span class="node on">{ico('check')}لنت</span><span class="sep">·</span>
          <span class="node">دیسک</span><span class="node">کاسه‌چرخ</span><span class="node">لوازم ترمز</span>
          <span class="sep" style="margin-inline-start:auto"></span>
          <span class="fs11 mut3">دسته‌بندی درختی — از <span class="en">/public/filters</span></span>
        </div>
        <div class="filt-tags">
          <span class="ftag">{ico('car')}پژو ۲۰۶ · تیپ ۵ {ico('x')}</span>
          <span class="ftag">{ico('folder')}ترمز › لنت {ico('x')}</span>
          <span class="ftag">{ico('check')}فقط موجود {ico('x')}</span>
          <span class="ftag" style="background:transparent;color:var(--text-3)">
            {ico('link')} <span class="en" style="font-size:10px">/?vehicle=peugeot-206-t5&amp;cat=brake-pads&amp;inStock=1</span></span>
        </div>
      </div>

      <div class="grid-p">{grid}</div>

      <div class="pager">
        <button class="btn btn-sm btn-ghost">{ico('chevronL')}قبلی</button>
        <span>اسکرول بی‌نهایت — ۲۴ قلم از ۱۲۴ بارگذاری شد</span>
        <div class="prog" style="width:120px"><i style="width:19%"></i></div>
      </div>
    </div>
  </section>

  <!-- 4. CONTACT -->
  <section class="s-contact" id="contact">
    <div class="s-contact-in">
      <div>
        <span class="badge b-brand">{ico('phone')}تماس و آدرس</span>
        <h3 style="font-size:19px;margin:10px 0 4px">استعلام قیمت و سفارش</h3>
        <p class="mut fs13">کد قطعه یا نام آن را بگویید؛ موجودی و قیمت روز را فوراً اعلام می‌کنیم.</p>
        <div class="info-list" style="margin-top:8px">
          <div class="it"><span class="ic">{ico('phone')}</span><div><b>تلفن تماس</b>
            <span class="mono" style="direction:ltr">{SHOP['phone2']}</span> · <span class="mono" style="direction:ltr">{SHOP['phone']}</span></span></div></div>
          <div class="it"><span class="ic">{ico('map')}</span><div><b>آدرس فروشگاه</b><span>{SHOP['addr']}</span></div></div>
          <div class="it"><span class="ic">{ico('clock')}</span><div><b>ساعات کاری</b><span>{SHOP['hours']}</span></div></div>
          <div class="it"><span class="ic">{ico('truck')}</span><div><b>ارسال شهرستان</b><span>باربری و پست پیشتاز — بسته‌بندی ضدضربه</span></div></div>
        </div>
        <div class="row" style="margin-top:14px;gap:8px">
          <button class="btn btn-sm btn-p">{ico('telegram')}تلگرام</button>
          <button class="btn btn-sm btn-o">{ico('bale')}بله</button>
          <button class="btn btn-sm btn-ghost">{ico('link')}کپی آدرس</button>
        </div>
        <div class="price-note" style="background:var(--warn-soft);color:var(--warn);margin-top:16px">
          {ico('alert')}<span>قیمت‌ها روزانه تغییر می‌کنند؛ مبلغ نهایی هنگام صدور فاکتور قطعی می‌شود.</span></div>
      </div>
      <div class="map">
        {MAP}
        <span class="pin">{ico('map')}</span>
        <div class="card-tag">
          <span class="thumb" style="width:34px;height:34px">{ico('map')}</span>
          <div class="wrap"><div class="b fs12">{SHOP['name']} — {SHOP['tag']}</div>
            <div class="fs11 mut3">مسیر یابی · نمایش در نقشه</div></div>
          <button class="btn btn-sm btn-ghost">{ico('link')}</button>
        </div>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="s-ft">
    <div class="s-ft-in">
      <div class="row" style="gap:10px">
        <div class="logo" style="background:#fff;color:var(--brand-900)"><span>س</span></div>
        <div><b style="font-size:14px">{SHOP['name']}</b><small>قطعات یدکی خودرو — تأمین، مشاورهٔ فنی و ارسال</small></div>
      </div>
      <div class="soc">
        <button>{ico('telegram')}</button><button>{ico('bale')}</button>
        <button>{ico('play')}</button><button>{ico('phone')}</button>
      </div>
      <div style="text-align:end">
        <span class="fs12" style="color:rgba(255,255,255,.6)">قیمت فقط با استعلام</span>
        <small>© ۱۴۰۵ کلیهٔ حقوق محفوظ است</small>
      </div>
    </div>
  </footer>
</div>'''


# ============================================================ MOBILE SITE
def site_mobile():
    ps = PRODUCTS[:2]
    grid = ''.join(product_card(p, compact=True) for p in ps)
    return f'''<div class="site">
  <header class="s-hd" style="padding:10px 14px;gap:10px">
    <div class="s-logo"><div class="logo" style="width:34px;height:34px"><span>س</span></div>
      <div><div class="n1" style="font-size:13.5px">{SHOP['name']}</div></div></div>
    <div class="grow"></div>
    <button class="btn btn-sm btn-ghost btn-icon" data-theme-btn>{ico('moon')}</button>
    <button class="btn btn-sm btn-ghost btn-icon">{ico('menu')}</button>
  </header>

  <section class="s-hero" style="padding:30px 16px 28px">
    <div class="s-hero-in" style="grid-template-columns:1fr;gap:16px">
      <div>
        <h1 style="font-size:24px">قطعهٔ ماشینت رو <em>پیدا کن</em>،<br>بقیه‌اش با ماست.</h1>
        <p class="lead" style="font-size:13px">موجودی لحظه‌ای و برندهای موجود در انبار.</p>
        <div class="hero-chips">
          <button>{ico('car')}۲۰۶</button><button>{ico('car')}پارس</button>
          <button>{ico('car')}پراید</button><button>{ico('car')}سمند</button>
        </div>
        <div class="hero-btns" style="margin-top:18px">
          <button class="btn btn-block btn-lg">{ico('phone')}تماس سریع</button>
          <button class="btn btn-block btn-lg btn-o">{ico('telegram')}تلگرام</button>
        </div>
      </div>
    </div>
  </section>

  <div style="padding:14px;background:var(--bg)">
    <div class="filt" style="position:static;padding:11px 12px">
      <div class="search search-sm">{ico('search')}<input class="inp" placeholder="نام قطعه یا شماره فنی…"></div>
      <div class="row" style="gap:7px;margin-top:10px">
        <div class="selwrap grow">{ico('chevron')}<select class="inp inp-s sel"><option>پژو ۲۰۶ · تیپ ۵</option></select></div>
        <div class="selwrap grow">{ico('chevron')}<select class="inp inp-s sel"><option>ترمز › لنت</option></select></div>
        <button class="btn btn-sm btn-p btn-icon" style="width:34px;height:34px">{ico('filter')}</button>
      </div>
      <div class="filt-tags" style="margin-top:9px">
        <span class="ftag">{ico('check')}فقط موجود</span><span class="badge b-line">۲۴ نتیجه</span>
      </div>
    </div>
    <div class="grid-p" style="grid-template-columns:1fr">{grid}</div>
    <div class="pager"><span>۲ از ۲۴ بارگذاری شد</span></div>
  </div>

  <div style="position:sticky;bottom:0;background:var(--surface);border-top:1px solid var(--border);
    display:flex;padding:9px 12px;gap:8px;z-index:20">
    <button class="btn btn-p btn-sm grow">{ico('phone')}تماس</button>
    <button class="btn btn-soft btn-sm grow">{ico('telegram')}تلگرام</button>
    <button class="btn btn-o btn-sm grow">{ico('bale')}بله</button>
  </div>
</div>'''


# ============================================================ INVOICE
def invoice_page():
    items = [
        dict(n='لنت ترمز جلو پژو ۲۰۶', b='ایساکو', q=2, p=18500000, d=0),
        dict(n='فیلتر روغن پراید و تیبا', b='بوش', q=1, p=4200000, d=0),
        dict(n='کمک فنر عقب پژو پارس', b='مونرو', q=2, p=96000000, d=3000000),
    ]
    rows = ''
    sub = 0
    for i, it in enumerate(items, 1):
        tot = it['q'] * it['p'] - it['d']
        sub += tot
        disc = f'<span class="fs11" style="color:var(--danger)">−{money(it["d"])}</span>' if it['d'] else '—'
        rows += f'''<tr>
          <td class="mut3">{i}</td>
          <td><div class="b fs13">{it['n']}</div><div class="fs11 mut3">BRK-00452</div></td>
          <td><span class="badge b-line">{it['b']}</span></td>
          <td class="num">{money(it['q'])}</td>
          <td class="num">{money(it['p'])}</td>
          <td class="num">{disc}</td>
          <td class="num b">{money(tot)}</td>
        </tr>'''
    discount = 1500000
    total = sub - discount
    paid = 150000000
    debt = total - paid
    return f'''<div class="inv">
  <header class="inv-hd">
    <div class="row" style="gap:10px">
      <div class="logo" style="width:34px;height:34px;background:#fff;color:var(--brand-900)"><span>س</span></div>
      <div><b style="font-size:14px">{SHOP['name']}</b><div style="font-size:10.5px;color:rgba(255,255,255,.55)">فاکتور فروش آنلاین</div></div>
    </div>
    <div class="row" style="gap:7px">
      <button class="btn btn-sm btn-o" style="border-color:rgba(255,255,255,.3);color:#fff">{ico('print')}چاپ</button>
      <button class="btn btn-sm" style="background:#fff;color:var(--brand-900)">{ico('download')}دانلود PDF</button>
    </div>
  </header>
  <div class="inv-w">
    <div class="inv-top">
      <div>
        <span class="badge b-brand">{ico('file')}فاکتور شمارهٔ <b class="mono">۱۴۰۵/۰۰۳۴۷</b></span>
        <div class="inv-meta">
          <div><span>تاریخ صدور</span><b class="mono">۱۴۰۵/۰۶/۰۳ — ۱۴:۲۲</b></div>
          <div><span>مشتری</span><b>علی محمدی</b></div>
          <div><span>فروشنده</span><b>م. سلیمانی</b></div>
          <div><span>خودرو</span><b>پژو ۲۰۶ تیپ ۵</b></div>
          <div><span>شمارهٔ تماس</span><b class="mono" style="direction:ltr">09123456789</b></div>
          <div><span>اعتبار لینک</span><b>۳۰ روز</b></div>
        </div>
      </div>
      <div class="inv-st">
        <span class="badge b-warn">{ico('clock')}پرداخت بخشی</span>
        <div class="qrbox">{ico('qr')}</div>
        <span class="fs11 mut3">اسکن برای مشاهدهٔ فاکتور</span>
      </div>
    </div>

    <div class="card" style="margin-top:14px;overflow:hidden">
      <div class="card-h"><h3>اقلام فاکتور</h3><span class="grow"></span>
        <span class="badge b-line">{ico('box')}۵ قلم</span></div>
      <table class="tbl">
        <thead><tr><th>#</th><th>شرح کالا</th><th>برند</th><th class="num">تعداد</th>
          <th class="num">فی (ریال)</th><th class="num">تخفیف</th><th class="num">جمع (ریال)</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>

    <div style="display:grid;grid-template-columns:1fr 300px;gap:14px;margin-top:14px;align-items:start">
      <div>
        <div class="pay-row">
          <div class="pay"><div class="m">{ico('money')}پرداخت نقدی</div><b class="mono">{money(60000000)} ریال</b>
            <div class="fs11 mut3">حضوری — ۱۴:۲۲</div></div>
          <div class="pay"><div class="m">{ico('money')}کارت‌خوان</div><b class="mono">{money(90000000)} ریال</b>
            <div class="fs11 mut3">رسید ۸۸۴۲۱۳ — ۱۴:۲۵</div></div>
        </div>
        <div class="debt-note">{ico('alert')}<span>باقی‌ماندهٔ این فاکتور به‌عنوان بدهی در حساب شما ثبت شده و
          در فاکتور بعدی قابل تسویه است. برای پرداخت، با فروشگاه تماس بگیرید.</span></div>
        <div class="card" style="margin-top:12px">
          <div class="card-b fs12 mut" style="line-height:2.1">
            <b class="b" style="color:var(--text)">شرایط:</b> کالا تا ۴۸ ساعت با ارائهٔ این فاکتور قابل تعویض است
            (به‌جز قطعات برقی و مصرفی). نصب توسط مشتری به‌منزلهٔ تأیید سلامت قطعه است.
          </div>
        </div>
      </div>
      <div class="inv-tot">
        <div class="ln"><span>جمع اقلام</span><b class="mono">{money(sub)}</b></div>
        <div class="ln"><span>تخفیف فاکتور</span><b class="mono">−{money(discount)}</b></div>
        <div class="ln big"><span>مبلغ قابل پرداخت</span><b class="mono">{money(total)}</b></div>
        <div class="ln paid"><span>پرداخت‌شده</span><b class="mono">{money(paid)}</b></div>
        <div class="ln debt"><span>باقی‌مانده (بدهی)</span><b class="mono">{money(debt)}</b></div>
      </div>
    </div>

    <div class="row" style="gap:9px;margin-top:16px;flex-wrap:wrap">
      <button class="btn btn-p btn-sm">{ico('download')}دانلود PDF</button>
      <button class="btn btn-o btn-sm">{ico('print')}چاپ</button>
      <button class="btn btn-ghost btn-sm">{ico('link')}کپی لینک فاکتور</button>
      <span class="grow"></span>
      <span class="fs11 mut3">این صفحه با توکن امن یک‌بارمصرف نمایش داده می‌شود · <span class="en">/invoice/9f2c…b71e</span></span>
    </div>
  </div>
</div>'''


def invoice_mobile():
    return f'''<div class="inv">
  <header class="inv-hd" style="padding:12px 14px">
    <div class="row" style="gap:8px"><div class="logo" style="width:30px;height:30px;background:#fff;color:var(--brand-900)"><span>س</span></div>
      <b style="font-size:13px">{SHOP['name']}</b></div>
    <button class="btn btn-sm" style="background:#fff;color:var(--brand-900);height:30px">{ico('download')}PDF</button>
  </header>
  <div class="inv-w" style="padding:0 12px">
    <div class="inv-top" style="grid-template-columns:1fr;padding:14px;margin-top:-20px">
      <div>
        <span class="badge b-brand">{ico('file')}فاکتور <b class="mono">۱۴۰۵/۰۰۳۴۷</b></span>
        <div class="row" style="gap:8px;margin-top:10px"><span class="badge b-warn">{ico('clock')}پرداخت بخشی</span>
          <span class="fs11 mut3 mono">۱۴۰۵/۰۶/۰۳</span></div>
        <div class="inv-meta" style="grid-template-columns:1fr 1fr;gap:9px">
          <div><span>مشتری</span><b>علی محمدی</b></div>
          <div><span>خودرو</span><b>پژو ۲۰۶ تیپ ۵</b></div>
        </div>
      </div>
    </div>
    <div class="card" style="margin-top:12px;overflow:hidden">
      <div class="card-h" style="padding:11px 13px"><h3 style="font-size:13px">اقلام</h3>
        <span class="grow"></span><span class="badge b-line">۵ قلم</span></div>
      <div style="padding:4px 13px">
        <div class="list-row"><span class="thumb">{part('brake-pad')}</span>
          <div class="wrap"><div class="nm">لنت ترمز جلو ۲۰۶</div>
            <div class="sub">ایساکو · ۲ عدد · ۱۸,۵۰۰,۰۰۰</div></div>
          <div class="val b fs12 mono">۳۷,۰۰۰,۰۰۰</div></div>
        <div class="list-row"><span class="thumb">{part('oil-filter')}</span>
          <div class="wrap"><div class="nm">فیلتر روغن پراید</div>
            <div class="sub">بوش · ۱ عدد · ۴,۲۰۰,۰۰۰</div></div>
          <div class="val b fs12 mono">۴,۲۰۰,۰۰۰</div></div>
        <div class="list-row"><span class="thumb">{part('shock')}</span>
          <div class="wrap"><div class="nm">کمک فنر عقب پارس</div>
            <div class="sub">مونرو · ۲ عدد · تخفیف ۳,۰۰۰,۰۰۰</div></div>
          <div class="val b fs12 mono">۱۸۹,۰۰۰,۰۰۰</div></div>
      </div>
    </div>
    <div class="inv-tot" style="margin-top:12px">
      <div class="ln"><span>جمع اقلام</span><b class="mono">۲۳۰,۲۰۰,۰۰۰</b></div>
      <div class="ln"><span>تخفیف</span><b class="mono">−۱,۵۰۰,۰۰۰</b></div>
      <div class="ln big"><span>قابل پرداخت</span><b class="mono">۲۲۸,۷۰۰,۰۰۰</b></div>
      <div class="ln paid"><span>پرداخت‌شده</span><b class="mono">۱۵۰,۰۰۰,۰۰۰</b></div>
      <div class="ln debt"><span>باقی‌مانده</span><b class="mono">۷۸,۷۰۰,۰۰۰</b></div>
    </div>
    <div class="row" style="gap:8px;margin-top:12px">
      <button class="btn btn-p btn-sm grow">{ico('print')}چاپ</button>
      <button class="btn btn-o btn-sm grow">{ico('phone')}تماس با فروشگاه</button>
    </div>
    <p class="fs11 mut3 c" style="margin:12px 0 16px">نمایش موبایلی — لینک پیامک‌شده به مشتری</p>
  </div>
</div>'''
