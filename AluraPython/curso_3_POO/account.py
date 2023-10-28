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

	def transfer(self, value, receiver):
		self.withdraw(value)
		receiver.deposit(value)
	
	def __update_miles_spend(self, value):
		self.__balance -= value
		return self.__balance
	
	def get_balance(self):
		return self.__balance
	
	def get_owner(self):
		return self.__owner
	
	def get_limit(self):
		return self.__limit
	
	def set_limit(self, new_limit):
		self.__limit = new_limit

	def __str__(self) -> str:
		string = f"Number: {self.__number}\nOwner: {self.__owner}\nBalance: {self.__balance}\nLimit: {self.__limit}\n"
		return string