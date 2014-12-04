from cv2 import *
import numpy as np

def transPic(img_name):
    img = imread(img_name)
    rows,cols,ch = img.shape
    pts1 = np.float32([[(cols-1)/4,(rows-1)/4],[cols-1,0],[(cols-1)/4,(rows-1)*3/4],[cols-1,rows-1]])
    pts2 = np.float32([[0,0],[(cols-1)*3/4,(rows-1)/4],[0,rows-1],[(cols-1)*3/4,(rows-1)*3/4]])
    M = getPerspectiveTransform(pts1,pts2)
    dst = warpPerspective(img,M,(cols,rows),borderValue=(255,255,255))
    img_name = img_name.split(".")[0]+"-1.jpg"
    print "create "+img_name+"...",
    imwrite(img_name,dst)
    print "done!"

if __name__ == "__main__":
    transPic("1.png")
