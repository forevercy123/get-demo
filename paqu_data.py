import urllib.request

#下载网站数据并解码
response = urllib.request.urlopen("http://www.fishc.com")
html = response.read()
html = html.decode("utf-8")
print(html)
