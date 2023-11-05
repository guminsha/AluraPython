from program import Program

class Serie(Program):
	def __init__(self, name, year, seasons) -> None:
		super().__init__(name, year)
		self.__seasons = seasons

	@property
	def seasons(self):
		return self.__seasons
	
	def __str__(self) -> str:
		return f"Serie name: {self.name} - Year: {self.year} - Seasons: {self.seasons} - Likes: {self.likes}"
		