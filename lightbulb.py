import pygame
pygame.init()
screen=pygame.display.set_mode((200,200))
screen.fill("white")
light_bulb_on=pygame.image.load("light_bulb_on.png")
ligh_bulb_off=pygame.image.load("ligh_bulb_off.png")

while True:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      exit()
    if event.type==pygame.MOUSEBUTTONDOWN:
      light_bulb_on
      screen.blit(light_bulb_on,(0,0))
    if event.type==pygame.MOUSEBUTTONUP:
      ligh_bulb_off
      screen.blit(ligh_bulb_off,(0,0))
    pygame.display.update()

    
 