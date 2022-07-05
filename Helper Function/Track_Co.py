import numpy as np
import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ' ,y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', '+ str(y)
        #cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 1)
        cv2.circle(img, (x,y), 1, (0,0,0), -1)
        cv2.imshow('Track Layout', img)



img = cv2.imread('test1.jpg')
cv2.imshow('Track Layout', img)

cv2.setMouseCallback('Track Layout', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()