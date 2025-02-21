from circleshape import CircleShape
from constants import *
import pygame

class Player(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        #self.containers = (0,0)
        self.timer = 0
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
        self.timer -= dt
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    def shoot(self, dt):
        if self.timer <= 0:
            shot = Shot(self.position)
            speed = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity = speed * PLAYER_SHOOT_SPEED  # Notice: removed dt here
            self.timer = PLAYER_SHOOT_COOLDOWN
class Shot(CircleShape):
    def __init__(self, position):
        super().__init__(position.x, position.y, SHOT_RADIUS)  # Use the constant
        self.velocity = pygame.Vector2(0, 0)
        #self.containers = (0,0)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    def update(self, dt):
        #forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += (self.velocity * dt)