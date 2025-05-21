import sys

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from frames import material_show
from db import database

class MainApp(QWidget):
    def __init__(self):
        super().__init__()

        self.db = database.Database()

        self.setWindowTitle('Образ Плюс')
        self.resize(1280, 720)
        self.setWindowIcon(QPixmap('res/icon.png'))

        self.layout = QVBoxLayout(self)

        self.frames_container = QStackedWidget(self)
        self.frame_start = material_show.MaterialShow(self)
        self.frames_container.addWidget(self.frame_start)

        self.layout.addWidget(self.frames_container)

    def refresh_main_frame(self):
        self.frames_container.removeWidget(self.frame_start)
        self.frame_start = material_show.MaterialShow(self)
        self.frames_container.addWidget(self.frame_start)
        self.frames_container.setCurrentWidget(self.frame_start)

style = '''
    * {
        font-family: Constantia
    }

    #title {
        font-size: 24px;
        font-weight: 500;
        qproperty-alignment: AlignCenter;
    }
    
    #title_main {
        font-size: 20px;
        font-weight: 500;
        margin-left: 20px;
    }
    
    #title_right {
        font-size: 20px;
        font-weight: 500;
        qproperty-alignment: AlignRight;
        margin-right: 20px;
    }
    
    #subtitle {
        font-size: 18px;
        font-weight: 500;
        margin-left: 20px;
    }
    
    #card {
        border: 1px solid black;
        background: #AED0FF;
    }
    
    #btn {
        background: #1D476B;
        font-size: 20px;
    }
'''

app = QApplication(sys.argv)
main_class = MainApp()
app.setStyleSheet(style)
app.setFont('Constantia')
main_class.show()
app.exec()

