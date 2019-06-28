#!/usr/bin/env python
import os
import threading
import argparse

from pynput import keyboard

from pl import Player
from title_parser import TitleParser
from discord_presence import DiscordPresence

parser = argparse.ArgumentParser(description="vlcwrapper")
parser.add_argument("filepath")
args = parser.parse_args()

fname = args.filepath.split("/")
fname = fname[len(fname) - 1]

video_info = TitleParser(fname)

pres = DiscordPresence(str(video_info))

player = Player(os.path.abspath(args.filepath))

def on_press(key):
	try:
		if (key.char == 'a'):
			print("heard a")
			player.play_content()
			pres.start_playing()
		if (key.char == 'p'):
			pres.pause_presence()
			player.pause_content()
	except AttributeError:
		pass
	
def on_release(key):
	if key == keyboard.Key.esc:
		return False

presence_timer = threading.Thread(target=pres.presence_start)
presence_timer.start()
# Collect events until released
with keyboard.Listener(
		on_press=on_press) as listener:
	listener.join()
