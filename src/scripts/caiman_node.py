#! /usr/bin/python3

##############################################################################################
## this script is the main station node that gether all data from differnt scripts          ##
## and direct them toward its distenation                                                   ##
## here we have the main ROS link node that connect laptop(with all its differnt scripts)   ##
## to raspberry                                                                             ##
##############################################################################################

import rospy
from rov_system.msg import ButtonsStateMessage,IMU,raspberry
from ROV_motion import motion
from qtpy.QtCore import QThread,pyqtSignal
class Caiman(QThread):
    def __init__(self) -> None:

        self.MotorsSpeed=pyqtSignal()
        self.SliderSignal=pyqtSignal()
        self.Grip_Led=pyqtSignal()
        self.Angles=pyqtSignal

        ## variables to store msgs with ROS costom data types ##
        self.ImuReads=IMU()
        self.motion=raspberry()
        #########################################################
        
        self.motionClass = motion()     # importing motion class for further use 

        rospy.init_node("Station_Node")
        
        ######################################### here we recive controller commands #################################### 
        self.ControllerSubscriber = rospy.Subscriber ("/Controller_to_caiman",ButtonsStateMessage,self.commandsHandler)
        self.AutoSubscriber       = rospy.Subscriber ("/Controller_to_caiman_auto",ButtonsStateMessage,self.autoMotion)
        #################################################################################################################

        ############################### caiman - Raspberry nodes communication ########################
        self.RaspberryPublisher   = rospy.Publisher  ("/Caiman_to_Raspberry",raspberry,queue_size=10)        
        self.RaspberrySubscriber  = rospy.Subscriber ("/Rasp_to_Caiman",IMU,self.IMU_Handler)
        ###############################################################################################

    def run(self) -> None:
        while True:
            pass

    def autoMotion(self, msg):
        pass
    
    def commandsHandler(self, msg):
        
        self.MotorsSpeed.emit(self.motion)
        self.SliderSignal.emit(self) #Dont know what to put here
        self.Grip_Led.emit(self.motion.ArduinoData)
        ##### here we call motion method and pass its paramiters then store its returned list ###########
        self.motion = self.motionClass.output(msg.MotionData.Forward_Backward_Axis,msg.MotionData.Up_Down_Axis,msg.MotionData.Left_Right_Axis,msg.MotionData.Yaw_Axis,msg.MotionData.Pitch_Axis,msg.MotionData.Speed,msg.MotionData.Reverse_Control,self.ImuReads.yaw_angle,self.ImuReads.pitch_angle)
        self.motion.insert(8,msg.ArduinoData) #### at the same list we add (LED and Grippers signals)
        self.RaspberryPublisher.publish(self.motion)
        self.motion.clear()     
        
        


    ########## when reciving data from IMU sensor this fn       ############### 
    ########## just buffer it to use in calling motion method   ###############
    def IMU_Handler (self,msg):
        self.ImuReads=msg
        self.Angles.emit(self.ImuReads)
    ############################################################################

