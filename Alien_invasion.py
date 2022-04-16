import sys
import pygame

class AlienInvasion:
	""" Общий класс руководящий ресурсами и поведением игры"""
	def __init__(self):
		""" game and resourses initializing"""
		pygame.init()
		self.screen = pygame.display.set_mode((1200, 800))
		pygame.display.set_caption("Alein invasion")

	def run_game(self):
		"""starting main cycles from game"""
		while True:
			# lookin for keys or mous anyone
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					sys.exit()

			#exponiren last painting screen
			pygame.display.flip()

if __name__=='__main__':
	# create new game
	ai=AlienInvasion()
	ai.run_game()

