"""

calender widget can be used to create calenders 
from which date can be selected 

"""

import PyQt5.QtWidgets as widgets 
from PyQt5.QtCore import Qt


class mainWindow(widgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(500 , 500)

        self.mainLayout = widgets.QVBoxLayout()

        self.calendar =  widgets.QCalendarWidget()
        self.calendar.clicked.connect(self.showDate) 


        self.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.calendar)
        self.show()

    def showDate(self):
        date = self.calendar.selectedDate()
        print(date.toString())



app =  widgets.QApplication([])
window =  mainWindow()
app.exec()
