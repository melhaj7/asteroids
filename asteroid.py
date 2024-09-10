import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255),
                           self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20, 50)
        vecotr_1 = self.position.rotate(rand_angle)
        vecotr_2 = self.position.rotate(-rand_angle)
        self.radius -= ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid_1.velocity = vecotr_1 * 1.2
        asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid_2.velocity = vecotr_2
