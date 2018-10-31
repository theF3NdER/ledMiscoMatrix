import pygame
import time
from Monitor import Monitor
from random import randint
import sys

pygame.init()
scale = 40
size = (44*scale, 15*scale)
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
        Monitor.__init__(self)

        #make a brand new black (empty) matrix
        self.matrix = []
        for pixelOffY in range(self.config['STRIPES_NO']*self.config['STRIPES_BLOCKS']):
            self.matrix.append([])
            for pixelOffX in range(self.config['LED_COUNT_PER_STRIPE']):
                self.matrix[pixelOffY].append(Pixel(pixelOffX*scale, pixelOffY*scale, (000, 000, 000)))

    #For each pixel of the matrix, assign a given color in a given position
    def setPixelColor(self, x, y, color):
        # Sembra che non faccia nulla, verificare
        # super().setPixelColor(x, y, color)
        self.matrix[y][x].color = (color.b, color.r, color.g)
    
    def show(self):
        display.fill(BLACK)

        for y in range(16):
            for x in range(45):
                 self.matrix[y][x].draw()

        pygame.display.flip()

