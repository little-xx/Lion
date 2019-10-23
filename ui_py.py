class Mymainwindow(QtWidgets.QMainWindow, Ui_MainWindow) :
    def __init__(self, parent = None) :
        super(Mymainwindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    myWin = Mymainwindow()
    myWin.show()
    sys.exit(app.exec())


