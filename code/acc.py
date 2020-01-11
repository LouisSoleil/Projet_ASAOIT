from adxl345 import ADXL345
import time
import grovepi
import pygame
import ecran
adxl345 = ADXL345()

button = 3
grovepi.pinMode(button, "INPUT")
    
def afficheAcc(x):
	fin = False
# On initialise la banque de son
	jouer = []
	guitare = ["/home/pi/son/guitare/guitare1.wav","/home/pi/son/guitare/guitare2.wav","/home/pi/son/guitare/guitare3.wav","/home/pi/son/guitare/guitare4.wav","/home/pi/son/guitare/guitare5.wav","/home/pi/son/guitare/guitare6.wav","/home/pi/son/guitare/guitare7.wav","/home/pi/son/guitare/guitare8.wav","/home/pi/son/guitare/guitare9.wav","/home/pi/son/guitare/guitare10.wav","/home/pi/son/guitare/guitare11.wav"]
	piano = ["/home/pi/son/piano/piano1.wav","/home/pi/son/piano/piano2.wav","/home/pi/son/piano/piano3.wav","/home/pi/son/piano/piano4.wav","/home/pi/son/piano/piano5.wav","/home/pi/son/piano/piano6.wav","/home/pi/son/piano/piano7.wav","/home/pi/son/piano/piano8.wav","/home/pi/son/piano/piano9.wav","/home/pi/son/piano/piano10.wav","/home/pi/son/piano/piano11.wav"]
	batterie=["/home/pi/son/b1.wav","/home/pi/son/b2.wav","/home/pi/son/b3.wav","/home/pi/son/b4.wav","/home/pi/son/b5.wav","/home/pi/son/b6.wav","/home/pi/son/b7.wav","/home/pi/son/b8.wav","/home/pi/son/b9.wav","/home/pi/son/b10.wav","/home/pi/son/b11.wav","/home/pi/son/b12.wav"]
	pygame.init()
	a = 0
# En fonction de la valeur de x 
#( qui est renvoye par le capteur ultrason en fonction de la distance )
# jouer prend la valeur de l'instrument souhaite
	if x == 1 : 
		jouer = guitare
	
	if x == 3 : 
		jouer = batterie
	
	if x == 2 :
		jouer = piano

	for i in jouer:
		jouer[a]=pygame.mixer.Sound(i)
		a +=1
	ecran.setText("Vous etes en train de jouer")
	time.sleep(.5)
	while True:
		axes = adxl345.getAxes(True)
# x,y et z prennnent les valeurs de la position dans l'espace de l'accelerometre

		x = axes['x']
		y = axes['y']
		z = axes['z']
# En fonction des differentes position (valeurs de x,y,z)
# On joue un son different
		if -1<x<-0.5:
			jouer[0].play()
		if -0.5<x<0:
        	        jouer[1].play()
		if 0.5<x<0:
        	        jouer[2].play()
		if 1<x<0.5:
        	        jouer[3].play()
		if -1<y<-0.5:
        	        jouer[4].play()
		if -0.5<y<0:
        	        jouer[5].play()
		if 0<y<0.5:
        	        jouer[6].play()
		if 0.5<y<1:
        	        jouer[7].play()
		if -1<z<-0.5:
        	        jouer[8].play()
		if -0.5<z<0:
        	        jouer[9].play()
		if 0<z<0.5:
        	        jouer[10].play()
		if 0.5<z<1:
        	        jouer[10].play()
# Si on appuie sur le bouton on sort de la boucle 
		if grovepi.digitalRead(button) == 1 :
			return fin
