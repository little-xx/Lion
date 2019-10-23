from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('/Users/tyxqaq/PycharmProjects/lion.jpeg'))
        self.show()

if __name__ == "__main__":
    app =QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

