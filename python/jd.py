import requests
url="https://item.jd.com/6946605.html"
try:
    r=requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:10000])
except:
    print("爬取失败")


