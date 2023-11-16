from account import Account

class SavingAccount(Account):
	def month_deductions(self):
		self._balance *= 1.01
		self._balance -= 3