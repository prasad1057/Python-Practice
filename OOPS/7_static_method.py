# Q. Add a static method to the Car class that returns a general description of car.

"""
@staticmethod means:

Method does not depend on object data

No use of self or cls
"""

class Car():
    
     # Constructor to initialize brand and model
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    @staticmethod           # Static method: does not use self or class variables   
    def general_description():
        return 'Car are means of transport'
    

# Creating an object of Car
my_car = Car('Tata', 'Nexon')

# Calling static method using object
print(my_car.general_description())

# Calling static method using class name (recommended)
print(Car.general_description())