import pygame

class GameStats:
	""" Statistic find and save"""

	def __init__(self, ai_game):
		""" Statistic init"""
		self.settings = ai_game.settings
		self.reset_stats()
		self.game_active=False
		self.image=pygame.image.load('images/ship_live.bmp')
		self.screen=ai_game.screen
		self.rect=self.image.get_rect()
		self.rect.y=0
		self.high_score=0
		


	def reset_stats(self):
		""" statistiks change"""
		self.ships_left = self.settings.ship_limit
		self.score=0
		self.level=1


	def life_blit (self):
		for i in range (self.ships_left):
			self.rect.x=self.rect.width*i
			self.screen.blit(self.image, self.rect)

