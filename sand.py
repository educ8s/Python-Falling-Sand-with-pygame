import random
import colorsys

class Particle:
	def __init__(self, row, column):
		self.row = row
		self.column = column
		self.color = self.random_color()

	def random_color(self):
		return (255, 255, 255)

	def update(self, grid):
		pass

class RockParticle(Particle):
		
	def random_color(self):
		hue = random.uniform(0.0, 0.1)  # Slightly reddish/brownish hue
		saturation = random.uniform(0.1, 0.3)  # Low saturation
		value = random.uniform(0.3, 0.5)  # Moderate brightness
		r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
		return int(r * 255), int(g * 255), int(b * 255)

class SandParticle(Particle):
	def random_color(self):
		hue = random.uniform(0.1, 0.12) 
		saturation = random.uniform(0.5, 0.7)
		value = random.uniform(0.6, 0.8)
		r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
		return int(r * 255), int(g * 255), int(b * 255)

	def update(self, grid):
		if grid.is_cell_empty(self.row + 1, self.column):
			grid.move_particle(self.row, self.column, self.row + 1, self.column)
			self.row += 1
		else:
			offsets = [-1, 1]
			random.shuffle(offsets) 
			for offset in [-1, 1]:  
				new_column = self.column + offset
				if (
					grid.is_cell_empty(self.row + 1, new_column) and
					isinstance(grid.get_particle(self.row + 1, self.column), SandParticle)
				):
					grid.move_particle(self.row, self.column, self.row + 1, new_column)
					self.row += 1
					self.column = new_column
					break