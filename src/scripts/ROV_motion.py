# this class is supposed to set the ROV motion by getting the controller inputs and IMU measured angels
# to get the final thrusters speed output as an array of 8 floats call the "output" method and don't forget to pass the new values

import PID_script
class motion:
    def __init__(self, forward_backward, up_down, slide, yaw, pitch, max_speed, reverse_motion, measured_yaw_angle, measured_pitch_angle):
        self.forward_backward = forward_backward         # controller forward    and backward float values range [2 : -2].
        self.up_down = up_down                           # controller up         and down     float values range [1 : -1].
        self.slide = slide                               # controller right      and left     float values range [1 : -1].

        self.yaw = yaw                                   # controller yaw_right  and yaw_left float values range [1 : -1].
        self.pitch = pitch                               # controller pitch_down and pitch_up float values range [1 : -1].
        
        self.max_speed = max_speed                       # controller desired max_speed range [50 : 200].
        self.reverse_motion = reverse_motion             # controller desired view "front camera view set it to 0" "back camera view set it to 1".
        
        self.measured_yaw_angle = measured_yaw_angle     # IMU measured yaw   angel.
        self.measured_pitch_angle = measured_pitch_angle # IMU measured pitch angel.

        self.TFR = 0 # top front right.
        self.TFL = 0 # top front left.
        self.TBR = 0 # top back  right.
        self.TBL = 0 # top back  left.
        
        self.BFR = 0 # bot front right.
        self.BFL = 0 # bot front left. 
        self.BBR = 0 # bot back  right. 
        self.BBL = 0 # bot back  left.
        
        self.yaw_PID   =  PID_script.Pid(self.yaw, self.measured_yaw_angle, self.max_speed)               # making PID_script object to control the yaw.
        self.pitch_PID =  PID_script.Pid(self.pitch, self.measured_pitch_angle, self.max_speed)           # making PID_script object to control the pitch.
        
        self.thrusters = [self.TFR, self.TFL, self.TBR, self.TBL, self.BFR, self.BFL, self.BBR, self.BBL] # making array of 8 floats to make it easier to transsfer thrusters data between the ROV and station.

    # the "motion_eqn" is the main motion method that adds the desired controller speed and direction.
    def motion_eqn(self):
        if self.reverse_motion == 0:                                                                                                 #front camera view "reverse_motion = 0".
            self.thrusters[0] = (( self.forward_backward / 2) - self.slide - self.up_down  - self.yaw + self.pitch) * self.max_speed #TFR.
            self.thrusters[1] = (( self.forward_backward / 2) + self.slide - self.up_down  + self.yaw + self.pitch) * self.max_speed #TFL.
            self.thrusters[2] = ((-self.forward_backward / 2) - self.slide - self.up_down  + self.yaw - self.pitch) * self.max_speed #TBR.
            self.thrusters[3] = ((-self.forward_backward / 2) + self.slide - self.up_down  - self.yaw - self.pitch) * self.max_speed #TBL.
            
            self.thrusters[4] = ((-self.forward_backward / 2) - self.slide + self.up_down  - self.yaw - self.pitch) * self.max_speed #BFR.
            self.thrusters[5] = ((-self.forward_backward / 2) + self.slide + self.up_down  + self.yaw - self.pitch) * self.max_speed #BFL.
            self.thrusters[6] = (( self.forward_backward / 2) - self.slide + self.up_down  + self.yaw + self.pitch) * self.max_speed #BBR.
            self.thrusters[7] = (( self.forward_backward / 2) + self.slide + self.up_down  - self.yaw + self.pitch) * self.max_speed #BBL.
        else:                                                                                                                        #back  camera view "reverse_motion = 1".
            self.thrusters[0] = ((-self.forward_backward / 2) + self.slide - self.up_down  - self.yaw - self.pitch) * self.max_speed #TFR.
            self.thrusters[1] = ((-self.forward_backward / 2) - self.slide - self.up_down  + self.yaw - self.pitch) * self.max_speed #TFL.
            self.thrusters[2] = ((+self.forward_backward / 2) + self.slide - self.up_down  + self.yaw + self.pitch) * self.max_speed #TBR.
            self.thrusters[3] = ((+self.forward_backward / 2) - self.slide - self.up_down  - self.yaw + self.pitch) * self.max_speed #TBL.
            
            self.thrusters[4] = ((+self.forward_backward / 2) + self.slide + self.up_down  - self.yaw + self.pitch) * self.max_speed #BFR.
            self.thrusters[5] = ((+self.forward_backward / 2) - self.slide + self.up_down  + self.yaw + self.pitch) * self.max_speed #BFL.
            self.thrusters[6] = ((-self.forward_backward / 2) + self.slide + self.up_down  + self.yaw - self.pitch) * self.max_speed #BBR.
            self.thrusters[7] = ((-self.forward_backward / 2) - self.slide + self.up_down  - self.yaw - self.pitch) * self.max_speed #BBL.

    # the "add_PID" is the main control method that adds the PID controller output speed on yaw and pitch.
    def add_PID(self):
        yaw_PID_add   = self.yaw_PID.pid_output(self.yaw, self.measured_yaw_angle, self.max_speed)       # yaw   control speed
        pitch_PID_add = self.pitch_PID.pid_output(self.pitch, self.measured_pitch_angle, self.max_speed) # pitch control speed
        
        if self.reverse_motion == 0:                          #front camera view "reverse_motion = 0".
            self.thrusters[0] += -yaw_PID_add + pitch_PID_add #TFR.
            self.thrusters[1] += +yaw_PID_add + pitch_PID_add #TFL.
            self.thrusters[2] += +yaw_PID_add - pitch_PID_add #TBR.
            self.thrusters[3] += -yaw_PID_add - pitch_PID_add #TBL.
            
            self.thrusters[4] += -yaw_PID_add - pitch_PID_add #BFR.
            self.thrusters[5] += +yaw_PID_add - pitch_PID_add #BFL.
            self.thrusters[6] += +yaw_PID_add + pitch_PID_add #BBR.
            self.thrusters[7] += -yaw_PID_add + pitch_PID_add #BBL.
        else:                                                 #back  camera view "reverse_motion = 1".
            self.thrusters[0] += -yaw_PID_add - pitch_PID_add #TFR.
            self.thrusters[1] += +yaw_PID_add - pitch_PID_add #TFL.
            self.thrusters[2] += +yaw_PID_add + pitch_PID_add #TBR.
            self.thrusters[3] += -yaw_PID_add + pitch_PID_add #TBL.
            
            self.thrusters[4] += -yaw_PID_add + pitch_PID_add #BFR.
            self.thrusters[5] += +yaw_PID_add + pitch_PID_add #BFL.
            self.thrusters[6] += +yaw_PID_add - pitch_PID_add #BBR.
            self.thrusters[7] += -yaw_PID_add - pitch_PID_add #BBL.

    # the "check_speed" is the thruster sfety method that checks if the applied speed won't damage the thrusters and then scaling the thrusters speed outputs to achieve the desired motion.
    def check_speed(self):
        max_val = max(map(abs, self.thrusters)) # getting max speed.
        scale = 1

        if max_val > self.max_speed:
            scale = self.max_speed / max_val
        
        self.thrusters = [element * scale for element in self.thrusters]
    # the "output" method is the only method you are going touse in this class as it uses all other methods and then eturning the final output "thrusters" array as 8 floats.
    def output(self, forward_backward, up_down, slide, yaw, pitch, max_speed, reverse_motion, measured_yaw_angle, measured_pitch_angle):
        self.forward_backward = forward_backward
        self.up_down = up_down
        self.slide = slide

        self.yaw = yaw
        self.pitch = pitch

        self.max_speed = max_speed
        self.reverse_motion = reverse_motion
        
        self.measured_yaw_angle = measured_yaw_angle
        self.measured_pitch_angle = measured_pitch_angle

        self.motion_eqn()
        self.add_PID()
        self.check_speed()

        return self.thrusters
