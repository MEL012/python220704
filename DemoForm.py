# DemoForm.py

# DemoForm.py(로직) + DemoForm.ui(화면)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 디자인 파일을 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]

# 폼클래스 정의
class DemoForm(QDialog, form_class):
    # 생성자 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 Qt데모~~")

# 진입점 체크
if __name__ == "__main__":
    # 실행프로세스 생성
    app = QApplication(sys.argv)

    # 화면 생성
    demoWindow = DemoForm()
    demoWindow.show()

    # 이벤트 대기
    app.exec_()