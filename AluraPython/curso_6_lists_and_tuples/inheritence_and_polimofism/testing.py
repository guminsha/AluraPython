from current_account import CurrentAccount
from saving_account import SavingAccount
from investiment_account import InvestimentAccount
from salary_account import SalaryAccount

account1 = CurrentAccount(111)
account2 = SavingAccount(222)
# account3 = InvestimentAccount(333)
account4 = SalaryAccount(444)
account5 = SalaryAccount(444)

accounts_list = [account1, account2]

# The elements of a lists must be treated the same way
# for account in accounts_list:
# 	account.deposit(1000)
# 	account.month_deductions()
# 	print(account)

print(account4)
print(account5)
print(account4 == account5) # __eq at salary_account
print(account5 in [account4])

account4.deposit(100)
print(account4 == account5) # __eq at salary_account

