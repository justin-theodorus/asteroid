import pygame
from constants import *
from player import Player   

def main():
    pygame.init()
    time = pygame.time.Clock()
    dt = 0
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    #Player.containers = (group_a, group_b)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    updateable.add(player)
    drawable.add(player)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        
        updateable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = time.tick(60) / 1000
        
    



if __name__ == "__main__":
    main()