"""
this shows the use of form layout 
rows are added using 
layout.addRow( text  , widget  )
"""

import PyQt5.QtWidgets as widgets 


class mainWindow(widgets.QWidget):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("24 pull request")
        self.setMinimumSize

        self.input1 =  widgets.QLineEdit()
        self.input2 =  widgets.QLineEdit()
        self.input3 =  widgets.QLineEdit()
        
        self.formLayout = widgets.QFormLayout();

        self.formLayout.addRow( "input1" , self.input1)
        self.formLayout.addRow( "input2" , self.input2)
        self.formLayout.addRow( "input3" , self.input3)

        self.setLayout(self.formLayout)
        self.show()


app =  widgets.QApplication([])
window =  mainWindow()
app.exec()
