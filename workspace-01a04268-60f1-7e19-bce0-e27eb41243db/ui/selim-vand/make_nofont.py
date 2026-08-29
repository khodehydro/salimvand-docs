import re, pathlib
h = pathlib.Path('ui/selim-vand/selimvand-ui.html').read_text(encoding='utf-8')
h2 = re.sub(r"<style>@font-face.*?</style>",
            '<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css">',
            h, flags=re.S)
pathlib.Path('deploy/selimvand-ui-nofont.html').write_text(h2, encoding='utf-8')
print('orig', len(h), '-> nofont', len(h2))
