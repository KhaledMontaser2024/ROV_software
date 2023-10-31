#this code is supposed to handle the pid impelmentaion for the ROv system
# first declare what is required for the class (attributes ) >>constractor
# then the code is done by using metods for each term of the pid three terms,method for calculating error(choosing the smallest error) , one method for the output calculations , 
# final pidoutput method that would be called interally in the motion script.
#finally  a method to determine wheter to turn off i-term or keep it on by changing the sum value to 0 or keep it the same , i will wxplain it as follow :
#the reason that make us clamp the output is mostly the i-term so why don't we just turn it off when the o/p is saturated with a flag that depends on the follows :
#1)if the o/p of the clamping is the same as the o/p before clamping this means there was no saturation so the sat_flag is 0 if not equal the sat_flag is 1 
#2)if the sign of the error is same as the sign of the i-term that means that the i-term is increasing the o/p so the sign_flag  is 1 if not equal the sign_flag  is 0
#3) the i-term  will work if (sat_flag && sign_flag )==1 else it won't work

import time
class Pid():
    def __init__(self,controller_signal,measured_angle) :
        self.controller_signal = controller_signal
        self.ts=.100
        self.tau=.02
        self.measured_angle=measured_angle
        self.error = 0  #e(n)
        self.p_error = 0  #e(n-1)
        self.p_iterm = 0  #previous integral term "I(n-1)"
        self.p_dterm = 0  #previous derivative term "D(n-1)"
        self.sat_flag = 0 #flag to determine if the o/p is saturated
        self.sign_flag = 0 #flag to determine whether the sign of the error is same as the sign of the i-term 
        self.output1 = 0 #''o/p before clamping ''
        self.output2 = 0 #''o/p after clamping ''
        self.kp=0
        self.ki=0
        self.kd = 0
        
    def error_calc(self) :
        
        if (self.controller_signal !=0 ) :
            setpoint = self.measured_angle 
             
        else :
            pass
        if (self.measured_angle < 0  & self.measured_angle  > -180 ) :#choosing the smallest angle 
            {
              self.measured_angle = self.measured_angle + 360   
            }
        elif (self.measured_angle=180 | self.measured_angle=-180 ):
            {
                self.measured_angle= 180
            }
       else :
            {
                self.measured_angle= self.measured_angle
            }
        self.error = setpoint-self.measured_angle #e(n)
        return self.error
            
  
    def p_term(self) : 
        pterm = self.kp * self.error_calc() #P(n)
        
        return pterm
        
    def i_term(self) :
        sum=self.error_calc+ self.p_error
        maxerror = 10 
        minerror = -10 
        if (sum > maxerror) :#windup
            sum = maxerror
        elif (sum < minerror) :
            sum = minerror 
        if (self.sat_flag & self.sign_flag )==1 :#condition to determinr whether the i=term work or not 
            iterm =  ((self.ki *self.ts/2 )*(sum) )+self.p_iterm #I(n)
        else :
            sum = 0 
        self.p_error = self.error_calc() 
        self.p_iterm=iterm
        
        return iterm
        
    def d_term(self):
        
        dterm = (((2*self.kd )/ (2*self.tau +self.ts) )*(self.error_calc()-self.p_error))+((2*self.tau-self.ts )/ (2*self.tau +self.ts))*self.p_dterm #D(n)
        self.p_dterm=dterm 
        return dterm
    
    def output(self) :#method that returns the o/p value
        self.output1 = self.p_term ()+ self.i_term()+ self.d_term() #U(n)= P(n)+I(n)+D(n) ''o/p before clamping ''
        if (self.output1 > self.maxspeed ) : #output clamping
            self.output2= self.maxspeed  
            return self.output2
        elif (self.output1 < self.minspeed):
            self.output2=self.minspeed
            return self.output2
        else :
            return self.output1
            
    def pid_output(self,controller_signal,measured_angle,maxspeed):#final method that would be called
        self.controller_signal = controller_signal
        self.measured_angle=measured_angle
        self.maxspeed = maxspeed #maxoutput limit 
        self.minspeed = -1*maxspeed #minoutput limit 
        self.error_calc()
        self.p_term()
        self.i_term()
        self.d_term()
        self.output()
            

    def clamping(self) :
        if (self.output1 == self.output())  :  
            self.sat_flag = 0 
        else :
            self.sat_flag=1 
        
        if (self.error > 0) & (self.i_term() >0) : 
            self.sign_flag =  1 
        elif (self.error < 0) & (self.i_term() < 0) : 
            self.sign_flag =  1       
        else :
            self.sign_flag =  0

