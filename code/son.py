import pygame
import time 

pygame.init()
fenetre = pygame.display.set_mode((300,300))
son = pygame.mixer.Sound("jul.wav")

continuer = 1 
joue = 0
son.play() 

while continuer:
	for event in pygame.event.get():
		
		#Lancer le son
		if event.type == KEYDOWN and event.key == K_SPACE and joue == 0:
			son.play()
			joue = 1
		#Sortir de pause
		if event.type == KEYDOWN and event.key == K_SPACE and joue == 1:
			pygame.mixer.unpause()
			joue = 0
		#Mettre en pause
		if event.type == KEYUP and event.key == K_SPACE:
			pygame.mixer.pause()
		#Stopper
		if event.type == KEYDOWN and event.key == K_RETURN:
			son.stop()
			joue = 0

