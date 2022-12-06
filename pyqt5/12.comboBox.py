"""
Label is one of the most basic widget , it basically a widget with some text 
in this code first we create a verticalLayout and we place the Label widget in it
a layout is a container that containers many widgets and even other layouts 
the concepts of layout will be disucussed more 

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
