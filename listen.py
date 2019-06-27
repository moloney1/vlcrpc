from pynput import keyboard
import pl

def on_press(key):
	try:
		if (key.char == 'a'):
			print("heard a")
			pl.play_content()
		if (key.char == 'p'):
			pl.pause_content()
	except AttributeError:
		pass
	
def on_release(key):
	if key == keyboard.Key.esc:
		return False

# Collect events until released
with keyboard.Listener(
		on_press=on_press) as listener:
	listener.join()
