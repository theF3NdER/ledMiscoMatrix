import cv2
import numpy as np
import pickle

print "OpenCV version :  {0}".format(cv2.__version__)
w = 45
h = 16

ghost = [cv2.imread('sprites/pacman/g1.bmp'), cv2.imread('sprites/pacman/g2.bmp')]
azure = [cv2.imread('sprites/pacman/a1.bmp'), cv2.imread('sprites/pacman/a2.bmp')]
red = [cv2.imread('sprites/pacman/r1.bmp'), cv2.imread('sprites/pacman/r2.bmp')]
pacman = [cv2.imread('sprites/pacman/p0.bmp'), cv2.imread('sprites/pacman/p1.bmp'), cv2.imread('sprites/pacman/p2.bmp'), cv2.imread('sprites/pacman/p1.bmp')]

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
    
        for i in xrange(23):
            tvnImg = cv2.imread('tvn/frame-'+'%d'%i+'.png')
            with open('srcAnimation/tvn/'+'%03d'%i+'.txt', "w") as output:
                for c in xrange(h):
                    for r in xrange(w):
                        if (tvnImg[c][r][0] != 0 or tvnImg[c][r][1] != 0 or tvnImg[c][r][2] != 0):
                            output.write(str(c)+','+str(r)+','+np.array2string(tvnImg[c][r][0])+','+np.array2string(tvnImg[c][r][1])+','+np.array2string(tvnImg[c][r][2])+'\n')
    
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
    makeFullImage()
    
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()