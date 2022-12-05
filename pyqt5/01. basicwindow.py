"""
this code creates a basic window with no layouts or widget in it 
"""

import PyQt5.QtWidgets as widgets 


class mainWindow(widgets.QWidget):

    def __init__(self):
        super().__init__()
        self.show()


app =  widgets.QApplication([])
window =  mainWindow()
app.exec()
