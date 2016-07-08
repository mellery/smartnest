#!/usr/bin/env python
#import RPi.GPIO as GPIO
import pigpio
import time
import datetime

import cgi
import cgitb
import ctypes
import os
import platform
import sys

servo = 12
#pigpio.start()

cgitb.enable()

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(12, GPIO.OUT)

#p = GPIO.PWM(12, 50)

#p.start(0)

pi = pigpio.pi()

angle = 90 

dc = float(angle)/10.0 + 2.5
print "Content-type: text/html\n\n"
print "<br>Door status: <span style='color:green'>OPEN</span>"
try:
   pi.set_servo_pulsewidth(servo, 1500)
   #p.ChangeDutyCycle(dc)
   time.sleep(1)
except KeyboardInterrupt:
   pass   
 
#p.stop()
#GPIO.cleanup()
#pigpio.stop()
