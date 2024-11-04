import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
class rects:
    def __init__(self,colour,dimensions):
        self.screen=screen
        self.colour=colour
        self.dimensions=dimensions
    def draw(self):
        self.draw_rect=pygame.draw.rect(self.screen,self.colour,self.dimensions)
Rect1=rects("green",(50,50,100,100))
Rect2=rects("pink",(180,180,200,200))
Rect3=rects("black",(415,415,100,100))
Rect4=rects("purple",(415,50,100,100))
Rect5=rects("red",(50,415,100,100))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    screen.fill("white")
    Rect1.draw()
    Rect2.draw()
    Rect3.draw()
    Rect4.draw()
    Rect5.draw()
    pygame.display.update()