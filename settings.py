class Settings:
	"""Клас для збереження налаштуваннь."""
	def __init__(self):
		"""Ініціалізувати налаштування гри."""
		# Screen settings
		self.screen_width=1200
		self.screen_height=800
		self.bg_color=(230,230,230)
		# Sheep settings
		self.ship_speed=1
		self.acceleration_ship=0.25
		# bullet settings
		self.bullet_speed=1
		self.bullet_width=4
		self.bullet_height=15
		self.bullet_color=(60,60,60)
		self.bullets_allowed=3
