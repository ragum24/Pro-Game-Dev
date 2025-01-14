import pygame # screen size= 700,700 border size= x=335 y=0 width=30 height=700 ships=orange chips=yellow
pygame.init() # pygame.init()=init= initialising
screen=pygame.display.set_mode((700,700))
pygame.display.set_caption("'Spacious' battle")
border=pygame.Rect(335,0,30,700)
yellowh=10
orangeh=10
winner=""
chips_ammo=[]
ships_ammo=[]
game_over=False 
clock=pygame.time.Clock()
font=pygame.font.SysFont("Times New Roman",30)
ships=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("orange_ship.png"),(50,50)),270)
chips=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("yellow_ship.png"),(50,50)),90)
ships_r=pygame.Rect(600,375,50,50)
chips_r=pygame.Rect(40,375,50,50)
def draw():
    bg=pygame.image.load("spacey_bg.png")
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen,"dark blue",border)
    screen.blit(ships,(ships_r.x,ships_r.y))
    screen.blit(chips,(chips_r.x,chips_r.y))
    chiptxt=font.render("Health:"+ str(orangeh),True,"white")
    shiptxt=font.render("Health:"+ str(yellowh),True,"white")
    screen.blit(chiptxt,(50,50))
    screen.blit(shiptxt,(550,50))
    if game_over:
        g_o_t=font.render(f"Game Over! The winner is {winner}!",True,"white")
        screen.blit(g_o_t,(100,340))
    for i in ships_ammo:
        pygame.draw.rect(screen,"yellow",i)
    for i in chips_ammo:
        pygame.draw.rect(screen,"orange",i)
def ship_move(keys_pressed):
    if keys_pressed[pygame.K_LEFT] and ships_r.x > 365:
        ships_r.x-=10
    if keys_pressed[pygame.K_RIGHT] and ships_r.x < 650:
        ships_r.x+=10
    if keys_pressed[pygame.K_UP] and ships_r.y > 0:
        ships_r.y-=10
    if keys_pressed[pygame.K_DOWN] and ships_r.y < 700:
        ships_r.y+=10
def chip_move(keys_pressed):
    if keys_pressed[pygame.K_a] and chips_r.x > 0:
        chips_r.x-=10
    if keys_pressed[pygame.K_d] and chips_r.x < 290:
        chips_r.x+=10
    if keys_pressed[pygame.K_w] and chips_r.y > 0:
        chips_r.y-=10
    if keys_pressed[pygame.K_s] and chips_r.y < 700:
        chips_r.y+=10
while True:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    draw()
    keys_pressed=pygame.key.get_pressed()
    ship_move(keys_pressed)
    chip_move(keys_pressed)
    pygame.display.update()