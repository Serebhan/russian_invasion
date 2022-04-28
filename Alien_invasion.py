import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from random import randint
from button import Button


class AlienInvasion:
	""" Общий класс руководящий ресурсами и поведением игры"""
	def __init__(self):
		""" game and resourses initializing"""
		pygame.init()
		self.settings=Settings()
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#		self.screen = pygame.display.set_mode((1200,800))
		self.settings.screen_width=self.screen.get_rect().width
		self.settings.screen_height=self.screen.get_rect().height
		pygame.display.set_caption("Бомби пришельцев!")
		self.stats=GameStats(self)
		self.ship=Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens=pygame.sprite.Group()
		self.button_active=1

		self._create_fleet()
		#create button "play":
		self.play_flier=Button(self, "Почати бій!", 
			(self.settings.screen_width/2-self.settings.button_width/2), 
				(self.settings.screen_height/2-self.settings.button_height/2)-
					2*self.settings.button_height,(0, 191, 255))


		self.play_button=Button(self, "Початківець",
			((self.settings.screen_width/2-self.settings.button_width/2)
				-1.5*self.settings.button_width), 
					(self.settings.screen_height/2-self.settings.button_height/2))

		self.play_button2=Button(self, "Гравець", 
			(self.settings.screen_width/2-self.settings.button_width/2), 
				(self.settings.screen_height/2-self.settings.button_height/2))

		self.play_button3=Button(self, "Експерт", 
			(self.settings.screen_width/2-self.settings.button_width/2+
					1.5*self.settings.button_width), 
					(self.settings.screen_height/2-self.settings.button_height/2))


		

	def run_game(self):
		"""starting main cycles from game"""
		while True:
			self._chek_events()
			if self.stats.game_active:
				self.ship.update()
				self._update_aliens()
				self._update_bullets()
			self._update_screen()

	def _ship_hit(self):
		"""ship down reaction"""
		if self.stats.ships_left>0:
			self.stats.ships_left -=1

			self.aliens.empty()
			self.bullets.empty()

			self._create_fleet()
			self.ship.center_ship()

			sleep (0.5)
		else:
			self.stats.game_active=False
			pygame.mouse.set_visible(True)

	def _update_aliens(self):
		"""update aliens position"""
		self._check_fleet_edges()
		self.aliens.update()

		# colision ship and aliens
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()
		# colision aliens and screen down
		self._chek_aliens_bottom()
		# if animation bum is compite, delete alien
		 

	def _create_fleet(self):
		"""Create fleet of the alien"""
		#create alien
		alien=Alien(self)
		alien_width, alien_height=alien.rect.size
		availaible_spase_x = self.settings.screen_width-(2* alien_width)
		number_aliens_x=availaible_spase_x//(2*alien_width)

		#How much line in the screen we need
		ship_height=self.ship.rect.height
		availaible_spase_y=self.settings.screen_height-(3*alien_height)-ship_height
		number_rows = availaible_spase_y//(2*alien_height)
		for row_number in range (number_rows):
			for alien_number in range(number_aliens_x):
				#create alien and standing her in line
				self._create_alien(alien_number, row_number)

	def _check_fleet_edges(self):
		"""reacton for end of screen"""
		for alien in self.aliens.sprites():
			if alien.chek_edges():
				self._change_fleet_direction()

	def _change_fleet_direction(self):
		"""Fleet down"""
		for alien in self.aliens.sprites():
			alien.rect.y+=self.settings.fleet_drop_speed
		
			

	def _create_alien(self, alien_number, row_number):
		alien=Alien(self)
		alien_width, alien_height=alien.rect.size
		alien.x=alien_width+2*alien_width*alien_number#+randint(-15,15) 
		alien.rect.x=alien.x
		alien.rect.y = alien.rect.height+2*alien.rect.height*row_number#+randint(-15,15)
		self.aliens.add(alien)

			 
			
	def _chek_events (self):
		# lookin for keys or mous anyone
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._chek_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._chek_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				self._chek_play_buttons(False, pygame.mouse.get_pos())

	def _chek_play_buttons(self,key, mouse_pos=(0,0)):
		if not self.stats.game_active:
			if self.play_button.rect.collidepoint(mouse_pos) or (self.button_active==0 and key==True):
				self.settings.initialize_dynamic_settings()
				self._game_activ()
			elif self.play_button2.rect.collidepoint(mouse_pos) or (self.button_active==1 and key==True):
				self.settings.difficulty_level_2()
				self._game_activ()
			elif self.play_button3.rect.collidepoint(mouse_pos) or (self.button_active==2 and key==True):
				self.settings.difficulty_level_3()
				self._game_activ()
			

	def _game_activ (self):
		
		self.stats.reset_stats()
		self.stats.game_active=True
		#clear screen
		self.aliens.empty()
		self.bullets.empty()
		#create roundq
		self._create_fleet()
		self.ship.center_ship()
		pygame.mouse.set_visible(False)


	def _chek_keydown_events(self, event):
		"""Keydown probe"""
		if event.key==pygame.K_RIGHT:
			# flay to right side
			if not self.stats.game_active and self.button_active<2:
				self.button_active+=1
			elif not self.stats.game_active and self.button_active>=2:
				self.button_active=0

			self.ship.moving_right=True
		elif event.key==pygame.K_LEFT:
			if not self.stats.game_active and self.button_active>0:
				self.button_active-=1
			elif not self.stats.game_active and self.button_active<=0:
				self.button_active=2
			# flay to left side
			self.ship.moving_left=True
		elif event.key == pygame.K_q or event.key==pygame.K_ESCAPE:
					sys.exit()	
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		elif (event.key==pygame.K_KP_ENTER or event.key==pygame.K_RETURN) and (not self.stats.game_active):
			self._chek_play_buttons(True)


	def _update_bullets(self):
		self.bullets.update()
		#delete  garbage bullets:
		for bullet in self.bullets.copy():
			if bullet.rect.bottom<=0:
				self.bullets.remove(bullet)
		self._chek_bullet_alien_collisions()
		

	def _chek_bullet_alien_collisions(self):
		"""Reaction on colision"""
		collisions= pygame.sprite.groupcollide(self.bullets, self.aliens, False, False)
		for key, wal in collisions.items():
			bum=pygame.sprite.spritecollideany(key,wal)
			if not bum.bum_flag:
				self.bullets.remove(key)
				bum.bum_flag=True
				bum.bum_number=bum
			
		if not self.aliens:
			self.bullets.empty()
			self._create_fleet()
			self.settings.increase_speed()



	def _fire_bullet(self):
		"""Creating new bullet and couple in bullet group"""
		if len(self.bullets)<self.settings.bullets_allowed:
			new_bullet=Bullet(self)
			self.bullets.add(new_bullet)

	def _chek_keyup_events(self, event):
		if event.key==pygame.K_RIGHT: 
			self.ship.moving_right=False
			self.ship.acceleration=0
		elif event.key==pygame.K_LEFT:
			self.ship.moving_left=False
			self.ship.acceleration=0

	def _chek_aliens_bottom(self):
		"""chek csreen end oh alien"""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom>=screen_rect.bottom:
				self._ship_hit()
				break
							

	def _update_screen (self):
		"""updating screen"""
		self.screen.fill(self.settings.bg_color)
		self.aliens.draw(self.screen)
		self.ship.blitme()
		self.stats.life_blit()
		# if game not activity painting button
		if not self.stats.game_active:
			self._create_menu()
			self._update_menu()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		pygame.display.flip()

	def _create_menu(self):
		self.play_flier.draw_button()
		self.play_button.draw_button()
		self.play_button2.draw_button()
		self.play_button3.draw_button()

	def _update_menu(self):
		if self.button_active==0:
			self.play_button.button_color=(255,255,0)
			self.play_button2.button_color=(255,255,150)
			self.play_button3.button_color=(255,255,150)
		elif self.button_active==1:
			self.play_button.button_color=(255,255,150)
			self.play_button2.button_color=(255,255,0)
			self.play_button3.button_color=(255,255,150)
		elif self.button_active==2:
			self.play_button.button_color=(255,255,150)
			self.play_button2.button_color=(255,255,150)
			self.play_button3.button_color=(255,255,0)



		
		



		#exponiren last painting screen
		pygame.display.flip()

	

 


if __name__=='__main__':
	# create new game
	ai=AlienInvasion()
	ai.run_game()

