import pygame
import random
from sys import exit

class Player:
    
    y_plyer = 50
    b = pygame.image.load('Images/Bird3.png')
    bird = pygame.transform.scale(b, (40, 40))
    bird_rect = bird.get_rect(topleft = (50, y_plyer))

    

    



class Game:
    
    pipeG_y_pos = random.randint(18, 65)*10
    pipeD_y_pos = pipeG_y_pos - 920
    
    pipeG2_y_pos = random.randint(18, 65)*10
    pipeD2_y_pos = pipeG2_y_pos - 920 
     
    width = 500
    height = 800
    pygame = pygame
    screen = None
    
    
    
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
    
    pG2 = pygame.image.load('Images/PipeG.png')
    pipeG2 = pygame.transform.scale(pG2, (60, 800))
    pipeG2_x_pos = 750
    #pipeG_y_pos = 400

    pD2 = pygame.image.load('Images/PipeD.png')
    pipeD2 = pygame.transform.scale(pD2, (60, 800))
    pipeD2_x_pos = 750
    #pipeD_y_pos = 0




    #Zde budou rectangle

    ground_rec = ground.get_rect(topleft = (ground_x_pos, 700))
    pipeG_rec = pipeG.get_rect(topleft = (pipeG_x_pos, pipeG_y_pos))
    pipeD_rec = pipeD.get_rect(topleft = (pipeD_x_pos, pipeD_y_pos))
    pipeG2_rec = pipeG2.get_rect(topleft = (pipeG2_x_pos, pipeG2_y_pos))
    pipeD2_rec = pipeD2.get_rect(topleft = (pipeD2_x_pos,pipeD2_y_pos))
    
    
    clock = pygame.time.Clock()
    
    @staticmethod
    def start():
        Game.pygame.init()
        Game.screen = Game.pygame.display.set_mode((Game.width, Game.height))

        icone = Game.pygame.image.load('Images/Icone.png')

        Game.pygame.display.set_caption("Flappy Bird")
        Game.pygame.display.set_icon(icone)


        score = 0


    
        
        #Tady je True loop, který se stará o běh hlvaního okna
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print('key')

            if (Game.pipeG_rec.x < -50):
                Game.pipeG_rec.x = 500
                Game.pipeD_rec.x = 500
                Game.pipeG_rec.y = random.randint(18, 65)*10
                Game.pipeD_rec.y = Game.pipeG_rec.y - 920
                
            if (Game.pipeG2_rec.x < -50):
                Game.pipeG2_rec.x = 500
                Game.pipeD2_rec.x = 500
                Game.pipeG2_rec.y = random.randint(18, 65)*10
                Game.pipeD2_rec.y = Game.pipeG2_rec.y - 920


            if (Game.ground_rec.x < -500):
                Game.ground_rec.x = 0
            
            
                
                
            Game.pipeG_rec.x -= 5
            Game.pipeD_rec.x -= 5
            
            Game.pipeG2_rec.x -= 5
            Game.pipeD2_rec.x -= 5
            
            Game.ground_rec.x -= 5


            mouse_pos = pygame.mouse.get_pos()
            if Player.bird_rect.collidepoint(mouse_pos):
                print('coll')

        
                    
            Game.imageLoader()
            pygame.display.update()
            Game.clock.tick(30) 


    #Funkce na načtení obrázků
    def imageLoader():
        Game.screen.blit(Game.back, (Game.back_x_pos, 0))
        Game.screen.blit(Game.pipeG, Game.pipeG_rec)
        Game.screen.blit(Game.pipeD, Game.pipeD_rec)
        Game.screen.blit(Game.pipeG2, Game.pipeG2_rec)
        Game.screen.blit(Game.pipeD2, Game.pipeD2_rec)
        Game.screen.blit(Player.bird, Player.bird_rect)
        Game.screen.blit(Game.ground, Game.ground_rec)








    
        


if __name__ == "__main__":
    Game.start()
    