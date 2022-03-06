import cv2 as cv
import numpy as np
from spiral_functions import *

def create(res=1024,scale=5):
    initialize(res,scale)
    img = np.zeros((res*scale,res*scale,3),np.uint8)
    for n in range(res**2):
        get_next_point()    
        cv.circle(img,get_pos(),int(compositeness(n)/10),(255,255,255),cv.FILLED)
        move()
    cv.imwrite('ulam_spiral_comp.png',img)