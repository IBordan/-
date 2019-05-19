import sys
import logging
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QLineEdit, QApplication, QPushButton, QMessageBox, QComboBox)


class Example(QWidget):

    logging.basicConfig(filename="logs.log", level=logging.INFO)
    a = -10000
    b = -10000
    c = 0
    e = -1
    logging.info("\na= %s \n b = %s\n c = %s\n e = %s\n" % (a,b,c,e))

    def f(self,x):
        return  x * x - 8 * x + 12

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setStyleSheet("""
                    #MainWidget {
                        background: white;
                    }
                    .QLabel {
                        color: #3f79db;
                    }
                """)

        self.lbl = QLabel(self)
        self.lbl.setText("Введите левую и правую границы:")
        self.lbl.move(20, 40)

        self.lbl4 = QLabel(self)
        self.lbl4.setText("Укажите точность вычисления ")
        self.lbl4.move(20, 110)

        self.lbl5 = QLabel(self)
        self.lbl5.setText("Функция: y = x^2 ? 8x + 12  ")
        self.lbl5.move(20, 20)

        qle = QLineEdit(self)
        qle2 = QLineEdit(self)
        qle3 = QLineEdit(self)

        qle.move(20, 60)
        qle2.move(20, 85)
        qle3.move(20, 130)

        qle.textChanged[str].connect(self.onChanged)
        qle2.textChanged[str].connect(self.onChanged2)
        qle3.textChanged[str].connect(self.onChanged3)

        btn1 = QPushButton("Расчёт", self)
        btn1.setStyleSheet("background-color: #b2edff")

        btn1.move(120, 160)
        btn1.clicked.connect(self.buttonClicked)

        self.lbl3 = QLabel(self)
        self.lbl3.setText("Ответ:                                                                    ")
        self.lbl3.move(20, 190)

        self.setGeometry(200, 200, 350, 250)
        self.setWindowTitle('QLineEdit')
        self.show()

    def onChanged(self, text):
        self.a = text
        logging.info("\n a= %s \n b = %s\n c = %s\n e = %s\n" % (self.a, self.b, self.c, self.e))

    def onChanged2(self, text):
        self.b = text
        logging.info("\n a= %s \n b = %s\n c = %s\n e = %s\n" % (self.a, self.b, self.c, self.e))

    def onChanged3(self, text):
        self.e = text
        logging.info("\n a= %s \n b = %s\n c = %s\n e = %s\n" % (self.a, self.b, self.c, self.e))

    def buttonClicked (self):

        if (self.verification(self.a) == False or self.verification(self.b) == False or self.verification_e(str(self.e)) == False):
            self.lbl3.setText("Данные ошибочны!")
            return

        a = float(self.a)
        b = float(self.b)
        e = 0.1 ** float(self.e)

        logging.info("\n a= %s \n b = %s\n c = %s\n e = %s\n" % (self.a, self.b, self.c, self.e))

        y1 = self.f(a)
        y2 = self.f(b)

        if y1 * y2 >= 0:
            self.lbl3.setText("Корней не сущесвует, или их > 1 в данном промежутке")
        else:
            n = 1

            self.c = (y2 * a - y1 * b) / (y2 - y1);

            y3 = self.f(self.c)
            while (abs(y3) > e):
                self.c = (y2 * a - y1 * b) / (y2 - y1);

                logging.info("\n c = %s" %self.c)

                y3 = self.f(self.c)
                if y1 * y3 < 0:
                    b = self.c
                else:
                    a = self.c
                n += 1

                self.lbl3.setText("Ответ: c = "+str(self.c))

    def verification(self, value):
        if value[0] == '-':
            value = value.replace('-', '', 1)
        print(value)
        if (value.replace('.', '', 1)).isdigit() is True:
            return True
        else:
            return False

    def verification_e(self, value):
        if value.isdigit() is False or int(value) < 0:
            return False
        else:
            return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())