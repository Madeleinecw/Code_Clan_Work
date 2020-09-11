import unittest
from classes.customer import Customer
from classes.drink import Drink
from classes.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Testy McTest", 30, 25.00)
        self.drinks = {"Weak Beer": Drink("Smol Beer", 2, 3.00),
                       "Strong Beer": Drink("Tol Boi", 4, 4.50)}
        self.food = Food("Pie", 5, 3)

    def test_buy_drink(self):
        self.customer.buy_drink(self.drinks["Weak Beer"])

        self.assertEqual(22, self.customer.wallet)

    def test_consume_drink(self):
        self.customer.consume_drink(self.drinks["Strong Beer"])
        
        self.assertEqual(4, self.customer.drunkeness)

    def test_buy_food(self):
        self.customer.buy_food(self.food)

        self.assertEqual(20.00, self.customer.wallet)

    def test_consume_food(self):
        self.customer.consume_food(self.food)

        self.assertEqual(-3, self.customer.drunkeness)