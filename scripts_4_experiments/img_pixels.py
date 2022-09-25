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

################################################################### V2 ##################################
##################################### V2, Right clic BGR Values, Left click dimensions (with mouse) #############################
# import cv2
# import numpy as np

# def click_event(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(x,', ',y)
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         strXY = str(x) + ', ' + str(y)
#         cv2.putText(img, strXY, (x,y), font, .4, (255,255,0), 2)
#         cv2.imshow('image', img)
#     if event == cv2.EVENT_RBUTTONDOWN:
#         blue = img[y,x,0]
#         green = img[y,x,1]
#         red = img[y,x,2]
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
#         cv2.putText(img, strBGR, (x,y), font, .4, (0,255,255), 2)
#         cv2.imshow('image', img)

# #img = np.zeros((512,512,3), np.uint8)
# img = cv2.imread('FFT.png')
# cv2.imshow('image', img)

# cv2.setMouseCallback('image', click_event)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
