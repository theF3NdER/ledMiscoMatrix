import cv2
import numpy as np

def assembleCentralBlock(one, two, three):
    two = np.hstack((two, one))
    twoAndSpace = np.hstack((np.zeros((16, 12, 3), np.uint8), two))
    three = np.hstack((three, twoAndSpace))

    return three

def loadSprites():
    ghost = [cv2.imread('sprites/pacman/g1.bmp'), cv2.imread('sprites/pacman/g2.bmp')]
    pacman = [cv2.imread('sprites/pacman/p0.bmp'), cv2.imread('sprites/pacman/p1.bmp'), cv2.imread('sprites/pacman/p2.bmp'), cv2.imread('sprites/pacman/p1.bmp')]

    return ghost, pacman

def leftBlock(centralBlock, size):
    leftAndCentral = np.hstack((np.zeros((16, size, 3), np.uint8), centralBlock))
    return leftAndCentral

def rightBlock(centralBlock, size):
    centralAndRight = np.hstack((centralBlock, (np.zeros((16, size, 3), np.uint8))))
    return centralAndRight

def makeFullImage(ghost, pacman, canvas):
    for i in range(120):
        centralBlock = assembleCentralBlock(ghost[i%2], ghost[i%2], pacman[i%4])
        asd = leftBlock(centralBlock, i)
        fullImage = rightBlock(asd, 240-i)
        extractCentralFrames(fullImage, 'frames/'+'%03d'%i+'.png')
    

def extractCentralFrames(fullImage, name):
    croppedImage = fullImage[:, 60:120]
    cv2.imwrite(name, croppedImage)


def main():
    canvas = np.zeros((16, 60*3, 3), np.uint8)

    ghost, pacman = loadSprites()

    makeFullImage(ghost, pacman, canvas)

if __name__ == "__main__":
    main()