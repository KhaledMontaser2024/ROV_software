class motion:
    def __init__(self, forward_backward, up_down, slide, yaw, pitch, roll, max_speed, reverse_control):
        self.forward_backward = forward_backward
        self.up_down = up_down
        self.slide = slide

        self.yaw = yaw
        self.pitch = pitch
        self.roll = roll

        self.max_speed = max_speed
        self.reverse_control = reverse_control

        self.TFR = 0
        self.TFL = 0
        self.TBR = 0
        self.TBL = 0
        
        self.BFR = 0
        self.BFL = 0
        self.BBR = 0
        self.BBL = 0
    
    def motion_eqn(self):
        self.TFR = (( self.forward_backward / 2) - self.slide - self.up_down + self.roll - self.yaw + self.pitch) * self.max_speed
        self.TFL = (( self.forward_backward / 2) + self.slide - self.up_down - self.roll + self.yaw + self.pitch) * self.max_speed
        self.TBR = ((-self.forward_backward / 2) - self.slide - self.up_down + self.roll + self.yaw - self.pitch) * self.max_speed
        self.TBL = ((-self.forward_backward / 2) + self.slide - self.up_down - self.roll - self.yaw - self.pitch) * self.max_speed
        
        self.BFR = ((-self.forward_backward / 2) - self.slide + self.up_down - self.roll - self.yaw - self.pitch) * self.max_speed
        self.BFL = ((-self.forward_backward / 2) + self.slide + self.up_down + self.roll + self.yaw - self.pitch) * self.max_speed
        self.BBR = (( self.forward_backward / 2) - self.slide + self.up_down - self.roll + self.yaw + self.pitch) * self.max_speed
        self.BBL = (( self.forward_backward / 2) + self.slide + self.up_down + self.roll - self.yaw + self.pitch) * self.max_speed
    
    def output(self):
        
        self.motion_eqn

if __name__ == "__main__":
    
    ROV= motion(2, 1, 1, 0, 0, 0, 200, 0)
