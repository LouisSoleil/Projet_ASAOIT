import time
from grovepi import *

# Connect the Grove LED to digital port D2
led = 2

pinMode(led,"OUTPUT")

def allumeB():
	digitalWrite(led,1)
    	time.sleep(0.4)

def eteindB():
	digitalWrite(led,0)
	time.sleep(0.4)
