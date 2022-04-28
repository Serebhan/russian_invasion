import pygame.font

class Button:

	def __init__ (self, ai_game, msg, x,y,color=(255,255,0)):
		""" initialise button atribute"""
		self.screen=ai_game.screen
		self.screen_rect=self.screen.get_rect()
		self.settings=ai_game.settings

		#button sise and properties
		self.width, self.height = self.settings.button_width, self.settings.button_height
		self.button_color=color
		self.text_color=(50,50,50)
		self.font=pygame.font.SysFont(None, 40)

		# create object rect for button and centering him
		self.rect = pygame.Rect(0,0,self.width,self.height)
		#self.rect.center = self.screen_rect.center
		self.rect.x=x
		self.rect.y=y
		self.mesage=msg

		#print on the button
		self._prep_msg(self.mesage)

	def _prep_msg(self, msg):
		"""text to picture and go in center"""
		self.msg_image=self.font.render(msg, True, self.text_color,
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
	
	def draw_button (self):
		self._prep_msg(self.mesage)
		"""painting batton and text"""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
