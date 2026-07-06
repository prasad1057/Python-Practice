# Q. Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.print

class Car():
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    
class Battery:
    def battery_info(self):
        return 'This is Battery Info'
    
class Engine:
    def enigne_info(self):
        return 'This is Engine Info'
    
class ElectricCar(Battery, Engine, Car):
    pass


my_car = ElectricCar('Tesla','Model S')
print(my_car.enigne_info())
print(my_car.battery_info())
