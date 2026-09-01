# -*- coding: utf-8 -*-
"""ساخت فایل تک‌فایلیِ «برچسب محصول» با فونت وزیرمتنِ جاسازی‌شده.

خروجی: product-labels.html  (کاملاً آفلاین، بدون منبع خارجی)

    python3 build_labels.py
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
FONTS = HERE.parent / 'workspace-01a04268-60f1-7e19-bce0-e27eb41243db' / 'ui' / 'selim-vand' / 'fonts_b64.json'
TPL = HERE / 'label_template.html'
OUT = HERE / 'product-labels.html'


def font_css() -> str:
    if not FONTS.exists():
        print(f'! فونت پیدا نشد ({FONTS}) — خروجی با فونت سیستمی ساخته می‌شود.')
        return '/* fonts not embedded */'
    fonts = json.loads(FONTS.read_text(encoding='utf-8'))
    return ''.join(
        f"@font-face{{font-family:'Vazirmatn UI FD';font-style:normal;font-weight:{w};"
        f"font-display:swap;src:url(data:font/woff2;base64,{b}) format('woff2')}}"
        for w, b in sorted(fonts.items(), key=lambda x: int(x[0])))


def main():
    html = TPL.read_text(encoding='utf-8').replace('/*__FONTS__*/', font_css())
    OUT.write_text(html, encoding='utf-8')
    print(f'✓ {OUT.name}  ({OUT.stat().st_size/1024:.0f} KB)')


if __name__ == '__main__':
    main()
