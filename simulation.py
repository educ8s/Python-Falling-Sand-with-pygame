import pygame, sys, random
from grid import Grid
from particle import SandParticle
from particle import RockParticle

class Simulation:
	def __init__(self, width, height, cell_size):
		self.cell_size = cell_size
		self.grid = Grid(width, height, cell_size)
		self.mode = "sand"
		self.brush_size = 3

	def draw(self, window):
		self.grid.draw(window)
		self.draw_brush(window)

	def add_particle(self, row, column):
	    if self.mode == "sand":
	        if random.random() < 0.2:
	            particle = SandParticle
	            self.grid.add_particle(row, column, particle)
	    elif self.mode == "rock":
	        particle = RockParticle
	        self.grid.add_particle(row, column, particle)

	def update(self):
		orientation = random.randint(0, 1)	
		for row in range(self.grid.rows - 1, -1, -1):
			if orientation == 0:
				for column in range(self.grid.columns - 1, -1, -1):
					self.process_particle(row, column)
			else:
				for column in range(self.grid.columns):
					self.process_particle(row, column)

	def process_particle(self, row, column):
		particle = self.grid.cells[row][column]
		if isinstance(particle, SandParticle):
			new_pos = particle.update(self.grid, row, column)
			if new_pos != (row, column):
				self.grid.set_cell(new_pos[0], new_pos[1], particle)
				self.grid.set_cell(row, column, None)

	def restart(self):
		self.grid.clear()

	def handle_controls(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				self.handle_key(event)
		
		self.handle_mouse()

	def handle_key(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				self.restart()
			elif event.key == pygame.K_s:
				self.mode = "sand"
				print("Sand Mode")
			elif event.key == pygame.K_r:
				self.mode = "rock"
				print("Rock Mode")
			elif event.key == pygame.K_e:
				self.mode = "erase"
				print("Eraser Mode")

	def handle_mouse(self):
		buttons = pygame.mouse.get_pressed()
		if buttons[0]:
			pos = pygame.mouse.get_pos()
			row = pos[1] // self.cell_size
			column = pos[0] // self.cell_size
			self.apply_brush(row, column)

	def apply_brush(self, row, column):
		for r in range(self.brush_size):
			for c in range(self.brush_size):
				current_row = row + r
				current_col = column + c

				if self.mode == "erase":
					self.grid.remove_particle(current_row, current_col)
				else:
					self.add_particle(current_row, current_col)

	def draw_brush(self, window):
		mouse_pos = pygame.mouse.get_pos()
		column = mouse_pos[0] // self.cell_size
		row = mouse_pos[1] // self.cell_size
		cursor_size = self.brush_size * self.cell_size
		color = (255, 255, 255)

		if self.mode == "rock":
			color = (100, 100, 100) 
		elif self.mode == "sand":
			color = (185, 142, 66)  
		elif self.mode == "erase":
			color = (255, 105, 180) 

		pygame.draw.rect(window, color, (column * self.cell_size, row * self.cell_size, cursor_size, cursor_size))