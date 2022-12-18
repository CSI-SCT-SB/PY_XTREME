
"""
Using input DialogBox we can create a dialogbox asking for input from the user


"""

import PyQt5.QtWidgets as widgets 
from PyQt5.QtCore import Qt


class mainWindow(widgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(500 , 500)

        self.mainLayout = widgets.QVBoxLayout()


        self.button = widgets.QPushButton("show dialog")
        self.button.clicked.connect( self.showDialog )


        self.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.button)

        self.show()

    def showDialog(self):
        
        inputDialog = widgets.QInputDialog()
        name , done  = inputDialog.getText(self , "name" , "enter your name" )
        #syntax : inputDialog.getText(self , dialog box title , question )
        print(name, done)




app =  widgets.QApplication([])
window =  mainWindow()
app.exec()
