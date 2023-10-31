# this code  Will print the orientation and calibration data every second.
import logging
import sys
import time
import json
import os
from Adafruit_BNO055 import BNO055


# Create and configure the BNO sensor connection.  Make sure the port number is correct
bno = BNO055.BNO055(serial_port='/dev/ttyUSB0')


# Enable verbose debug logging if -v is passed as a parameter.
if len(sys.argv) == 2 and sys.argv[1].lower() == '-v':
    logging.basicConfig(level=logging.DEBUG)

# Initialize the BNO055 and stop if something went wrong.
if not bno.begin():
    raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')

#save calibration if the file empty if not set the save calibration.
    file = open ('data_stored.json', "r")
    data = json.loads(file.read())
    bno.set_calibration(data)
    file.close()



print('Reading BNO055 data, press Ctrl-C to quit...')
while True:
    # Read the calibration status, 0=uncalibrated and 3=fully calibrated.
    system, gyro, accel, mag = bno.get_calibration_status()
    # Print everything out.
    print('Sys_cal={3} Gyro_cal={4} Accel_cal={5} Mag_cal={6}'.format(system, gyro, accel, mag))
    if(system==3&gyro==3&accel==3&mag==3):
        file = open("data_stored.json", "x")
        calibration_data = bno.get_calibration()
        json.dump(calibration_data, file)
        break
    time.sleep(0.02)