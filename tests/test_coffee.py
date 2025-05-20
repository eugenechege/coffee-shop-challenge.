import unittest
from customer import Customer
from coffee import Coffee

class TestCoffee(unittest.TestCase):

    def test_valid_coffee_name(self):
        coffee = Coffee("Latte")
        self.assertEqual(coffee.name, "Latte")

    def test_invalid_coffee_name(self):
        with self.assertRaises(ValueError):
            Coffee("Al")

    def test_orders_and_customers(self):
        c1 = Customer("Eugene")
        c2 = Customer("Sifa")
        coffee = Coffee("Mocha")

        c1.create_order(coffee, 4.0)
        c2.create_order(coffee, 5.0)

        self.assertEqual(coffee.num_orders(), 2)
        self.assertEqual(len(coffee.customers()), 2)

    def test_average_price(self):
        coffee = Coffee("Cappuccino")
        c1 = Customer("Jude")
        c2 = Customer("Lana")

        c1.create_order(coffee, 4.0)
        c2.create_order(coffee, 6.0)

        self.assertEqual(coffee.average_price(), 5.0)

if __name__ == '__main__':
    unittest.main()
