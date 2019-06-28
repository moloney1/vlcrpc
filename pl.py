import time

import vlc

class Player:
	def __init__(self, path):
		self.player = vlc.MediaPlayer(path)
		print(path)
	
	def play_content(self):
		self.player.play()
	
	def pause_content(self):
		print("pausing")
		self.player.pause()

