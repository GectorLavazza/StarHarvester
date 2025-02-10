from sys import exit
from time import time

import pygame
from settings import *
from star import Star

from load_image import load_image


def main():
    pygame.init()
    pygame.mouse.set_visible(True)
    pygame.event.set_allowed(
        [pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP, pygame.MOUSEBUTTONDOWN,
         pygame.MOUSEBUTTONUP])

    flags = pygame.DOUBLEBUF | pygame.SCALED
    screen = pygame.display.set_mode(screen_size, flags, depth=8, vsync=1)
    pygame.display.set_caption('Star Harvester')

    clock = pygame.time.Clock()
    last_time = time()

    running = 1

    star = Star(screen, 40, (40, 40, 80), 10)

    image = load_image('img')

    while running:
        dt = time() - last_time
        dt *= 60
        last_time = time()

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = 0

                if event.key == pygame.K_F10:
                    pygame.display.toggle_fullscreen()

        screen.fill((0, 0, 0))

        screen.blit(image, (0, 0))
        star.rect.center = mouse_pos
        star.update(dt)

        pygame.display.update(pygame.Rect(0, 0, WIDTH, HEIGHT))
        clock.tick()

    pygame.quit()
    exit()


if __name__ == '__main__':
    main()
