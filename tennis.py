import pygame 
pygame.init() 
screen=pygame.display.set_mode((700,700))
pygame.display.set_caption("Tennis")
border=pygame.Rect(335,0,30,700)
screen.fill("forest green")
player_1h=10
player_2h=10
winner="" 
game_over=False
font=pygame.font.SysFont("Times New Roman",30)
player_1=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("player_one.png"),(160,160)),0)
player_2=pygame.image.load("player_two.png") 
player_1_r=pygame.Rect(600,375,50,50)
player_2_r=pygame.Rect(40,375,50,50)
def draw():
    pygame.draw.rect(screen,"white",border)
    screen.blit(player_1,(player_1_r.x,player_1_r.y))
    screen.blit(player_2,(player_2_r.x,player_2_r.y))
    player_2_txt=font.render("Health:"+ str(player_1h),True,"white")
    player_1_txt=font.render("Health:"+ str(player_2h),True,"white")
    screen.blit(player_2_txt,(50,50))
    screen.blit(player_1_txt,(550,50))
    if game_over:
        g_o_t=font.render(f"Game Over! The winner is {winner}!",True,"white")
        screen.blit(g_o_t,(100,340))

def player1_move(keys_pressed):
    if keys_pressed[pygame.K_LEFT] and player_1_r.x > 365:
        player_1_r.x-=10
    if keys_pressed[pygame.K_RIGHT] and player_1_r.x < 650:
        player_1_r.x+=10
    if keys_pressed[pygame.K_UP] and player_1_r.y > 0:
        player_1_r.y-=10
    if keys_pressed[pygame.K_DOWN] and player_1_r.y < 700:
        player_1_r.y+=10
def player2_move(keys_pressed):
    if keys_pressed[pygame.K_a] and player_2_r.x > 0:
        player_2_r.x-=10
    if keys_pressed[pygame.K_d] and player_2_r.x < 290:
        player_2_r.x+=10
    if keys_pressed[pygame.K_w] and player_2_r.y > 0:
        player_2_r.y-=10
    if keys_pressed[pygame.K_s] and player_2_r.y < 700:
        player_2_r.y+=10
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    draw()
    keys_pressed=pygame.key.get_pressed()
    player1_move(keys_pressed)
    player2_move(keys_pressed)
    pygame.display.update()