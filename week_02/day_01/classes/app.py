from modules.bank_account import *

bank_account = BankAccount("John", 500, "Business")
bank_account_2 = BankAccount("Carol", 300, "Personal")
# print(get_account_name(account))

print(bank_account.holder_name)

bank_account.holder_name = "Ada"

print(bank_account.holder_name)

print(bank_account.balance)

bank_account.pay_in(50)

print(bank_account.balance)
print(bank_account_2.balance)

bank_account.pay_monthly_fee()
bank_account_2.pay_monthly_fee()

print(bank_account.balance)
print(bank_account_2.balance)

