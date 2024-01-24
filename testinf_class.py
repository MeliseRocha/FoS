from utils import Address, Circle


address = Address(street= "Passauer", number= "10", postcode= "84347", city= "Pfarrkirchen")

print(address.get_address())


r = Circle(radius = 1)

print(r.get_area())