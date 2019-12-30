import bge
import math
from math import *
import mathutils
import time

import sys
#sys.path.append("/usr/lib/python3/dist-packages")
import serial
import glob

#port=''.join(glob.glob("/dev/ttyACM*"))
#port=''.join(glob.glob("/dev/ttyUSB*"))
#port=''.join(glob.glob("/dev/rfcomm"))  
ser = serial.Serial('COM6',115200)
print("connected to: " + ser.portstr)


