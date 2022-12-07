"""
this code creates a basic window with no layouts or widget in it 
"""

import PyQt5.QtWidgets as widgets 


class mainWindow(widgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(500 , 500)

        self.mainLayout = widgets.QVBoxLayout()

        self.spinBox = widgets.QSpinBox()

        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(10)
        self.spinBox.setSingleStep(1)
        self.spinBox.valueChanged.connect(self.getValue)

        

        self.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.spinBox)

        self.show()

    def getValue(self):
        sender = self.sender()
        value = sender.value()
        print(value)



app =  widgets.QApplication([])
window =  mainWindow()
app.exec()
