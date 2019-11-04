from PyQt5 import QtWidgets
from ui_calculator import Ui_Calculator

class CalculatorWindow(QtWidgets.QMainWindow,Ui_Calculator):

    firstNum = None
    userIsTypingSecondNumber = False


    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.show()

        # Connect buttons

        self.b0.clicked.connect(self.digit_pressed)
        self.b1.clicked.connect(self.digit_pressed)
        self.b2.clicked.connect(self.digit_pressed)
        self.b3.clicked.connect(self.digit_pressed)
        self.b4.clicked.connect(self.digit_pressed)
        self.b5.clicked.connect(self.digit_pressed)
        self.b6.clicked.connect(self.digit_pressed)
        self.b7.clicked.connect(self.digit_pressed)
        self.b8.clicked.connect(self.digit_pressed)
        self.b9.clicked.connect(self.digit_pressed)

        self.point.clicked.connect(self.decimal_pressed)


        self.plusmin.clicked.connect(self.unary_operation_pressed)
        self.percent.clicked.connect(self.unary_operation_pressed)

        self.plus.clicked.connect(self.binary_operation_pressed)
        self.minus.clicked.connect(self.binary_operation_pressed)
        self.multiply.clicked.connect(self.binary_operation_pressed)
        self.div.clicked.connect(self.binary_operation_pressed)

        self.equal.clicked.connect(self.equals_pressed)
        self.clear.clicked.connect(self.clear_pressed)


        self.plus.setCheckable(True)
        self.minus.setCheckable(True)
        self.multiply.setCheckable(True)
        self.div.setCheckable(True)






    def digit_pressed(self):

        button = self.sender()

        #Clear the screen

        if ((self.plus.isChecked() or self.minus.isChecked() or
                self.multiply.isChecked() or self.div.isChecked()) and (not self.userIsTypingSecondNumber)):

            newLabel = format(float(button.text()), '.15g')
            self.userIsTypingSecondNumber = True

        else:
            if ( ('.' in self.label.text() ) and (button.text() == "0") ):
                newLabel = format(self.label.text() + button.text(),'.15')
            else:
                newLabel = format(float(self.label.text() + button.text()),'.15g')

        self.label.setText(newLabel)

    def decimal_pressed(self):
        self.label.setText(self.label.text() + '.')

    def unary_operation_pressed(self):
        button = self.sender()
        labelNumber = float(self.label.text())
        if button.text() == '+/-':
            labelNumber = labelNumber * -1
        else: # button text == '%'
            labelNumber = labelNumber * 0.01

        newLabel = format(labelNumber,'.15g')
        self.label.setText(newLabel)

    def binary_operation_pressed(self):
        button = self.sender()

        self.firstNum = float(self.label.text())

        button.setChecked(True)

    def equals_pressed(self):

        secondNum = float(self.label.text())

        if self.plus.isChecked():
            labelNumber = self.firstNum + secondNum
            newLabel = format(labelNumber,'.15g')
            self.label.setText(newLabel)
            self.plus.setChecked(False)
        elif self.minus.isChecked():
            labelNumber = self.firstNum - secondNum
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.minus.setChecked(False)
        elif self.div.isChecked():
            labelNumber = self.firstNum / secondNum
            newLabel = format(labelNumber,'.15g')
            self.label.setText(newLabel)
            self.div.setChecked(False)
        elif self.multiply.isChecked():
            labelNumber = self.firstNum * secondNum
            newLabel = format(labelNumber,'.15g')
            self.label.setText(newLabel)
            self.multiply.setChecked(False)

        self.userIsTypingSecondNumber = False

    def clear_pressed(self):

        self.plus.setChecked(False)
        self.minus.setChecked(False)
        self.div.setChecked(False)
        self.multiply.setChecked(False)

        self.userIsTypingSecondNumber = False

        self.label.setText("0")