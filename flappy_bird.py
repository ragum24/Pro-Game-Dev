import pygame,random
from pygame.locals import *
pygame.init()
screen_width=850
screen_height=900
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Flappy Bird")

score=0
game_over=False
bg=pygame.image.load("b_g.jpg")
floor=pygame.image.load("floor.png")
restart=pygame.image.load("restart.png")

class bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__(self)
        self.images=[]
        self.index=0
        self.counter=0
        for i in range(1,4):
            load=pygame.image.load(f'bird_{i}.png')
            self.images.append(load)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
   
    def update(self):
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
    screen.blit(bg,(0,0))
    flock.draw(screen)
    flock.update()
    screen.blit(floor,(0,768))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()



        
    pygame.display.update()