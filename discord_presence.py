from pypresence import Presence
from config import client_id
import time, datetime

RPC = Presence(client_id)
RPC.connect()

class DiscordPresence:
	def __init__(self, video_info):
		self.playing = False
		self.timer = 0
		self.info_string = ""
		self.video_info = video_info

	def start_playing(self):
		self.playing = True

	def pause_presence(self):
		self.playing = not self.playing

	def presence_start(self):
		while True:
			#RPC.update(state=f"Time: {self.timer}")
			RPC.update(state=f"Watching {self.video_info} for {self.timer}s")
			if self.playing:
				self.timer += 1
			time.sleep(1)
			print(self.playing)

