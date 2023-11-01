from program import Program

class Serie(Program):
	def __init__(self, name, year, seasons) -> None:
		super().__init__(name, year)
		self.__seasons = seasons

	@property
	def seasons(self):
		return self.__seasons
	
	def show_info(self):
		print(f"{super().show_info()} - Seasons: {self.seasons}")
		