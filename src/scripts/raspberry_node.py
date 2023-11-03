#! /usr/bin/python3
import rospy
from sensor_msgs.msg import Imu
from rov_system.msg import ButtonsStateMessage

class Raspberry():
    def __init__(self) -> None:
        
        rospy.init_node("Raspberry_node")        
        self.ControlSubscriber=rospy.Subscriber("/IMU_to_Raspberry",Imu,self.IMU_data_buffer)
        self.CaimanSubscriber=rospy.Subscriber("/Caiman_to_Raspberry",ButtonsStateMessage.ArduinoData,self.Command_buffer)
        

        self.ArduinoPublisher=rospy.Publisher("/Rasp_to_Arduino",ButtonsStateMessage.ArduinoData,queue_size=10)
        self.CaimanPublisher=rospy.Publisher("/Rasp_to_Caiman",Imu,queue_size=10)
        rospy.spin()

    def IMU_data_buffer(self,msg):
        self.CaimanPublisher.publish(msg)


    def Command_buffer(self,msg):
        self.ArduinoPublisher.publish(msg)
