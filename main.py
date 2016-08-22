import pygame, sys
from pygame.locals import *
from Tkinter import *
from tileset import *

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

DISPLAYSURF = pygame.display.set_mode((1024, 768), 0, 0)

#-----------------FILES IMAGES -------------------------------------
megaImg = pygame.image.load('img/mega.png')
scenaryImg = pygame.image.load('img/BG.png')



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

tile_w = 128
tile_h = 128

width = 200
height = 240

COLOR = (200, 100, 100)

sprite_sheet = pygame.image.load('img/png/walk02.png').convert()
image = pygame.Surface([width, height]	).convert()
image.blit(sprite_sheet, (0, 0), (0, 0, width, height))
image.set_colorkey(COLOR)

image1  = SpriteSheet('img/1.png')
image2  = SpriteSheet('img/2.png')
image3  = SpriteSheet('img/3.png')
image4  = SpriteSheet('img/4.png')
image5  = SpriteSheet('img/5.png')
image6  = SpriteSheet('img/6.png')


image13  = SpriteSheet('img/13.png')
image14  = SpriteSheet('img/14.png')
image15  = SpriteSheet('img/15.png')



mapSet = [
			[0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0],
			[0,0,0,0,13,14,15,0],
			[1,2,2,3,0,0,0,0],
			[4,5,5,6,0,0,0,0]
		]

def drawMap():
	for tile_x in range(0,8):
		for tile_y in range(0, 6):
			if mapSet[tile_y][tile_x] == 1:
				DISPLAYSURF.blit(image1.get_image(0,0,tile_w,tile_h), (0 + (tile_w * tile_x), 0 + (tile_h * tile_y)))
			elif mapSet[tile_y][tile_x] == 2:
				DISPLAYSURF.blit(image2.get_image(0,0,tile_w,tile_h), (0 + (tile_w * tile_x), 0 + (tile_h * tile_y)))
			elif mapSet[tile_y][tile_x] == 3:
				DISPLAYSURF.blit(image3.get_image(0,0,tile_w,tile_h), (0 + (tile_w * tile_x), 0 + (tile_h * tile_y)))
			elif mapSet[tile_y][tile_x] == 4:
				DISPLAYSURF.blit(image4.get_image(0,0,tile_w,tile_h), (0 + (tile_w * tile_x), 0 + (tile_h * tile_y)))
			elif mapSet[tile_y][tile_x] == 5:
				DISPLAYSURF.blit(image5.get_image(0,0,tile_w,tile_h), (0 + (tile_w * tile_x), 0 + (tile_h * tile_y)))
			elif mapSet[tile_y][tile_x] == 6:
				DISPLAYSURF.blit(image6.get_image(0,0,tile_w,tile_h), (0 + (tile_w * tile_x), 0 + (tile_h * tile_y)))
			elif mapSet[tile_y][tile_x] == 13:
				DISPLAYSURF.blit(image13.get_image(0,0,tile_w,93), (0 + (tile_w * tile_x), 0 + (tile_h * tile_y)))
			elif mapSet[tile_y][tile_x] == 14:
				DISPLAYSURF.blit(image14.get_image(0,0,tile_w,93), (0 + (tile_w * tile_x), 0 + (tile_h * tile_y)))
			elif mapSet[tile_y][tile_x] == 15:
				DISPLAYSURF.blit(image15.get_image(0,0,tile_w,93), (0 + (tile_w * tile_x), 0 + (tile_h * tile_y)))

while True:
	DISPLAYSURF.fill(WHITE)
	DISPLAYSURF.blit(scenaryImg, (0, 0))
	#DISPLAYSURF.blit(megaImg, (megaX, megaY))
	#DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	DISPLAYSURF.blit(image, (megaX, megaY))
	#DISPLAYSURF.blit(image1.get_image(1,0,515,435), (0, 0))
	#DISPLAYSURF.blit(image1.get_image(1,0,515,435), (510, 0))
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
