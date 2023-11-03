#! /usr/bin/python3
import rospy
from rov_system.msg import ButtonsStateMessage
from sensor_msgs.msg import Imu
#from ROV_motion import motion

class Caiman():
    def __init__(self) -> None:
        
        rospy.init_node("Station_Node")
        self.ControllerSubscriber = rospy.Subscriber ("/Controller_to_caiman",ButtonsStateMessage,self.commandsHandler)
        self.RaspberryPublisher   = rospy.Publisher  ("/Caiman_to_Raspberry",ButtonsStateMessage.ArduinoData,queue_size=10)        
        self.RaspberrySubscriber  = rospy.Subscriber ("/Rasp_to_Caiman",Imu,self.IMU_Handler)
        rospy.spin()

    def commandsHandler(self, msg):
        #rospy.loginfo(msg.motion)
        motion = motion(msg.MotionData.Forward_Backward_Axis, msg.MotionData.Up_Down_Axis, msg.ButtonsState.MotionData.Left_Right_Axis, msg.MotionData.Yaw_Axis, msg.MotionData.Pitch_Axis, roll, 200, msg.MotionData.Reverse_Control)
        msg.ArduinoData = (motion.output() << 8)
        self.RaspberryPublisher.publish(msg.ArduinoData)
        

    def IMU_Handler (self,msg):
        pass




Caiman()
