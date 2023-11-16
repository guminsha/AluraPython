from abc import ABCMeta, abstractmethod

class Account(metaclass=ABCMeta):
	def __init__(self, code) -> None:
		self._code = code
		self._balance = 0
	
	def deposit(self, value):
		self._balance += value

	def deposit_for_all(accounts_list):
		for account in accounts_list:
			account.deposit(100)
	
	@abstractmethod
	def month_deductions(self):
		pass
	
	def __str__(self) -> str:
		return f"Account's Code: {self._code} \nBalance: {self._balance}"
	
	
