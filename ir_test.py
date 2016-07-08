import RPi.GPIO as GPIO
import time
import datetime

from time import sleep

import picamera


irpin = 16

camera = picamera.PiCamera()

GPIO.setmode(GPIO.BOARD)

GPIO.setup(irpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def my_callback(channel):
    event_time = time.time()
    f = open("beambreaks.txt", 'a')
    if GPIO.input(irpin):
        line = str(event_time) + ",close\n"
        f.write(line)
        print event_time, ",\t", "close"
    else:
        line = str(event_time) + ",open\n"
        f.write(line)
        print event_time, ",\t", "open"
        print "recording for 10 seconds"
        camera.start_recording(str(event_time)+'.h264')
        sleep(10)
        camera.stop_recording()
        print "done recording"



GPIO.add_event_detect(irpin, GPIO.BOTH, callback=my_callback, bouncetime=300)  

#GPIO.add_event_detect(irpin, GPIO.FALLING, callback=my_callback, bouncetime=300)  
#GPIO.add_event_detect(irpin, GPIO.RISING, callback=my_callback2, bouncetime=300)  

last_value = GPIO.input(irpin)

try:
    while(1):
        #value = GPIO.input(irpin)
        #if value != last_value:
        #   print datetime.datetime.now().time() , GPIO.input(irpin)
        #last_value = value
        time.sleep(1)    

except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()

