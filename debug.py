from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Eugene")
c2 = Customer("Sifa")

latte = Coffee("Latte")
mocha = Coffee("Mocha")

c1.create_order(latte, 3.5)
c2.create_order(latte, 4.5)
c1.create_order(mocha, 5.0)

print(c1.coffees())
print(latte.num_orders())
print(mocha.average_price())
