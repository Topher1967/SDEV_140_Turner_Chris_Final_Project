
"""create a window that contains 3 images"""

#import resources

from PyQt5 import QtCore, QtGui, QtWidgets

#import qrc, xml links converted to python

import resources

#set up main class

class Ui_SecondWindow(object):
    
#set up main window and define the images size, shape and location

    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(1039, 895)
        SecondWindow.setStyleSheet("image\n"
"background-image: url(:/newPrefix/Python_Fun.jpg);")
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 130, 511, 421))
        self.label_2.setStyleSheet("background-image: url(:/newPrefix/PyQt5_image.jpg);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/PyQt5_image.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 130, 441, 421))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("image: url(:/newPrefix/Code_python.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 610, 401, 231))
        self.label_3.setStyleSheet("image: url(:/newPrefix/Python_Fun.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 40, 921, 41))
        palette = QtGui.QPalette()
        self.label_4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1039, 21))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

#set up the text
   
    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MainWindow"))
        self.label_4.setText(_translate("SecondWindow", "<html><head/><body><p><span style=\" color:#1d00ff;\">Working with images using PyQt5 designer </span></p></body></html>"))


#set up main logic to run window
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())
