import PyQt5.QtWidgets as widgets 


class mainWindow(widgets.QWidget):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("24 pull request")
        self.setMinimumSize(500 , 500)

        self.label1 =  widgets.QLabel("label 1")
        self.label2 =  widgets.QLabel("label 2")
        self.label3 =  widgets.QLabel("label 3")
        self.label4 =  widgets.QLabel("label 4")
        
        self.horizontalLayout= widgets.QHBoxLayout();

        self.horizontalLayout.addWidget(self.label1)
        self.horizontalLayout.addWidget(self.label2)
        self.horizontalLayout.addWidget(self.label3)
        self.horizontalLayout.addWidget(self.label4)

        self.setLayout(self.horizontalLayout)
        self.show()


app =  widgets.QApplication([])
window =  mainWindow()
app.exec()
