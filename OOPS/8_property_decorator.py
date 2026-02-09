# Q. Use a property decorator in the Car class to make the model attribute read only.

'''
Using the @property decorator, we can expose a variable for reading but 
restrict modification by not defining a setter. 
This makes the attribute read-only and improves data safety

'''

class Car():
    
    def __init__(self, brand, model):
        self.__brand = brand         # private variable 
        self.__model = model         #  private variable (read-only)
        
    def full_name(self):
        return f'{self.__brand} {self.__model}'
    
    @property
    def model(self):
        # getter method → allows read access
        return self.__model
      
      
my_car = Car('Tata', 'Nexon')

# my_car.model = 'Safari'       # ❌ ERROR: can't set attribute (read-only)
print(my_car.model)             # ✅ Allowed