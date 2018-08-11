#!/usr/bin/env python3
# NeoPixel library strandtest example
# Authors: Davide Giuffrida (gffdvd@gmail.com)
#          Riccardo Ancona  (riccardo.ancona@gmail.com)
from abc import ABC, abstractmethod

LED_COUNT_PER_STRIPE = 45
STRIPES_NO = 4
STRIPES_BLOCKS = 4
SCALE = 30

class Monitor:

    def __init__(self):
        self.config = {
            "LED_COUNT_PER_STRIPE": 45,
            "STRIPES_NO": 4,
            "STRIPES_BLOCKS": 4,
            "LED_COUNT": LED_COUNT_PER_STRIPE * STRIPES_NO,
            "TOTAL_LEDS": LED_COUNT_PER_STRIPE * STRIPES_NO * STRIPES_BLOCKS
        }

    @abstractmethod
    def setPixelColor(self, x, y, color):
        pass

    @abstractmethod
    def show(self):
        pass