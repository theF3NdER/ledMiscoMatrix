#!/usr/bin/env python3
# NeoPixel library strandtest example
# Authors: Davide Giuffrida (gffdvd@gmail.com)
#          Riccardo Ancona  (riccardo.ancona@gmail.com)


from neopixel import *
from collections import namedtuple
import time

def powerPercentage(percentage):
    return int(255/100)*percentage

# LED strip configuration:
LED_COUNT_PER_STRIPE = 45
STRIPES_NO = 8
LED_COUNT      = LED_COUNT_PER_STRIPE * STRIPES_NO      # Number of LED pixels.
LED_PIN        = 21      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_SPI_HZ    = 400000  # LED signal frequency in hertz (usually 800khz)
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 50      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = powerPercentage(30)     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


LedStripCfg = namedtuple('LedStripCfg', 'pin channel dma freq')
LedStripsCfgs = [ LedStripCfg(13, 1, 10, LED_FREQ_HZ), LedStripCfg(18, 0, 10, LED_FREQ_HZ)]

def stripFactory(cfg):
    return Adafruit_NeoPixel(LED_COUNT, cfg.pin, cfg.freq, cfg.dma, LED_INVERT, LED_BRIGHTNESS, cfg.channel)

class HardwareMonitor:

    strips = []

    def __init__(self):
        for cfg in LedStripsCfgs:
            strip = stripFactory(cfg)
            self.strips.append(strip)
            print("Starting strip with GPIO %s and channel %s" % (cfg.pin, cfg.channel))
            strip.begin()

    def setPixelColor(self, x, y, color):
        col = Color(color.r, color.g, color.b)
        odd_row = y % 2
        offset = (y % STRIPES_NO) * LED_COUNT_PER_STRIPE
        multiplier = 1
        if odd_row == 1:
            offset += LED_COUNT_PER_STRIPE-1
            multiplier = -1

        i = offset + multiplier * x

        row = y // STRIPES_NO
        self.strips[row].setPixelColor(i, col)

    def show(self):
        for i in range(len(LedStripsCfgs)):
            self.strips[i].show()
