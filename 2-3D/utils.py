from math import sin, cos
import pygame
from pygame.locals import *

pygame.init()

WIDTH = 1280
HEIGHT = 720

SCALE = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))

rotationX = lambda A: (
    (1, 0, 0),
    (0, cos(A), -sin(A)),
    (0, sin(A), cos(A))
)

rotationY = lambda A: (
    (cos(A), 0, sin(A)),
    (0, 1, 0),
    (-sin(A), 0, cos(A))
)

rotationZ = lambda A: (
    (cos(A), -sin(A), 0),
    (sin(A), cos(A), 0),
    (0, 0, 1)
)


def matmul(M, v):
    if len(M[0]) != len(v):
        raise Exception("Incompatible Matrix with Vector")

    Vn = [0] * len(M)

    for l in range(len(M)):
        for i in range(len(v)):
            Vn[l] += M[l][i] * v[i]

    return Vn


def vec3d2vec2d(v):
    M = (
        (1/(v[2]+2), 0, 0),
        (0, 1/(v[2]+2), 0)
    )

    return matmul(M, v)


def vec2d2displayVec(v):
    return WIDTH // 2 + v[0] * SCALE, HEIGHT // 2 + v[1] * SCALE
