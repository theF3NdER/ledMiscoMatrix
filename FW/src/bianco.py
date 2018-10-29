#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

from __future__ import division
import time
from neopixel import *
import argparse
from collections import namedtuple

def powerPercentage(percentage):
    return int(255/100)*percentage

LED_COUNT_PER_STRIPE = 45
STRIPES_NO = 8
LED_COUNT      = LED_COUNT_PER_STRIPE * STRIPES_NO      # Number of LED pixels
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = powerPercentage(100)     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
MONITOR_WIDTH = 45
MONITOR_HEIGHT = 16

LedStripCfg = namedtuple('LedStripCfg', 'pin channel dma freq')
LedStripsCfgs = [ LedStripCfg(13, 1, 10, LED_FREQ_HZ), LedStripCfg(18, 0, 10, LED_FREQ_HZ)]
strips = []

def stripFactory(cfg):
    return Adafruit_NeoPixel(LED_COUNT, cfg.pin, cfg.freq, cfg.dma, LED_INVERT, LED_BRIGHTNESS, cfg.channel)

def white():
    for i in range(len(LedStripsCfgs)):
        for j in range(LED_COUNT):
            strips[i].setPixelColor(j, Color(255,255,255))

def lumos():
    for i in range(len(LedStripsCfgs)):
        strips[i].show()


def hsv_to_rgb(h, s, v):
    if s == 0.0:
        return v, v, v
    i = int(h*6.0) # XXX assume int() truncates!
    f = (h*6.0) - i
    p = v*(1.0 - s)
    q = v*(1.0 - s*f)
    t = v*(1.0 - s*(1.0-f))
    i = i%6
    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q

def rainbow():
    for ofs in range(MONITOR_WIDTH):
        for x in range(MONITOR_WIDTH):
            for y in range(MONITOR_HEIGHT):
                odd_row = y % 2
                offset = (y % STRIPES_NO) * LED_COUNT_PER_STRIPE
                multiplier = 1
                if odd_row == 1:
                    offset += LED_COUNT_PER_STRIPE-1
                    multiplier = -1

                i = offset + multiplier * x

                row = y // STRIPES_NO

                r, g, b = hsv_to_rgb(x/44, 1, 1)

                #GRB
                strips[row].setPixelColorRGB(i+(ofs*16), int(g*255), int(r*255), int(b*255))
            lumos()


def run():
    for cfg in LedStripsCfgs:
        strip = stripFactory(cfg)
        strips.append(strip)
        print("Starting strip with GPIO %s and channel %s" % (cfg.pin, cfg.channel))
        strip.begin()
 
    white()
    while True:
         for i in range(len(LedStripsCfgs)):
             strips[i].show()

    # except KeyboardInterrupt:
    #     if args.clear:
    #         colorWipe(strip, Color(0,0,0), 10)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    parser.add_argument('--hw', action='store_true', help='Initialize hw monitor')
    args = parser.parse_args()

    run()
