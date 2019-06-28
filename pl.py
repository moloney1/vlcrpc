import time
import vlc

file_str = '/home/eric/Videos/series/Silicon_Valley/Season_2/Silicon.Valley.S02E10.720p.BluRay.x264.ShAaNiG.mkv' 
#player = vlc.MediaPlayer(file_str)

class Player:
	def __init__(self, path):
		self.player = vlc.MediaPlayer(path)
		print(path)
	
	def play_content(self):
		self.player.play()
	
	def pause_content(self):
		print("pausing")
		self.player.pause()

