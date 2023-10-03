#! /usr/bin/python3
import pygame
import rospy
import json ,os
from ROV_software.msg import ps4


Button = ps4()
class PS_Controller:
    def __init__(self) -> None:
        pygame.init()
        rospy.init_node("publisher")
        self.pub=rospy.Publisher("/PsController_signal", ps4 ,queue_size=1)
        rospy.loginfo("pub node started")    
        pygame.joystick.Joystick(0).init()
        
        with open(os.path.join("/home/montaser/catkin_ws/src/ROV_software/src/scripts/ps4_keys.json"), 'r+') as file:
            self.button_keys = json.load(file)
        
        while True:
            self.pub.publish(Button)
            self.event_type_check()    
        
    
    def event_type_check(self):
        for event in pygame.event.get():
            if event.type == pygame.JOYHATMOTION:
                self.Arrows(event)
            
            if event.type == pygame.JOYBUTTONDOWN:
                self.Buttons(event,True)

            if event.type == pygame.JOYBUTTONUP:
                self.Buttons(event,False)


    def Arrows(self,event):
        if event.value[0] == -1:
            Button.LeftArrow = True

        if event.value[0] == 1:
            Button.RightArrow = True

        if event.value[1] == -1:
            Button.DownArrow = True

        if event.value[1] == 1:
            Button.UpArrow = True

        
        if event.value[0] == 0:
            Button.LeftArrow = False

        if event.value[0] == 0:
            Button.RightArrow = False

        if event.value[1] == 0:
            Button.DownArrow = False

        if event.value[1] == 0:
            Button.UpArrow = False

        
    def Buttons(self,event, buttonState):
        
        if event.button == self.button_keys['x']:
           Button.x = buttonState
        if event.button == self.button_keys['circle']:
            Button.circle = buttonState
        if event.button == self.button_keys['triangle']:
            Button.triangle = buttonState
        if event.button == self.button_keys['square']:
            Button.square = buttonState
        
        if event.button == self.button_keys['L1']:
           Button.L1 = buttonState
        if event.button == self.button_keys['L2']:
            Button.L2 = buttonState
        if event.button == self.button_keys['R1']:
            Button.R1 = buttonState
        if event.button == self.button_keys['R2']:
            Button.R2 = buttonState

        if event.button == self.button_keys['PS']:
           Button.PS = buttonState
        if event.button == self.button_keys['share']:
            Button.share = buttonState
        if event.button == self.button_keys['options']:
            Button.options = buttonState
            


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




    
 
