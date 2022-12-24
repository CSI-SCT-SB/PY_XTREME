"""
MenuBar is an essential part of gui 
in this code creation of a menubar in demonstrated 

we can a add a menu bar and menus to it 
in the menus we can give actions that on click trigger a fuction 
or submenus

"""

import PyQt5.QtWidgets as widgets 
from PyQt5.QtCore import Qt


class mainWindow(widgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(500 , 500)

        self.mainLayout = widgets.QVBoxLayout()

        self.menuBar =  widgets.QMenuBar()

        self.menu1 =  self.menuBar.addMenu("file")
        self.menu1.addAction("new" ,  self.menuItemClicked )
        self.menu1.addAction("save" ,  self.menuItemClicked )

        self.menu1 =  self.menuBar.addMenu("edit")
        self.menu1.addAction("copy" , self.menuItemClicked )
        self.menu1.addAction("paste", self.menuItemClicked )

        

        self.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.menuBar)

        self.show()

    def menuItemClicked(self):
        print(self.sender().text())



app =  widgets.QApplication([])
window =  mainWindow()
app.exec()
