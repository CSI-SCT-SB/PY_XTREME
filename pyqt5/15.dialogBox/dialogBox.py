"""

dialogBoxes are separate window that appear on screen to show messages , warnings or take inputs 
in this example a button had been created that on clicked creates a dialogbox with a label and a 
close button

"""

import PyQt5.QtWidgets as widgets 
from PyQt5.QtCore import Qt


class mainWindow(widgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(500 , 500)

        self.mainLayout = widgets.QVBoxLayout()


        self.button = widgets.QPushButton("show item")
        self.button.clicked.connect( self.showDialog )


        self.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.button)

        self.show()

    def showDialog(self):
        dialogBox = widgets.QDialog()
        dialogBox.setWindowTitle('dialog box')
        dialogBox.setMinimumSize(200 , 100)

        dialogBoxLayout = widgets.QVBoxLayout()

        #adding widgets to dialog box

        label = widgets.QLabel("this is a sample dialogBox")

        closeButton =  widgets.QPushButton("close")
        closeButton.clicked.connect(lambda : dialogBox.close()) # .close() method closed the dialogbox

        dialogBoxLayout.addWidget(label)
        dialogBoxLayout.addWidget(closeButton)
        dialogBox.setLayout(dialogBoxLayout)

        dialogBox.exec()




app =  widgets.QApplication([])
window =  mainWindow()
app.exec()
