# Q.  Add a class variable to Car that keeps track of the number of cars created. 


class Car():
    
    total_car = 0
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
        Car.total_car += 1
        
    def full_name(self):
        return f'{self.brand} {self.model}'
    


Car('Tata', 'Safari')
Car('Tata', 'Nexon')
Car('Suzuki', 'Ertiga')

print(Car.total_car)        # output = 3