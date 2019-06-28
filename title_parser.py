class TitleParser:
	#	The-Office_0-01.avi
	def __init__(self, path):
		self.info = path.split(".")
		self.info = str(self.info[0])
		self.info = self.info.split("_")
		print(f"tf: {self.info}")
		self.showname = self.info[0].replace("-", " ")
		self.season_ep = self.info[1].split("-")

	def __str__(self):
		return f"{self.showname} S{self.season_ep[0]}E{self.season_ep[1]}"
	
