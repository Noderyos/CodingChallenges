from math import sqrt
from random import randint, random

import pygame
from pygame.locals import *
pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, v):
        self.x = self.x + v.x
        self.y = self.y + v.y

    def sub(self, v):
        self.x = self.x - v.x
        self.y = self.y - v.y

    def mul(self, k):
        self.x = self.x * k
        self.y = self.y * k

    def div(self, k):
        self.x = self.x / k
        self.y = self.y / k

    def normalise(self):
        norm = sqrt(self.x ** 2 + self.y ** 2)
        if norm != 0:
            self.x = self.x / norm
            self.y = self.y / norm

    @property
    def norm(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return f"({self.x}, {self.y})"


class Boid:
    def __init__(self):
        self.position = Vector(randint(10, WIDTH - 10), randint(10, HEIGHT - 10))

        self.velocity = Vector(random()*2-1, random()*2-1)
        self.velocity.normalise()

        self.acceleration = Vector(0, 0)


    def alignment(self, boids):
        average = Vector(0, 0)
        number = 0
        for boid in boids:
            distance = sqrt((boid.position.x - self.position.x)**2 + (boid.position.y - self.position.y)**2)

            if not(boid is self) and distance < 100:
                average.add(boid.velocity)
                number += 1
        if number > 0:
            average.div(number)
            average.sub(self.velocity)
        average.normalise()
        average.mul(0.02)
        return average

    def separation(self, boids):

        average = Vector(0, 0)

        number = 0

        for boid in boids:
            distance = sqrt((boid.position.x - self.position.x) ** 2 + (boid.position.y - self.position.y) ** 2)
            if not (boid is self) and distance < 50:
                difference = Vector(self.position.x, self.position.y)
                difference.sub(boid.position)
                difference.div(distance)
                average.add(difference)
                number += 1
        if number > 0:
            average.div(number)
            average.sub(self.velocity)
        average.normalise()
        average.mul(0.05)
        return average

    def cohesion(self, boids):

        average = Vector(0, 0)
        number = 0
        for boid in boids:
            distance = sqrt((boid.position.x - self.position.x) ** 2 + (boid.position.y - self.position.y) ** 2)

            if not (boid is self) and distance < 150:
                average.add(boid.position)
                number += 1
        if number > 0:
            average.div(number)
            average.sub(self.position)
            average.sub(self.velocity)
        average.normalise()
        average.mul(0.01)
        return average

    def update(self, boids):
        self.position.add(self.velocity)
        self.acceleration.mul(0)

        self.acceleration.add(self.alignment(boids))
        self.acceleration.add(self.separation(boids))
        self.acceleration.add(self.cohesion(boids))



        if self.position.x > (WIDTH-10):
            self.velocity.x = -self.velocity.x
        if self.position.x < 10:
            self.velocity.x = -self.velocity.x

        if self.position.y > (HEIGHT-10):
            self.velocity.y = -self.velocity.y
        if self.position.y < 10:
            self.velocity.y = -self.velocity.y


        self.velocity.add(self.acceleration)
        self.velocity.normalise()

    def display(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), 3)
