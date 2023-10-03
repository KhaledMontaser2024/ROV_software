#! /usr/bin/python3

import rospy
from ROV_software.msg import ps4
def Print (msg):
    if msg.UpArrow:
        rospy.loginfo("Up")
    if msg.DownArrow:
        rospy.loginfo("Down")
    if msg.LeftArrow:
        rospy.loginfo("Left")
    if msg.RightArrow:
        rospy.loginfo("Right")
    
    if msg.x:
        rospy.loginfo("x")
    if msg.circle:
        rospy.loginfo("circle")
    if msg.triangle:
        rospy.loginfo("triangle")
    if msg.square:
        rospy.loginfo("square")

    if msg.L1:
        rospy.loginfo("L1")
    if msg.L2:
        rospy.loginfo("L2")
    if msg.R1:
        rospy.loginfo("R1")
    if msg.R2:
        rospy.loginfo("R2")

    if msg.share:
        rospy.loginfo("share")
    if msg.options:
        rospy.loginfo("options")
    if msg.PS:
        rospy.loginfo("PS")
    



if __name__ == '__main__':
    rospy.init_node("sub")
    rospy.loginfo("Sub node started")
    sub=rospy.Subscriber("/PsController_signal",ps4,Print)
    rospy.spin()