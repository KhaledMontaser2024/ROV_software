#! /usr/bin/python3

###########################################################################################
## This script is for connecting ps controller to the system and manipulate its output   ##
## to match our needs then creating a ROS node to periodically send commands to the main ##
## system node                                                                           ##
###########################################################################################


import pygame
import rospy
import json
from rov_system.msg import ButtonsStateMessage

class controller():
    def __init__(self) -> None:
        
        #### initializing pygame and controller #####
        pygame.init()
        self.PS_Controller = pygame.joystick.Joystick(0)
        self.PS_Controller.init()
        
        ##############################################

        rospy.init_node("Controller_Node")
        command_publisher=rospy.Publisher("/Controller_to_caiman",ButtonsStateMessage,queue_size=10)

        ########### json file that contains ps keys to easily manipulate them ######## 
        file = open('/home/montaser/catkin_ws/src/rov_system/src/scripts/ps_keys.json', 'r+')
        self.keys = json.load(file)
        ##############################################################################


        self.ButtonsState = ButtonsStateMessage() ## custom ros msg contains all ps keys 
        self.ButtonsState.motion.L1_R1=50
        
        #### to use later in L2 R2 axis combination ######
        self.L2=float()
        self.R2=float()
        ##################################################
        
        ########## main ROS loop #######################
        while not rospy.is_shutdown():
            self.event_type_check()
            command_publisher.publish(self.ButtonsState)
            print(self.ButtonsState.motion)
            
        ################################################

        
    ######### this function checks pygame events and call the corresponding fn ##########  
    def event_type_check(self):
        for event in pygame.event.get():
            if event.type == pygame.JOYHATMOTION and (event.value[0] or event.value[1]): ## arrows events store buttons push and release  
                self.Arrows(event)                                                       ## the additional check is for eliminate release events
            if event.type == pygame.JOYBUTTONDOWN :
                self.Buttons(event)
            if event.type == pygame.JOYAXISMOTION:
                self.Analogs(event)
    #######################################################################################
    
    ############# this fn toggles the state of each button when pressed ###################
    def Buttons(self,event):
        self.ButtonsState.x        ^= event.button == self.keys['x']
        self.ButtonsState.square   ^= event.button == self.keys['square']
        self.ButtonsState.triangle ^= event.button == self.keys['triangle']
        self.ButtonsState.circle   ^= event.button == self.keys['circle']
        
        self.ButtonsState.PS      ^= event.button == self.keys['PS']
        self.ButtonsState.share   ^= event.button == self.keys['share']
        self.ButtonsState.options ^= event.button == self.keys['options']
        
        self.ButtonsState.L3 ^= event.button == self.keys['L3']
        self.ButtonsState.R3 ^= event.button == self.keys['R3']
       
        ######################### R1 and L1 use one variable to change speed taking range from 50 to 200 ##################
        self.ButtonsState.motion.L1_R1 -= 50 * ((event.button == self.keys['L1']) and  (self.ButtonsState.motion.L1_R1>50))
        self.ButtonsState.motion.L1_R1 += 50 * ((event.button == self.keys['R1']) and (self.ButtonsState.motion.L1_R1<200))
    
    ########################################################################################


    ############ this fn toggles the state of each Arrow when pressed ######################
    def Arrows(self,event):
        self.ButtonsState.UpArrow    ^= event.value[1] == self.keys['UpArrow']
        self.ButtonsState.DownArrow  ^= event.value[1] == self.keys['DownArrow']
        self.ButtonsState.LeftArrow  ^= event.value[0] == self.keys['LeftArrow']
        self.ButtonsState.RightArrow ^= event.value[0] == self.keys['RightArrow']
    #########################################################################################


    def Analogs(self,event):
        
        ################# R2 and L2 axises are combined into one axis ####################### 
        if event.axis == self.keys['R2']:
            self.R2 = round(event.value + 1 , 4)
        if event.axis == self.keys['L2']:
            self.L2 = round(event.value + 1 , 4) 
        self.ButtonsState.motion.R2_L2_Axis = self.R2 - self.L2
        ######################################################################################

        ############### right and left analogs manipulation ##################################
        self.ButtonsState.motion.RightAnalog_Up_Down_Axis    =  round(-self.PS_Controller.get_axis(self.keys['RightAnalog_Up_Down_Axis']),4)
        self.ButtonsState.motion.RightAnalog_Left_Right_Axis =  round( self.PS_Controller.get_axis(self.keys['RightAnalog_Left_Right_Axis']),4)
        self.ButtonsState.motion.LeftAnalog_Up_Down_Axis     =  round(-self.PS_Controller.get_axis(self.keys['LeftAnalog_Up_Down_Axis']),4)
        self.ButtonsState.motion.LeftAnalog_Left_Right_Axis  =  round( self.PS_Controller.get_axis(self.keys['LeftAnalog_Left_Right_Axis']),4)
        #######################################################################################


controller()