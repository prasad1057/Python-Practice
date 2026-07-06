# Q. Modify the car class to encapsulate the brand attribute, making it private, and provide a getter method fot it.

'''
Encapsualtion:
Encapsulation is an OOP concept where data is hidden inside a class and accessed only through methods.
It helps protect data from direct modification and ensures controlled access.

For example, in a bank account class, balance is hidden and 
            can only be accessed using deposit or withdraw methods.
'''

# __ (double underline) se mamla hota he private , u can access within class but outside class u access with methods only

class Car():
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand + " !"          # here __ before brand meand we are making the brand is private (Enscapsulation) 
    

class ElectricCar(Car):
    
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
        
        
my_car = ElectricCar('Tesla', 'Model S', '85kWh') 
#print(my_car.__brand)                  # we can not access directly 

print(my_car.get_brand())               # we can access with the helf of method called get_brand whcih are made 