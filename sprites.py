import pygame
import os

WIDTH, HEIGHT = 1280, 720

"""Load images for players"""
# Kazumi
KAZUMI = pygame.image.load(os.path.join("images", "kazumi_neutral.png"))
KAZUMI_DOWN = pygame.image.load(os.path.join("images", "kazumi_down.png"))

"""Load images for stages"""
# Infinite Azure 2
INFINITE_AZURE_2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "infinite_azure_2.png")),
                                          (WIDTH, HEIGHT))