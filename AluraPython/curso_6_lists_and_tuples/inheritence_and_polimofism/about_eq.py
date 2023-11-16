from account import Account
from current_account import CurrentAccount
from saving_account import SavingAccount
from investiment_account import InvestimentAccount
from salary_account import SalaryAccount

print(isinstance(CurrentAccount(34), CurrentAccount))
print(isinstance(InvestimentAccount(134), InvestimentAccount))
print(isinstance(SalaryAccount(6322), SalaryAccount))

