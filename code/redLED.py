import time
from grovepi import *

# Connect the Grove LED to digital port D3
led = 3

pinMode(led,"OUTPUT")
time.sleep(1)



def clignoteR():
    test = True
    while test : 
        digitalWrite(led,1)
        time.sleep(0.5)
        digitalWrite(led,0)
        time.sleep(0.5)
        if button() == 1 :
            test = False