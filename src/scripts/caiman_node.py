#! /usr/bin/python3
import rospy
from rov_system.msg import ButtonsStateMessage,IMU,raspberry
from ROV_motion import motion
from std_msgs.msg import UInt8MultiArray
class Caiman():
    def __init__(self) -> None:
        self.motionClass = motion()
        self.ImuReads=IMU()
        self.motion=raspberry()
        self.motion=[1,2,3,4]
        rospy.init_node("Station_Node")
        self.ControllerSubscriber = rospy.Subscriber ("/Controller_to_caiman",ButtonsStateMessage,self.commandsHandler)
        self.RaspberryPublisher   = rospy.Publisher  ("/Caiman_to_Raspberry",raspberry,queue_size=10)        
        self.RaspberrySubscriber  = rospy.Subscriber ("/Rasp_to_Caiman",IMU,self.IMU_Handler)
        
        rospy.spin()
#def output(self, forward_backward, up_down, slide, yaw, pitch, max_speed, reverse_motion, measured_yaw_angle, measured_pitch_angle):

    def commandsHandler(self, msg):
        self.motion = self.motionClass.output(msg.MotionData.Forward_Backward_Axis,msg.MotionData.Up_Down_Axis,msg.MotionData.Left_Right_Axis,msg.MotionData.Yaw_Axis,msg.MotionData.Pitch_Axis,msg.MotionData.Speed,msg.MotionData.Reverse_Control,self.ImuReads.yaw_angle,self.ImuReads.pitch_angle)
        self.motion.insert(8,msg.ArduinoData)
        self.motion.pop(8)
        
        self.RaspberryPublisher.publish(self.motion)
        

    def IMU_Handler (self,msg):
        self.ImuReads=msg




Caiman()
