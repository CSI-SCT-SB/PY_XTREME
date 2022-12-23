
"""
this code shows how to use pushbuttons in pyqt5
"""

import PyQt5.QtWidgets as widgets 

def clicked():
    print("the button is clicked")

class mainWindow(widgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("24 pull requet")
        self.setMinimumSize(500 , 500);

        self.verticalLayout = widgets.QVBoxLayout()


        self.button = widgets.QPushButton("click me")
        self.button.clicked.connect( clicked )


        self.verticalLayout.addWidget(self.button)
        self.setLayout(self.verticalLayout)

        self.show()


app =  widgets.QApplication([])
window =  mainWindow()
app.exec()
