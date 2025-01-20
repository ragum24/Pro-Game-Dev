import pygame # screen size= 700,700 border size= x=335 y=0 width=30 height=700 dips=orange chips=yellow
pygame.init() # pygame.init()=init= initialising
screen=pygame.display.set_mode((700,700))
pygame.display.set_caption("'Spacious' battle")
border=pygame.Rect(335,0,30,700)
yellowh=10
orangeh=10
winner=""
chips_ammo=[]
dips_ammo=[]
game_over=False 
clock=pygame.time.Clock()
font=pygame.font.SysFont("Times New Roman",30)
dips=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("orange_ship.png"),(50,50)),270)
chips=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("yellow_ship.png"),(50,50)),90)
dips_r=pygame.Rect(600,375,50,50)
chips_r=pygame.Rect(40,375,50,50)
bg=pygame.image.load("spacey_bg.png")
def draw():
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen,"dark blue",border)
    screen.blit(dips,(dips_r.x,dips_r.y))
    screen.blit(chips,(chips_r.x,chips_r.y))
    chiptxt=font.render("Health:"+ str(orangeh),True,"white")
    diptxt=font.render("Health:"+ str(yellowh),True,"white")
    screen.blit(chiptxt,(50,50))
    screen.blit(diptxt,(550,50))
    if game_over:
        g_o_t=font.render(f"Game Over! The winner is {winner}!",True,"white")
        screen.blit(g_o_t,(150,340))
    for bullet in dips_ammo:
        pygame.draw.rect(screen,"yellow",bullet)
    for bullet in chips_ammo:
        pygame.draw.rect(screen,"orange",bullet)
def dip_move(keys_pressed):
    if keys_pressed[pygame.K_LEFT] and dips_r.x > 365:
        dips_r.x-=10
    if keys_pressed[pygame.K_RIGHT] and dips_r.x < 650:
        dips_r.x+=10
    if keys_pressed[pygame.K_UP] and dips_r.y > 0:
        dips_r.y-=10
    if keys_pressed[pygame.K_DOWN] and dips_r.y < 700:
        dips_r.y+=10
def chip_move(keys_pressed):
    if keys_pressed[pygame.K_a] and chips_r.x > 0:
        chips_r.x-=10
    if keys_pressed[pygame.K_d] and chips_r.x < 290:
        chips_r.x+=10
    if keys_pressed[pygame.K_w] and chips_r.y > 0:
        chips_r.y-=10
    if keys_pressed[pygame.K_s] and chips_r.y < 700:
        chips_r.y+=10
def ammo(chips_ammo,dips_ammo):
    global orangeh,yellowh,bullet
    for bullet in chips_ammo:
        bullet.x+=8
        if dips_r.colliderect(bullet):
            orangeh-=1
            chips_ammo.remove(bullet)
        elif bullet.x > 700:
            chips_ammo.remove(bullet)
    for bullet in dips_ammo:
        bullet.x-=8
        if chips_r.colliderect(bullet):
            yellowh-=1
            dips_ammo.remove(bullet)
        elif bullet.x < 0:
            dips_ammo.remove(bullet)
def G_O_F():
    global winner,game_over,yellowh,orangeh
    if yellowh==0:
        winner="dips"
        game_over=True
    elif orangeh==0:
        winner="chips"
        game_over=True


while True:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_9:
                bullet=pygame.Rect(chips_r.x+25,chips_r.y+25,10,5)
                chips_ammo.append(bullet)
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_1:
                bullet=pygame.Rect(dips_r.x+25,dips_r.y+25,10,5)
                dips_ammo.append(bullet)        
    draw()
    G_O_F()
    ammo(chips_ammo,dips_ammo)
    keys_pressed=pygame.key.get_pressed()
    dip_move(keys_pressed)
    chip_move(keys_pressed)
    pygame.display.update()