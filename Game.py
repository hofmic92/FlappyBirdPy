import pygame
import random
from sys import exit

pygame.init()

width = 400
height = 800

icone = pygame.image.load('Images/Icone.png')
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Flappy Bird")
pygame.display.set_icon(icone)

clock = pygame.time.Clock()

#Zde jsou obrazky
bc = pygame.image.load('Images/Background.png')
back = pygame.transform.scale(bc, (400, 800))
g = pygame.image.load('Images/Ground.png')
ground = pygame.transform.scale(g, (400, 200))




#Funkce na načtení obrázků
def imageLoader():
    screen.blit(back, (0, 0))
    screen.blit(ground, (0, 700))




#Tady je True loop, který se stará o běh hlvaního okna
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    imageLoader()
    pygame.display.update()
    clock.tick(15)
    
