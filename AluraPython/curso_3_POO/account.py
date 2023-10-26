class Account:
	def __init__(self, number, owner, balance, limit = 10000) -> None:
		self.number = number
		self.owner = owner
		self.balance = balance
		self.limit = limit

	def extract(self):
		print(f"Your balance is {self.balance}, Mr/Ms.{self.owner}")

	def deposit(self, value):
		self.balance += value
	
	def withdraw(self, value):
		self.balance -= value


	def __str__(self) -> str:
		string = f"Number: {self.number}\nOwner: {self.owner}\nBalance: {self.balance}\nLimit: {self.limit}\n"
		return string