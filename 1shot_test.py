import cv2
import numpy as np

# Coordinates of background
# background = {'top': 334, 'left': 26, 'width': 1868, 'height': 620}
filename = 'Sample_image.png'
# Loads an image
src = cv2.imread(filename)
nsrc = src[334:334+620 , 26:26+1868]
bottom_bar = src[962:962+50  , 23:23+1860]
bottom_bar_gray = cv2.cvtColor(bottom_bar,cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(nsrc, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)   
rows = gray.shape[0]
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8, param1=100, param2=30, minRadius=10, maxRadius=15)


if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        # circle center
        cv2.circle(src, center, 1, (0, 100, 100), 3)
        # circle outline
        radius = i[2]
        if nsrc[i[1],i[0],0] == 153:
            print("R: "+str(nsrc[i[1],i[0],0]))
            print("x:"+ str(i[0]) + " y:" + str(i[1]) + " r:" + str(i[2]))
            cv2.circle(nsrc, center, radius, (255, 0, 255), 3)
            print()
ret, thresh = cv2.threshold(bottom_bar_gray, 60, 255, 0)
contours = cv2.findContours(
                thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
x, y, w, h = cv2.boundingRect(cnt)
caught_you = cv2.rectangle(bottom_bar,(x,y),(x+w,y+h),(255,255,255),5)
#cv2.imshow('caught_you',caught_you)
#cv2.imshow("detected circles", nsrc)
cv2.waitKey(0)

import time
a = []
c=gray.flatten()
t1 = time.time()
d = list(c)
t2 = time.time()
print(t2-t1)
