import pygame

class Ship:
	"""Driving Ship class"""
	def __init__(self, ai_game):
		"""initialize ship, and position"""
		self.screen=ai_game.screen
		self.screen_rect=ai_game.screen.get_rect()
		# loading and getting rect for ship
		self.image=pygame.image.load('images/ship.bmp')
		self.rect=self.image.get_rect()
		self.rect.midbottom = self.screen_rect.midbottom

	def blitme (self):
		self.screen.blit(self.image, self.rect)