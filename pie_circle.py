import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
screen.fill("white")
class pie_circles:
  def __init__(self,color,pos,rad):
    self.screen=screen
    self.color=color
    self.pos=pos
    self.rad=rad
  def draw(self):
    pygame.draw.circle(self.screen,self.color,self.pos,self.rad)
  def grow(self,x):
    self.rad+=x
    pygame.draw.circle(self.screen,self.color,self.pos,self.rad)
pos=300,150
c=pie_circles("red",pos,100)
i=pie_circles("yellow",pos,50)
r=pie_circles("green",pos,25)
while True:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      exit()
    if event.type==pygame.MOUSEBUTTONDOWN:
      c.draw()
      i.draw()
      r.draw()
      pygame.display.update()
    if event.type==pygame.MOUSEBUTTONUP:
      c.grow(5)
      i.grow(5)
      r.grow(5)
      pygame.display.update()
    if event.type==pygame.MOUSEMOTION:
      pos=pygame.mouse.get_pos()
      cles=pie_circles("black",pos,5)
      cles.draw()
      pygame.display.update()

    
    