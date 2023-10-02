#! /usr/bin/python3
import pygame
import rospy
import json ,os
from std_msgs.msg import String

#if __name__ == '__main__':

class PS_Controller:
    def __init__(self) -> None:
        pygame.init()
        rospy.init_node("publisher")
        self.pub=rospy.Publisher("/test",String,queue_size=1)
        rospy.loginfo("pub node started")    
        pygame.joystick.Joystick(0).init()
        self.LEFT, self.RIGHT, self.DOWN, self.UP =False,False,False,False 
        
        with open(os.path.join("/home/montaser/catkin_ws/src/ROV_software/src/scripts/ps4_keys.json"), 'r+') as file:
            self.button_keys = json.load(file)
        
        while True:
            self.ROS_Publish_event()
            self.event_type_check()    
        
    
    
    def event_type_check(self):
        for event in pygame.event.get():
            if event.type == pygame.JOYHATMOTION:
                self.Arrows(event)
            
            if event.type == pygame.JOYBUTTONDOWN:
                self.Buttons(event)



    def ROS_Publish_event(self):
        if self.LEFT:
            self.pub.publish("LEFT")
        
        if self.RIGHT:
            self.pub.publish("RIGHT")
        
        if self.UP:
            self.pub.publish("UP")
        
        if self.DOWN:
            self.pub.publish("DOWN")
    


    def Arrows(self,event):
        if event.value[0] == -1:
            self.LEFT = True
        if event.value[0] == 1:
            self.RIGHT = True
        if event.value[1] == -1:
            self.DOWN = True
        if event.value[1] == 1:
            self.UP = True
        
        if event.value[0] == 0:
            self.LEFT = False
        if event.value[0] == 0:
            self.RIGHT = False
        if event.value[1] == 0:
            self.DOWN = False
        if event.value[1] == 0:
            self.UP = False
        


    def Buttons(self,event):
        if event.button == self.button_keys['x']:
           self.pub.publish("x")
        if event.button == self.button_keys['circle']:
            self.pub.publish("circle")
        if event.button == self.button_keys['triangle']:
            self.pub.publish("triangle")
        if event.button == self.button_keys['square']:
            self.pub.publish("square")
        

    



PS_Controller()
























#while True:
#    for event in pygame.event.get():
#
#        if event.type == pygame.JOYHATMOTION:
#        
#            if event.value[0] == -1:
#                LEFT = True
#            if event.value[0] == 1:
#                RIGHT = True
#            if event.value[1] == -1:
#                DOWN = True
#            if event.value[1] == 1:
#                UP = True
#            
#            if event.value[0] == 0:
#                LEFT = False
#            if event.value[0] == 0:
#                RIGHT = False
#            if event.value[1] == 0:
#                DOWN = False
#            if event.value[1] == 0:
#                UP = False
#        

#    if LEFT:
#        pub.publish("LEFT")
#        
#    if RIGHT:
#        pub.publish("RIGHT")
#        
#    if UP:
#        pub.publish("UP")
#        
#    if DOWN:
#        pub.publish("DOWN")
            








######################################################################





#        if event.type == pygame.JOYBUTTONDOWN:
#            
#            if event.button == button_keys['left_arrow']:
#                rospy.loginfo("LEFT")
#            
#
#            if event.button == button_keys['right_arrow']:
#                rospy.loginfo("RIGHT")
#        
#
#
#            if event.button == button_keys['down_arrow']:
#                rospy.loginfo("DOWN")
#
#
#            if event.button == button_keys['up_arrow']:
#                rospy.loginfo("UP")
#        
#        if event.type == pygame.JOYBUTTONUP:
#            if event.button == button_keys['left_arrow']:
#                
#                
#                rospy.loginfo("END_LEFT")
#            if event.button == button_keys['right_arrow']:
#                
#                
#                rospy.loginfo("END_RIGHT")
#            if event.button == button_keys['down_arrow']:
#                
                
#                rospy.loginfo("END_DOWN")
#            if event.button == button_keys['up_arrow']:
#                
#                rospy.loginfo("END_UP")




    
 
