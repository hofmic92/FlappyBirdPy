import pygame
import random
from sys import exit

class Player:

    gravity = 0
    b1 = pygame.image.load('Images/Bird4.png')
    b2 = pygame.image.load('Images/Bird3.png')
    b3 = pygame.image.load('Images/Bird2.png')
    bird_index = 0
    bird_fly = [b1, b2, b3]

    bird = pygame.transform.scale(bird_fly[int(bird_index)], (40, 40))
    bird_rect = bird.get_rect(topleft = (50, 50))







    score = 0



class Game:
    in_game = False

    pipeG_y_pos = random.randint(23, 59)*10
    pipeD_y_pos = pipeG_y_pos - 920

    pipeG2_y_pos = random.randint(23, 59)*10
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

    def display_score():
        pygame.font.init()
        #Score
        font = pygame.font.Font(None, 50)

        score_surf = font.render(f'Score: {Player.score}', False, (64, 64, 64))
        score_rect = score_surf.get_rect(center = (400, 50))


        Game.screen.blit(score_surf, score_rect)
    time = 0
    clock = pygame.time.Clock()

    @staticmethod
    def start():
        Game.in_game = True
        Game.pygame.init()
        Game.screen = Game.pygame.display.set_mode((Game.width, Game.height))

        icone = Game.pygame.image.load('Images/Icone.png')

        Game.pygame.display.set_caption("Flappy Bird")
        Game.pygame.display.set_icon(icone)






        #Tady je True loop, který se stará o běh hlvaního okna
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if Game.in_game:   
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            Player.gravity = 0
                            Player.gravity -= 6

                else:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        Game.in_game = True

                        Player.score = 0
                        Player.gravity = 0
                        Player.bird_rect = Player.bird.get_rect(topleft = (50, 50))
                        Game.ground_rec = Game.ground.get_rect(topleft = (Game.ground_x_pos, 700))
                        Game.pipeG_rec = Game.pipeG.get_rect(topleft = (Game.pipeG_x_pos, Game.pipeG_y_pos))
                        Game.pipeD_rec = Game.pipeD.get_rect(topleft = (Game.pipeD_x_pos, Game.pipeD_y_pos))
                        Game.pipeG2_rec = Game.pipeG2.get_rect(topleft = (Game.pipeG2_x_pos, Game.pipeG2_y_pos))
                        Game.pipeD2_rec = Game.pipeD2.get_rect(topleft = (Game.pipeD2_x_pos, Game.pipeD2_y_pos))

                        Game.pipeG_y_pos = random.randint(23, 59)*10
                        Game.pipeD_y_pos = Game.pipeG_y_pos - 920
                        Game.pipeG2_y_pos = random.randint(23, 59)*10
                        Game.pipeD2_y_pos = Game.pipeG2_y_pos - 920

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()



            if (Game.pipeG_rec.x < -50):
                Game.pipeG_rec.x = 500
                Game.pipeD_rec.x = 500
                Game.pipeG_rec.y = random.randint(23, 59)*10
                Game.pipeD_rec.y = Game.pipeG_rec.y - 920
                Player.score += 1

            if (Game.pipeG2_rec.x < -50):
                Game.pipeG2_rec.x = 500
                Game.pipeD2_rec.x = 500
                Game.pipeG2_rec.y = random.randint(23, 59)*10
                Game.pipeD2_rec.y = Game.pipeG2_rec.y - 920
                Player.score += 1


            if (Game.ground_rec.x < -500):
                Game.ground_rec.x = 0


            if Game.in_game:    
                #Pohyb trubek
                Game.pipeG_rec.x -= 3
                Game.pipeD_rec.x -= 3

                Game.pipeG2_rec.x -= 3
                Game.pipeD2_rec.x -= 3

                Game.ground_rec.x -= 3

                Player.gravity += 0.35
                Player.bird_index += 0.1
                if Player.bird_index >= len(Player.bird_fly): Player.bird_index = 0
                Player.bird = pygame.transform.scale(Player.bird_fly[int(Player.bird_index)], (40, 40))


                Player.bird_rect.y = Player.bird_rect.y + Player.gravity





                collide = pygame.Rect.colliderect(Player.bird_rect, Game.pipeD_rec)
                collide2 = pygame.Rect.colliderect(Player.bird_rect, Game.pipeG_rec)
                collide3 = pygame.Rect.colliderect(Player.bird_rect, Game.pipeD2_rec)
                collide4 = pygame.Rect.colliderect(Player.bird_rect, Game.pipeG2_rec)
                collide5 = pygame.Rect.colliderect(Player.bird_rect, Game.ground_rec)

                if collide or collide2 or collide3 or collide4 or collide5:
                    Game.in_game = False






                Game.imageLoader()
                Game.display_score()

            else:
                Game.gameOver()

            pygame.display.update()
            Game.clock.tick(60) 


    #Funkce na načtení obrázků
    def imageLoader():
        Game.screen.blit(Game.back, (Game.back_x_pos, 0))
        Game.screen.blit(Game.pipeG, Game.pipeG_rec)
        Game.screen.blit(Game.pipeD, Game.pipeD_rec)
        Game.screen.blit(Game.pipeG2, Game.pipeG2_rec)
        Game.screen.blit(Game.pipeD2, Game.pipeD2_rec)
        Game.screen.blit(Player.bird, Player.bird_rect)
        Game.screen.blit(Game.ground, Game.ground_rec)


    def gameOver():
        pygame.draw.rect(Game.screen, (213, 117, 0), pygame.Rect(50, 180, 400, 460))
        fontGameOver = pygame.font.Font(None, 50)
        textFontGameOver = pygame.font.Font(None, 35)
        text = ['Press SPACE to play again', 'Press ESC to exit game']
        score_surfGameOver = fontGameOver.render(f'Your Score: {Player.score}', False, (64, 64, 64))
        score_rect2GameOver = score_surfGameOver.get_rect(center = (250, 200))
        y = 250
        for x in text:
            text_surfGameOver = textFontGameOver.render(x, False, (64, 64, 64))
            text_rectGameOver = text_surfGameOver.get_rect(center = (250, y))
            Game.screen.blit(text_surfGameOver, text_rectGameOver)
            y = y + 30
        Game.screen.blit(score_surfGameOver, score_rect2GameOver)











if __name__ == "__main__":
    Game.start()