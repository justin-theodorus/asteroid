from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        #self.containers = (0,0)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    def update(self, dt):
        #forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            up = self.velocity.rotate(random_angle)
            down = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = up * 1.2
            asteroid2.velocity = down * 1.2
