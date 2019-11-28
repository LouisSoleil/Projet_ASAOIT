import time
from grovepi import *

# Connect the Grove LED to digital port D2
led = 2

pinMode(led,"OUTPUT")
time.sleep(1)



def continueB():
    test = True
    while test : 
        digitalWrite(led,1)
        time.sleep(1)
        if button() == 1 :
            test = False