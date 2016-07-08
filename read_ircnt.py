#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import time

import cgi
import cgitb
import ctypes
import os
import platform
import sys

cgitb.enable()
print("Content-type: text/html\n\n");
#result = instance.read()

f = open("/home/pi/beambreaks.txt", 'r')
contents = f.read()
print("IR Breaks: "+str(contents.count("open")))

