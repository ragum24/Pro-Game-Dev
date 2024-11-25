import pygame,time
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("My Birthay Party Invite")
while True:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            exit()
    image=pygame.image.load("card1.jpg")
    font=pygame.font.SysFont("Times New Roman",50)
    txt=font.render("Darshika's",True,"black")
    txting=font.render("Birthday Party!",True,"black")
    screen.blit(image,(0,0))
    screen.blit(txt,(100,200))
    screen.blit(txting,(200,300))
    pygame.display.update()
    time.sleep(2)

    image=pygame.image.load("card2.jpg")
    font=pygame.font.SysFont("Times New Roman",30)
    txt=font.render("I'm waiting to get amazing presents!",True,"black")
    txting=font.render("(please get me good presents,PLEASE)",True,"black")
    screen.blit(image,(0,0))
    screen.blit(txt,(20,50))
    screen.blit(txting,(40,500))
    pygame.display.update()
    time.sleep(1)