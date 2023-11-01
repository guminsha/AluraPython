from program import Program

class Movie(Program):
	def __init__(self, name, year, duration) -> None:
		super().__init__(name, year)
		self.__duration = duration

	@property
	def duration(self):
		return self.__duration

	def show_info(self):
		print(f"{super().show_info()} - Duration: {self.duration}min")