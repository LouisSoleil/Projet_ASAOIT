# GrovePi + Grove Ultrasonic Ranger


from grovepi import *
import grovepi
import time
import ecran
import blueLED


# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND
button = 3
grovepi.pinMode(button, "INPUT")

ultrasonic_ranger = 4


def distance() : 
	return ultrasonicRead(ultrasonic_ranger)

def affichageInstru() :
	test = True
	instru = int
	ecran.resetEcran()
	time.sleep(0.3)
	while test :
		while 0 <= distance() <= 20 :
			print("on detecte frere") 
			ecran.setRGB(0,250,130)
			time.sleep(.5)
			ecran.setText_norefresh("Tu choisis \nla guitare")
			time.sleep(.2)
			if grovepi.digitalRead(button) == 1 :
				instru = 1
				test = False
		while 21 <= distance() <= 30 :
			print ("la aussi on detecte")
			ecran.setRGB(0,250,130)
			time.sleep(.5) 
			ecran.setText_norefresh("Tu choisis \nle piano")
			time.sleep(.2)
			if grovepi.digitalRead(button) == 1 :
				instru = 2
				test = False
		while 31 <= distance() <= 40 :
			print ("la aussi bg")
			ecran.setRGB(0,250,130)
			time.sleep(.5)
			ecran.setText_norefresh("Tu choisis \nla batterie")
			time.sleep(.2)
			if grovepi.digitalRead(button) == 1 :
				instru = 3
				test = False
	print(instru)			
	return instru
#def choixInstru(instru) :
#	if instru == 1 : 
#		#on charge la banque de donnee de la guitare
#	if instru == 2 : 
		#on charge la banque de donnee du piano
#	if instru == 3 : 
		#on charge la banque de donnee de la batterie
