import pygame as p

class Buttons():
    '''
    A blueprint for creating pygame buttons
    Fields:
    x,y
    width, height
    color
    text
    box using x,y,width,height
    Functions:
    draw ()
    '''
    def __init__(self,x, y, width, color, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = 50
        self.color = color
        self.text = text
        self.box = p.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        p.draw.rect(screen, self.color, self.box)
        #TODO- blit text onto self.box
        font = p.font.SysFont('Bradley Hand ITC', 22)
        text = font.render(self.text, True, 'black')
        screen.blit(text, (self.x+10, self.y+5))
