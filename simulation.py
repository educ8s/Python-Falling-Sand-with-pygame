from grid import Grid

class Simulation:
	def __init__(self, width, height, cell_size):
		self.current_mode = "sand"
		self.grid = Grid(width, height, cell_size)

	def set_current_mode(self, mode_type):
		self.current_mode = mode_type

	def update(self):
		for row in range(self.grid.rows - 1, -1, -1):
			for column in range(self.grid.columns):
				particle = self.grid.cells[row][column]
				if particle:
					particle.update(self.grid)

	def remove_particle(self, row, column):
		self.grid.remove_particle(row, column)

	def draw(self, window):
		self.grid.draw(window)

	def restart(self):
		self.grid.clear()

	def add_particle(self, row, column):
		if self.current_mode == "sand":
			self.grid.add_sand_particle(row, column)
		elif self.current_mode == "rock":
			self.grid.add_rock_particle(row, column)