import pygame
import os
import time
import random

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PEKKEN")

"""Load images for players"""
# Kazumi


"""Load images for stages"""
# Pink Cherry Blossom
PINK_CHERRY_BLOSSOM = pygame.transform.scale(pygame.image.load(os.path.join("images", "pink_cherry_blossom.jpg")),
                                             (WIDTH, HEIGHT))

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(PINK_CHERRY_BLOSSOM, (0, 0))
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run - False

main()