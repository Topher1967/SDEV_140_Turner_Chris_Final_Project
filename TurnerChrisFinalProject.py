""" Main window that sets up the logic to open 3 more windows, 1 for my images, 
a second for a GUI of a calculator, and a third for the PyQt5 Schema"""

#imports necessary files 
from PyQt5 import QtCore, QtGui, QtWidgets
from Window2 import Ui_SecondWindow
from Calc import  Ui_CalcWindow
from Window3 import Ui_Window3

# Main class to create main window and definitions

class Ui_MainWindow(object):
   
# 3 definitions to open the different windows
    
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindow2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CalcWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindow3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Window3()
        self.ui.setupUi(self.window)
        self.window.show()

#sets up the layout for the main window
   
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(77, 155, 232);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow())  #opens window 1 for images
        self.pushButton.setGeometry(QtCore.QRect(300, 140, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 10, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 90, 331, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 210, 661, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow2()) #opens window 2 for GUI calculator
        self.pushButton_2.setGeometry(QtCore.QRect(300, 280, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"selection-background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 340, 761, 91))
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow3()) #opens window 3 for PyQt5 Schema
        self.pushButton_3.setGeometry(QtCore.QRect(300, 430, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#sets up the text for all of the buttons and labels
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", " Second Window "))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">Welcome to my app for the Python final project</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">Window #2 is the doorway to my Images</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#ff0000;\">To extend functionality I have added a GUI calculator</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "GUI Calculator shell"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#ff0000;\">Python QT5 can easily extend the capabilities of any application</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "PyQt5 Schema"))

#main logic to start the window
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
