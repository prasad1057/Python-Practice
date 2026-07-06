# Q. Demonstrate polymorphoism by defining a mthod fuel_type in both Car and ElectricCar classes, but with different bheaviour

# Polymorphsim measn same class name with different functionalities


class Car():
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def fuel_type(self):
        return 'Petrol or Diesel'
        
class ElectricCar(Car):
    
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):                # fuel_type method is already in Car class but thier working is different
        return 'Electric Charge'
    

my_tesla = ElectricCar('Tesla', 'Model S', '85kWh')
print(my_tesla.fuel_type())

my_safari = Car('Tata', 'Safari')
print(my_safari.fuel_type())