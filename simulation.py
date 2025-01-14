import random, math, pygame
from grid import Grid
from sand import SandParticle, RockParticle

class Simulation:
	def __init__(self, width, height, cell_size):
		self.current_mode = "sand"
		self.grid = Grid(width, height, cell_size)

	def set_current_mode(self, mode_type):
		if mode_type in ["sand", "rock", "eraser"]:
			self.current_mode = mode_type
		else:
			raise ValueError(f"Invalid mode: {mode_type}")

	def update(self):
		for row in range(self.grid.rows - 1, -1, -1):
			for column in range(self.grid.columns):
				particle = self.grid.cells[row][column]
				if particle:
					particle.update(self.grid)

	def remove_particle(self, row, column):
		self.grid.remove_particle(row, column)

	def draw(self, window, row, column):
		self.grid.draw(window)
		self.draw_cursor(window, row, column)

	def restart(self):
		self.grid.clear()

	def add_particle(self, row, column):
		if self.current_mode == "sand":
			self.grid.add_particle(row, column, SandParticle)
		elif self.current_mode == "rock":
			self.grid.add_particle(row, column, RockParticle)

	def add_particles_square(self, row, column, size, probability):
		for row_offset in range(size):
			for col_offset in range(size):
				if random.random() < probability:
					self.add_particle(row + row_offset, column + col_offset)

	def erase(self, row, column, size):
		for row_offset in range(size):
			for col_offset in range(size):
				self.remove_particle(row + row_offset, column + col_offset)

	def draw_cursor(self, window, row, column):
		
		cursor_size = 4 * self.grid.cell_size
		color = (255, 255, 255)

		if self.current_mode == "rock":
			color = (100, 100, 100) 
			cursor_size = 2 * self.grid.cell_size
		elif self.current_mode == "sand":
			color = (210, 180, 140)  
			cursor_size = 4 * self.grid.cell_size
		elif self.current_mode == "eraser":
			color = (255, 105, 180) 
			cursor_size = 4 * self.grid.cell_size

		pygame.draw.rect(
			window,
			color,
			(column * self.grid.cell_size, row * self.grid.cell_size, cursor_size, cursor_size),
		)