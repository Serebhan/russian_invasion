import pygame
from pygame.sprite import Sprite
from random import randint


class Alien (Sprite):
	"""Class for one alien from float"""
	def __init__(self, ai_game):
		""" Initialithing alien and his start position """
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.ai_game=ai_game

		#Load the alien image and set its rect atribute
		self.image=pygame.image.load('images/tu-95.bmp')
		self.image_explosion1=pygame.image.load('images/explosion1.bmp')
		self.image_explosion2=pygame.image.load('images/explosion2.bmp')
		self.image_explosion3=pygame.image.load('images/explosion3.bmp')
		self.rect=self.image.get_rect()

		#Start each new alien near the top left on the screen
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height

		#Store the alien's exact horizontal position
		self.x = float(self.rect.x)

		# get bum_flag from settings
		self.bum_flag=self.settings.bum_flag
		self.bum_number=""
		self.i=0
		


	def chek_edges(self):
		"""get true if alien on the blade"""
		screen_rect = self.screen.get_rect()

		if self.rect.right>=screen_rect.right:
			self.settings.fleet_direction=-1
			return True
		if self.rect.left<=0:
			self.settings.fleet_direction=1
			return True


	def update (self):
		"""Go alien right"""
		self.x +=(self.settings.alien_speed*self.settings.fleet_direction)
		self.rect.x=self.x
		self.rect.y=self.rect.y+randint(0, 100)//self.settings.random_go

		if self.bum_flag:
			self.explosion_alien()



	def explosion_alien (self):
		if self.i==0:
			self.image=self.image_explosion1
		elif self.i==15:
			self.image=self.image_explosion2
		elif self.i==30:
			self.image=self.image_explosion3
		self.i+=1

		if self.i>=30:
			self.ai_game.aliens.remove(self.bum_number)




