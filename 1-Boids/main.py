from utils import *

import pygame
from pygame.locals import *
from copy import deepcopy

boids = [Boid() for _ in range(50)]

quit = False
clock = pygame.time.Clock()
while not quit:
    pygame.display.set_caption(str(clock.get_fps()))

    # EVENTS
    for event in pygame.event.get():
        if event.type == QUIT:
            quit = True

    u = deepcopy(boids)
    for boid in boids:
        boid.update(u)

    # DISPLAY
    screen.fill((0, 0, 0))

    for boid in boids:
        boid.display()

    pygame.display.update()
    clock.tick(500)
pygame.quit()
