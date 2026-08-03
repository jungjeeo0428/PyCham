import os
import urllib.request


import requests
from bs4 import BeautifulSoup

url = "https://www.moviechart.co.kr/rank/realtime/index/image"
img_path = "../img"
if not os.path.exists(img_path):
    os.mkdir(img_path)

res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")
imgs = soup.select(".movieBox-list .movieBox-item img")
for img in imgs:
    src_value = img["src"].split('=')[-1]
    title= img['alt'].replace(":","_")
    file_nm = os.path.join(img_path, title+'.png')
    urllib.request.urlretrieve(src_value, file_nm)
    