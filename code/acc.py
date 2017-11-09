from adxl345 import ADXL345
import time
import pygame
adxl345 = ADXL345()
    
#def afficheAcc():
listesons=["./../son/b1.wav","./../son/b2.wav","./../son/b3.wav","./../son/b4.wav","./../son/b5.wav","./../son/b6.wav","./../son/b7.wav","./../son/b8.wav","./../son/b9.wav","./../son/b10.wav"]
pygame.init()

drum1 = pygame.mixer.Sound("drum1.mp3")
drum2 = pygame.mixer.Sound("14601.wav")

while True:
	axes = adxl345.getAxes(True)
	print("x = "+str(( axes['x'])) )
	print("y = "+str(( axes['y'] )))
	print("z = "+str(( axes['z'] )))
	
	x = axes['x']
	y = axes['y']
	z = axes['z']


	drum1.play()
	time.sleep(1)
