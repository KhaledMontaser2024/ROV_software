#include <Servo.h>

byte thrust_TFR = D3;
byte thrust_TFL = D5;
byte thrust_TBR = D6;
byte thrust_TBL = D9;

byte thrust_BFR = D10;
byte thrust_BFL = D11;
byte thrust_BBR = A0;
byte thrust_BBL = A1;


Servo set_thrust_TFR;
Servo set_thrust_TFL;
Servo set_thrust_TBR;
Servo set_thrust_TBL;

Servo set_thrust_BFR;
Servo set_thrust_BFL;
Servo set_thrust_BBR;
Servo set_thrust_BBL;

void setup()
{
 Serial.begin(9600);
  
 set_thrust_TFR.attach(thrust_TFR);
 set_thrust_TFR.writeMicroseconds(1500);
 
 set_thrust_TFL.attach(thrust_TFL);
 set_thrust_TFL.writeMicroseconds(1500);
 
 set_thrust_TBR.attach(thrust_TBR);
 set_thrust_TBR.writeMicroseconds(1500);
 
 set_thrust_TBL.attach(thrust_TBL);
 set_thrust_TBL.writeMicroseconds(1500);


 set_thrust_BFR.attach(thrust_BFR);
 set_thrust_BFR.writeMicroseconds(1500);

 set_thrust_BFL.attach(thrust_BFL);
 set_thrust_BFL.writeMicroseconds(1500);

 set_thrust_BBR.attach(thrust_BBR);
 set_thrust_BBR.writeMicroseconds(1500);

 set_thrust_BBL.attach(thrust_BBL);
 set_thrust_BBL.writeMicroseconds(1500);

 delay(7000);
}

void loop()
{
  set_thrust_TFR.writeMicroseconds(1500 + );
  set_thrust_TFL.writeMicroseconds(1500 + );
  set_thrust_TBR.writeMicroseconds(1500 + );
  set_thrust_TBL.writeMicroseconds(1500 + );
  
  set_thrust_BFR.writeMicroseconds(1500 + );
  set_thrust_BFL.writeMicroseconds(1500 + );
  set_thrust_BBR.writeMicroseconds(1500 + );
  set_thrust_BBL.writeMicroseconds(1500 + );
}