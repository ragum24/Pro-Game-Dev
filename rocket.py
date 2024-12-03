import pygame 
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,600))

bg=pygame.transform.scale(pygame.image.load("spacebg.jpg"),(800,800))
rocket=pygame.image.load("rocket.png")
player_x=200
player_y=200
while player_y < 600:
    y=0
    screen.blit(bg,(0,y))
    y-=10
    if abs(y)>200:
        y=0
    screen.blit(rocket,(player_x,player_y))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.KEYDOWN:

            if event.key==K_UP and player_y > 0:
                player_y-=10
            if event.key==K_DOWN and player_y < 600:
                player_y+=10
            if event.key==K_RIGHT and player_y < 600:
                player_x+=10
            if event.key==K_LEFT and player_y > 0:
                player_x-=10

    player_y+=0.01

    pygame.display.update()