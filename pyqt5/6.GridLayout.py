"""
the grid layout arranges the givern files in grid format the row and column 
to place the element can be specifed the by the user 
"""

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
        
        self.gridlLayout = widgets.QGridLayout();

        self.gridlLayout.addWidget(self.label1 , 0 , 0)
        self.gridlLayout.addWidget(self.label2 , 0 , 1)
        self.gridlLayout.addWidget(self.label3 , 1 , 0)
        self.gridlLayout.addWidget(self.label4 , 1, 1)

        self.setLayout(self.gridlLayout)
        self.show()


app =  widgets.QApplication([])
window =  mainWindow()
app.exec()
