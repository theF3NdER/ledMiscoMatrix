import pygame
import time
import sys
from random import randint

#Config
pygame.init()
scale = 30
size = (45*scale, 16*scale)
screen = pygame.display.set_mode(size)
BLACK = (0, 0, 0)

class Pixel():
    def __init__(self, x, y, color):
        self.width = scale
        self.height = scale
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color,(self.x,self.y,self.width,self.height))

while(1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(BLACK)
    for pixel in range(720):
        pixel = Pixel(pixel%self.width*scale, pixel//self.height*scale, (randint(0, 255), randint(0, 255), randint(0, 255)))
        pixel.draw()
    
    pygame.display.flip() 
    time.sleep(5/30)