class Playlist:
	def __init__(self, name, programs) -> None:
		self.name = name
		self._programs = programs

	def __getitem__(self, item):
		return self._programs[item]

	@property
	def listing(self):
		return self._programs

	def __len__(self):
		return len(self._programs)

	def verify(self, program):
		if program in self:
			return "Yes"
		else:
			return "No"