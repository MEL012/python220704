# web1.py

# 웹크롤링(웹 데이터 수집 기술)
from bs4 import BeautifulSoup

# 문서 로딩
page = open("c:\\work\\python220704\\test01.html", "rt", encoding="utf-8").read()

# 검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
# print(soup.prettify())

# 문서의 태그 모두 검색(List)
# print(soup.find_all("p"))
# print(soup.find_all("a"))

# 첫번째 검색
print(soup.find("p"))

# 약간의 검색 조건
print(soup.find_all("p", class_="outer-text"))

# 문자열만 추출
for item in soup.find_all("p"):
    # 내부를 삭제하고 내부 컨텐츠만 리턴
    title = item.text
    title = title.replace("\n", "")
    print(title.strip())