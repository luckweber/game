import pygame, sys
from pygame.locals import *

pygame.init()

#-------------------------BACKGROUND MUSIC-------------------------
pygame.mixer.music.load('sound/Kevin_Hartnell_-_11_-_Earth_and_Stone.mp3')
pygame.mixer.music.play(-1, 0.0)

FPS = 30
fpsClock = pygame.time.Clock()
fpsClock.tick(FPS)

DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)

megaImg = pygame.image.load('img/mega.png')
megaX = 10;
megaY = 10;
direction = 'right'

WHITE = (255, 255, 255)

#-----------------ENCHER O DISPLAY COM BRANCO-----------------
#DISPLAYSURF.fill(WHITE)

RED = (255, 0, 0)
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 40, 40))

pygame.display.set_caption('Hello World!')

while True:
	DISPLAYSURF.fill(WHITE)
	
	
	if direction == 'right':
		megaX +=5
	elif direction == 'down':
		megaY += 5
	elif direction == 'left':
		megaX -= 5
	elif direction == 'up':
		megaY -=4
	
	DISPLAYSURF.blit(megaImg, (megaX, megaY))

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		
		pygame.display.update()	

