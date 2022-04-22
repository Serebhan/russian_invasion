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
		self.image_move_left=pygame.image.load('images/sokol_move_left.bmp')
		self.image_move_right=pygame.image.load('images/sokol_move_right.bmp')
		self.rect=self.image.get_rect()
		self.rect.midbottom = self.screen_rect.midbottom
		#Індикатори руху:
		self.moving_right=False
		self.moving_left=False
		self.acceleration=0
		self.x=float(self.rect.x)


	def blitme (self):
		if self.moving_right:
			self.screen.blit(self.image_move_right, self.rect)
		elif self.moving_left:
			self.screen.blit(self.image_move_left, self.rect)
		else:
			self.screen.blit(self.image, self.rect)


	def update(self):
		#Оновити позицію корабля якщо натиснуті клавіші вправо або вліво
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x+=self.settings.ship_speed+(self.acceleration)//1
			self.acceleration+=self.settings.acceleration_ship
		if self.moving_left and self.rect.left>0:
			self.x-=self.settings.ship_speed+(self.acceleration)//1
			self.acceleration+=self.settings.acceleration_ship
		#updating rect.x, from x
		self.rect.x=self.x
