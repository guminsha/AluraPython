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
		if self.__can_withdraw(value):
			self.__balance -= value
		else:
			print("The amount exceeds your limit")

	def __can_withdraw(self, value):
		can_withdraw = self.balance + self.limit >= value
		return can_withdraw

	def transfer(self, value, receiver):
		self.withdraw(value)
		receiver.deposit(value)
	
	@property
	def balance(self):
		return self.__balance
	
	@property
	def owner(self):
		return self.__owner
	
	@property
	def limit(self):
		return self.__limit
	
	@limit.setter
	def limit(self, new_limit):
		self.__limit = new_limit

	@staticmethod
	def bank_code():
		return "001"
	
	@staticmethod
	def code_banks():
		return {"BB":"001", "Caixa":"104", "Bradesco":"237"}
	

	def __str__(self) -> str:
		string = f"Number: {self.__number}\nOwner: {self.__owner}\nBalance: {self.__balance}\nLimit: {self.__limit}\n"
		return string