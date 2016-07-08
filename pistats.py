#!/usr/bin/python
import cgi
import cgitb
import time
import ctypes
import os
import platform
import sys

def get_free_space_mb(dirname):
    """Return folder/drive free space (in megabytes)."""
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(dirname), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value / 1024 / 1024
    else:
        st = os.statvfs(dirname)
        return st.f_bavail * st.f_frsize / 1024 / 1024

cgitb.enable()
import commands
import sys
import string
print "Content-type: text/html\n\n";
mytemp1 = commands.getoutput('/opt/vc/bin/vcgencmd measure_temp | cut -d "=" -f2 | cut -f1')
output = "CPU Temp: " + mytemp1
print output
print "<br>Disk Free: " + str(get_free_space_mb("/")) + "MB"
date = commands.getoutput('date')
print "<br>", date
