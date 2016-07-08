#!/usr/bin/env python

import glob
import time

for sensor in glob.glob("/sys/bus/w1/devices/28-00*/w1_slave"):
    id = sensor.split("/")[5]

    try:
        f = open(sensor,"r")
        data = f.read()
        f.close()
        if "YES" in data:
            (discard, sep, reading) = data.partition(' t=')
            t = float(reading) / 1000.0
            print("{} {:.1f}".format(id, t))
        else:
            print ("999.9")
    except:
        pass

