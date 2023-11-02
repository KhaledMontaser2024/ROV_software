#! /usr/bin/python3
import rospy
from rov_system.msg import ButtonsStateMessage
from ROV_motion import motion

class Caiman():
    def __init__(self) -> None:
        
        rospy.init_node("Station_Node")
        ControllerSubscriber=rospy.Subscriber("/Controller_to_caiman",ButtonsStateMessage,self.commandsHandler)
        rospy.spin()

    def commandsHandler(self, msg):
        rospy.loginfo(msg.motion)
        motion= motion(msg.MotionData.Forward_Backward_Axis, msg.MotionData.Up_Down_Axis, msg.ButtonsState.MotionData.Left_Right_Axis, msg.MotionData.Yaw_Axis, msg.MotionData.Pitch_Axis, roll, 200, msg.MotionData.Reverse_Control)
        thrusters_speeds=motion.output()
        

Caiman()
