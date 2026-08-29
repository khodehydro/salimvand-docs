const fs = require('fs');
const { JSDOM } = require('jsdom');

const html = fs.readFileSync('/home/user/ui/selim-vand/selimvand-ui.html', 'utf8');
const errs = [];
const dom = new JSDOM(html, { runScripts: 'dangerously', pretendToBeVisual: true });
dom.window.addEventListener('error', e => errs.push('window.error: ' + e.message));
dom.virtualConsole.on('jsdomError', e => errs.push('jsdomError: ' + e.message));
const d = dom.window.document;
const ok = [];
const fail = [];
function t(name, cond, extra='') { (cond ? ok : fail).push(name + (extra ? ' → ' + extra : '')); }

const root = d.documentElement;
// 1. initial state set by the inline IIFE
t('پوستهٔ اولیه = لایت', root.getAttribute('data-theme') === 'light', root.getAttribute('data-theme'));
t('برچسب اولیهٔ دکمه', /دارک/.test(d.querySelector('[data-theme-label]').textContent), d.querySelector('[data-theme-label]').textContent.trim());
t('آیکون اولیه = moon', d.querySelector('[data-theme-btn] svg use').getAttribute('href') === '#i-moon');

// 2. theme toggle (topbar)
d.querySelector('.topbar [data-theme-btn]').click();
t('کلیک → دارک', root.getAttribute('data-theme') === 'dark', root.getAttribute('data-theme'));
t('برچسب → لایت مود', /لایت/.test(d.querySelector('[data-theme-label]').textContent));
t('آیکون → sun', d.querySelector('[data-theme-btn] svg use').getAttribute('href') === '#i-sun');
// every theme button in the mockups must flip too
d.querySelector('.adm-top [data-theme-btn]').click();
t('دکمهٔ داخل پنل هم کار می‌کند → لایت', root.getAttribute('data-theme') === 'light', root.getAttribute('data-theme'));

// 3. palette switch
const pal = d.querySelector('[data-pal="petrol"]');
pal.click();
t('پالت → petrol', root.getAttribute('data-palette') === 'petrol', root.getAttribute('data-palette'));
t('کلاس on جابه‌جا شد', pal.classList.contains('on') && !d.querySelector('[data-pal=""]').classList.contains('on'));

// 4. view switching
const panes = [...d.querySelectorAll('[data-viewpane]')];
t('سه نما وجود دارد', panes.length === 3, String(panes.length));
d.querySelector('[data-view="admin"]').click();
t('نمای پنل فعال شد', panes.find(p => p.getAttribute('data-viewpane') === 'admin').style.display === 'block');
t('نمای سایت پنهان شد', panes.find(p => p.getAttribute('data-viewpane') === 'site').style.display === 'none');
d.querySelector('[data-view="ds"]').click();
t('نمای سیستم طراحی فعال شد', panes.find(p => p.getAttribute('data-viewpane') === 'ds').style.display === 'block');
d.querySelector('[data-view="site"]').click();
t('بازگشت به سایت', panes.find(p => p.getAttribute('data-viewpane') === 'site').style.display === 'block');

// 5. component toggles (switch / checkbox / segmented)
const sw = d.querySelector('.sw'); const wasSw = sw.classList.contains('on');
sw.click();
t('سوییچ تغییر وضعیت داد', sw.classList.contains('on') !== wasSw);
const ck = d.querySelector('.chk'); const wasCk = ck.classList.contains('on');
ck.click();
t('چک‌باکس تغییر وضعیت داد', ck.classList.contains('on') !== wasCk);
const segBtns = d.querySelectorAll('.seg button');
segBtns[2].click();
t('تب بخشی فعال شد', segBtns[2].classList.contains('on') && !segBtns[0].classList.contains('on'));

// 6. content sanity
t('کارت محصول ≥ ۱۲', d.querySelectorAll('.pcard').length >= 12, String(d.querySelectorAll('.pcard').length));
t('فریم‌های نمایش = ۱۴', d.querySelectorAll('.frame').length === 14, String(d.querySelectorAll('.frame').length));
t('نمودار میله‌ای رندر شد', d.querySelectorAll('.bars .bcol').length > 10, String(d.querySelectorAll('.bars .bcol').length));
t('دونات SVG رندر شد', d.querySelectorAll('.donut svg circle').length >= 5, String(d.querySelectorAll('.donut svg circle').length));
t('فونت جاسازی‌شده', /@font-face/.test(html) && html.includes('data:font/woff2;base64,'));
t('بدون منبع خارجی', !/(src|href)="https?:\/\//.test(html.replace(/href="#/g, 'href="#')));

console.log('PASS:'); ok.forEach(x => console.log('  ✓ ' + x));
if (fail.length) { console.log('FAIL:'); fail.forEach(x => console.log('  ✗ ' + x)); }
if (errs.length) { console.log('JS ERRORS:'); errs.forEach(x => console.log('  ! ' + x)); }
console.log('\n' + ok.length + ' passed, ' + fail.length + ' failed, ' + errs.length + ' js errors');
process.exit(fail.length || errs.length ? 1 : 0);
