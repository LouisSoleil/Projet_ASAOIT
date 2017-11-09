
import grovepi 
import time 
import ultrason as US 
import ecran 
import blueLED
#import acc

button = 3 #le bouton est en D3

grovepi.pinMode(button, "INPUT")

boucle = True 
while boucle : 
	if grovepi.digitalRead(button) == 1 : 
		print ("ca marche")
		ecran.setText_norefresh("Welcome to \nAIR DJ !! ")
		time.sleep(3)
		US.affichageInstru()
		blueLED.allumeB()
		time.sleep(2)
		blueLED.eteindB()
		time.sleep(.2)
		ecran.resetEcran()
		#acc.afficheAcc()
		print ("On a fini")		
		boucle = False
