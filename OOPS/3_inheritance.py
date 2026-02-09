# Q. Create an ElectricCar class that inherits from the Car class and has an additonal attribute battery_size.

# Parent class Car

class Car():
    
    # Constructor: runs automatically when object is created
    # Initializes brand and model of the car
    def __init__(self, brand, model):
        self.brand = brand               # Stores car brand (e.g., Tesla)
        self.model = model
    
    def full_name(self):
        return f'{self.brand} {self.model}'
    

class ElectricCar(Car):
    # Constructor for ElectricCar
    # It takes brand, model (from Car) and battery_size (new attribute)

    def __init__(self, brand, model, battery_size): 
        super().__init__(brand, model)          # initialize Car attributes
        self.battery_size = battery_size


# Creating an object of ElectricCar class
my_tesla = ElectricCar('Tesla', 'Model S', '85kWh') 
print(my_tesla.model) 

# Calling full_name() method from Car class
# Even though object is ElectricCar, it can use parent methods
print(my_tesla.full_name())      