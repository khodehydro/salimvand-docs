const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1500, height: 1000 }, deviceScaleFactor: 1 });
  const msgs = [];
  p.on('console', m => { if (m.type() === 'error') msgs.push(m.text()); });
  p.on('pageerror', e => msgs.push('pageerror: ' + e.message));
  await p.goto('file:///home/user/ui/selim-vand/selimvand-ui.html');
  await p.waitForTimeout(600);
  const out = '/home/user/ui/selim-vand/shots';
  await p.screenshot({ path: out + '/01-site-light.png' });

  await p.click('[data-theme-btn]');           // dark
  await p.waitForTimeout(300);
  await p.screenshot({ path: out + '/02-site-dark.png' });

  await p.click('[data-view="admin"]');        // admin view
  await p.waitForTimeout(400);
  await p.screenshot({ path: out + '/03-admin-dark.png' });

  await p.click('[data-theme-btn]');           // back to light
  await p.waitForTimeout(300);
  await p.click('[data-view="ds"]');
  await p.waitForTimeout(400);
  await p.screenshot({ path: out + '/04-ds-light.png' });

  // layout health checks
  const checks = await p.evaluate(() => {
    const r = {};
    r.hOverflow = document.documentElement.scrollWidth > window.innerWidth + 2;
    const fonts = [...document.querySelectorAll('*')].some(e => getComputedStyle(e).fontFamily.includes('Vazirmatn'));
    r.fontApplied = fonts;
    const f = document.querySelector('.pcard');
    r.cardW = Math.round(f.getBoundingClientRect().width);
    r.cardH = Math.round(f.getBoundingClientRect().height);
    r.frames = document.querySelectorAll('.frame').length;
    return r;
  });
  console.log(JSON.stringify(checks));
  console.log('console errors:', msgs.length ? msgs : 'none');
  await b.close();
})();
