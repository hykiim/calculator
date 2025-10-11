import sys
from ui import View  #ui.py의 View 클래스 추가
from ctrl import Control # ctrl.py의 Control 클래스 추가
from PyQt5.QtWidgets import QApplication

def main():
    # calc = QApplication(sys.argv)
    app = QApplication(sys.argv)
    view = View()
    Control(view=view)
    sys.exit(app.exec_())    

if __name__=='__main__':
    main()