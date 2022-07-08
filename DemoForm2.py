# DemoForm.py

# DemoForm.py(로직) + DemoForm.ui(화면)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 웹서버에 요청
import urllib.request

# 크롤링
from bs4 import BeautifulSoup

# 디자인 파일을 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

# 폼클래스 정의
class DemoForm(QMainWindow, form_class):
    # 생성자 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def firstClick(self):
        f = open("c:\\work\\python220704\\webtoon.txt", "wt", encoding="utf-8");

        # 수열을 생성해서 URL주소 만들기
        try:
            for i in range(1, 11):
                url = "https://comic.naver.com/webtoon/list?titleId=729964&page=" + str(i)
                print(url)
                data = urllib.request.urlopen(url)
                soup = BeautifulSoup(data, "html.parser")

                cartoons = soup.find_all("td", class_="title")

                for item in cartoons:
                    title = item.find("a").text
                    print(title.strip())
                    f.write(title + "\n")

            f.close()
            print("웹 크롤링 종료")
        except:
            pass
    def secondClick(self):
        self.label.setText("두번째 버튼")
    def thirdClick(self):
        self.label.setText("세번째 버튼")

# 진입점 체크
if __name__ == "__main__":
    # 실행프로세스 생성
    app = QApplication(sys.argv)

    # 화면 생성
    demoWindow = DemoForm()
    demoWindow.show()

    # 이벤트 대기
    app.exec_()