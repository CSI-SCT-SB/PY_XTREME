"""
this code creates a basic window with no layouts or widget in it 
"""
"""
date time pick is used to pick a date. it has a up and down arrow
and we can increaste or decrease each component like month , year , day , 
hour in it
"""
import PyQt5.QtWidgets as widgets 


class mainWindow(widgets.QWidget):

    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("24 pull request")
        self.setMinimumSize(500 , 500)

        self.mainLayout = widgets.QVBoxLayout()

        self.dateTimePick = widgets.QDateTimeEdit()

        self.button = widgets.QPushButton("get date")
        self.button.clicked.connect(self.getDate)


        self.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.dateTimePick)
        self.mainLayout.addWidget(self.button)

        self.show()

    def getDate(self):
        dateTime = self.dateTimePick.dateTime()
        print( dateTime.toString("dd.MM.yyyy.hh.mm") )


app =  widgets.QApplication([])
window =  mainWindow()
app.exec()
