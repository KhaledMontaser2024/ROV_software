##############################################################################################
#these script for gui code and have main class called gui and some func 1-start which used to start timmer 2-stop which stop the timmer 3- display_motion /timer which used to desplay time on lcd number in gui
# and have switch func which used to switch betwwen 2 stacked widget the first widget is used to desplay timer and the scond used to desplay slider 
#we have some variables 1-switch which used to handel the switch between the 2 pages in stacked widget 2-counter_time and mession which used to convert from sec to munits
#3-elapsed time which used increase the time every sec
###################################################################################################
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget
from pathlib import Path
from PyQt5.QtCore import QTimer, QResource
from background_rc import*
from logo_rc import*
from PyQt5.QtCore import QTime
import os
QResource.registerResource("background.qrc")
QResource.registerResource("logo.qrc")


class GUI(QMainWindow): #main class
    def __init__(self, parent=None):
        super(GUI, self).__init__(parent)
        self.script_dir = os.path.abspath(os.path.dirname(__file__))
        self.gui_path = os.path.join(self.script_dir, 'gui.ui')        
        uic.loadUi(self.gui_path, self)

        self.start_timer_button.clicked.connect(self.start_timer)
        self.stop_timer_button.clicked.connect(self.stop_timer)
        self.reset_timer_button.clicked.connect(self.reset_timer)
        self.start_mession_button.clicked.connect(self.start_mession)
        self.stop_mession_button.clicked.connect(self.stop_mession)
        self.reset_mession_button.clicked.connect(self.reset_mession)

        self.switch_buttons.clicked.connect(self.switch_func)      #button used to switch between staked widget

        
        self.switch = 1   #used to switch between stacked wideget of timer and slider  
        self.counter_time=0  #used to convert sec  to minutes in timer  
        self.counter_time_mession=0


        self.mession=QTimer()
        self.mession.timeout.connect(self.update_mession)         #used to handel time of the mession
        self.elapsed_time_mession = 0                              #count time in sec in the timer mession



        self.timer = QTimer()
        self.timer.timeout.connect(self.update_display)             #used to handel the min timer
        self.elapsed_time = 0                                        #used to count sec in the main timer

    def start_timer(self):
        self.timer.start(1000)
      

    def stop_timer(self):                        #used to stop the the main timer
       self.timer.stop()

    def reset_timer(self):                 #used to reset the main timer
            self.timerlcd.display(0)
            self.elapsed_time=0
            self.counter_time=0
            self.update_display()
  
    def update_display(self):             #used to desplay  in the main timer
        self.elapsed_time += 1
        if self.elapsed_time %60 ==0 :
            self.counter_time+=1
            self.timerlcd.display(self.counter_time) 

       


    def start_mession(self):
        self.mession.start(1000)
    def update_mession(self):         #used to update the desplay in the timer mession
         self.elapsed_time_mession += 1
         if self.elapsed_time_mession %60 ==0 :
            self.counter_time_mession+=1
            self.timer_mession.display(self.counter_time_mession)

    def stop_mession(self):
       self.mession.stop()

    def reset_mession(self):           # used to reset the mession timer
         self.timer_mession.display(0)
         self.elapsed_time_mession=0
         self.counter_time_mession=0
         self.update_mession()
 

    def switch_func(self) :
        if self.switch==1 :
            self.stackedWidget_2.setCurrentWidget(self.page_5)
            self.switch=2
        elif self.switch==2:
            self.stackedWidget_2.setCurrentWidget(self.page_6)
            self.switch=1


    
    def setup_sliders(self):
        self.horizontalSlider.setRange(0,20)
        self.horizontalSlider_2.setRange(0,20)
        self.horizontalSlider_3.setRange(0,20)
        self.horizontalSlider_4.setRange(0,20)
        self.horizontalSlider.setSingleStep(0.1)
        self.horizontalSlider_2.setSingleStep(0.1)
        self.horizontalSlider_3.setSingleStep(0.1)
        self.horizontalSlider_4.setSingleStep(0.1)
        self.horizontalSlider.valueChanged.connect(self.update_sliders1)
        self.horizontalSlider_2.valueChanged.connect(self.update_sliders2)
        self.horizontalSlider_3.valueChanged.connect(self.update_sliders3)
        self.horizontalSlider_4.valueChanged.connect(self.update_sliders4)

    def update_sliders1(self,value):
        self.label_15.setText(str(value))
    def update_sliders2(self,value):
        self.label_12.setText(str(value))
    def update_sliders3(self,value):
        self.label_13.setText(str(value))
    def update_sliders4(self,value):
        self.label_14.setText(str(value))
    
    
        

app = QApplication([])
window = QStackedWidget()
window.addWidget(GUI())
window.show()
app.exec_()
