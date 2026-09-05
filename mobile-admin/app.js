(() => {
  const root = document.documentElement;
  const main = document.getElementById('mainContent');
  const pages = [...document.querySelectorAll('.page')];
  const navItems = [...document.querySelectorAll('.bottom-nav [data-page-target]')];
  const overlays = [...document.querySelectorAll('[data-overlay]')];
  const toast = document.getElementById('toast');
  const toastText = document.getElementById('toastText');
  let toastTimer;
  let currentPage = 'home';
  let stockFilter = 'all';
  let productCategory = 'all';

  const pageNames = {
    home: 'داشبورد',
    sales: 'فروش',
    inventory: 'انبار',
    products: 'محصولات',
    more: 'بیشتر'
  };

  function setTheme(theme) {
    root.dataset.theme = theme;
    try { localStorage.setItem('salimvand-mobile-theme', theme); } catch (error) { /* private mode */ }
    document.querySelectorAll('[data-theme-icon] use').forEach((icon) => {
      icon.setAttribute('href', theme === 'dark' ? '#i-sun' : '#i-moon');
    });
    document.querySelectorAll('[data-theme-text]').forEach((text) => {
      text.textContent = theme === 'dark' ? 'حالت تاریک' : 'حالت روشن';
    });
    document.querySelector('meta[name="theme-color"]')?.setAttribute('content', theme === 'dark' ? '#050b14' : '#071c30');
  }

  function loadTheme() {
    let saved = '';
    try { saved = localStorage.getItem('salimvand-mobile-theme') || ''; } catch (error) { /* private mode */ }
    setTheme(saved === 'dark' ? 'dark' : 'light');
  }

  function openSheet(id) {
    const sheet = document.getElementById(id);
    if (!sheet) return;
    overlays.forEach((overlay) => { overlay.hidden = true; });
    sheet.hidden = false;
    document.body.style.overflow = 'hidden';
    const focusable = sheet.querySelector('input, button');
    if (focusable && focusable.tagName === 'INPUT') {
      window.setTimeout(() => focusable.focus(), 120);
    }
  }

  function closeSheets() {
    overlays.forEach((overlay) => { overlay.hidden = true; });
    document.body.style.overflow = '';
  }

  function navigate(page) {
    if (!page || !pageNames[page]) return;
    currentPage = page;
    pages.forEach((section) => section.classList.toggle('active', section.dataset.page === page));
    navItems.forEach((item) => item.classList.toggle('active', item.dataset.pageTarget === page));
    closeSheets();
    if (main) main.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function showToast(message) {
    if (!toast || !toastText) return;
    toastText.textContent = message;
    toast.hidden = false;
    window.clearTimeout(toastTimer);
    toastTimer = window.setTimeout(() => { toast.hidden = true; }, 3300);
  }

  function hideToast() {
    if (toast) toast.hidden = true;
    window.clearTimeout(toastTimer);
  }

  function renderInventory() {
    const query = (document.querySelector('[data-inventory-search]')?.value || '').trim().toLocaleLowerCase('fa');
    const items = [...document.querySelectorAll('.inventory-item')];
    let visible = 0;
    items.forEach((item) => {
      const matchesFilter = stockFilter === 'all' || item.dataset.stock === stockFilter;
      const matchesSearch = !query || item.dataset.search.toLocaleLowerCase('fa').includes(query);
      const shouldShow = matchesFilter && matchesSearch;
      item.classList.toggle('is-hidden', !shouldShow);
      if (shouldShow) visible += 1;
    });
    document.getElementById('inventoryEmpty')?.classList.toggle('visible', visible === 0);
  }

  function renderProducts() {
    const query = (document.querySelector('[data-product-search]')?.value || '').trim().toLocaleLowerCase('fa');
    const cards = [...document.querySelectorAll('.product-card')];
    let visible = 0;
    cards.forEach((card) => {
      const matchesCategory = productCategory === 'all' || card.dataset.category === productCategory;
      const matchesSearch = !query || card.dataset.search.toLocaleLowerCase('fa').includes(query);
      const shouldShow = matchesCategory && matchesSearch;
      card.style.display = shouldShow ? 'flex' : 'none';
      if (shouldShow) visible += 1;
    });
    document.getElementById('productEmpty')?.classList.toggle('visible', visible === 0);
  }

  function activateFilter(button, selector) {
    document.querySelectorAll(selector).forEach((item) => item.classList.remove('active'));
    button.classList.add('active');
  }

  function toggleTheme() {
    setTheme(root.dataset.theme === 'dark' ? 'light' : 'dark');
    showToast(root.dataset.theme === 'dark' ? 'پوستهٔ تاریک فعال شد.' : 'پوستهٔ روشن فعال شد.');
  }

  document.addEventListener('click', (event) => {
    const pageTarget = event.target.closest('[data-page-target]');
    if (pageTarget) {
      event.preventDefault();
      navigate(pageTarget.dataset.pageTarget);
      return;
    }

    const openTarget = event.target.closest('[data-open-sheet]');
    if (openTarget) {
      event.preventDefault();
      openSheet(openTarget.dataset.openSheet);
      return;
    }

    if (event.target.matches('[data-overlay]')) {
      closeSheets();
      return;
    }

    if (event.target.closest('[data-close-sheet]')) {
      closeSheets();
      return;
    }

    const inventoryFilter = event.target.closest('[data-stock-filter]');
    if (inventoryFilter) {
      stockFilter = inventoryFilter.dataset.stockFilter;
      activateFilter(inventoryFilter, '[data-stock-filter]');
      renderInventory();
      return;
    }

    const category = event.target.closest('[data-category]');
    if (category) {
      productCategory = category.dataset.category;
      activateFilter(category, '[data-category]');
      renderProducts();
      return;
    }

    const invoiceFilter = event.target.closest('[data-filter-group]');
    if (invoiceFilter) {
      activateFilter(invoiceFilter, '[data-filter-group]');
      showToast(`فیلتر «${invoiceFilter.textContent.trim().replace(/\s+/g, ' ')}» فعال شد.`);
      return;
    }

    const segmented = event.target.closest('.segmented button');
    if (segmented) {
      activateFilter(segmented, '.segmented button');
      showToast(`نمای ${segmented.textContent.trim()} انتخاب شد.`);
      return;
    }

    const actionElement = event.target.closest('[data-action]');
    if (!actionElement) return;
    const action = actionElement.dataset.action;

    switch (action) {
      case 'theme':
        toggleTheme();
        break;
      case 'calendar':
        showToast('تقویم فروش امروز آمادهٔ نمایش است.');
        break;
      case 'edit-shortcuts':
        showToast('ویرایش میانبرها در نسخهٔ بعدی فعال می‌شود.');
        break;
      case 'export':
        showToast('خروجی فروش در حال آماده‌سازی است.');
        break;
      case 'receive':
        showToast('فرم ورود کالا آماده شد؛ یک قلم را اسکن کنید.');
        break;
      case 'scan':
      case 'camera':
        showToast('دوربین بارکدخوان در نسخهٔ اندروید باز می‌شود.');
        break;
      case 'adjust':
        showToast('شیت اصلاح موجودی برای این قلم باز می‌شود.');
        break;
      case 'clear-inventory':
        stockFilter = 'all';
        if (document.querySelector('[data-inventory-search]')) document.querySelector('[data-inventory-search]').value = '';
        activateFilter(document.querySelector('[data-stock-filter="all"]'), '[data-stock-filter]');
        renderInventory();
        break;
      case 'filter-products':
        showToast('فیلترهای محصولات آمادهٔ انتخاب هستند.');
        break;
      case 'new-product':
        showToast('فرم محصول جدید آمادهٔ ورود اطلاعات است.');
        break;
      case 'product-menu':
        showToast('گزینه‌های ویرایش محصول در دسترس است.');
        break;
      case 'clear-products':
        productCategory = 'all';
        if (document.querySelector('[data-product-search]')) document.querySelector('[data-product-search]').value = '';
        activateFilter(document.querySelector('[data-category="all"]'), '[data-category]');
        renderProducts();
        break;
      case 'reports':
        showToast('گزارش‌های فروش و سود در حال بارگذاری است.');
        break;
      case 'customers':
        showToast('فهرست مشتریان در نسخهٔ کامل نمایش داده می‌شود.');
        break;
      case 'suppliers':
        showToast('فهرست تأمین‌کنندگان باز شد.');
        break;
      case 'settings':
        showToast('تنظیمات فروشگاه باز شد.');
        break;
      case 'backup':
        showToast('آخرین پشتیبان‌گیری امروز ساعت ۰۳:۰۰ موفق بوده است.');
        break;
      case 'security':
      case 'profile-settings':
        showToast('تنظیمات حساب شما امن و به‌روز است.');
        break;
      case 'choose-customer':
        showToast('انتخاب مشتری در نسخهٔ اندروید با جست‌وجوی سریع انجام می‌شود.');
        break;
      case 'plus':
      case 'minus': {
        const quantity = actionElement.closest('.quantity')?.querySelector('[data-quantity]');
        if (quantity) {
          const normalized = quantity.textContent.replace(/[۰-۹]/g, (digit) => String('۰۱۲۳۴۵۶۷۸۹'.indexOf(digit))).replace(/[٠-٩]/g, (digit) => String('٠١٢٣٤٥٦٧٨٩'.indexOf(digit)));
          const current = Number(normalized) || 1;
          const next = Math.max(1, current + (action === 'plus' ? 1 : -1));
          quantity.textContent = String(next).replace(/\d/g, (digit) => '۰۱۲۳۴۵۶۷۸۹'[digit]);
        }
        break;
      }
      case 'create-invoice':
        closeSheets();
        showToast('فاکتور ۱۴۰۵/۰۰۳۴۸ صادر و لینک آن پیامک شد.');
        navigate('sales');
        break;
      case 'mark-read':
        closeSheets();
        showToast('همهٔ اعلان‌ها خوانده شد.');
        document.querySelector('.notification-dot')?.remove();
        break;
      case 'clear-recent':
        showToast('جست‌وجوهای اخیر پاک شد.');
        break;
      case 'logout':
        closeSheets();
        showToast('برای خروج از حساب، تأیید نهایی لازم است.');
        break;
      case 'close-toast':
        hideToast();
        break;
      default:
        break;
    }
  });

  document.querySelector('[data-search-global]')?.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
      const query = event.currentTarget.value.trim();
      navigate('inventory');
      const inventorySearch = document.querySelector('[data-inventory-search]');
      if (inventorySearch) inventorySearch.value = query;
      renderInventory();
    }
  });
  document.querySelector('[data-inventory-search]')?.addEventListener('input', renderInventory);
  document.querySelector('[data-product-search]')?.addEventListener('input', renderProducts);

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      if (overlays.some((overlay) => !overlay.hidden)) closeSheets();
      if (toast && !toast.hidden) hideToast();
    }
    if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k') {
      event.preventDefault();
      openSheet('searchSheet');
    }
  });

  loadTheme();
  renderInventory();
  renderProducts();
})();
