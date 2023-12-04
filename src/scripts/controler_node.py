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
from std_msgs.msg import UInt8MultiArray
class controller():
    def __init__(self) -> None:

        #### initializing pygame and controller #####
        pygame.init()
        self.PS_Controller = pygame.joystick.Joystick(0)
        self.PS_Controller.init()
        ##############################################

        rospy.init_node("Controller_Node")
        command_publisher=rospy.Publisher("/Controller_to_caiman",ButtonsStateMessage,queue_size=10)
        auto_publisher=rospy.Publisher("/Controller_to_caiman_auto",ButtonsStateMessage,queue_size=10)

        ########### json file that contains ps keys to easily manipulate them ######## 
        file = open('src/scripts/ps_keys.json', 'r+')
        self.keys = json.load(file)
        ##############################################################################


        self.ButtonsState = ButtonsStateMessage() ## custom ros msg contains all ps keys 
        self.ButtonsState.MotionData.Speed=50
        
        #### to use later in L2 R2 axis combination ######
        self.L2=float()
        self.R2=float()
        ##################################################
        
        ########## main ROS loop #######################
        while not rospy.is_shutdown():
            self.event_type_check()
            command_publisher.publish(self.ButtonsState)
            #print(self.array)
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
    
    ######################## this fn toggles the state of each button when pressed ##########################
    def Buttons(self,event):
        ################# in 4 bits, 4 buttons are toggled when pressed and sent to arduino #################
        self.ButtonsState.ArduinoData ^= ((event.button == self.keys['x'])        << 0)  
        self.ButtonsState.ArduinoData ^= ((event.button == self.keys['square'])   << 1)  
        self.ButtonsState.ArduinoData ^= ((event.button == self.keys['triangle']) << 2) 
        self.ButtonsState.ArduinoData ^= ((event.button == self.keys['circle'])   << 3) 
        #####################################################################################################
        
        ################# in 4 bits, 4 buttons are toggled when pressed and sent to Caiman #################
        self.ButtonsState.CommunicationData ^= ((event.button == self.keys['share'])   << 0) 
        self.ButtonsState.CommunicationData ^= ((event.button == self.keys['options']) << 1) 
        self.ButtonsState.CommunicationData ^= ((event.button == self.keys['L3'])      << 2)
        self.ButtonsState.CommunicationData ^= ((event.button == self.keys['R3'])      << 3)
        #####################################################################################################

        ######################### R1 and L1 use one variable to change speed taking range from 50 to 200 ##################
        self.ButtonsState.MotionData.Speed -= 50 * ((event.button == self.keys['L1']) and (self.ButtonsState.MotionData.Speed>50))
        self.ButtonsState.MotionData.Speed += 50 * ((event.button == self.keys['R1']) and (self.ButtonsState.MotionData.Speed<200))
        ###################################################################################################################
    
        self.ButtonsState.MotionData.Reverse_Control ^= event.button == self.keys['PS'] 
    
    ########################################################################################################################


    ############ this fn toggles the state of each Arrow when pressed ##########################
    def Arrows(self,event): 
        ##in Communication higher nibble arrows are stored and sent to caiman ## Modify for further use 
        self.ButtonsState.CommunicationData ^= ((event.value[1] == self.keys['UpArrow'])    << 4)
        self.ButtonsState.CommunicationData ^= ((event.value[1] == self.keys['DownArrow'])  << 5)  
        self.ButtonsState.CommunicationData ^= ((event.value[0] == self.keys['LeftArrow'])  << 6) 
        self.ButtonsState.CommunicationData ^= ((event.value[0] == self.keys['RightArrow']) << 7) 
    #########################################################################################
    

    def Analogs(self,event):


        ################# R2 and L2 axises are combined into one axis ####################### 
        if event.axis == self.keys['R2']:
            self.R2 = round(event.value + 1 , 4)
        if event.axis == self.keys['L2']:
            self.L2 = round(event.value + 1 , 4) 
        self.ButtonsState.MotionData.Forward_Backward_Axis = self.R2 - self.L2
        ######################################################################################

        ############### right and left analogs manipulation ##################################
        self.ButtonsState.MotionData.Pitch_Axis       =  round(-self.PS_Controller.get_axis(self.keys['RightAnalog_Up_Down_Axis']),4)
        self.ButtonsState.MotionData.Yaw_Axis         =  round( self.PS_Controller.get_axis(self.keys['RightAnalog_Left_Right_Axis']),4)
        self.ButtonsState.MotionData.Up_Down_Axis     =  round(-self.PS_Controller.get_axis(self.keys['LeftAnalog_Up_Down_Axis']),4)
        self.ButtonsState.MotionData.Left_Right_Axis  =  round( self.PS_Controller.get_axis(self.keys['LeftAnalog_Left_Right_Axis']),4)
        #######################################################################################


controller()
