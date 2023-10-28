class Account:
	def __init__(self, number, owner, balance, limit = 10000) -> None:
		self.__number = number
		self.__owner = owner
		self.__balance = balance
		self.__limit = limit

	def extract(self):
		print(f"Your balance is {self.__balance}, Mr/Ms.{self.__owner}")

	def deposit(self, value):
		self.__balance += value
	
	def withdraw(self, value):
		self.__balance -= value


	def __str__(self) -> str:
		string = f"Number: {self.__number}\nOwner: {self.__owner}\nBalance: {self.__balance}\nLimit: {self.__limit}\n"
		return string