import unittest
from classes.pub import Pub
from classes.drink import Drink
from classes.customer import Customer


class TestPub(unittest.TestCase):
    def setUp(self):
        drinkCollection = [Drink("Smol Beer", 2, 3.00),
                           Drink("Tol Boi", 4, 4.50)]
        self.pub = Pub("The Testing Arms", drinkCollection)

        self.customers = {"customer older than 18": Customer("Rosie", 29, 25.00),
                        "customer younger than 18": Customer("Oliver", 10, 4)}
                        

    def test_increase_till(self):
        self.pub.increase_till(5)

        self.assertEqual(55, self.pub.till)

    def test_sell_drink_customer__older_than_18__does_sell(self):
        self.pub.sell_drink(self.customers["customer older than 18"], self.pub.drinks[0])

        self.assertEqual(22, self.customers["customer older than 18"].wallet)
        self.assertEqual(53, self.pub.till)

    def test_sell_drink_customer__younger_than_18__doesnt_sell(self):
        self.pub.sell_drink(self.customers["customer younger than 18"], self.pub.drinks[0])

        self.assertEqual(4, self.customers["customer younger than 18"].wallet)
        self.assertEqual(50, self.pub.till)

    def test_sell_drink_to_customer__drunk__doesnt_sell(self):
        self.customers["customer older than 18"].consume_drink(self.pub.drinks[1])
        self.customers["customer older than 18"].consume_drink(self.pub.drinks[1])
        self.customers["customer older than 18"].consume_drink(self.pub.drinks[1])

        self.pub.sell_drink(self.customers["customer older than 18"], self.pub.drinks[1])
        self.assertEqual(25.00, self.customers["customer older than 18"].wallet)
        self.assertEqual(50, self.pub.till)

    def test_sell_drink_to_customer__sober__does_sell(self):
        self.pub.sell_drink(self.customers["customer older than 18"], self.pub.drinks[1])
        self.assertEqual(20.50, self.customers["customer older than 18"].wallet)
        self.assertEqual(54.50, self.pub.till)