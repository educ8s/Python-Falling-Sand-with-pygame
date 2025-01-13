import pygame, sys, math, random
from simulation import Simulation

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 4
GREY =  (50, 50, 50)

FPS = 100
pygame.init()
pygame.mouse.set_visible(False)  # Hide the cursor


row, column = 0,  0

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Falling Sand")

clock = pygame.time.Clock()
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

def add_particles_square(simulation, row, column, size, probability):
	for row_offset in range(size):
		for col_offset in range(size):
			if random.random() < probability:  # Add particle based on probability
				simulation.add_particle(row + row_offset, column + col_offset)

def erase(simulation, row, column, size):
	for row_offset in range(size):
		for col_offset in range(size):
			simulation.remove_particle(row + row_offset, column + col_offset)

# main loop
while True:
	#1. Event Handling
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:  # Switch to rock particles
				simulation.set_current_mode("rock")
			if event.key == pygame.K_s:  # Switch to sand particles
				simulation.set_current_mode("sand")
			if event.key == pygame.K_SPACE:  # Switch to sand particles
				simulation.restart()
			if event.key == pygame.K_e:  # Switch to sand particles
				simulation.set_current_mode("eraser")
		if event.type == pygame.MOUSEMOTION:
			pos = pygame.mouse.get_pos()
			row = pos[1] // CELL_SIZE
			column = pos[0] // CELL_SIZE

	buttons = pygame.mouse.get_pressed()
	if buttons[0]:  # Left mouse button is pressed
		pos = pygame.mouse.get_pos()
		row = pos[1] // CELL_SIZE
		column = pos[0] // CELL_SIZE

		if simulation.current_mode == "rock":
			add_particles_square(simulation, row, column, size=2, probability = 1)
		elif simulation.current_mode == "sand":
			add_particles_square(simulation, row, column, size = 4, probability = 0.2)
		elif simulation.current_mode == "eraser":
			erase(simulation, row, column, size = 4)  

	#2. Updating State
	simulation.update()

	#3. Drawing
	window.fill(GREY)
	simulation.draw(window)
	# Draw the square indicator around the mouse
	indicator_size = 4 * CELL_SIZE  # Adjust based on mode
	color = (255, 255, 255)  # Default white color

	if simulation.current_mode == "rock":
		color = (100, 100, 100)  # Gray for rock
		indicator_size = 2 * CELL_SIZE
	elif simulation.current_mode == "sand":
		color = (210, 180, 140)  # Sandy color
		indicator_size = 4 * CELL_SIZE
	elif simulation.current_mode == "eraser":
		color = (255, 105, 180) 
		indicator_size = 4 * CELL_SIZE

	pygame.draw.rect(
		window,
		color,
		(column * CELL_SIZE, row * CELL_SIZE, indicator_size, indicator_size))

	pygame.display.flip()
	clock.tick(FPS)
	print(clock.get_fps())