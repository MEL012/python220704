# web2.py

# 웹서버에 요청
import urllib.request

# 크롤링
from bs4 import BeautifulSoup

data = urllib.request.urlopen("https://comic.naver.com/webtoon/list?titleId=796218&weekday=wed")
soup = BeautifulSoup(data, "html.parser")

cartoons = soup.find_all("td", class_="title")
print("갯수:{0}".format(len(cartoons)))
title = cartoons[0].find("a").text
link = cartoons[0].find("a")["href"]
print(title)
print(link)

for item in cartoons:
    title = item.find("a").text
    print(title.strip())