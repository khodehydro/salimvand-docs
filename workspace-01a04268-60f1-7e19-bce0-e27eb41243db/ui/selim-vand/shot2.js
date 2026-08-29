const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1500, height: 950 } });
  const msgs = [];
  p.on('pageerror', e => msgs.push(e.message));
  await p.goto('file:///home/user/ui/selim-vand/selimvand-ui.html');
  await p.waitForTimeout(500);
  const out = '/home/user/ui/selim-vand/shots/';
  // catalog grid closeup
  await p.evaluate(() => document.getElementById('s1').scrollIntoView());
  await p.waitForTimeout(200);
  await p.evaluate(() => window.scrollBy(0, 1300));
  await p.waitForTimeout(200);
  await p.screenshot({ path: out + '05-catalog-grid.png' });

  // contact + footer
  await p.evaluate(() => document.querySelector('.s-contact').scrollIntoView());
  await p.waitForTimeout(200);
  await p.screenshot({ path: out + '06-contact.png' });

  // admin dashboard (light)
  await p.click('[data-view="admin"]'); await p.waitForTimeout(300);
  await p.evaluate(() => document.getElementById('a2').scrollIntoView());
  await p.waitForTimeout(200);
  await p.screenshot({ path: out + '07-dash-light.png' });
  await p.evaluate(() => window.scrollBy(0, 900));
  await p.waitForTimeout(150);
  await p.screenshot({ path: out + '08-dash-light-2.png' });

  // invoice create
  await p.evaluate(() => document.getElementById('a3').scrollIntoView());
  await p.waitForTimeout(200);
  await p.screenshot({ path: out + '09-invoice-create.png' });

  // inventory with sheet
  await p.evaluate(() => document.getElementById('a5').scrollIntoView());
  await p.waitForTimeout(200);
  await p.screenshot({ path: out + '10-inventory.png' });

  // palette
  await p.evaluate(() => document.getElementById('a9').scrollIntoView());
  await p.waitForTimeout(200);
  await p.screenshot({ path: out + '11-palette.png' });

  // invoice public page
  await p.click('[data-view="site"]'); await p.waitForTimeout(300);
  await p.evaluate(() => document.getElementById('s3').scrollIntoView());
  await p.waitForTimeout(200);
  await p.screenshot({ path: out + '12-invoice-public.png' });

  console.log('errors:', msgs.length ? msgs : 'none');
  await b.close();
})();
