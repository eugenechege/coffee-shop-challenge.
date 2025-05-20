import unittest
from customer import Customer
from coffee import Coffee

class TestCustomer(unittest.TestCase):

    def test_name_setter_and_getter(self):
        c = Customer("Alice")
        self.assertEqual(c.name, "Alice")

    def test_invalid_name_too_long(self):
        with self.assertRaises(ValueError):
            Customer("A" * 16)

    def test_invalid_name_not_string(self):
        with self.assertRaises(ValueError):
            Customer(123)

    def test_create_order_and_relationships(self):
        c = Customer("Bob")
        coffee = Coffee("Espresso")
        c.create_order(coffee, 2.5)
        self.assertEqual(len(c.orders()), 1)
        self.assertEqual(c.coffees()[0], coffee)

if __name__ == '__main__':
    unittest.main()
