import pygame
import os
import time
import random
import sprites

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PEKKEN")


class Character():
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.character_neutral = None
        self.character_down = None

    def draw(self, window):
        window.blit(self.character_neutral, (self.x, self.y))

    def get_width(self):
        return self.character_neutral.get_width()

    def get_height(self):
        return self.character_neutral.get_height()

class Player1(Character):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.character_neutral = sprites.KAZUMI
        self.character_down = sprites.KAZUMI_DOWN
        self.mask = pygame.mask.from_surface(self.character_neutral)





def main():
    is_jump = False
    jump_count = 10
    is_duck = False
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    player = Player1(0,360)
    player_vel = 5
    walkCount = 0

    def redraw_window():
        global walkCount
        WIN.blit(sprites.INFINITE_AZURE_2, (0, 0))
        player.draw(WIN)
        if is_duck:
            player.draw()
        pygame.display.update()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        """PLAYER MOVEMENT"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0: # LEFT
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: # RIGHT
            player.x += player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() < HEIGHT:  # DUCK
            is_duck = True
        if not(is_jump):
            if keys[pygame.K_w] or keys[pygame.K_SPACE] and player.y - player_vel > 0: # UP
                is_jump = True
        else:
            if jump_count >= -10:
                neg = 1
                if jump_count < 0:
                    neg = -1
                player.y -= (jump_count ** 2) * 0.5 * neg
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 10

        clock.tick(FPS)
        redraw_window()




main()