from functools import total_ordering

@total_ordering
class SalaryAccount:
	def __init__(self, code) -> None:
		self._code = code
		self._balance = 0

	def deposit(self, value):
		self._balance += value

	def __str__(self) -> str:
		return f"Account: {self._code}\nBalance: {self._balance}"
	
	def __eq__(self, another_object) -> bool:
		if type(self) != type(another_object):
			return False
		return self._code == another_object._code and self._balance == another_object._balance
	
	def __lt__(self, other):
		if self._balance != other._balance:
			return self._balance < other._balance
		return self._code < other._code
	
		