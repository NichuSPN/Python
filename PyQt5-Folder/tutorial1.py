#python -m PyQt5.uic.pyuic -x test.ui -o test.py
#Use the above code in the folder containing ui file to convert it into a python file

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My First Label")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("You clicked the button")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.setGeometry(0, 0, 400, 400)
    win.setWindowTitle("Hello!!!")
    win.show()
    sys.exit(app.exec_())


window()
