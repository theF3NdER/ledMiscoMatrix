import pygame
import time
from Monitor import Monitor
from random import randint
import sys
# import cv2

pygame.init()
scale = 35
size = (45*scale, 16*scale)
display = pygame.display.set_mode(size)
BLACK = (0, 0, 0)

class Pixel():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.height = scale
        self.width = scale
        self.color = color
    
    def draw(self):
        pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height))

class SoftwareMonitor(Monitor):
    def __init__(self):
        super(Monitor, self).__init__()
        

    def setPixelColor(self):
        super().setPixelColor(x, y, color)
    
    def show(self):
        display.fill(BLACK)
        for pixelOffY in range(16):
            for pixelOffX in range(45):
                pixel = Pixel(pixelOffX*scale, pixelOffY*scale, (randint(30, 255), randint(30, 255), randint(30, 255)))
                pixel.draw()

        pygame.display.flip()
        

while(1):
    screen = SoftwareMonitor()
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT: sys.exit()
    
    screen.show()
    
    time.sleep(1/30)

