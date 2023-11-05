from program import Program

class Movie(Program):
	def __init__(self, name, year, duration) -> None:
		super().__init__(name, year)
		self.__duration = duration

	@property
	def duration(self):
		return self.__duration
	
	def __str__(self) -> str:
		return f"Movie name: {self.name} - Year: {self.year} - Duration: {self.duration} - Likes: {self.likes}"
	