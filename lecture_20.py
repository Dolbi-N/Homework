# ###############
# Task 1
# ###############

from dataclasses import dataclass, asdict
import json

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool

product1 = Product("Phone", 5500.50, True)
product2 = Product("Laptop", 4300.00, True)
product3 = Product("Tablet", 1200.25, False)

print(product1)
print(product2)
print(product3)


# ##############
# Task2
# ##############

data1 = asdict(product1)
data2 = asdict(product2)
data3 = asdict(product3)

json_data1 = json.dumps(data1, indent=4)
json_data2 = json.dumps(data2, indent=4)
json_data3 = json.dumps(data3, indent=4)

print(json_data1)
print(json_data2)
print(json_data3)


# ##########
# Task 3
# ##########

json_string = '{"name": "Laptop", "price": 2500, "in_stock": true}'

data = json.loads(json_string)

p = Product(**data)

print(type(p))
print(p)
print(p.name)
print(p.price)
print(p.in_stock)