from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout, QLineEdit, QComboBox) # QLineEdit, QComboBox 추가
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore # 모듈 추가

class View(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.le1=QLineEdit('0', self) #라인 에디트1 추가
        self.le1.setAlignment(QtCore.Qt.AlignRight) # 라인 에디트1 문자열 배치 설정 
        self.le2=QLineEdit('0', self) #라인 에디트2 추가
        self.le2.setAlignment(QtCore.Qt.AlignRight) # 라인 에디트2 문자열 배치 설정 

        self.cb = QComboBox(self) #콤포 박스 추가
        self.cb.addItems(['+','-','*','/']) # 콤보 박스 항목 추가(연산자로 사용)

        self.te1 = QPlainTextEdit() # 텍스트 에디트 위젯 생성
        self.te1.setReadOnly(True) # 텍스트 에디트 위젯을 읽기만 하도록 수정 

        self.btn1 = QPushButton('Message', self) #버튼 추가
        self.btn2 = QPushButton('Clear', self) #버튼2 추가 

        hbox = QHBoxLayout() # 수평 박스 레이아웃을 추가하고 버튼1, 2 추가
        hbox.addStretch(1) #공백
        hbox.addWidget(self.btn1) #버튼1 배치
        hbox.addWidget(self.btn2) #버튼2 배치
        hbox_formular = QHBoxLayout() # 새로 정의한 위젯을 QHBoxLayout에 배치
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)

        vbox=QVBoxLayout() # 수직 레이아웃 위젯 생성
        vbox.addWidget(self.te1)# 빈 공간
        vbox.addLayout(hbox_formular) # hbox_formular 배치
        vbox.addLayout(hbox)
        vbox.addStretch(1) # 빈 공간        
        
        self.setLayout(vbox) # 빈 공간 - 버튼 - 빈 공간 순으로 수직 배치된 레이아웃 설정

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256, 256)
        self.show()

    def activateMessage(self): #버튼을 클릭할 때 동작하는 함수: 메시지 박스 출력 
        self.te1.appendPlainText("Button clicked!")

    def clearMessage(self): #버튼2 핸들러 함수
        self.te1.clear()