from pypresence import Presence
from config import client_id
import time

RPC = Presence(client_id)
RPC.connect()

timer = 0
while True:
	RPC.update(state=f"Test...{timer}")
	timer += 5
	time.sleep(5)


