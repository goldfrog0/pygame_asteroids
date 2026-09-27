import pygame
from player import Player
from constants import (PLAYER_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH)
from logger import (log_state)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0.0

    #temporary 
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    
    # Game Loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("red")

        p1 = Player(x,y,PLAYER_RADIUS)
        p1.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000
        #print(dt)
if __name__ == "__main__":
    main()
