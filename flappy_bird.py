import pygame,random
from pygame.locals import *
pygame.init()
screen_width=850
screen_height=900
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Flappy Bird")
clock=pygame.time.Clock()
score=0
font=pygame.font.SysFont("Times New Roman",60)
game_over=False
pipe_gap=200
pipe_spawn=2500 #milliseconds
last_pipe=pygame.time.get_ticks()-pipe_spawn
bg=pygame.image.load("b_g.jpg")
floor=pygame.image.load("floor.png")
restart=pygame.image.load("restart.png")
pass_pipe=False
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
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False: #left click pressed
                self.clicked=True
                self.speed=-10
            if pygame.mouse.get_pressed()[0]==0: #left click unpressed
                self.clicked=False


            self.counter+=1 
            if self.counter==5:
                self.counter=0
                self.index+=1
                if self.index >= len(self.images):
                    self.index=0
                self.image=self.images[self.index]

class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("pole.png")
        self.rect=self.image.get_rect()
        if pos==1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y-(pipe_gap//2)]
        elif pos==-1:
            self.rect.topleft=[x,y+(pipe_gap//2)]
    def update(self):
        self.rect.x-=4
        if self.rect.x < 0:
            self.kill()

pipes=pygame.sprite.Group()
flock=pygame.sprite.Group()
flappy=bird(100,300)
flock.add(flappy)

while True:
    clock.tick(60)
    screen.blit(bg,(0,0))
    pipes.draw(screen)
    flock.draw(screen)
    flock.update()
    screen.blit(floor,(ground_scroll,768))
    if len(pipes) >0:
        if flock.sprites()[0].rect.left > pipes.sprites()[0].rect.left\
            and flock.sprites()[0].rect.right < pipes.sprites()[0].rect.right\
            and pass_pipe == False:
            pass_pipe = True
        if pass_pipe==True:

            if flock.sprites()[0].rect.left >pipes.sprites()[0].rect.right:
                score+=1
                pass_pipe=False
    txt=font.render("score:"+str(score),True,"black")
    screen.blit(txt,(425,30))
     #looking for collision
    if pygame.sprite.groupcollide(flock,pipes,False,False):
        game_over=True
    if game_over==False and flying==True:
        current_time=pygame.time.get_ticks()
        if current_time-last_pipe > pipe_spawn:
            pipe_hieght=random.randint(-100,100)
            top_pipe=Pipe(screen_width,(screen_height//2)+pipe_hieght,1)
            bottom_pipe=Pipe(screen_width,(screen_height//2)+pipe_hieght,-1)
            pipes.add(top_pipe)
            pipes.add(bottom_pipe)
            last_pipe=current_time
        pipes.update()

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