import pygame
import sys
import random

def print_map(map1):
	for line in map1:
		print(line)

def init():
	snake_map = """
	vvvvvvvvvvvvvv
	v            v
	v            v
	v            v
	v            v
	v            v
	v            v
	v            v
	vvvvvvvvvvvvvv
	"""
	return(snake_map)

def main():
	print('ceeeeee partiiii')

	from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
	pygame.init()

	SCREEN_WIDTH = 800
	SCREEN_HEIGHT = 600
	# Create the screen
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	# Infinite loop
	running = True
	while running:
		for event in pygame.event.get():
			# 2 ways to close the window
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
			elif event.type == QUIT: #red cross
				running = False
		
		screen.fill((255, 255, 255))
		surf = pygame.Surface((50, 50))
		surf.fill((0, 0, 0))
		rect = surf.get_rect()
		screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
		#pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
		
		#affiche display
		pygame.display.flip() 
	
	pygame.quit()
	#pygame.display.set_caption("minimal program")
	#snake_map = init()
	#map1 = snake_map.splitlines()
	#print_map(map1)

if __name__ == "__main__" :
	main()

