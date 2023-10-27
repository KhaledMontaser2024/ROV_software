#! /usr/bin/python3
import rospy
from rov_system.msg import ButtonsStateMessage


class Caymen():
    def __init__(self) -> None:
        
        rospy.init_node("Station_Node")
        ControllerSubscriber=rospy.Subscriber("/Controller_to_Caymen",ButtonsStateMessage,self.commandsHandler)
        rospy.spin()

    def commandsHandler(self, msg):
        rospy.loginfo(msg)

Caymen()