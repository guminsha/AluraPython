from account import Account
from client import Client

account1 = Account(5321, "Caio", 15000, 20000)
account2 = Account(1532, "Leo", 5000)
account3 = Account(6265, "Brian", 2000)

account1.transfer(500, account2)

client1 = Client("evandro")
client1.name = "brian"

print(client1.name)

account3.limit = 3000
print(account3.limit)

account3.withdraw(7000)
print(account3.balance)

print(Account.bank_code())
print(Account.code_banks()["Bradesco"])


