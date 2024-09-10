import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0,0,0))

        pygame.display.flip()
    
    # print("Starting asteroids!")
    # print("Screen width: 1280")
    # print("Screen height: 720")




if __name__ == "__main__":
    main()
