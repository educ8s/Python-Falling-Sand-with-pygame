import random
import colorsys

class Particle:
	def __init__(self):
		self.color = self.random_color()

	def random_color(self):
		return (255, 255, 255)

	def update(self, grid, row, column):
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

	def update(self, grid, row, column):
		if grid.is_cell_empty(row + 1, column):
			grid.move_particle(row, column, row + 1, column)
		else:
			# Only try diagonal movement if blocked below
			offsets = [-1, 1]
			random.shuffle(offsets)
			for offset in offsets:
				new_column = column + offset
				if grid.is_cell_empty(row + 1, new_column):
					grid.move_particle(row, column, row + 1, new_column)
					break