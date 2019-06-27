import time
import vlc

file_str = '/home/eric/Videos/series/Silicon_Valley/Season_2/Silicon.Valley.S02E10.720p.BluRay.x264.ShAaNiG.mkv' 
player = vlc.MediaPlayer(file_str)

def play_content():
	player.play()

def pause_content():
	print("pausing")
	player.pause()

