
""" working GUI of a calculator"""

#import resources

from PyQt5 import QtCore, QtGui, QtWidgets

#set up the main class

class Ui_CalcWindow(object):
    
    #set up the main window and all of the buttons and the output box

    def setupUi(self, CalcWindow):
        CalcWindow.setObjectName("CalcWindow")
        CalcWindow.resize(361, 588)
        self.centralwidget = QtWidgets.QWidget(CalcWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("%"))
        self.percentButton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.cButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("C"))
        self.cButton.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.remove_it())
        self.arrowButton.setGeometry(QtCore.QRect(190, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("/"))
        self.divideButton.setGeometry(QtCore.QRect(275, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(190, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(275, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(100, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(190, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(275, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(100, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(190, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("+"))
        self.addButton.setGeometry(QtCore.QRect(275, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(100, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.plusminusButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.plus_minus_it())
        self.plusminusButton.setGeometry(QtCore.QRect(10, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setObjectName("plusminusButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.dot_it())
        self.decimalButton.setGeometry(QtCore.QRect(190, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.decimalButton.setFont(font)
        self.decimalButton.setObjectName("decimalButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.math_it())
        self.equalButton.setGeometry(QtCore.QRect(275, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(100, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        CalcWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CalcWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 21))
        self.menubar.setObjectName("menubar")
        CalcWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CalcWindow)
        self.statusbar.setObjectName("statusbar")
        CalcWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CalcWindow)
        QtCore.QMetaObject.connectSlotsByName(CalcWindow)
   
    #set up a function for when the button is pressed
    #Remove character
    def remove_it(self):
        screen = self.outputLabel.text()
        screen = screen [:-1]
        self.outputLabel.setText(screen)
    
    #Math calculations
    def math_it(self):
        screen = self.outputLabel.text()
        #error detection
        try:
            answer = eval(screen)
            self.outputLabel.setText(str(answer))
        except:
            #Output error
              self.outputLabel.setText("ERROR")

    #Change from positive to negative
    def   plus_minus_it(self):
        screen = self.outputLabel.text()
        if "-" in screen:
            self.outputLabel.setText(screen.replace("-", ""))
        else:
             self.outputLabel.setText(f'{screen}')
    


    #Add a decimal
    def dot_it(self):
        screen = self.outputLabel.text()
        
        if [-1]  == ".":
            pass
        else:
             self.outputLabel.setText(f'{screen}.')

    

    def press_it(self,pressed):
        if pressed == "C":
            self.outputLabel.setText("0")
        else:
            
            #Check to see if starts with 0 and delete the 0
            
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")
            
            #otherwise concantenate the button with what was already there    
            
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')
    
     #set up the text for the buttons

    def retranslateUi(self, CalcWindow):
        _translate = QtCore.QCoreApplication.translate
        CalcWindow.setWindowTitle(_translate("CalcWindow", "Calculator"))
        self.outputLabel.setText(_translate("CalcWindow", "0"))
        self.percentButton.setText(_translate("CalcWindow", "%"))
        self.cButton.setText(_translate("CalcWindow", "C"))
        self.arrowButton.setText(_translate("CalcWindow", "<<"))
        self.divideButton.setText(_translate("CalcWindow", "/"))
        self.sevenButton.setText(_translate("CalcWindow", "7"))
        self.nineButton.setText(_translate("CalcWindow", "9"))
        self.multiplyButton.setText(_translate("CalcWindow", "x"))
        self.eightButton.setText(_translate("CalcWindow", "8"))
        self.fourButton.setText(_translate("CalcWindow", "4"))
        self.sixButton.setText(_translate("CalcWindow", "6"))
        self.minusButton.setText(_translate("CalcWindow", "-"))
        self.fiveButton.setText(_translate("CalcWindow", "5"))
        self.oneButton.setText(_translate("CalcWindow", "1"))
        self.threeButton.setText(_translate("CalcWindow", "3"))
        self.addButton.setText(_translate("CalcWindow", "+"))
        self.twoButton.setText(_translate("CalcWindow", "2"))
        self.plusminusButton.setText(_translate("CalcWindow", "+/-"))
        self.decimalButton.setText(_translate("CalcWindow", "."))
        self.equalButton.setText(_translate("CalcWindow", "="))
        self.zeroButton.setText(_translate("CalcWindow", "0"))

# set up main to start the window
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CalcWindow = QtWidgets.QMainWindow()
    ui = Ui_CalcWindow()
    ui.setupUi(CalcWindow)
    CalcWindow.show()
    sys.exit(app.exec_())
