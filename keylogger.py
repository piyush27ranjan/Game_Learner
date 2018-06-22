from pynput import keyboard
import time
import csv
import logging
csvFile = open('dataset.csv', 'w')
csvWriter = csv.writer(csvFile,lineterminator = "\n")
dataset_keylogger = []
logging.basicConfig(level=logging.DEBUG, format= ' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable()

def on_press(key):
    t = time.time()
    if not dataset_keylogger:
        dataset_keylogger.append([str(key), t])
        logging.info('%s pressed at %f'%(str(key), t))
    elif dataset_keylogger[-1][0] != str(key) and len(dataset_keylogger[-1]) == 3:
        dataset_keylogger.append([str(key), t])
        logging.info('%s pressed at %f'%(str(key), t))
    elif dataset_keylogger[-1][0] == str(key) and len(dataset_keylogger[-1]) == 3:
        dataset_keylogger.append([str(key), t])
        logging.info('%s pressed at %f'%(str(key), t))
    
    if key is not None:
        try:
            if key.char == 'q':
                logging.info('Will exit now')
                return False
        except AttributeError:
            pass
    
            

def on_release(key):
    t = time.time()
    for i in range(len(dataset_keylogger)):
        if dataset_keylogger[-i-1][0] == str(key) and len(dataset_keylogger[-i-1]) == 2:
            dataset_keylogger[-i-1].append(t)
            logging.info('%s released at time %f'%(str(key), t))
            
with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
for j in dataset_keylogger:
    csvWriter.writerow(j)
    logging.info('Writing new row')
csvFile.close()
logging.info('Closing File')