import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((800, 600))

WHITE = (255, 255, 255)
DISPLAYSURF.fill(WHITE)
RED = (255, 0, 0)
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 40, 40))

pygame.display.set_caption('Hello World!')

verdade = 1

while verdade == 1:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		
		pygame.display.update()	

