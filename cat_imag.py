import urllib.request

#下载一张尺寸为500*600的猫的照片
response = urllib.request.urlopen("http://placekitten.com/g/500/600")
cat_img = response.read()

with open("cat_500_600.jpg","wb") as f:
    f.write(cat_img)