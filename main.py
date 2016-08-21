import pygame, sys
from pygame.locals import *
from Tkinter import *

root = Tk()
pygame.init()

#-------------------------BACKGROUND MUSIC-------------------------
#pygame.mixer.music.load('sound/ryu-theme.mp3')
#pygame.mixer.music.play(-1, 0.0)

FPS = 30
fpsClock = pygame.time.Clock()
fpsClock.tick(FPS)

#---------------------------ICON WINDOW--------------------------
icon = pygame.image.load('img/icon.jpg')
pygame.display.set_icon(icon)

DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)

#-----------------FILES IMAGES -------------------------------------
megaImg = pygame.image.load('img/mega.png')
scenaryImg = pygame.image.load('img/phase-guile.png')



megaX = 10;
megaY = 10;
#direction = 'right'

WHITE = (255, 255, 255)

#-----------------ENCHER O DISPLAY COM BRANCO-----------------
#DISPLAYSURF.fill(WHITE)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BLACK = (0,0,0)

pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 40, 40))

pygame.display.set_caption('Favela Fight')

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (100, 150)

tile_w = 50
tile_h = 50
mapSet = [
			[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
			[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
			[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
			[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
			[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
			[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
			[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
			[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
			[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
			[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
			[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
			[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
		]

def drawMap():
	for tile_x in range(0,16):
		for tile_y in range(0, 12):
			if mapSet[tile_y][tile_x] == 1:
				pygame.draw.rect(DISPLAYSURF, RED, (0 + (tile_w * tile_x), 0 + (tile_y * tile_h), tile_w, tile_h))
			elif mapSet[tile_y][tile_x] == 0:
				pygame.draw.rect(DISPLAYSURF, BLACK, (0 + (tile_w * tile_x), 0 + (tile_h * tile_y), tile_w, tile_h))
				
while True:
	DISPLAYSURF.fill(WHITE)
	DISPLAYSURF.blit(scenaryImg, (0, 0))
	DISPLAYSURF.blit(megaImg, (megaX, megaY))
	
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	drawMap();
	
	for event in pygame.event.get():
		#print (event)
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
				
	if pygame.key.get_pressed()[K_RIGHT] == True:
			megaX +=5
	elif pygame.key.get_pressed()[K_LEFT] == True:
		megaX -=5
	elif pygame.key.get_pressed()[K_DOWN] == True:
		megaY +=5
	elif pygame.key.get_pressed()[K_UP] == True:
		megaY -=5
	
	pygame.display.update()	
	pygame.time.delay(100)
