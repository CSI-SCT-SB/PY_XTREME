"""
TextEdit is used to take multiline text input from the user
in this code a textEdit is created and also a button is created 
that on being pressed prints the content in the textEdit in the
terminal
"""


import PyQt5.QtWidgets as widgets 

class mainWindow(widgets.QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("24 pull request") 
        self.setMinimumSize(500, 500)  
        
        self.mainLayout = widgets.QVBoxLayout();
        

        self.setLayout(self.mainLayout) # this sets the layout of the main window

        self.textEdit =  widgets.QTextEdit()
        self.textEdit.resize(400, 300)

        self.button = widgets.QPushButton("submit")
        self.button.clicked.connect( self.getValue )
        
        

        self.mainLayout.addWidget(self.textEdit)
        self.mainLayout.addWidget(self.button)


        self.show()
    
    def getValue(self):
        value = self.textEdit.toPlainText()
        print(value)


app =  widgets.QApplication([])
window =  mainWindow()
app.exec()
