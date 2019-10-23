from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(1048, 600)
        self.setWindowTitle("Lion")
        self.setStyleSheet("background:#36393e;")
        self.listWidget = QtWidgets.QListWidget(self)
        item1 = QtWidgets.QListWidgetItem()
        item1.setText("xxxxxx")
        self.listWidget.addItem(item1)


        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MWindow = MainWindow()
    sys.exit(app.exec())
