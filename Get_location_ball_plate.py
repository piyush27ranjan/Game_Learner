import numpy as np
import cv2
import mss
import numpy
from pynput import keyboard
import time
import threading
import csv
import logging
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable()

# csv
key_File = open('dataset_keylogger.csv', 'w')
key_Writer = csv.writer(key_File, lineterminator="\n")
coord_File = open('dataset_coords.csv', 'w')
coord_Writer = csv.writer(coord_File, lineterminator ="\n")

# dataset variables
dataset_keylogger = []
dataset_coordinates = []

def on_press(key):
    global dataset_keylogger
    t = time.time()
    if not dataset_keylogger:
        dataset_keylogger.append([str(key), t])
        logging.info('%s pressed at %f' % (str(key), t))
    elif dataset_keylogger[-1][0] != str(key) and len(dataset_keylogger[-1]) == 3:
        dataset_keylogger.append([str(key), t])
        logging.info('%s pressed at %f' % (str(key), t))
    elif dataset_keylogger[-1][0] == str(key) and len(dataset_keylogger[-1]) == 3:
        dataset_keylogger.append([str(key), t])
        logging.info('%s pressed at %f' % (str(key), t))

    if key is not None:
        try:
            if key.char == 'q':
                logging.info('Will exit now')
                return False
        except AttributeError:
            pass

#	except:
#		print( str(time.time()) + ' ' +str(key) + '\n') 
def on_release(key):
    global dataset_keylogger
    t = time.time()
    for i in range(len(dataset_keylogger)):
        if dataset_keylogger[-i - 1][0] == str(key) and len(dataset_keylogger[-i - 1]) == 2:
            dataset_keylogger[-i - 1].append(t)
            logging.info('%s released at time %f' % (str(key), t))
        
def keylogger():
    with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    		listener.join()
def imageProcessing():
    global dataset_coordinates
    image_count = 0
    with mss.mss() as sct:
        # bottom part of the screen
        bottom_bar = {'top': 962, 'left': 23, 'width': 1860, 'height': 50}
        # background part of the screen
        background = {'top': 334, 'left': 26, 'width': 1868, 'height': 620}
        while 'Screen capturing':
            image_time = time.time()
            image_count += 1

            # Get bottom part
            img_bottom_bar = numpy.array(sct.grab(bottom_bar))
            bottom_bar_gray = cv2.cvtColor(img_bottom_bar, cv2.COLOR_BGRA2GRAY)
            # Get background part
            img_background = numpy.array(sct.grab(background))
            background_gray = cv2.cvtColor(img_background, cv2.COLOR_BGRA2GRAY)
            background_gray = cv2.medianBlur(background_gray, 5)
            # reduce image quality
            resized_image = cv2.resize(background_gray, (100, 50))
    
            # White color for block and black for background
            ret_background, thresh_background_small = cv2.threshold(
                resized_image, 40, 255, 0)
            # cv2.imshow('resized',thresh_background_small)
            # Store thresh_background_small


            # Display the picture in grayscale
            # cv2.imshow('OpenCV/Numpy grayscale',bottom_bar_gray)
    
            # Find circle
            rows = background_gray.shape[0]
            circles = cv2.HoughCircles(background_gray, cv2.HOUGH_GRADIENT,
                                       1, rows / 8, param1=100, param2=30, minRadius=10, maxRadius=15)
    
            if circles is not None:
                circles = np.uint16(np.around(circles))
                for (b_x,b_y,r) in circles[0, :]:
                    # If center of the circle is grey(153,153,153)
                    if img_background[b_y, b_x, 1] == 153:
                        # draw the outer circle
                        cv2.circle(img_background,
                                   (b_x, b_y), r, (0, 255, 0), 2)
                        # draw the center of the circle
                        cv2.circle(img_background, (b_x, b_y), 2, (0, 0, 255), 3)
                        img_background_copy = cv2.resize(
                            img_background, (500, 200))
                        # cv2.imshow('detected circles', img_background_copy)
                        # Light Color=34 dark=109 for threshold
                        ret, thresh = cv2.threshold(bottom_bar_gray, 60, 255, 0)
                        contours = cv2.findContours(
                            thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                        cnt = contours[0]
                        x, y, w, h = cv2.boundingRect(cnt)
                        # M = cv2.moments(cnt)
                        # caught_you = cv2.rectangle(bottom_bar_gray,(x,y),(x+w,y+h),(255,255,255),5)
                        # Display caught_you
                        # cv2.imshow('caught_you',caught_you)
                
                        p_x = x + w / 2
                        # p_y = y + h / 2
                        row = [b_x, b_y, p_x, image_time]
                        dataset_coordinates.append(row + list(thresh_background_small.flatten()))
                        logging.debug('New image appended')
            # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
if(__name__ == '__main__'):
    keylogger_thread = threading.Thread(target = keylogger)
    imageprocessing_thread = threading.Thread(target = imageProcessing )
    
    keylogger_thread.start()
    imageprocessing_thread.start()

    # Writing key strokes
    logging.info('Writing key strokes to csv file')
    for j in dataset_keylogger:
        key_Writer.writerow(j)
        logging.info('Writing new row of keys')
    key_File.close()
    logging.info('Closing key strokes csv File\n')

    # Writing coordinates
    logging.info('Writing coordinates to csv file')
    for k in dataset_coordinates:
        coord_Writer.writerow(k)
        logging.info('Writing new row of coordinates')
    coord_File.close()
    logging.info('Closing coordinates csv File\n')
