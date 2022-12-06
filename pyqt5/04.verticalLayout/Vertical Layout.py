import PyQt5.QtWidgets as widgets 


class mainWindow(widgets.QWidget):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("24 pull request")
        self.setMinimumSize

        self.label1 =  widgets.QLabel("label 1")
        self.label2 =  widgets.QLabel("label 2")
        self.label3 =  widgets.QLabel("label 3")
        self.label4 =  widgets.QLabel("label 4")
        
        self.verticalLayout = widgets.QVBoxLayout();

        self.verticalLayout.addWidget(self.label1)
        self.verticalLayout.addWidget(self.label2)
        self.verticalLayout.addWidget(self.label3)
        self.verticalLayout.addWidget(self.label4)

        self.setLayout(self.verticalLayout)
        self.show()


app =  widgets.QApplication([])
window =  mainWindow()
app.exec()
