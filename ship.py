import pygame


class Ship:
	"""Driving Ship class"""
	def __init__(self, ai_game):
		self.settings=ai_game.settings
		"""initialize ship, and position"""
		self.screen=ai_game.screen
		self.screen_rect=ai_game.screen.get_rect()
		# loading and getting rect for ship
		self.image=pygame.image.load('images/ship.bmp')
		self.rect=self.image.get_rect()
		self.rect.midbottom = self.screen_rect.midbottom
		#Індикатори руху:
		self.moving_right=False
		self.moving_left=False
		self.acceleration=0
		self.x=float(self.rect.x)


	def blitme (self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		#Оновити позицію корабля якщо натиснуті клавіші вправо або вліво
		if self.moving_right:
			self.rect.x+=1+(self.acceleration)//1
			self.acceleration+=self.settings.acceleration_ship
		if self.moving_left:
			self.rect.x-=1+(self.acceleration)//1
			self.acceleration+=self.settings.acceleration_ship
