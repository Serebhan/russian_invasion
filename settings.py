class Settings:
	"""Клас для збереження налаштуваннь."""
	def __init__(self):
		"""Ініціалізувати налаштування гри."""
		# Screen settings
		self.screen_width=1200
		self.screen_height=800
		self.bg_color=(230,230,230)
		self.ship_speed=1.5
		self.acceleration_ship=0.02