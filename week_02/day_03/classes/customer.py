
class Customer:
    def __init__(self, name, age, wallet):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkeness = 0

    def buy_drink(self, drink):
        self.wallet -= drink.price

    def consume_drink(self, drink):
        self.drunkeness += drink.alcohol_level

    def buy_food(self, food):
        self.wallet -= food.price

    def consume_food(self, food):
        self.drunkeness -= food.rejuvenation_level