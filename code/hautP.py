import pygame
window_resolution(640,480)
launched = True

pygame.init()
pygame.display.set_caption("Python 42 - jouer son")
window_surface = pygame.display.set_mode(window_resolution)

celtc_song = pygame.mixer.Sound("celtic.ogg")
celtic_song.play()

pygame.display.flip()

while launched : 
	for event in pygame.event.get() : 
		if event.type == pygame.QUIT : 
			launched = False
