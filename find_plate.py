import time

import cv2
import mss
import numpy


with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {'top': 962, 'left': 23, 'width': 1860, 'height': 50}

    while 'Screen capturing':
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))
        gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

#         Display the pictures
#        cv2.imshow('OpenCV/Numpy normal', img)

#         Display the picture in grayscale
#        cv2.imshow('OpenCV/Numpy grayscale',gray)

# Light Color=34 dark=109 for threshold
        ret,thresh = cv2.threshold(gray,60,255,0)
        contours = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cnt = contours[0]
        M = cv2.moments(cnt)
        x,y,w,h = cv2.boundingRect(cnt)
        caught_you = cv2.rectangle(gray,(x,y),(x+w,y+h),(255,255,255),5)
        cv2.imshow('caught_you',caught_you)
        
        cx = x + w/2
        cy = y + h/2
         
        print('x: '+str(cx)+ ' y: '+str(cy))
        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
