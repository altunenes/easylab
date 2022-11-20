
############################################################## Enes Altun 21.11.2022  ##############################################################
###############################################################  Print RGB VALUES ############################################################
################################## Usage: Import the image, when the image is displayed, press the left mouse button to print the coordinates of the pixel, press the right mouse button to print the RGB values of the pixel. ##################################
######################################################### RGB values are printed in the terminal with the mouse movement. #########################################################
import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x,y), font, .4, (255,255,0), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strBGR, (x,y), font, .4, (0,255,255), 2)
        cv2.imshow('image', img)
#also print the rgb valus in real time in the terminal mouse is over
    if event == cv2.EVENT_MOUSEMOVE:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        #print on terminal
        print(strBGR)
        
        
img = cv2.imread('output.png')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()

