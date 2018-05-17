import time

import cv2
import mss
import numpy as np

ball_color = [152, 152, 152]
with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}

    while 'Screen capturing':
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = np.array(sct.grab(monitor))

        # Converting image to greyscal
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Display the picture in grayscale
#        cv2.imshow('image',gray_image)

        ## Finding the ball
        cimg = cv2.medianBlur(img,5)
#        cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30)

        circles = np.uint16(np.around(circles))
        for (x, y, r) in circles[0,:]:
            # If ball centre of the circle matches the color of the ball
            if img[x,y] == eval(ball_color):
                ball_x , ball_y = x, y # TODO : check if x and y need to be swapped or not
                # draw the outer circle with green color
                cv2.circle(cimg,(x,y),r,(0,255,0),2)
                # draw the center of the circle with red color
                cv2.circle(cimg,(x,y),2,(0,0,255),3)



        print('fps: {0}'.format(1 / (time.time()-last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break