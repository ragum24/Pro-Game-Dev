import pygame,random
pygame.init()
screen=pygame.display.set_mode((700,700))
screen.fill("white")
drawing=False
cr="black"
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                drawing=True
                startpos=event.pos
                pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            if event.button==1:
                drawing=False
                pygame.display.update()
        elif event.type==pygame.MOUSEMOTION:
            if drawing:
                currentpos=event.pos
                pygame.draw.line(screen,cr,startpos,currentpos)
                startpos=currentpos
                pygame.display.update()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_h:
             r=random.randint(0,255)
             g=random.randint(0,255)
             b=random.randint(0,255)
             cr=(r,g,b)
             pygame.display.update()