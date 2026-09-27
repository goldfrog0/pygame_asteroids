import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from constants import (PLAYER_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH)
from logger import (log_state)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0.0

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    p1 = Player(x,y,PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    
    #temporary 
    # Game Loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000
        #print(dt)
if __name__ == "__main__":
    main()
