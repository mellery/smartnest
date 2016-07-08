#!/usr/bin/env python
#import RPi.GPIO as GPIO
import pigpio
import time
import sys
import cgi
import cgitb
import ctypes
import os
import platform

cgitb.enable()

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(12, GPIO.OUT)

#p = GPIO.PWM(12, 50)

pi = pigpio.pi()
servo = 12

#p.start(0)

angle = 45 

dc = float(angle)/10.0 + 2.5
print "Content-type: text/html\n\n";
print "<br>Door status: <span style='color:red'>CLOSED</span>"
try:
   #p.ChangeDutyCycle(dc)
   #print dc
   pi.set_servo_pulsewidth(servo, 1250)
   time.sleep(1)
except KeyboardInterrupt:
   pass   
 
#p.stop()
#GPIO.cleanup()
