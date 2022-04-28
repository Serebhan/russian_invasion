import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""Bullet control class"""
	def __init__(self, ai_game):
		"""Creation bullet objekt in ship plase"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		#self.color= self.settings.bullet_color
		self.rocet_image1 = pygame.image.load('images/rocet1.bmp')
		self.rocet_image2 = pygame.image.load('images/rocet2.bmp')
		self.rocet_image3 = pygame.image.load('images/rocet3.bmp')
		# Create rect for bullet in (0,0) and correct position
		self.rect = self.rocet_image1.get_rect()
		b_x,b_y=ai_game.ship.rect.midtop
		self.rect.midtop = b_x-3,b_y-16
		self.i=0

		#Save bullet position
		self.y=float (self.rect.y)

	def update (self):
		"""running bullet"""
		self.y-=self.settings.bullet_speed
		# save new position bullet
		self.rect.y=self.y 

	def draw_bullet(self):
		"""painting bullen at screen"""
		if self.i==0:
			self.screen.blit(self.rocet_image1, self.rect)
		elif self.i==1:
			self.screen.blit(self.rocet_image2, self.rect)
		else:
			self.screen.blit(self.rocet_image3, self.rect)
			self.i=0
		self.i+=1



		