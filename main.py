import pygame
from simulation import Simulation

GREY = (29, 29, 29)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 6

FPS = 120
pygame.init()
pygame.mouse.set_visible(False)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Falling Sand")

clock = pygame.time.Clock()
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

# main loop
while True:
	#1. Event Handling
	simulation.handle_controls()

	#2. Updating State
	simulation.update()

	#3. Drawing
	window.fill(GREY)
	simulation.draw(window)

	pygame.display.flip()
	clock.tick(FPS)