from math import pi

class Address:

    #contstructor 

    def __init__(self, street: str, number: int, postcode: int, city: str):

        self.street = street
        self.number = number 
        self.postcode = postcode
        self.city = city 


    def get_address(self):
        return f"Street: {self.street}, {self.number}, postal code: {self.postcode}, city: {self.city}"


class Circle:

    def __init__(self, radius: int):

        self.radius = radius 

    
    def get_area(self):

        radius = self.radius

        radius_squared = radius * radius 

        area = pi * radius_squared

        return  f"The area is: {area}"