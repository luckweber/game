import pygame, sys
from pygame.locals import *
from Tkinter import *

root = Tk()
pygame.init()

#-------------------------BACKGROUND MUSIC-------------------------
pygame.mixer.music.load('sound/Kevin_Hartnell_-_11_-_Earth_and_Stone.mp3')
pygame.mixer.music.play(-1, 0.0)

FPS = 30
fpsClock = pygame.time.Clock()
fpsClock.tick(FPS)

#---------------------------ICON WINDOW--------------------------
icon = pygame.image.load('img/icon.jpg')
pygame.display.set_icon(icon)

DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)

#-----------------FILES IMAGES -------------------------------------
megaImg = pygame.image.load('img/mega.png')
scenaryImg = pygame.image.load('img/street.jpg')



megaX = 10;
megaY = 10;
#direction = 'right'

WHITE = (255, 255, 255)

#-----------------ENCHER O DISPLAY COM BRANCO-----------------
#DISPLAYSURF.fill(WHITE)

RED = (255, 0, 0)
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 40, 40))

pygame.display.set_caption('Favela Fight')
index = 0

move_right = False



	
while True:
	DISPLAYSURF.fill(WHITE)
	DISPLAYSURF.blit(scenaryImg, (0, 0))
	DISPLAYSURF.blit(megaImg, (megaX, megaY))
	
	
	
	for event in pygame.event.get():
		#print (event)
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if pygame.key.get_pressed()[K_RIGHT]:
				
				#print (event.unicode)
				move_right == True
			elif event.key == K_LEFT: 	
				megaX -=5
			elif event.key == K_UP:
				megaY -=5
			elif event.key == K_DOWN:
				megaY +=5	
		elif event.type == KEYUP:
			move_right = False
			
		
				
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
