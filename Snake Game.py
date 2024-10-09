#Initiating
import random

import pygame
pygame.init()

#Size of Window
dis_wid,dis_hei = 500,500

#Window
window = pygame.display.set_mode((dis_wid,dis_hei))
pygame.display.set_caption("Snake Game")

#Colours

Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue=(0,0,255)
font_style = pygame.font.SysFont(None,40)
def scoree(score):
    msg = font_style.render("Score :"+str(score), True, Black)
    window.blit(msg, (50,50))
def message(content,posx,posy):
    msg = font_style.render(content,True,Red)
    window.blit(msg,(posx,posy))

def snk(snk_block,snk_list):
    for s in snk_list:
        pygame.draw.rect(window,Black,(s[0],s[1],snk_block,snk_block))

#clock
clock = pygame.time.Clock()

#snk = snake
snk_block = 20
snk_speed = 10
bg2 = pygame.image.load('bg2.jpg')
bg2 = pygame.transform.scale(bg2,(dis_wid,dis_hei))
apple_sound = pygame.mixer.Sound('crunchy-bite-001-86703.mp3')
def gameloop():
    run = True
    close = False
    scores = 0
    foodx = round(random.randrange(0,dis_wid))
    foody = round(random.randrange(0,dis_hei))

    snk_list = []
    snk_len = 1
    x1 =dis_wid/2
    y1 = dis_hei/2
    x2 = 0
    y2 = 0
    while run:

        while close:
            window.fill(White)
            message("You Lost!",dis_wid/3,250)
            message("Press P to Play again",dis_wid/3,300)
            message("Press Q to Quit",dis_wid/3,350)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        gameloop()
                    if event.key == pygame.K_q:
                        close = False
                        run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x2 = -snk_speed
                    y2 = 0
                if event.key == pygame.K_RIGHT:
                    x2 = +snk_speed
                    y2 = 0
                if event.key == pygame.K_UP:
                    y2 = -snk_speed
                    x2 = 0
                if event.key == pygame.K_DOWN:
                    y2 = +snk_speed
                    x2 = 0
        if x1 < 0 or x1 >= dis_wid or y1 < 0 or y1 >= dis_hei:
            close = True
        x1 += x2
        y1 += y2
        window.blit(bg2,(0,0))
        clock.tick(20)
        scoree(scores)
        pygame.draw.rect(window,Red, (foodx, foody, snk_block, snk_block))
        snk_head = [x1,y1]
        snk_list.append(snk_head)
        if len(snk_list)>snk_len:
            del snk_list[0]
        for x in snk_list[:-1]:
            if x == snk_head:
                close = True
        snk(snk_block,snk_list)
        if( x1+snk_block > foodx and x1 < foodx+snk_block and y1+snk_block > foody and y1 < foody+snk_block):
            foodx = round(random.randrange(0, dis_wid))
            foody = round(random.randrange(0, dis_hei))
            snk_len += 1
            scores = scores + 1
            apple_sound.play()
        pygame.display.update()
gameloop()