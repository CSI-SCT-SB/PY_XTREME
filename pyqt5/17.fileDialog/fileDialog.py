"""

FileDialogs are used to select file paths from the computer 
here we create a button which one clicking creates a file
dialog box 

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
        
        fileDialog = widgets.QFileDialog()
        fileDialog.setFileMode(widgets.QFileDialog.AnyFile)
        fileDialog.exec()
        files = fileDialog.selectedFiles()
        print(files)




app =  widgets.QApplication([])
window =  mainWindow()
app.exec()
