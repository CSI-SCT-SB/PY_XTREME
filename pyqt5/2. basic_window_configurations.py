'''
this shows the basic methods to configure a window such as to set the title
height , width and add stylesheet
'''

import PyQt5.QtWidgets as widgets 


class mainWindow(widgets.QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("24 pull request")  #setting window title
        self.setMinimumHeight(900)  # setting window height
        self.setMinimumWidth(800)  # setting window width 
        self.setMinimumSize(800, 900)  # setting window height and width together
        self.setStyleSheet(" background-color : red") # adding style sheet ie adding css in text form 
       
        self.show()


app =  widgets.QApplication([])
window =  mainWindow()
app.exec()
