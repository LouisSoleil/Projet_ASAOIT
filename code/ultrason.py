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

# fonction qui renvoie la distance
def distance() : 
	return ultrasonicRead(ultrasonic_ranger)

def affichageInstru() :
	test = True
	instru = int
	ecran.resetEcran()
	ecran.setRGB(0,250,130)
	time.sleep(0.3)
	bouton = False
	ecran.setText_norefresh("Choississez votre instrument")
	time.sleep(2)
	ecran.resetEcran()
	time.sleep(.5)
	while test :
# Si la distance est entre 3 et 20 l'utilisateur choisit la guitare
		while 3 <= distance() <= 20 : 
			ecran.setText_norefresh("Tu choisis \nla guitare")
			time.sleep(.02)
# Si on apuie sur le bouton on sort de la boucle et on renvoie instru = 1
			if grovepi.digitalRead(button) == 1 :
				instru = 1
				test = False
# Si la distance est entre 21 et 30 l'utilisateur choisit le piano
		while 21 <= distance() <= 30 : 
			ecran.setText_norefresh("Tu choisis \nle piano")
			time.sleep(.02)
# Si on apuie sur le bouton on sort de la boucle et on renvoie instru = 2

			if grovepi.digitalRead(button) == 1 :
				instru = 2
				test = False
# Si la distance est entre 31 et 40 l'utilisateur choisit la batterie
		while 31 <= distance() <= 40 :
			ecran.setText_norefresh("Tu choisis \nla batterie")
			time.sleep(.02)
# Si on apuie sur le bouton on sort de la boucle et on renvoie instru = 3

			if grovepi.digitalRead(button) == 1 :
				instru = 3
				test = False
	print(instru)			
	return instru
