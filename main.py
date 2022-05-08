import pygame
import os
import time
import random

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PEKKEN")

"""Load images for players"""
# Kazumi
KAZUMI = pygame.image.load(os.path.join("images", "kazumi_neutral.png"))

"""Load images for stages"""
# Pink Cherry Blossom
PINK_CHERRY_BLOSSOM = pygame.transform.scale(pygame.image.load(os.path.join("images", "pink_cherry_blossom.jpg")),
                                             (WIDTH, HEIGHT))

class Character():

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.character_img = None
        self.attacks = None

    def draw(self, window):
        window.blit(self.character_img, (self.x, self.y))

class Player1(Character):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.character_img = KAZUMI
        self.mask = pygame.mask.from_surface(self.character_img)


##### LEFT OFF HERE. RESIZE CHARACTERS AND THEN BEGIN MOVEMENT. FIGURE OUT EQUATION TO HAVE BOTTOM OF CHARACTER MEET BOTTOM OF SCREEN
def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    player1 = Player1(0,530)



    def redraw_window():
        WIN.blit(PINK_CHERRY_BLOSSOM, (0, 0))
        player1.draw(WIN)
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run - False

main()