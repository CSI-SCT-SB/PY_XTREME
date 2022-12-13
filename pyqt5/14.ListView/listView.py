"""
List Viw is used to show items in a list and user can select an item from the list
in this code there is a list view and also a button which on pressed shows the item 
that is currently selected in list viwe

"""

import PyQt5.QtWidgets as widgets 
from PyQt5.QtCore import Qt


class mainWindow(widgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(500 , 500)

        self.mainLayout = widgets.QVBoxLayout()

        self.list =  widgets.QListWidget()

        self.list.addItem("apple")   # adds one item at a time 
        self.list.addItems(["orange" , "mango" , "guavava"]) # adds multiple items
        self.list.insertItem(0 , "pineapple") #used to insert inbetween

        self.button = widgets.QPushButton("show item")
        self.button.clicked.connect( self.getValue )


        self.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.list)
        self.mainLayout.addWidget(self.button)

        self.show()

    def getValue(self):
        value = self.list.currentItem().text()
        print(value)



app =  widgets.QApplication([])
window =  mainWindow()
app.exec()
