import time
import pygame

pygame.init()

son1 = pygame.mixer.Sound("14601.wav")
son2 = pygame.mixer.Sound("jul.wav")
#son3 = pygame.mixer.Sound('drum1.mp3')

son1.play(-1)
son2.play()
#son3.play()

cpt = 0
while True:
	cpt+=1
	time.sleep(5)	
