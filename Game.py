import pygame
from sys import exit

pygame.init()

width = 500
height = 800

screen = pygame.display.set_mode((width, height))

icone = pygame.image.load('Images/Icone.png')

pygame.display.set_caption("Flappy Bird")
pygame.display.set_icon(icone)

clock = pygame.time.Clock()

#Zde jsou obrazky
bc = pygame.image.load('Images/Background.png')
back = pygame.transform.scale(bc, (1000, 800))
back_x_pos = 0

g = pygame.image.load('Images/Ground.png')
ground = pygame.transform.scale(g, (1000, 200))
ground_x_pos = 0

pG = pygame.image.load('Images/PipeG3.png')
pipeG = pygame.transform.scale(pG, (50, 400))
pipeG_x_pos = 480




#Funkce na načtení obrázků
def imageLoader():
    screen.blit(back, (back_x_pos, 0))
    screen.blit(pipeG, (pipeG_x_pos, 400))
    screen.blit(ground, (ground_x_pos, 700))




#Tady je True loop, který se stará o běh hlvaního okna
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if (pipeG_x_pos < -50):
        pipeG_x_pos = 500

    if (back_x_pos < -500):
        back_x_pos = 0
    if (ground_x_pos < -500):
        ground_x_pos = 0

    back_x_pos -= 1
    pipeG_x_pos -= 3
    ground_x_pos -= 3
            
    imageLoader()
    pygame.display.update()
    clock.tick(30)
    
