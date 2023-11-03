import PID_script
class motion:
    def __init__(self, forward_backward, up_down, slide, yaw, pitch, max_speed, reverse_motion, measured_yaw_angle, measured_pitch_angle):
        self.forward_backward = forward_backward
        self.up_down = up_down
        self.slide = slide

        self.yaw = yaw
        self.pitch = pitch

        self.max_speed = max_speed
        self.reverse_motion = reverse_motion
        
        self.measured_yaw_angle = measured_yaw_angle
        self.measured_pitch_angle = measured_pitch_angle

        self.TFR = 0 # top front right
        self.TFL = 0 # top front left
        self.TBR = 0 # top back  right
        self.TBL = 0 # top back  left
        
        self.BFR = 0 # bot front right
        self.BFL = 0 # bot front left 
        self.BBR = 0 # bot back  right 
        self.BBL = 0 # bot back  left 
        
        self.yaw_PID   =  PID_script.Pid(self.yaw, self.measured_yaw_angle, self.max_speed)
        self.pitch_PID =  PID_script.Pid(self.pitch, self.measured_pitch_angle, self.max_speed)
        
        self.thrusters = [self.TFR, self.TFL, self.TBR, self.TBL, self.BFR, self.BFL, self.BBR, self.BBL]
    
    def motion_eqn(self):
        if self.reverse_control == 0:
            self.thrusters[0] = (( self.forward_backward / 2) - self.slide - self.up_down  - self.yaw + self.pitch) * self.max_speed #TFR
            self.thrusters[1] = (( self.forward_backward / 2) + self.slide - self.up_down  + self.yaw + self.pitch) * self.max_speed #TFL
            self.thrusters[2] = ((-self.forward_backward / 2) - self.slide - self.up_down  + self.yaw - self.pitch) * self.max_speed #TBR
            self.thrusters[3] = ((-self.forward_backward / 2) + self.slide - self.up_down  - self.yaw - self.pitch) * self.max_speed #TBL
            
            self.thrusters[4] = ((-self.forward_backward / 2) - self.slide + self.up_down  - self.yaw - self.pitch) * self.max_speed #BFR
            self.thrusters[5] = ((-self.forward_backward / 2) + self.slide + self.up_down  + self.yaw - self.pitch) * self.max_speed #BFL
            self.thrusters[6] = (( self.forward_backward / 2) - self.slide + self.up_down  + self.yaw + self.pitch) * self.max_speed #BBR
            self.thrusters[7] = (( self.forward_backward / 2) + self.slide + self.up_down  - self.yaw + self.pitch) * self.max_speed #BBL
        else:
            self.thrusters[0] = ((-self.forward_backward / 2) + self.slide - self.up_down  - self.yaw - self.pitch) * self.max_speed #TFR
            self.thrusters[1] = ((-self.forward_backward / 2) - self.slide - self.up_down  + self.yaw - self.pitch) * self.max_speed #TFL
            self.thrusters[2] = ((+self.forward_backward / 2) + self.slide - self.up_down  + self.yaw + self.pitch) * self.max_speed #TBR
            self.thrusters[3] = ((+self.forward_backward / 2) - self.slide - self.up_down  - self.yaw + self.pitch) * self.max_speed #TBL
            
            self.thrusters[4] = ((+self.forward_backward / 2) + self.slide + self.up_down  - self.yaw + self.pitch) * self.max_speed #BFR
            self.thrusters[5] = ((+self.forward_backward / 2) - self.slide + self.up_down  + self.yaw + self.pitch) * self.max_speed #BFL
            self.thrusters[6] = ((-self.forward_backward / 2) + self.slide + self.up_down  + self.yaw - self.pitch) * self.max_speed #BBR
            self.thrusters[7] = ((-self.forward_backward / 2) - self.slide + self.up_down  - self.yaw - self.pitch) * self.max_speed #BBL
    
    def add_PID(self):
        yaw_PID_add = self.yaw_PID.pid_output(self.yaw, self.measured_yaw_angle, self.max_speed)
        pitch_PID_add = self.pitch_PID.pid_output(self.pitch, self.measured_pitch_angle, self.max_speed)
        
        if self.reverse_motion == 0:
            self.thrusters[0] += -yaw_PID_add + pitch_PID_add #TFR
            self.thrusters[1] += +yaw_PID_add + pitch_PID_add #TFL
            self.thrusters[2] += +yaw_PID_add - pitch_PID_add #TBR
            self.thrusters[3] += -yaw_PID_add - pitch_PID_add #TBL
            
            self.thrusters[4] += -yaw_PID_add - pitch_PID_add #BFR
            self.thrusters[5] += +yaw_PID_add - pitch_PID_add #BFL
            self.thrusters[6] += +yaw_PID_add + pitch_PID_add #BBR
            self.thrusters[7] += -yaw_PID_add + pitch_PID_add #BBL
        else:
            self.thrusters[0] += -yaw_PID_add - pitch_PID_add #TFR
            self.thrusters[1] += +yaw_PID_add - pitch_PID_add #TFL
            self.thrusters[2] += +yaw_PID_add + pitch_PID_add #TBR
            self.thrusters[3] += -yaw_PID_add + pitch_PID_add #TBL
            
            self.thrusters[4] += -yaw_PID_add + pitch_PID_add #BFR
            self.thrusters[5] += +yaw_PID_add + pitch_PID_add #BFL
            self.thrusters[6] += +yaw_PID_add - pitch_PID_add #BBR
            self.thrusters[7] += -yaw_PID_add - pitch_PID_add #BBL
    
    def check_speed(self):
        max_val = max(map(abs, self.thrusters))
        scale = 1

        if max_val > self.max_speed:
            scale = self.max_speed / max_val
        
        self.thrusters = [element * scale for element in self.thrusters]
    
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
