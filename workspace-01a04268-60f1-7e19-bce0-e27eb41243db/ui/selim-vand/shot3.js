const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1500, height: 950 } });
  await p.goto('file:///home/user/ui/selim-vand/selimvand-ui.html');
  await p.waitForTimeout(400);
  const out = '/home/user/ui/selim-vand/shots/';
  await p.click('[data-view="admin"]'); await p.waitForTimeout(300);
  // hide overlays to see underlying forms
  await p.addStyleTag({ content: '.modal-mask,.sheet{display:none!important}' });
  await p.evaluate(() => document.getElementById('a3').scrollIntoView());
  await p.waitForTimeout(150);
  await p.evaluate(() => window.scrollBy(0, 420));
  await p.screenshot({ path: out + '13-invform.png' });
  await p.evaluate(() => document.getElementById('a4').scrollIntoView());
  await p.waitForTimeout(150);
  await p.screenshot({ path: out + '14-product.png' });
  await p.evaluate(() => document.getElementById('a7').scrollIntoView());
  await p.waitForTimeout(150);
  await p.evaluate(() => window.scrollBy(0, 300));
  await p.screenshot({ path: out + '15-reports.png' });
  await p.evaluate(() => document.getElementById('a10').scrollIntoView());
  await p.waitForTimeout(150);
  await p.screenshot({ path: out + '16-mobile-admin.png' });
  // mobile site + dark dashboard for coverage
  await p.click('[data-view="site"]'); await p.waitForTimeout(250);
  await p.evaluate(() => document.getElementById('s2').scrollIntoView());
  await p.waitForTimeout(150);
  await p.screenshot({ path: out + '17-mobile-site.png' });
  await b.close();
  console.log('done');
})();
