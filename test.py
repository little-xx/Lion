from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 200, 600))
        self.listWidget.setStyleSheet(
            "QListWidget{background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #223946,stop:0.5 #273b4c ,stop:1 #2d4657);border : 0px, solid, gray;font-size:16px;padding-top:100px;}"
            "QListWidget::Item{color:rgb(125,125,125);height:40px;padding-left:40;border:0px solid gray;}"
            "QListWidget::Item:hover{color:#ffffff;background:#234053;border:0px solid gray;}"
            "QListWidget::Item:selected{border-image:url(images/listwidget_h.png); color:rgb(255,255,255);border:0px solid gray;}"
            "QListWidget::Item:selected:active{background:#1a303e;color:#0f8a8f;border:0px solid gray;}"
            )
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Team"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Import"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Export"))
        self.listWidget.setSortingEnabled(__sortingEnabled)


class Mymainwindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Mymainwindow, self).__init__(parent)
        self.setupUi(self)

    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self, "Extract",
                                                "Get into the chopper?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            print("xixixixixixixi!!!")
            sys.exit()
        else:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWin = Mymainwindow()
    myWin.show()
    sys.exit(app.exec())