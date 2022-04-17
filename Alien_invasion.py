import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
	""" Общий класс руководящий ресурсами и поведением игры"""
	def __init__(self):
		""" game and resourses initializing"""
		pygame.init()
		self.settings=Settings()
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alein invasion")
		self.ship=Ship(self)

	def run_game(self):
		"""starting main cycles from game"""
		while True:
			self._chek_events()
			self._update_screen()
			
	def _chek_events (self):
		# lookin for keys or mous anyone
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()

	def _update_screen (self):
		"""updating screen"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		#exponiren last painting screen
		pygame.display.flip()




if __name__=='__main__':
	# create new game
	ai=AlienInvasion()
	ai.run_game()

