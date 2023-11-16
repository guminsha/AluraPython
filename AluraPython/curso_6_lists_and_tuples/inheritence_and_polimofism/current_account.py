from account import Account

class CurrentAccount(Account):
	def month_deductions(self):
		self._balance -= 2

