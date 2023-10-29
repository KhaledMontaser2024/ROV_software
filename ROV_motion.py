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
        
        self.thrusters = [None] * 8
    
    def motion_eqn(self):
        self.TFR = (( self.forward_backward / 2) - self.slide - self.up_down + self.roll - self.yaw + self.pitch) * self.max_speed
        self.TFL = (( self.forward_backward / 2) + self.slide - self.up_down - self.roll + self.yaw + self.pitch) * self.max_speed
        self.TBR = ((-self.forward_backward / 2) - self.slide - self.up_down + self.roll + self.yaw - self.pitch) * self.max_speed
        self.TBL = ((-self.forward_backward / 2) + self.slide - self.up_down - self.roll - self.yaw - self.pitch) * self.max_speed
        
        self.BFR = ((-self.forward_backward / 2) - self.slide + self.up_down - self.roll - self.yaw - self.pitch) * self.max_speed
        self.BFL = ((-self.forward_backward / 2) + self.slide + self.up_down + self.roll + self.yaw - self.pitch) * self.max_speed
        self.BBR = (( self.forward_backward / 2) - self.slide + self.up_down - self.roll + self.yaw + self.pitch) * self.max_speed
        self.BBL = (( self.forward_backward / 2) + self.slide + self.up_down + self.roll - self.yaw + self.pitch) * self.max_speed
        
        self.thrusters = [self.TFR, self.TFL, self.TBR, self.TBL, self.BFR, self.BFL, self.BBR, self.BBL]
    
    def add_PID(self):
        x = 0
    
    def check_speed(self):
        max_val = max(map(abs, self.thrusters))
        scale = 1
        
        if max_val > self.max_speed:
            scale = self.max_speed / max_val
        
        self.thrusters = [element * scale for element in self.thrusters]
    
    def output(self):
        self.motion_eqn
        #self.add_PID()
        self.check_speed()          

        return self.thrusters

if __name__ == "__main__":
    
    ROV= motion(2, 1, 1, 0, 0, 0, 200, 0)
    print(ROV.output())
    ROV= motion(2, 1, 1, 0.6, -1, 1, 200, 0)
    print(ROV.output())
    ROV= motion(2, 1, 1, 0.8, -0.3, 0, 200, 0)
    print(ROV.output())
    ROV= motion(2, -1, 1, 0, 0, -0.6, 200, 0)
    print(ROV.output())
    ROV= motion(2, 1, 1, 0.5, -0.8, 0, 200, 0)
    print(ROV.output())
