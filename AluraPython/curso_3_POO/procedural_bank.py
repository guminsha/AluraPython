def create_account(number, owner, balance, limit):
	account = {"number": number, "owner": owner, "balance": balance, "limit": limit}
	return account

def deposit(account, value):
	account["balance"] += value

def withdraw(account, value):
	account["balance"] -= value

def extrato(account):
	print(account["balance"])

