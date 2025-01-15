import pygame, random
from sand import SandParticle
from sand import RockParticle

class Grid:
	def __init__(self, width, height, cell_size):
		self.rows = height // cell_size
		self.columns = width // cell_size
		self.cell_size = cell_size
		self.cells = [[None for _ in range(self.columns)] for _ in range(self.rows)]

	def add_particle(self, row, column, particle_class):
		if 0 <= row < self.rows and 0 <= column < self.columns and not self.cells[row][column]:
			self.cells[row][column] = particle_class()

	def draw(self, window):
		for row in range(self.rows):
			for column in range(self.columns):
				particle = self.cells[row][column]
				if particle:
					color = particle.color
					pygame.draw.rect(
						window, color,
						(column * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))

	def is_cell_empty(self, row, column):
		return 0 <= row < self.rows and 0 <= column < self.columns and self.cells[row][column] is None

	def clear(self):
		for row in range(self.rows):
			for column in range(self.columns):
				self.cells[row][column] = None

	def move_particle(self, from_row, from_column, to_row, to_column):
		if self.is_cell_empty(to_row, to_column) and self.cells[from_row][from_column]:
			self.cells[to_row][to_column] = self.cells[from_row][from_column]
			self.cells[from_row][from_column] = None

	def remove_particle(self, row, column):
		if 0 <= row < self.rows and 0 <= column < self.columns:
			self.cells[row][column] = None 