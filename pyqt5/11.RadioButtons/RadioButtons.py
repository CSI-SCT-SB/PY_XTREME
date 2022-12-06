"""
RadioButtons are used for input with multiple choice answers 
here we have created 6 radiobuttons 
to make few radiobuttons answert to same input 
i.e we can only select only one among those 
we have to add them to a buttonGroup
here there two button group option1, option2, option are in group1
and option4 , option5 , option6 are in group2
"""


import PyQt5.QtWidgets as widgets 

class mainWindow(widgets.QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("24 pull request") 
        self.setMinimumSize(500, 500)  
        
        self.mainLayout = widgets.QVBoxLayout();

        self.buttonGroup1 =  widgets.QButtonGroup();
        self.buttonGroup2 =  widgets.QButtonGroup()

        self.option1 =  widgets.QRadioButton("option1")
        self.option1.clicked.connect(self.radioButtonClicked)

        self.option2 =  widgets.QRadioButton("option2")
        self.option2.clicked.connect(self.radioButtonClicked)

        self.option3 =  widgets.QRadioButton("option3")
        self.option3.clicked.connect(self.radioButtonClicked)

        self.option4 = widgets.QRadioButton("option4")
        self.option4.clicked.connect(self.radioButtonClicked)
        
        self.option5 = widgets.QRadioButton("option5")
        self.option5.clicked.connect(self.radioButtonClicked)

        self.option6 = widgets.QRadioButton("option6")
        self.option6.clicked.connect(self.radioButtonClicked)


        self.buttonGroup1.addButton(self.option1)
        self.buttonGroup1.addButton(self.option2)
        self.buttonGroup1.addButton(self.option3)

        self.buttonGroup2.addButton(self.option4)
        self.buttonGroup2.addButton(self.option5)
        self.buttonGroup2.addButton(self.option6)

        self.setLayout(self.mainLayout) # this sets the layout of the main window
        self.mainLayout.addWidget(self.option1)
        self.mainLayout.addWidget(self.option2)
        self.mainLayout.addWidget(self.option3)

        self.mainLayout.addWidget(self.option4)
        self.mainLayout.addWidget(self.option5)
        self.mainLayout.addWidget(self.option6)

        self.show()
    
    def radioButtonClicked(self):
        sender = self.sender()
        print(sender.text())



app =  widgets.QApplication([])
window =  mainWindow()
app.exec()
