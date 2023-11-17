from salary_account import SalaryAccount
from operator import attrgetter

account1 = SalaryAccount(1312)
account2 = SalaryAccount(270)
account3 = SalaryAccount(133)

account1.deposit(500)
account2.deposit(1000)
account3.deposit(1000)

accounts = [account1, account2, account3]
# sorted(accounts) # cant do it because there is no element to see if is less then another

# for account in sorted(accounts, key=SalaryAccount.get_code): # not good acess a private attribute
# 	print(account)


# for account in sorted(accounts, key=attrgetter("_code")): # still acessing a private attribute
# 	print(account)

for account in sorted(accounts): # afther implemmenting __lt__ (less than)
	print(account)
# for account in sorted(accounts, reverse=True):
# 	print(account)
print("____________________")
for account in sorted(accounts, key=attrgetter("_balance", "_code")): # if balance is the same, compare code
	print(account)

print(account1 < account2)
print(account1 == account2)

print(account1 <= account3)

print(account2 == account3)
print(account2 < account3)
