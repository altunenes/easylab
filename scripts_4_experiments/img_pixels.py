############################################################### under construction ############################################################

import cv2
import numpy as np

def pixel_value(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(img[y,x])

        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]

        cv2.circle(img,(x,y),3,(0,0,255),-1)
        mycolorImage = np.zeros((512,512,3),np.uint8)

        mycolorImage[:] = [blue,green,red]

        cv2.imshow('color',mycolorImage)

img = cv2.imread('Lena.png')
cv2.imshow('image',img)
cv2.setMouseCallback('image',pixel_value)

cv2.waitKey(0)
cv2.destroyAllWindows()
