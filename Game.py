import pygame
import random
from sys import exit


pipeG_y_pos = random.randint(18, 65)*10
pipeD_y_pos = pipeG_y_pos - 920 


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
back = pygame.transform.scale(bc, (500, 800))
back_x_pos = 0

g = pygame.image.load('Images/Ground.png')
ground = pygame.transform.scale(g, (1000, 200))
ground_x_pos = 0

pG = pygame.image.load('Images/PipeG.png')
pipeG = pygame.transform.scale(pG, (60, 800))
pipeG_x_pos = 480
#pipeG_y_pos = 400

pD = pygame.image.load('Images/PipeD.png')
pipeD = pygame.transform.scale(pD, (60, 800))
pipeD_x_pos = 480
#pipeD_y_pos = 0




#Funkce na načtení obrázků
def imageLoader():
    screen.blit(back, (back_x_pos, 0))
    screen.blit(pipeG, (pipeG_x_pos, pipeG_y_pos))
    screen.blit(pipeD, (pipeD_x_pos, pipeD_y_pos))
    screen.blit(ground, (ground_x_pos, 700))




#Tady je True loop, který se stará o běh hlvaního okna
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if (pipeG_x_pos < -50):
        pipeG_x_pos = 500
        pipeD_x_pos = 500
        pipeG_y_pos = random.randint(18, 65)*10
        pipeD_y_pos = pipeG_y_pos - 920


    if (ground_x_pos < -500):
        ground_x_pos = 0
        
        
    pipeG_x_pos -= 5
    pipeD_x_pos -= 5
    ground_x_pos -= 5
            
    imageLoader()
    pygame.display.update()
    clock.tick(30)
    
