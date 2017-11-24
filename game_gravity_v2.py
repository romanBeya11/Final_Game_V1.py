from scene import *
import sound
import random
import math
import time
A = Action

class MyScene (Scene):
	def setup(self):
		# Setting the background
		# add background color
		self.size_of_screen_x = self.size.x 
		self.size_of_screen_y = self.size.y 
		self.screen_center_x = self.size_of_screen_x / 2
		self.screen_center_y = self.size_of_screen_y / 2
		
		# Creating the bg
		self.background_position = Vector2(self.screen_center_x, self.screen_center_y)
		#background_color = SpriteNode(color = '#49b8ff', position = background_position, parent = self, size = self.size)
		background_image = SpriteNode('./assets/sprites/bg_1.PNG', position = self.background_position, parent = self, size = self.size)
		
		'''# Creating the tiles(the ground)
		self.tile_position = Vector2(self.screen_center_x, self.screen_center_y - 250)
		self.tile = SpriteNode('plf:Ground_GrassMid' , position = self.tile_position, parent = self, size = self.size / 6, alpha = 0)'''
		#print "", self.tile_position.y
		
		# Boundary Detection
		# Setting the ground height
		self.height_of_ground = 262
		# Setting the top of screen boundary
		self.top_of_screen_boundary = 650
		# Left side of screen
		self.left_side_of_screen_boundary = self.screen_center_x - 480
		# Right side of screen
		self.right_side_of_screen_boundary = 980
		
		# Creating the player sprite
		#self.tile_position.y + 127
		self.player_position = Vector2(self.screen_center_x, self.height_of_ground)
		self.player = SpriteNode('plf:AlienBeige_jump', position = self.player_position, parent = self, size = self.size / 6)
		
		# Creating enemy sprites
		self.enemy_position = Vector2(self.screen_center_x + 620, self.height_of_ground) #self.screen_center_y
		self.enemy = SpriteNode('plf:Enemy_Bee_move', position = self.enemy_position, parent = self, size = self.size / 6)
		'''# Enemy Copies
		self.enemy_position_copy = Vector2(self.screen_center_x + 620, self.screen_center_y)
		self.enemy_copy = SpriteNode('plf:Enemy_Bee_move', position = self.enemy_position_copy, parent = self, size = self.size / 6)'''
		
		# Laser Icon
		self.shoot = False
		self.laser = Vector2()
		self.laser.x = self.player_position.x
		self.laser.y = self.player_position.y - 20
		self.laser_shoot = SpriteNode('spc:LaserRed13', position = self.laser, parent = self, alpha = 1, size = self.size / 12)
		
		# Shoot button
		self.attack_button = Vector2(self.screen_center_x + 350, self.height_of_ground - 270)
		self.attack_button_position = SpriteNode('plf:Tile_BridgeB', position = self.attack_button, parent = self, alpha = 0, size = self.size / 3)
		
		# Jump button
		self.jump = False
		self.jump_button = Vector2(self.screen_center_x + 60, self.height_of_ground - 245)
		self.jump_button_position = SpriteNode('plf:Tile_BridgeB', position = self.jump_button, parent = self, alpha = 0, size = self.size / 4)
		
		'''# Creating the health bar
		self.health_bar_position = Vector2(self.player_position.x - 515, self.player_position.y - 100)
		self.health_bar = SpriteNode('./assets/sprites/health_bar_8.PNG', position = self.health_bar_position, parent = self.player, size = self.size / 6)'''
		
		# Creating buttons that cannot be seen
		up_button = Vector2()
		up_button.x = 149.5
		up_button.y = 129.0
		self.up = SpriteNode( 'iob:arrow_up_c_256' ,position = up_button, parent = self, alpha = 0, size = self.size / 8)
		down_button = Vector2()
		down_button.x = 149.5
		down_button.y = 50.5
		self.down = SpriteNode('iob:arrow_down_c_256', position = down_button, parent = self, alpha = 0, size = self.size / 8)
		right_button = Vector2()
		right_button.x = 216.5
		right_button.y = 91.0
		self.right = SpriteNode('iob:arrow_right_c_256', position = right_button, parent = self, alpha = 0, size = self.size / 8)
		left_button = Vector2()
		left_button.x = 90.5
		left_button.y = 91
		self.left = SpriteNode('iob:arrow_left_c_256', position = left_button, parent = self, alpha = 0, size = self.size / 8)
		# Creating wave label
		self.wave_counter = 0
		self.wave_label_position = Vector2(self.screen_center_x + 200, self.screen_center_y + 350)
		self.wave_number = LabelNode(text = 'Wave: ' + str(self.wave_counter), position = self.wave_label_position, parent = self, font  = ('Copperplate', 60))
		
		# Number of times the players has hit the enemy
		self.num_of_hits = 0
	
		# Obviously these wont work at the beginning of the game
		self.player_moved_left = False
		self.player_moved_right = False
		self.player_moved_up = False
		self.player_moved_down = False
		
	def did_change_size(self):
		pass
	
	def enemy_waves(self):
		# Creating enemy waves
		'''# Choosing a random Y value
		rand_num = random.randint(1, 20)
		for i in range(rand_num):
			rand_y = random.randint(0, 320)
			# Set the y value of the enemy to the random value calculated
			self.enemy_position.y = rand_y'''
		if self.enemy_position.x >= self.screen_center_x - 800:
			attack = self.enemy_position.x = self.enemy_position.x - 5
			move_enemy = Action.move_to(attack, self.enemy_position.y)
			self.enemy.run_action(move_enemy)
			# Testing player + enemy collision
			if self.player_position.x == self.enemy_position.x and self.player_position.y == self.enemy_position.y:
				self.num_of_hits = self.num_of_hits + 1
				if self.num_of_hits == 1:
					#self.wave_number.text = 'Wave: ' + str(self.wave_counter)
					self.health_bar = SpriteNode('./assets/sprites/bg_2.PNG', position = self.background_position, parent = self, size = self.size)
					#self.hits_label_position = Vector2(self.screen_center_x + 200, self.screen_center_y + 350)
					#self.hits_num = LabelNode(text = 'Wave: ' + str(self.num_of_hits), position = self.hits_label_position, parent = self, font  = ('Copperplate', 60))
					# Creating enemy sprites
					#self.enemy_position = Vector2(self.screen_center_x + 620, self.screen_center_y)
					#self.enemy = SpriteNode('plf:Enemy_Bee_move', position = self.enemy_position, parent = self, size = self.size / 6)
				elif self.num_of_hits == 2:
					self.health_bar = SpriteNode('./assets/sprites/bg_3.PNG', position = self.background_position, parent = self, size = self.size)
					#self.hits_label_position = Vector2(self.screen_center_x + 200, self.screen_center_y + 350)
					#self.hits_num = LabelNode(text = 'Wave: ' + str(self.num_of_hits), position = self.hits_label_position, parent = self, font  = ('Copperplate', 60))
					#self.wave_number.text = 'Wave: ' + str(self.wave_counter)
					# Creating enemy sprites
					#self.enemy_position = Vector2(self.screen_center_x + 620, self.screen_center_y)
					#self.enemy = SpriteNode('plf:Enemy_Bee_move', position = self.enemy_position, parent = self, size = self.size / 6)
				elif self.num_of_hits == 3:
					self.health_bar = SpriteNode('./assets/sprites/bg_4.PNG', position = self.background_position, parent = self, size = self.size)
					#self.hits_label_position = Vector2(self.screen_center_x + 200, self.screen_center_y + 350)
					#self.hits_num = LabelNode(text = 'Wave: ' + str(self.num_of_hits), position = self.hits_label_position, parent = self, font  = ('Copperplate', 60))
					#self.wave_number.text = 'Wave: ' + str(self.wave_counter)
					# Creating enemy sprites
					#self.enemy_position = Vector2(self.screen_center_x + 620, self.screen_center_y)
					#self.enemy = SpriteNode('plf:Enemy_Bee_move', position = self.enemy_position, parent = self, size = self.size / 6)
				elif self.num_of_hits == 4:
					self.health_bar = SpriteNode('./assets/sprites/bg_5.PNG', position = self.background_position, parent = self, size = self.size)
					self.hits_label_position = Vector2(self.screen_center_x + 200, self.screen_center_y + 350)
					self.hits_num = LabelNode(text = 'Wave: ' + str(self.num_of_hits), position = self.hits_label_position, parent = self, font  = ('Copperplate', 60))
					#self.wave_number.text = 'Wave: ' + str(self.wave_counter)
					# Creating enemy sprites
					#self.enemy_position = Vector2(self.screen_center_x + 620, self.screen_center_y)
					#self.enemy = SpriteNode('plf:Enemy_Bee_move', position = self.enemy_position, parent = self, size = self.size / 6)
				elif self.num_of_hits == 5:
					self.health_bar = SpriteNode('./assets/sprites/bg_6.PNG', position = self.background_position, parent = self, size = self.size)
					self.hits_label_position = Vector2(self.screen_center_x + 200, self.screen_center_y + 350)
					self.hits_num = LabelNode(text = 'Wave: ' + str(self.num_of_hits), position = self.hits_label_position, parent = self, font  = ('Copperplate', 60))
					#self.wave_number.text = 'Wave: ' + str(self.wave_counter)
					# Creating enemy sprites
					#self.enemy_position = Vector2(self.screen_center_x + 620, self.screen_center_y)
					#self.enemy = SpriteNode('plf:Enemy_Bee_move', position = self.enemy_position, parent = self, size = self.size / 6)
				elif self.num_of_hits == 6:
					# Game over
					self.health_bar = SpriteNode('./assets/sprites/bg_7.PNG', position = self.background_position, parent = self, size = self.size)
					self.hits_label_position = Vector2(self.screen_center_x + 200, self.screen_center_y + 350)
					self.hits_num = LabelNode(text = 'Wave: ' + str(self.num_of_hits), position = self.hits_label_position, parent = self, font  = ('Copperplate', 60))
					#self.wave_number.text = 'Wave: ' + str(self.wave_counter)
					# Creating enemy sprites
					#self.enemy_position = Vector2(self.screen_center_x + 620, self.screen_center_y)
					#self.enemy = SpriteNode('plf:Enemy_Bee_move', position = self.enemy_position, parent = self, size = self.size / 6)
					self.player_position.x = self.screen_center_x
					self.player_position.y = self.height_of_ground
					self.enemy_position.x = 2000
				
		if self.enemy_position.x <= self.screen_center_x - 800: #self.screen_center_x - 800
			# Increment the wave cycle
			'''self.wave_counter = self.wave_counter + 1
			if self.wave_counter == 1:
				self.wave_number.text = 'Wave: ' + str(self.wave_counter)
				#self.health_bar = SpriteNode('./assets/sprites/bg_2.PNG', position = self.background_position, parent = self, size = self.size)
			elif self.wave_counter == 2:
				#self.health_bar = SpriteNode('./assets/sprites/bg_3.PNG', position = self.background_position, parent = self, size = self.size)
				self.wave_number.text = 'Wave: ' + str(self.wave_counter)
			elif self.wave_counter == 3:
				#self.health_bar = SpriteNode('./assets/sprites/bg_4.PNG', position = self.background_position, parent = self, size = self.size)
				self.wave_number.text = 'Wave: ' + str(self.wave_counter)
			elif self.wave_counter == 4:
				#self.health_bar = SpriteNode('./assets/sprites/bg_5.PNG', position = self.background_position, parent = self, size = self.size)
				self.wave_number.text = 'Wave: ' + str(self.wave_counter)
			elif self.wave_counter == 5:
				#self.health_bar = SpriteNode('./assets/sprites/bg_6.PNG', position = self.background_position, parent = self, size = self.size)
				self.wave_number.text = 'Wave: ' + str(self.wave_counter)
			elif self.wave_counter == 6:
				# Game over
				#self.health_bar = SpriteNode('./assets/sprites/bg_7.PNG', position = self.background_position, parent = self, size = self.size)
				print "game over"'''
				
			self.enemy.alpha = 0
			self.enemy_position.x = 1700
			time.sleep(0.5)
			self.enemy.alpha = 1
					
	def attack_vector(self):
		'''laser = Vector2()
		laser.x = self.player_position.x
		laser.y = self.player_position.y - 20
		self.laser_shoot = SpriteNode('spc:LaserRed13', position = laser, parent = self, alpha = 1, size = self.size / 12)'''
		laser_move_x = self.player_position.x
		laser_move_y = self.player_position.y
	
		horizontal_velocity = self.player_position.x = self.player_position.x + 5
		laser_move = Action.move_to(horizontal_velocity, self.player_position.y)
		self.laser_shoot.run_action(laser_move)
		if horizontal_velocity >= self.right_side_of_screen_boundary:
			'''laser = Vector2()
			self.laser_shoot = SpriteNode('spc:LaserRed13', position = laser, parent = self, alpha = 1, size = self.size / 12)'''
			self.laser.x = self.player_position.x
			self.laser.y = self.player_position.y - 20
			
	def jumping_jelly_beans(self):
		up = self.player_position.y = self.player_position.y + 10
		player_move = Action.move_to(self.player_position.x, up)
		self.player.run_action(player_move)
	def update(self):
		if self.player_moved_up == True:
			up = self.player_position.y = self.player_position.y + 10
			player_move = Action.move_to(self.player_position.x, up)
			self.player.run_action(player_move)
		if self.player_moved_down == True:
			down = self.player_position.y = self.player_position.y - 10
			player_move = Action.move_to(self.player_position.x, down)
			self.player.run_action(player_move)
		if self.player_moved_right == True:
			right = self.player_position.x = self.player_position.x + 10
			player_move = Action.move_to(right, self.player_position.y)
			self.player.run_action(player_move)
		if self.player_moved_left == True:
			left = self.player_position.x = self.player_position.x - 10
			player_move = Action.move_to(left, self.player_position.x)
			self.player.run_action(player_move)
		
		if self.player_moved_left == True:
			# Moving to the left
			player_move = Action.move_by(-30, 0.0, 0.1)
			self.player.run_action(player_move)
			#if self.player_position.x == self.screen_center_x:
				#self.player_position.x = 1500
				#print "here"
			#left = self.player_position.x = self.player_position.x - 10
			#player_gravity = Action.move_to(left, self.player_position.x)
			#self.player.run_action(player_gravity)
		# moving to the right
		if self.player_moved_right == True:
			# Moving to the right
			player_move = Action.move_by(30, 0.0, 0.1)
			self.player.run_action(player_move)
		# moving up    
		if self.player_moved_up == True:
			player_move = Action.move_by(0.0, -30, 0.1)
			self.player.run_action(player_move)
		# moving down
		if self.player_moved_up == True:
			player_move = Action.move_by(0.0, 30, 0.1)
			self.player.run_action(player_move)
			
		# GRAVITY STARTS HERE!!!!!!!!!!!!!!!
		if self.player_position.y == self.height_of_ground:
			self.player_position.y = self.height_of_ground
		else:
			if self.player_position.y >= self.top_of_screen_boundary:
				self.player_position.y = self.top_of_screen_boundary
			if self.player_position.x >= self.right_side_of_screen_boundary:
				self.player_position.x = self.right_side_of_screen_boundary
			if self.player_position.x <= self.left_side_of_screen_boundary:
				self.player_position.x = self.left_side_of_screen_boundary
			
			# Find the distance between the ground and the players current pos
			distance_to_grnd = self.player_position.y - self.height_of_ground
			if distance_to_grnd <= self.height_of_ground + 20:
				descend = self.player_position.y = self.player_position.y - 4
				action = Action.move_to(self.player_position.x, descend)
				self.player.run_action(action)
				if descend <= self.height_of_ground:
					#self.player_position.x = self.screen_center_x
					self.player_position.y = self.height_of_ground
					#print 'reset NOW'
			elif distance_to_grnd >= self.height_of_ground + 100:
				descend = self.player_position.y = self.player_position.y - 2
				action = Action.move_to(self.player_position.x, descend)
				self.player.run_action(action)
				if descend <= self.height_of_ground:
					#self.player_position.x = self.screen_center_x
					self.player_position.y = self.height_of_ground
					#print 'reset NOW'
			else:
				descend = self.player_position.y = self.player_position.y - 1
				action = Action.move_to(self.player_position.x, descend)
				self.player.run_action(action)
				if descend <= self.height_of_ground:
					#self.player_position.x = self.screen_center_x
					self.player_position.y = self.height_of_ground
					#print 'reset NOW'
		self.enemy_waves()
		if self.shoot == True:
			self.attack_vector()
		if self.jump == True:
			self.jumping_jelly_beans()
	def touch_began(self, touch):
		# check if left or right button, or up or down 
		'''if self.up.frame.contains_point(touch.location):
			self.player_moved_up = True'''
		if self.down.frame.contains_point(touch.location):
			self.player_moved_down = True
		if self.right.frame.contains_point(touch.location):
			self.player_moved_right = True
		if self.left.frame.contains_point(touch.location):
			self.player_moved_left = True
		
		# checking if attack button is oressed
		if self.attack_button_position.frame.contains_point(touch.location):
			self.shoot = True
			
		# Checking for jumping
		if self.jump_button_position.frame.contains_point(touch.location):
			self.jump = True
			
	def touch_moved(self, touch):
		pass
		
	def touch_ended(self, touch):
		self.player_moved_up = False
		self.player_moved_down = False
		self.player_moved_left = False
		self.player_moved_right = False
		self.shoot = False
		self.jump = False
if __name__ == '__main__':
	run(MyScene(), orientation = "Landscape", show_fps=True)
