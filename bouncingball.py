import pygame
pygame.init()
w=1000
h=800
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption("Bouncing_ball_4_no_reason")
ball=pygame.draw.circle(surface=screen,color="purple",center=[400,100],radius=30)
ball2=pygame.draw.circle(surface=screen,color="pink",center=[0,200],radius=20)
speed=[1,1]
speed2=[100,100]# x direction speed and y direction speed positive
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.fill("Light Blue")
    ball=ball.move(speed)
    if ball.left<=0 or ball.right>=w:
        speed[0]=-speed[0]
    if ball.top<=0 or ball.bottom>=h:
        speed[1]=-speed[1]
    ball2=ball2.move(speed2)
    if ball2.left<=2 or ball2.right>=w:
        speed2[0]=-speed2[0]
    if ball2.top<=2 or ball2.bottom>=h:
        speed2[1]=-speed2[1]
    pygame.draw.circle(surface=screen,color="purple",center=ball.center,radius=30)
    pygame.draw.circle(surface=screen,color="pink",center=ball2.center,radius=20)
    pygame.display.update()