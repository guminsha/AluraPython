class Client():
	def __init__(self, name) -> None:
		self.__name = name

	@property
	def name(self):
		print("Calling @property name")
		return self.__name.title()
	
	@name.setter
	def name(self, name):
		print("Calling @name.setter")
		self.__name = name