// تست‌های صحت برچسب — اجرا:  npm i jsdom && node verify_labels.js
const fs=require('fs');const {JSDOM}=require('jsdom');
const html=fs.readFileSync(require('path').join(__dirname,'product-labels.html'),'utf8');
const dom=new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true});
const d=dom.window.document;
const t=[];const ok=(n,c)=>t.push([c?'PASS':'FAIL',n]);
const lbs=d.querySelectorAll('#preview .lb');
ok('یک برچسب رندر شد',lbs.length===1);
const lb=lbs[0];
ok('نام فروشگاه',lb.textContent.includes('فروشگاه سلیم‌وند'));
ok('سایت روی برچسب',lb.querySelector('.lb-h .url').textContent==='salimvand.ir');
ok('نام محصول',lb.querySelector('.lb-name').textContent.includes('لنت ترمز'));
ok('SKU',lb.textContent.includes('BRK-00452'));
const dig=lb.querySelector('.lb-digits').textContent.replace(/\s/g,'');
ok('۱۳ رقم بارکد ('+dig+')',/^\d{13}$/.test(dig));
// checksum
const cd=(b)=>{let s=0;for(let i=0;i<12;i++)s+=(+b[i])*(i%2?3:1);return String((10-s%10)%10)};
ok('رقم کنترلی صحیح',dig[12]===cd(dig.slice(0,12)));
ok('پیشوند ایران ۶۲۶',dig.startsWith('626'));
const rects=lb.querySelectorAll('.lb-bc svg rect');
ok('خطوط بارکد رسم شد ('+rects.length+' میله)',rects.length>25);
const vb=lb.querySelector('.lb-bc svg').getAttribute('viewBox');
ok('عرض EAN-13 = ۹۵ ماژول ('+vb+')',vb.split(' ')[2]==='95');
ok('سه اندازه',d.querySelectorAll('#allSizes .lb').length===3);
ok('سه سبک',d.querySelectorAll('#allStyles .lb').length===3);
ok('برگهٔ چاپ ۲۴ تایی',d.querySelectorAll('#sheet .lb').length===24);
// code128
const btn=[...d.querySelectorAll('#typeSeg button')].find(b=>b.dataset.v==='code128');btn.click();
const l2=d.querySelector('#preview .lb');
ok('Code128 رقم/متن',l2.querySelector('.lb-digits').textContent==='BRK-00452');
ok('Code128 میله دارد',l2.querySelectorAll('.lb-bc svg rect').length>20);
const w=+l2.querySelector('.lb-bc svg').getAttribute('viewBox').split(' ')[2];
ok('عرض Code128 = 11*(1+9+1)+13 = 134 ('+w+')',w===134);
ok('فونت جاسازی شده',html.includes('data:font/woff2;base64'));
console.log(t.map(([s,n])=>`${s==='PASS'?'✓':'✗'} ${n}`).join('\n'));
console.log('\n'+t.filter(x=>x[0]==='PASS').length+'/'+t.length+' passed');
