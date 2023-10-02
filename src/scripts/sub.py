#! /usr/bin/python3

import rospy
from std_msgs.msg import String

def Print (msg):
    rospy.loginfo(msg)

if __name__ == '__main__':
    rospy.init_node("sub")
    rospy.loginfo("Sub node started")
    sub=rospy.Subscriber("/test",String,Print)
    rospy.spin()