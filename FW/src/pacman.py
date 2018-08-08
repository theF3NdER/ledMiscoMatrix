# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# NeoPixel library strandtest example
# Authors: Davide Giuffrida (dvdgff@gmail.com)
#          Riccardo Ancona  (riccardo.ancona@gmail.com)
<<<<<<< HEAD
 
LED_DRIVE_PINS[""]
 
=======

>>>>>>> master
import time
import argparse
import math
import numpy as np
from collections import namedtuple


MONITOR_WIDTH = 45
MONITOR_HEIGHT = 16
monitor = [] # will be instanciated afterwards

Color = namedtuple('Color', 'r g b')

import csv

def openFrame(file):
    with open(file, 'r') as f:
        aList = []
        reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:
            aList.append(row)
        return(aList)

def openAnimation(directory):
    anAnimation = []
    maxFrames = 89

    foreground = Color(255,255,0)
    background = Color(30,30,30)

    for index in range (0,maxFrames):
        with open(directory+'%03d'%index+'.txt', 'r') as f:
            aList = []
            reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
            for row in reader:
                aList.append(row)
            anAnimation.append(aList)
        percentage =(float(index+1)/maxFrames) * 100.0
        print("Loading "+ str(percentage) + "%") 
        showProgressBar(foreground, background, percentage/100.0,0)
    return(anAnimation)

def colorWipe(color, wait_ms=50):
    """Wipe color across display a pixel at a time."""

    for x in range(0,MONITOR_WIDTH-1):
        for y in range(0,MONITOR_HEIGHT-1):
            pos = x + y * MONITOR_WIDTH
            monitor[0].setPixelColor(x, y, color)
            monitor[0].show()
            time.sleep(wait_ms/1000.0)

def showProgressBar(colorForeground, colorBackground, progress, wait_ms=50):
    """Show a progress bar for the entire monitor"""

    for x in range(0,MONITOR_WIDTH-1):
        for y in range(0,MONITOR_HEIGHT-1):
            pos = x + y * MONITOR_WIDTH

            color = colorForeground
            if (x/MONITOR_WIDTH > progress):
                color = colorBackground

            monitor[0].setPixelColor(x, y, color)

    monitor[0].show()
    time.sleep(wait_ms/1000.0)

def init_hw_monitor():
    from hardwaremonitor import HardwareMonitor
    monitor.append(HardwareMonitor())

def run():
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    parser.add_argument('--hw', action='store_true', help='Initialize hw monitor')
    args = parser.parse_args()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    if args.hw:
        init_hw_monitor()

    try:
        FPS = 30
        wait_ms = 1000.0/FPS
        colorvalue = 0
        color = Color(colorvalue,colorvalue,colorvalue)

        my_animation = openAnimation("../../pacmanAnimation/frames/4/")

        while True:

            for frame in my_animation:
                for x in range(0,MONITOR_WIDTH-1):
                    for y in range(0,MONITOR_HEIGHT-1):
                        pos = (x + y * MONITOR_WIDTH)%180
                        color = Color(int(frame[pos][2]),int(frame[pos][1]),int(frame[pos][0]))
                        monitor[0].setPixelColor(x, y, color)

                monitor[0].show()
                time.sleep(wait_ms/1000.0)

    except KeyboardInterrupt:
        #if args.clear:
        colorWipe(Color(0,0,0), 10)



# Main program logic follows:
if __name__ == '__main__':
    run()
