# GrovePi + Grove Ultrasonic Ranger

from grovepi import *
import bouton
# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND

ultrasonic_ranger = 4


def distance() : 
	return ultrasonicRead(ultrasonic_ranger)

def affichageInstru() :
	test = True
	instru = int
	while test :
		if 10 <= distance() <= 20 : 
			setText_norefresh("Vous êtes en train de choisir la guitare")
			time.sleep(.2)
			instru = 1
		if 21 <= distance() <= 30 : 
			setText_norefresh("Vous êtes en train de choisir le piano")
			time.sleep(.2)
			instru = 2
		if 31 <= distance() <= 40 : 
			setText_norefresh("Vous êtes en train de choisir la batterie")
			time.sleep(.2)
			instru = 3
		if button()==1 :
			test = False
			time.sleep(.2)
	return instru

def choixInstru() :
	if affichageInstru() == 1 : 
		#on charge la banque de donnée de la guitare
	if affichageInstru() == 2 : 
		#on charge la banque de donnée du piano
	if affichageInstru() == 3 : 
		#on charge la banque de donnée de la batterie



