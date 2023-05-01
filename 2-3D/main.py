from utils import *

import pygame
from pygame.locals import *


clock = pygame.time.Clock()


points = [
    (0.5, 0.5, 0.5),
    (0.5, -0.5, 0.5),
    (-0.5, 0.5, 0.5),
    (-0.5, -0.5, 0.5),
    (0.5, 0.5, -0.5),
    (0.5, -0.5, -0.5),
    (-0.5, 0.5, -0.5),
    (-0.5, -0.5, -0.5),
]

vertices = [
    (0, 1),
    (1, 3),
    (3, 2),
    (2, 0),

    (4, 5),
    (5, 7),
    (7, 6),
    (6, 4),

    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7),
]


quit = False

X, Y, Z = 0.01, 0.02, 0.03

while not quit:
    pygame.display.set_caption(str(clock.get_fps()))

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            quit = True

    for p in range(len(points)):

        px = matmul(rotationX(X), points[p])
        py = matmul(rotationY(Y), px)
        pz = matmul(rotationZ(Z), py)

        points[p] = pz

        pygame.draw.circle(screen, (255, 255, 255), vec2d2displayVec(vec3d2vec2d(pz)), 3)

    for v in vertices:
        pygame.draw.line(screen, (255, 255, 255), vec2d2displayVec(vec3d2vec2d(points[v[0]])), vec2d2displayVec(vec3d2vec2d(points[v[1]])))

    pygame.display.update()
    clock.tick(60)

pygame.quit()