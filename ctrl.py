class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calculate(self):  # calculate 메서드 추가, 내용은 추후 작성
        num1 = float(self.view.le1.text())  # 첫 번째 라인 에디트에 입력된 숫자를 읽어옴
        num2 = float(self.view.le2.text())  # 두 번째 라인 에디트에 입력된 숫자를 읽어옴
        operator = self.view.cb.currentText()  # 콤포 박스에 선택된 연산자 확인

        if operator == "+":
            return f"{num1} + {num2} = {self.sum(num1, num2)}"
        elif operator == "-":
            return f"{num1} - {num2} = {self.sub(num1, num2)}"
        elif operator == "*":
            return f"{num1} * {num2} = {self.mul(num1, num2)}"
        elif operator == "/":
            return f"{num1} / {num2} = {self.div(num1, num2)}"
        else:
            return "Calculation Error"

    def connectSignals(self):  # btn1을 클릭하면 calculate 결과가 화면에 표시되도록 수정
        self.view.btn1.clicked.connect(lambda: self.view.setDisplay(self.calculate()))
        self.view.btn2.clicked.connect(self.view.clearMessage)

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):  # 뺄셈 함수 추가
        return a - b

    def mul(self, a, b):  # 곱셈 함수 추가
        return a * b

    def div(self, a, b):  # 예외 처리를 사용하도록 수정
        try:
            if b == 0:
                raise Exception("Divisor Error")
        except Exception as e:
            return e
        return a / b
