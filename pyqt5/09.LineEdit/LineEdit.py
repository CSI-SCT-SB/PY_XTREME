"""
LineEdit is used to take text input from a the user
in this a line edit is created and a button is made 
which on being pressed displays the text inside 
LineEdit in the terminal

"""


import PyQt5.QtWidgets as widgets 

class mainWindow(widgets.QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("24 pull request") 
        self.setMinimumSize(500, 500)  
        
        self.mainLayout = widgets.QVBoxLayout();
        

        self.setLayout(self.mainLayout) # this sets the layout of the main window

        self.lineEdit =  widgets.QLineEdit()

        self.button = widgets.QPushButton("submit")
        self.button.clicked.connect( self.getValue )
        
        

        self.mainLayout.addWidget(self.lineEdit)
        self.mainLayout.addWidget(self.button)


        self.show()
    
    def getValue(self):
        value = self.lineEdit.text()
        print(value)


app =  widgets.QApplication([])
window =  mainWindow()
app.exec()
