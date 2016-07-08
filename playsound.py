#!/usr/bin/python
import cgi
import cgitb
import time
import ctypes
import os
import platform
import sys

import pygame

cgitb.enable()
import commands
import sys
import string

#mytemp1 = commands.getoutput(' aplay -vv /home/pi/WilhelmScream.wav -D sysdefault:CARD=2')
mytemp1 = commands.getoutput(' aplay /home/pi/portal.wav')

print "Content-type: text/html"
print
print "<html><head><title>CGI</title></head>"
print "<body>"
print "play sound"
print "</body>"
print "</html>"
