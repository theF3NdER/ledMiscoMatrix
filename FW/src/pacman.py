# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# NeoPixel library strandtest example
# Authors: Davide Giuffrida (dvdgff@gmail.com)
#          Riccardo Ancona  (riccardo.ancona@gmail.com)


import time
import argparse
import math
import numpy as np
from collections import namedtuple
import pickle


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

def openAnimation(directory, maxFrames):
    anAnimation = []
    # maxFrames = 216

    foreground = Color(255,255,0)
    background = Color(30,30,30)

    ## TXT
    for index in range(maxFrames):
        with open(directory+'%03d'%index+'.txt', 'r') as f:
            aList = []
            reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
            for row in reader:
                aList.append(row)
            anAnimation.append(aList)
        percentage =(float(index+1)/maxFrames) * 100.0
        print("Loading "+ str(percentage)[:5] + "%") 
        showProgressBar(foreground, background, percentage/100.0,0)


    ##PICKLE
    # for index in range (0, maxFrames):
    #     with open(directory+'%03d'%index+'.pickle', 'r') as inputFile:
    #         anAnimation.append(pickle.load(inputFile))
    #     percentage =(float(index+1)/maxFrames) * 100.0
    #     print("Loading "+ str(percentage)[:5] + "%") 
    #     showProgressBar(foreground, background, percentage/100.0,0)
    
    # colorWipe(Color(0,0,0), 0)
    return(anAnimation)

def colorWipe(color, wait_ms=50):
    """Wipe color across display a pixel at a time."""

    for x in range(0,MONITOR_WIDTH):
        for y in range(0,MONITOR_HEIGHT):
            pos = x + y * MONITOR_WIDTH
            monitor[0].setPixelColor(x, y, color)
            monitor[0].show()
            time.sleep(wait_ms/1000.0)

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
    while True:
        for ofs in range(MONITOR_WIDTH):
            for x in range(MONITOR_WIDTH):
                for y in range(MONITOR_HEIGHT):
                    odd_row = y % 2
                    offset = (y % 8) * 45
                    multiplier = 1
                    if odd_row == 1:
                        offset += 45-1
                        multiplier = -1

                    i = offset + multiplier * x

                    row = y // 8

                    r, g, b = hsv_to_rgb(x/44, 1, 1)
                    color = Color(int(g*255), int(b*255), int(r*255))
                    monitor[0].setPixelColor(x, y, color)
                monitor[0].show()
            break
            


def showProgressBar(colorForeground, colorBackground, progress, wait_ms=0):
    """Show a progress bar for the entire monitor"""

    # for x in range(MONITOR_WIDTH):
    #     for y in range(MONITOR_HEIGHT):

    #         color = Color(0,255-int(255*y/16),int(255*y/16))
    #         if (x/MONITOR_WIDTH > progress):
    #             color = colorBackground

    #         monitor[0].setPixelColor(x, y, color)

    # monitor[0].show()
    # time.sleep(wait_ms/1000.0)

    for x in range(0,MONITOR_WIDTH):
        for y in range(0,MONITOR_HEIGHT):
            pos = x + y * MONITOR_WIDTH

            color = Color(0, 255-int(255*y/16), int(255*y/16))
            if (x > progress*45):
                color = colorBackground

            monitor[0].setPixelColor(x, y, color)

    monitor[0].show()
    time.sleep(wait_ms/1000.0)

def init_hw_monitor():
    from hardwaremonitor import HardwareMonitor
    monitor.append(HardwareMonitor())

def init_sw_monitor():
    from SoftwareMonitor import SoftwareMonitor
    monitor.append(SoftwareMonitor())

def run():
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    parser.add_argument('--hw', action='store_true', help='Initialize hw monitor')
    parser.add_argument('--tvn', action='store_true', help='Write TVN on the display')
    parser.add_argument('--capitano', action='store_true', help='')
    parser.add_argument('--aulin', action='store_true', help='Write Aulink2k18 on the display')
    parser.add_argument('--rainbow', action='store_true', help='Play a rainbow animation')
    args = parser.parse_args()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    if args.hw:
        init_hw_monitor()
    else:
        init_sw_monitor()

    try:
        FPS = 12
        wait_ms = 1000.0/FPS
        colorvalue = 0
        color = Color(colorvalue,colorvalue,colorvalue)

        # my_animation = openAnimation("pickle/")

        if args.tvn:
            my_animation = openAnimation("srcAnimation/text/tvn/", 23)
        elif args.capitano:
            my_animation = openAnimation("srcAnimation/text/capitano/", 490)
        elif args.aulin:
            my_animation = openAnimation("srcAnimation/text/aulin/", 93)
        elif args.rainbow:
            rainbow()
        else:
            my_animation = openAnimation("srcAnimation/new/", 216)

        black = Color(0, 0, 0)

        while True:
            # for frame in my_animation:
            #     for x in range(MONITOR_WIDTH):
            #         for y in range(MONITOR_HEIGHT):
            #             #the index of the pos-th led in the matrix (from 1 up to 720)
            #             pos = (x + y * MONITOR_WIDTH)
            #             color = Color(int(frame[pos][1]), int(frame[pos][2]), int(frame[pos][0]))
            #             monitor[0].setPixelColor(x, y, color)

            #     monitor[0].show()
            #     time.sleep(wait_ms/1000.0)
            
            for frame in my_animation:
                for x in range(MONITOR_WIDTH):
                    for y in range(MONITOR_HEIGHT):
                        monitor[0].setPixelColor(x, y, black)

                if len(frame)>0:
                    for element in frame:
                        color = Color(int(element[3]), int(element[4]), int(element[2]))
                        monitor[0].setPixelColor(int(element[1]), int(element[0]), color)
                    monitor[0].show()
                    time.sleep(wait_ms/1000.0)

    except KeyboardInterrupt:
        #if args.clear:
        colorWipe(Color(0,0,0), 10)



# Main program logic follows:
if __name__ == '__main__':
    run()
