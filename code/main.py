#desole pour les accents, on ne pouvait pas les mettre sinon le code ne compile pas 
import grovepi 
import time 
import ultrason as US 
import ecran
import acc 
import blueLED

button = 3 #le bouton est en D3

grovepi.pinMode(button, "INPUT")

#on definit une fonction recommencer qui va etre utiliser dans le main et qui va permettre a l'utilisateur 
#de pouvoir rejouer d'un instrument sans avoir besoin de redemarrer le dispositif

def recommencer() : 
	reco = 0 
	instru = US.affichageInstru()	#instru est une entier 1,2,3 qui est donne par la fonction affichageInstru et qui permettra de charger de savoir quelle bibliotheque charger
	blueLED.allumeB()
	time.sleep(2)
	blueLED.eteindB()
	time.sleep(.2)
	ecran.resetEcran() #on supprime ce qui etait afficher sur l'ecran 
	acc.afficheAcc(instru)
	ecran.setText_norefresh("Voulez vous recommencer ?")
	time.sleep(2)
	ecran.setText_norefresh("Si oui, maintenez le bouton")
	time.sleep(1)
	while reco != 4 : #on definit une boucle de 4sec qui va permettre a l'utilisateur de choisir s'il veut recommencer ou non
		reco +=1 
		time.sleep(1)
		if grovepi.digitalRead(button) == 1 : #durant cette boucle s'il appuie sur le bouton il recommence depuis le debut de cette fonction et on sort de la boucle
			recommencer()
			reco = 4
	ecran.setText_norefresh ("A bientot !!") #s'il a decide de ne pas recommencer on sort de la fonction recommencer et on continue dans le main
	time.sleep(2)

#ceci est le vrai main

boucle = True 
while boucle : #cette boucle permet d'attendre que l'utilisateur appuie bien sur le bouton pour commencer et pour que le programme ne s'arrete pas avant 
	if grovepi.digitalRead(button) == 1 :
		ecran.setRGB(0,250,130)
		time.sleep(.2)
		ecran.setText_norefresh("Welcome to \nAIR DJ !! ")
		time.sleep(1.5)
		recommencer() #on utilise directement la fonction recommencer pour eviter les redondances de code
		ecran.resetEcran()
		time.sleep(.5)
		ecran.setRGB(0,0,0)
		time.sleep(.5)
		boucle = False
