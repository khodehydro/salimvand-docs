import sys, json, pathlib, urllib.request, urllib.parse, http.cookiejar

path = sys.argv[1]
content = pathlib.Path(path).read_text(encoding='utf-8')

cj = http.cookiejar.CookieJar()
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64)')]
op.open('https://rentry.co/', timeout=30).read()
token = next(c.value for c in cj if c.name == 'csrftoken')

data = urllib.parse.urlencode({
    'csrfmiddlewaretoken': token,
    'text': content,
}).encode()
req = urllib.request.Request('https://rentry.co/api/new', data=data, headers={
    'Referer': 'https://rentry.co/',
    'X-CSRFToken': token,
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)',
})
res = op.open(req, timeout=60).read().decode()
print(res[:400])
