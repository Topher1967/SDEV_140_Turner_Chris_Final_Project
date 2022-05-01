
"""create a window that contains PyQt5 Schema"""

#import resources

from PyQt5 import QtCore, QtGui, QtWidgets

#import qrc, xml links converted to python

import resources

#set up main class

class Ui_Window3(object):
    
#set up main window and define the image size, shape and location
    def setupUi(self, Window3):
        Window3.setObjectName("Window3")
        Window3.resize(1073, 909)
        Window3.setAutoFillBackground(True)
        Window3.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Window3)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 1061, 891))
        self.label.setStyleSheet("background-image: url(:/newPrefix/PyQt5_schema.webp);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/PyQt5_schema.webp"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        Window3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1073, 21))
        self.menubar.setObjectName("menubar")
        Window3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Window3)
        self.statusbar.setObjectName("statusbar")
        Window3.setStatusBar(self.statusbar)

        self.retranslateUi(Window3)
        QtCore.QMetaObject.connectSlotsByName(Window3)

    def retranslateUi(self, Window3):
        _translate = QtCore.QCoreApplication.translate
        Window3.setWindowTitle(_translate("Window3", "MainWindow"))


#set up main logic to start the window
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window3 = QtWidgets.QMainWindow()
    ui = Ui_Window3()
    ui.setupUi(Window3)
    Window3.show()
    sys.exit(app.exec_())
