import pygame
import numpy
import time

pygame.init()
clock = pygame.time.Clock() 
screen = pygame.display.set_mode((600, 600))

dft_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
obj_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

dx = 0
dy = 0
freq = 6
a = 150

inits = [0, numpy.pi/4, numpy.pi/2, numpy.pi]
index = 0

running = True 

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				if index >= (len(inits) - 1):
					index = 0
				else:
					index += 1

			if event.key == pygame.K_s:
				if (index - 1) < 0:
					index = len(inits) - 1
				else:
					index -= 1


	screen.fill("white")

	pygame.draw.circle(screen, 'red', obj_pos, 40)
	dx = a*numpy.cos(freq*(pygame.time.get_ticks()/1000))
	dy = a*numpy.cos(freq*(pygame.time.get_ticks()/1000) + inits[index])
	obj_pos.x = dft_pos.x + dx
	obj_pos.y = dft_pos.y + dy

	keys = pygame.key.get_pressed()

	

	#print(f'dx = {dx}, pos.x = {obj_pos.x}, default_position_x = {dft_pos.x}')
	pygame.display.update()

