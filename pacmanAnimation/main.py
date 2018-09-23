import cv2
import numpy as np
import pickle

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

def makeFullImage(ghost, pacman, w):
    for i in range(w*3):
        centralBlock = assembleCentralBlock(ghost[i%2], ghost[i%2], pacman[i%4])
        asd = leftBlock(centralBlock, i)
        fullImage = rightBlock(asd, w*4-i)
        # extractCentralFrames(fullImage, '%03d'%i+'.txt', w)
        extractCentralFrames(fullImage, 'frames/4/'+'%03d'%i+'.txt', 'frames/4/'+'%03d'%i+'.png', w)
    

def extractCentralFrames(fullImage, nameTxt, namePng, w):
    # croppedImage = fullImage[7:11, w:w*2]
    croppedImage = fullImage[:, 60:105]
    cv2.imwrite(namePng, croppedImage)
    # cv2.imshow("pacman", fullImage)
    # np.savetxt(nameTxt, fullImage)
    # fullImage.tofile(nameTxt, sep=" ",format="%s")

    # output = open(name, 'wb')
    # pickle.dump(fullImage, output)
    # output.close()

    with open(nameTxt, "w") as output:
        for c in xrange(16):
            for r in xrange(w):
                string = ','.join(map(str, croppedImage[c][r]))+"\n"
                output.write(string)


def main():
    w = 45

    ghost, pacman = loadSprites()

    # while True:
    makeFullImage(ghost, pacman, w)
    
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()