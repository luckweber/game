import pygame

class Sprite:
	def _init_(self, fileName):
		self.sprite_sheet = pygame.image.load(fileName).convert()
	
	
	def