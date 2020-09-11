class BankAccount:

    def __init__(self, input_holder_name, input_balance, input_type):
        self.holder_name = input_holder_name
        self.balance = input_balance
        self.type = input_type
        self._rates = {
            "Personal": 10,
            "Business": 50,
        }

    def pay_in(self, amount):
        self.balance += amount 

    def pay_monthly_fee(self):
        if self.type == "Business":
            self.balance -= 50
        else:
            self.balance -= 10

# def get_account_name(account):
#     return account["holder_name"]