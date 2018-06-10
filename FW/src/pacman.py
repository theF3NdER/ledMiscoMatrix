#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
 
import time
from neopixel import *
import argparse
import math
import numpy as np

# LED strip configuration:
LED_COUNT_PER_STRIPE = 45
STRIPES_NO = 4
LED_COUNT      = LED_COUNT_PER_STRIPE * STRIPES_NO      # Number of LED pixels.
LED_PIN        = 21      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 150     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
 
# Pin Funzionanti:

# 13 con LED_CHANNEL 1
# 18 con LED_CHANNEL 0
# 19 con LED_CHANNEL 1
# 21 con LED_CHANNEL 1


def colorWipe(strip, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms/1000.0)

import csv
def openFrame(file):
    with open(file, 'r') as f:
        aList = []
        reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:
            aList.append(row)
        # i need to strip the extra white space from each string in the row
        return(aList)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()
 
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
 
    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')
 
    try:
        FPS = 30
        wait_ms = 1000.0/FPS
        colorvalue = 0
        color = Color(colorvalue,colorvalue,colorvalue)
        
        index = 0

        while True:
            my_data = openFrame("./4/"+'%03d'%index+'.txt')
            #np.genfromtxt( "./4/"+'%03d'%index+'.txt', delimiter=' ')
            index += 1
            index = index % 89

            for i in range(strip.numPixels()):
                r = i // LED_COUNT_PER_STRIPE
                odd_row = r % 2
                pos = i
                if (odd_row == 1):
                    pos = int(LED_COUNT_PER_STRIPE * (r+1)) - 1 - i % LED_COUNT_PER_STRIPE
                
                color = Color(int(my_data[pos][2]),int(my_data[pos][1]),int(my_data[pos][0]))
                strip.setPixelColor(i, color)
            
            
            strip.show()
            time.sleep(wait_ms/1000.0)
    
    except KeyboardInterrupt:
        #if args.clear:
        colorWipe(strip, Color(0,0,0), 10)
