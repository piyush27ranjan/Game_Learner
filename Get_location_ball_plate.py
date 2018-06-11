import numpy as np
import cv2
import mss
import numpy
dataset = []


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
        background_gray = cv2.medianBlur(background_gray,5)
        #reduce image quality
        resized_image = cv2.resize(background_gray, (100, 50))

        # White color for block and black for background
        ret_background,thresh_background_small = cv2.threshold(resized_image,40,255,0)
      #  cv2.imshow('resized',thresh_background_small)
#         Display the pictures
#        cv2.imshow('OpenCV/Numpy normal', img_bottom_bar)

#         Display the picture in grayscale
#        cv2.imshow('OpenCV/Numpy grayscale',bottom_bar_gray)
        
        #Find circle
        rows = background_gray.shape[0]
        circles = cv2.HoughCircles(background_gray, cv2.HOUGH_GRADIENT, 1, rows / 8, param1=100, param2=30, minRadius=10, maxRadius=15)


        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0,:]:
                if img_background[i[1], i[0], 1] == 153:
                    # draw the outer circle
                    cv2.circle(img_background,(i[0],i[1]),i[2],(0,255,0),2)
                    # draw the center of the circle
                    cv2.circle(img_background,(i[0],i[1]),2,(0,0,255),3)
                    img_background_copy = cv2.resize(img_background,(500,200))
                    cv2.imshow('detected circles',img_background_copy)
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



