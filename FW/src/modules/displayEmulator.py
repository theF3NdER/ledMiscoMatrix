import cv2
import numpy as np


def createBlankFrame(h, w):
    frame = np.zeros([h, w, 3], np.uint8)
    return frame

def fillFrame(frame):
    for h in range(frame.shape[0]):
        for w in range(frame.shape[1]):
            if w%2 == 0:
                frame[h][w] = [137, 56, 25]
            else:
                frame[h][w] = [54, 190, 173]

def scale(oldFrame, factor):
    newFrame = np.zeros([oldFrame.shape[0]*factor, oldFrame.shape[1]*factor, 3], np.uint8)

    for row in range(oldFrame.shape[0]):
        for col in range(oldFrame.shape[1]):
            newFrame[col*factor:col*factor+factor][row*factor:row*factor+factor] = oldFrame[row][col]

    return newFrame
    


frame = createBlankFrame(16, 45)
fillFrame(frame)
scaled = scale(frame, 30)