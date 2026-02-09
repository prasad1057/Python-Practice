# Q. Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

class Car():
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def full_name(self):
        return f'{self.brand} {self.model}'
    
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)           # initialize Car attributes
        self.battery_size = battery_size
        
my_car = ElectricCar('Tesla','Safari','85kWh')

# Checking instance types
print(isinstance(my_car,Car))
print(isinstance(my_car,ElectricCar))