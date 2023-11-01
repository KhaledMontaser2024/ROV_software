from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget
from pathlib import Path
from PyQt5.QtCore import QTimer, QResource
from background_rc import*
from logo_rc import*
import os
QResource.registerResource("background.qrc")
QResource.registerResource("logo.qrc")
flage=0

class GUI(QMainWindow):
    def __init__(self, parent=None):
        super(GUI, self).__init__(parent)
        self.script_dir = os.path.abspath(os.path.dirname(__file__))
        self.gui_path = os.path.join(self.script_dir, 'gui.ui')        
        uic.loadUi(self.gui_path, self)

        self.start_timer_button.clicked.connect(self.start_timer)
        self.stop_timer_button.clicked.connect(self.stop_timer)
        self.reset_timer_button.clicked.connect(self.reset_timer)
        self.start_mession_button.clicked.connect(self.start_mession)



        self.timer = QTimer()
        self.timer.timeout.connect(self.update_display)
        self.elapsed_time = 0

    def start_timer(self):
       self.flage=2
       self.timer.start(1000)
      

    def stop_timer(self):
       self.timer.stop()

    def reset_timer(self):
         self.elapsed_time = 0
         self.update_display()
    def start_mession(self):
        self.flage=1
        self.timer.start(1000)



    def update_display(self):
        self.elapsed_time += 1
        if self.flage==1 :
          self.timer_mession.display(self.elapsed_time)
        elif self.flage==2 :
            self.timerlcd.display(self.elapsed_time)

app = QApplication([])
window = QStackedWidget()
window.addWidget(GUI())
window.show()
app.exec_()
