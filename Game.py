import pygame
import sys

pygame.init()

width = 400
height = 800

screen = pygame.display.set_mode((width, height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pygame.display.flip