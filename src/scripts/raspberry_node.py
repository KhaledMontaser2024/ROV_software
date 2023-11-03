#! /usr/bin/python3


##############################################################################################
## this script is the main ROV Script that gether all data from differnt scripts            ##
## and direct them toward its distenation                                                   ##
## here we have the main ROS link node that connect Raspberry with IMU sensor and arduino   ##
## to main laptop node on station                                                           ##
##############################################################################################

import rospy
from rov_system.msg import IMU,raspberry

class Raspberry():
    def __init__(self) -> None:
        
        rospy.init_node("Raspberry_node")        
        
        self.ControlSubscriber=rospy.Subscriber("/IMU_to_Raspberry",IMU,self.IMU_data_buffer)
        self.CaimanSubscriber=rospy.Subscriber("/Caiman_to_Raspberry",raspberry,self.Command_buffer)
        

        self.ArduinoPublisher=rospy.Publisher("/Rasp_to_Arduino",raspberry,queue_size=10)
        self.CaimanPublisher=rospy.Publisher("/Rasp_to_Caiman",IMU,queue_size=10)
        rospy.spin()

    def IMU_data_buffer(self,msg):
        self.CaimanPublisher.publish(msg)


    def Command_buffer(self,msg):
        self.ArduinoPublisher.publish(msg)
