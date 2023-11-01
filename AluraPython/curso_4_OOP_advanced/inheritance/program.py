class Program:
	def __init__(self, name, year) -> None:
		self._name = name.title()
		self.year = year
		self._likes = 0

	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, new_name):
		self._name = new_name.title()

	@property
	def likes(self):
		return self._likes
	
	def new_like(self):
		self._likes += 1

	def show_info(self):
		return f"Movie name: {self.name} - Year: {self.year} - Likes: {self.likes}"