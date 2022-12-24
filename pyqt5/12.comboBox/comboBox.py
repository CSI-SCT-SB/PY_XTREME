
"""
comboBox are drop down list with multiple options
here we are creating a comboBox and a button that will
display the currently selected option in comboBox

"""


import PyQt5.QtWidgets as widgets 

class mainWindow(widgets.QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("24 pull request") 
        self.setMinimumSize(500, 500)  
        
        self.mainLayout = widgets.QVBoxLayout();
        

        self.setLayout(self.mainLayout) # this sets the layout of the main window

        self.comboBox =  widgets.QComboBox()

        self.comboBox.addItem("option1")  # options can be added individually like this
        self.comboBox.addItem("option2")
        self.comboBox.addItems(["option3" , "option4" , "option5"])

        

        self.button = widgets.QPushButton("submit")
        self.button.clicked.connect( self.getValue )
        
        

        self.mainLayout.addWidget(self.comboBox)
        self.mainLayout.addWidget(self.button)


        self.show()
    
    def getValue(self):
        value = self.comboBox.currentText()
        index = self.comboBox.currentIndex()
        print(  index, value)
        


app =  widgets.QApplication([])
window =  mainWindow()
app.exec()
