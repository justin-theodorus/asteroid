import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField  # Don't forget this import!

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    
    # Create all groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Set up containers for all classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)  # Note the comma to make it a tuple!
    
    # Create instances
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()  # This will spawn asteroids automatically
    
    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for asteroid in asteroids:
            if player.check_collisions(asteroid):
                print("Game Over!")
                exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collisions(asteroid):
                    asteroid.split()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = time.tick(60) / 1000

if __name__ == "__main__":
    main()