import pygame, sys
from simulation import Simulation

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 4
GREY =  (50, 50, 50)

FPS = 120
pygame.init()
pygame.mouse.set_visible(False)

row, column = 0, 0

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Falling Sand")

clock = pygame.time.Clock()
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

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
	if buttons[0]:
		pos = pygame.mouse.get_pos()
		row = pos[1] // CELL_SIZE
		column = pos[0] // CELL_SIZE

		if simulation.current_mode == "rock":
			simulation.add_particles_square(row, column, size=2, probability=1)
		elif simulation.current_mode == "sand":
			simulation.add_particles_square(row, column, size=4, probability=0.2)
		elif simulation.current_mode == "eraser":
			simulation.erase(row, column, size=4)

	#2. Updating State
	simulation.update()

	#3. Drawing
	window.fill(GREY)
	simulation.draw(window, row, column)

	pygame.display.flip()
	clock.tick(FPS)