class Pub:
    def __init__(self, name, drinks):
        self.name = name
        self.till = 50
        self.drinks = drinks

    def increase_till(self, amount):
        self.till += amount

    def sell_drink(self, customer, drink):
        if customer.age < 18 or customer.drunkeness > 10:
            return
            
        customer.buy_drink(drink)
        self.increase_till(drink.price)
