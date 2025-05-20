import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):

    def test_order_creation_valid(self):
        c = Customer("John")
        coffee = Coffee("Americano")
        order = Order(c, coffee, 3.0)

        self.assertEqual(order.customer, c)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 3.0)

    def test_invalid_price_low(self):
        c = Customer("Jane")
        coffee = Coffee("Latte")
        with self.assertRaises(ValueError):
            Order(c, coffee, 0.5)

    def test_invalid_price_type(self):
        c = Customer("Jane")
        coffee = Coffee("Latte")
        with self.assertRaises(ValueError):
            Order(c, coffee, "expensive")

if __name__ == '__main__':
    unittest.main()
