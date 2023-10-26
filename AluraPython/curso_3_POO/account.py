class Account:
	def __init__(self, number, owner, balance, limit = 10000) -> None:
		self.number = number
		self.owner = owner
		self.balance = balance
		self.limit = limit

	def __str__(self) -> str:
		string = f"Number: {self.number}\nOwner: {self.owner}\nBalance: {self.balance}\nLimit: {self.limit}\n"
		return string