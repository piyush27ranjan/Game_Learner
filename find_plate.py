import time

import cv2
import mss
import numpy


with mss.mss() as sct:
    # bottom part of the screen
    bottom_bar = {'top': 962, 'left': 23, 'width': 1860, 'height': 50}
    # background part of the screen
    background = {'top': 334, 'left': 26, 'width': 1868, 'height': 620}
    while 'Screen capturing':
       
        # Get bottom part
        img_bottom_bar = numpy.array(sct.grab(bottom_bar))
        bottom_bar_gray = cv2.cvtColor(img_bottom_bar, cv2.COLOR_BGRA2GRAY)
        # Get background part
        img_background = numpy.array(sct.grab(background))
        background_gray = cv2.cvtColor(img_background, cv2.COLOR_BGRA2GRAY)

        # White color for block and black for background
        ret_background,thresh_background = cv2.threshold(background_gray,40,255,0)
        cv2.imshow('background',thresh_background)
#         Display the pictures
#        cv2.imshow('OpenCV/Numpy normal', img_bottom_bar)

#         Display the picture in grayscale
#        cv2.imshow('OpenCV/Numpy grayscale',bottom_bar_gray)

        # Light Color=34 dark=109 for threshold
        ret,thresh = cv2.threshold(bottom_bar_gray,60,255,0)
        contours = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cnt = contours[0]
        x,y,w,h = cv2.boundingRect(cnt)
#        M = cv2.moments(cnt)
#        caught_you = cv2.rectangle(bottom_bar_gray,(x,y),(x+w,y+h),(255,255,255),5)
#        Display caught_you
#        cv2.imshow('caught_you',caught_you)
        
        cx = x + w/2
        cy = y + h/2
         
        print('x: '+str(cx)+ ' y: '+str(cy))
        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
