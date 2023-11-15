from account import Account

print("Creating Accounts 1 and 2 with balance of 500 and 1000")
account1 = Account(15)
account1.deposit(500)

account2 = Account(47685)
account2.deposit(1000)

print("Print the memory adress")
account_list = [account1, account2]
print(account_list)

print("Print the account's info")
for account in account_list:
	print(account)

# account1, account_list[0] and account_list[1] points to the same object
account_list = [account1, account2, account1]

Account.deposit_for_all(account_list)

print("Print the account's info")
for account in account_list:
	print(account)

account_list.insert(0, 76)

# Cant deposit at account_list[0] because isn't a account anymore
# Account.deposit_for_all(account_list)

# Tuple wont change size but whats is inside CAN change the references
account_tuple = (account1, account2)
print(account_tuple[0])
account_tuple[0].deposit(300)
print(account_tuple[0])