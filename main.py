# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
color = (0,0,0)
def main():
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color)
        player.draw(screen)
        pygame.display.flip()
        dt = Clock.tick()/1000
if __name__ == "__main__":
    main()