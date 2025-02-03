import pygame,random
from pygame.locals import *
pygame.init()
screen_width=850
screen_height=900
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Flappy Bird")
clock=pygame.time.Clock()
score=0
game_over=False
bg=pygame.image.load("b_g.jpg")
floor=pygame.image.load("floor.png")
restart=pygame.image.load("restart.png")
ground_scroll=0
flying=False

class bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        self.counter=0 #time
        for i in range(1,4):
            img=pygame.image.load(f'bird_{i}.png')
            self.images.append(img)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.clicked=False
        self.speed=0
   
    def update(self):
        if flying==True:
            self.speed+=0.5
            if self.rect.bottom <768:
                self.rect.y+=self.speed
        if game_over==False:
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                self.speed=-10
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked=False


            self.counter+=1
            if self.counter==5:
                self.counter=0
                self.index+=1
                if self.index >= len(self.images):
                    self.index=0
                self.image=self.images[self.index]
flock=pygame.sprite.Group()
flappy=bird(100,300)
flock.add(flappy)

while True:
    clock.tick(60)
    screen.blit(bg,(0,0))
    flock.draw(screen)
    flock.update()
    screen.blit(floor,(ground_scroll,768))
    if game_over==False:

        ground_scroll-=2
        if ground_scroll<-35:
            ground_scroll=0
    if flappy.rect.bottom>=768:
        game_over=True
        flying=False
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN and flying==False and game_over==False:
            flying=True



        
    pygame.display.update()