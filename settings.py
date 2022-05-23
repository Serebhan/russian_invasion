

class Settings:
	"""Клас для збереження налаштуваннь."""
	def __init__(self):
		"""Ініціалізувати налаштування гри."""
		# Screen settings
		self.screen_width=1200
		self.screen_height=800
		self.bg_color=(230,230,230)
		# Ship settings
		self.ship_limit = 3
		
		self.button_width = 200
		self.button_height =50
		
		
		#alien settings
		self.fleet_drop_speed=15
		
		
		#explosion flag for alien
		self.bum_flag=False
		# scale for speed game
		self.speedup_scale=1.1
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""init settings not constant"""
		self.ship_speed=1
		self.acceleration_ship=0.25
		self.alien_speed=1
		self.bullet_speed=2
		# for moving individual aliens
		self.random_go=115
		# dir 1 left or -1 right
		self.fleet_direction=1
		self.bullets_allowed=3
		self.alien_points=50

	def increase_speed(self):
		#increase all
		self.ship_speed*=self.speedup_scale
		self.acceleration_ship*=self.speedup_scale
		self.alien_speed*=self.speedup_scale
		self.bullet_speed*=self.speedup_scale
		self.alien_points*=self.speedup_scale
		# for increase we hawe to 
		self.random_go//=(self.speedup_scale/1.085)

		if self.ship_speed >=3.797:
			self.bullets_allowed=5
		elif self.ship_speed >=5:
			self.bullets_allowed=6
		

	def difficulty_level_2 (self):
		self.ship_speed=1.949
		self.acceleration_ship=0.487
		self.alien_speed=1.949
		self.bullet_speed=3.898
		# for moving individual aliens
		self.random_go=104.5
		# dir 1 left or -1 right
		self.fleet_direction=1
		self.bullets_allowed=4
		self.alien_points=97.45

	def difficulty_level_3 (self):
		self.ship_speed=3.797
		self.acceleration_ship=0.949
		self.alien_speed=3.797
		self.bullet_speed=7.5594
		# for moving individual aliens
		self.random_go=94.88
		# dir 1 left or -1 right
		self.fleet_direction=1
		self.bullets_allowed=5
		self.alien_points=189.85




