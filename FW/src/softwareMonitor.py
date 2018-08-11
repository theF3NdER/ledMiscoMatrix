#!/usr/bin/env python3
# NeoPixel library strandtest example
# Authors: Davide Giuffrida (gffdvd@gmail.com)
#          Riccardo Ancona  (riccardo.ancona@gmail.com)


from neopixel import *
from collections import namedtuple


# LED strip configuration:
LED_COUNT_PER_STRIPE = 45
STRIPES_NO = 4
LED_COUNT      = LED_COUNT_PER_STRIPE * STRIPES_NO      # Number of LED pixels.
LED_PIN        = 21      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 50     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


LedStripCfg = namedtuple('LedStripCfg', 'pin channel')
LedStripsCfgs = [LedStripCfg(13, 1), LedStripCfg(18, 0), LedStripCfg(19, 1), LedStripCfg(21, 0)]

# Mock here
def stripFactory(cfg):
    return Adafruit_NeoPixel(LED_COUNT, cfg.pin, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, cfg.channel)


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
        offset = y * LED_COUNT_PER_STRIPE
        multiplier = 1
        if odd_row == 1:
            offset += LED_COUNT_PER_STRIPE-1
            multiplier = -1

        i = multiplier * x + offset

        self.strips[y // LED_COUNT_PER_STRIPE].setPixelColor(i, col)

    def show(self):
        for strip in self.strips:
            strip.show()
