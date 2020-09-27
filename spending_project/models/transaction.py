class Transaction:
    def __init__(self, amount, user, merchant, id = None, tag = None):
        self.amount = amount
        self.user = user
        self.merchant = merchant
        self.id = id
        self.tag = tag