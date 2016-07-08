#!/usr/bin/env python
import glob
import time
import cgi
import cgitb
import ctypes
import os
import platform
import sys

cgitb.enable()


for sensor in glob.glob("/sys/bus/w1/devices/28-00*/w1_slave"):
    id = sensor.split("/")[5]

    try:
        f = open(sensor,"r")
        data = f.read()
        f.close()
	print "Content-type: text/html\n\n";
        if "YES" in data:
            (discard, sep, reading) = data.partition(' t=')
            t = float(reading) / 1000.0
            print("Nest Temp: {:.1f}'C".format(t))
        else:
            print ("999.9")
    except:
        pass



