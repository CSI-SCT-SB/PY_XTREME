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
        self.setMinimumSize(800, 900)  
        
        self.mainLayout = widgets.QVBoxLayout();

        self.setLayout(self.mainLayout) # this sets the layout of the main window

        self.label =  widgets.QLabel()
        self.label.setText("this is the text for label1 ")

        self.mainLayout.addWidget(self.label)


        self.show()


app =  widgets.QApplication([])
window =  mainWindow()
app.exec()
