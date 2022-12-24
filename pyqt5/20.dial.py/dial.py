"""
dials are rotatable circular objects which can 
be roated and values correseponding to the rotation 
can be obtained 

"""

import PyQt5.QtWidgets as widgets 
from PyQt5.QtCore import Qt


class mainWindow(widgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(500 , 500)

        self.mainLayout = widgets.QVBoxLayout()

        self.dial = widgets.QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setSingleStep(1)

        self.dial.valueChanged.connect(self.showValue)

        self.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.dial)
        self.show()

    def showValue(self):
        print(self.dial.value())

 



app =  widgets.QApplication([])
window =  mainWindow()
app.exec()
