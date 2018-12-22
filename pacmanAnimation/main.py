from __future__ import division
import cv2
import numpy as np
import pickle

# print "OpenCV version :  {0}".format(cv2.__version__)
w = 45
h = 16

ghost = [cv2.imread('sprites/pacman/g1.bmp'), cv2.imread('sprites/pacman/g2.bmp')]
azure = [cv2.imread('sprites/pacman/a1.bmp'), cv2.imread('sprites/pacman/a2.bmp')]
red = [cv2.imread('sprites/pacman/r1.bmp'), cv2.imread('sprites/pacman/r2.bmp')]
pacman = [cv2.imread('sprites/pacman/p0.bmp'), cv2.imread('sprites/pacman/p1.bmp'), cv2.imread('sprites/pacman/p2.bmp'), cv2.imread('sprites/pacman/p1.bmp')]

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

def andata(i):
    ghosts = np.hstack((ghost[i%2], ghost[i%2]))
    space_ghosts = np.hstack((np.zeros((16, 16, 3), np.uint8), ghosts))
    pacman_space_ghosts = np.hstack((pacman[i%4], space_ghosts))

    black_pacman_space_ghosts = np.hstack(((np.zeros((16, i, 3), np.uint8), pacman_space_ghosts)))
    black_pacman_space_ghosts_black = np.hstack((black_pacman_space_ghosts, (np.zeros((16, w*4-i, 3), np.uint8))))

    return black_pacman_space_ghosts_black[:, 64:64+w]

def ritorno(i):
    enemies = np.hstack((cv2.flip(azure[i%2], 1), cv2.flip(red[i%2], 1)))
    space_enemies = np.hstack((np.zeros((16, 16, 3), np.uint8), enemies))
    pacman_space_enemies = np.hstack((cv2.flip(pacman[i%4], 1), space_enemies))

    black_pacman_space_enemies = np.hstack((pacman_space_enemies, (np.zeros((16, i, 3), np.uint8))))
    black_pacman_space_enemies_black = np.hstack(((np.zeros((16, 108-i, 3), np.uint8), black_pacman_space_enemies)))

    return black_pacman_space_enemies_black[:, 64:64+w]

def makeText(string, color):
    font = cv2.FONT_HERSHEY_PLAIN
    fontScale = 1
    size = cv2.getTextSize(string, font, 1, fontScale)
    w = size[0][0]
    h = 16
    blank = np.zeros((h, w, 3), np.uint8)

    cv2.putText(blank, string, (0,13), font, fontScale, (255, 255, 255), 1)
    cv2.imwrite('pippo.png', blank)

    blank = np.zeros((h, w+45, 3), np.uint8)


    for i in xrange(w):
        # color = hsv_to_rgb(i/w, 1, 1)
        # cv2.putText(blank, string, (0,13), font, fontScale, (color[2]*255, color[1]*255, color[0]*255), 1)

        cv2.putText(blank, string, (0,13), font, fontScale, color, 2)
        img = blank[:, i:i+45]
        # cv2.imwrite('text/aulin/'+'%03d'%i+'.png', img)

        with open('../FW/src/srcAnimation/text/xmas/'+'%03d'%i+'.txt', "w") as output:
            for c in xrange(16):
                for r in xrange(45):
                    if (img[c][r][0] != 0 or img[c][r][1] != 0 or img[c][r][2] != 0):
                        output.write(str(c)+','+str(r)+','+np.array2string(img[c][r][0])+','+np.array2string(img[c][r][1])+','+np.array2string(img[c][r][2])+'\n')


def makeFullImage():
    for i in range(108):
        andataImg = andata(i)
        ritornoImg = ritorno(i)
        
        # cv2.imwrite('srcAnimation/png/'+'%03d'%i+'.png', andataImg)
        # with open('srcAnimation/'+'%03d'%i+'.txt', "w") as output:
        #     for c in xrange(h):
        #         for r in xrange(w):
        #             string = ','.join(map(str, andataImg[c][r]))+"\n"
        #             output.write(string)

        # cv2.imwrite('srcAnimation/png/'+'%03d'%(108+i)+'.png', ritornoImg)
        # with open('srcAnimation/'+'%03d'%(108+i)+'.txt', "w") as output:
        #     for c in xrange(h):
        #         for r in xrange(w):
        #             string = ','.join(map(str, ritornoImg[c][r]))+"\n"
        #             output.write(string)
    
        # with open('srcAnimation/new/'+'%03d'%i+'.txt', "w") as output:
        #     for c in xrange(h):
        #         for r in xrange(w):
        #             if (andataImg[c][r][0] != 0 or andataImg[c][r][1] != 0 or andataImg[c][r][2] != 0):
        #                 output.write(str(c)+','+str(r)+','+np.array2string(andataImg[c][r][0])+','+np.array2string(andataImg[c][r][1])+','+np.array2string(andataImg[c][r][2])+'\n')
        
        # with open('srcAnimation/new/'+'%03d'%(108+i)+'.txt', "w") as output:
        #     for c in xrange(h):
        #         for r in xrange(w):
        #             if (ritornoImg[c][r][0] != 0 or ritornoImg[c][r][1] != 0 or ritornoImg[c][r][2] != 0):
        #                 output.write(str(c)+','+str(r)+','+np.array2string(ritornoImg[c][r][0])+','+np.array2string(ritornoImg[c][r][1])+','+np.array2string(ritornoImg[c][r][2])+'\n')



def main():
    # makeFullImage()
    makeText("111 XMAS", (0, 0, 255))
    
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()