print('-----------------Example 1: Age Validation-------------------')

class InvalidAge(Exception):
    pass

age = int(input('ENter the age: '))

try:
    if age < 18:
        raise InvalidAge('Age must be 18 or above')
    
    print('Eligible to vote')
    
except InvalidAge as e:
    print(e)
    
    
    
    
print('---------------------Example 2: Negative Number Not Allowed--------------------')

class NegativeNumberError(Exception):
    pass


num = int(input("Enter a number: "))

try:
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")

    print("Number is:", num)

except NegativeNumberError as e:
    print(e)
    
    
    
print('---------Example 3: Bank Balance------------')   
    
class InsufficientBalance(Exception):
    pass


balance = 5000
withdraw = int(input("Enter withdrawal amount: "))

try:
    if withdraw > balance:
        raise InsufficientBalance("Insufficient balance.")

    balance -= withdraw
    print("Remaining Balance:", balance)

except InsufficientBalance as e:
    print(e)
    
    
    
    
    

'''
## Interview Tip

To create your own exception, always follow these 3 steps:

1. Create a class that inherits from Exception.
class MyException(Exception):
    pass


2. Raise the exception.
raise MyException("Error message")


3. Handle it using try...except.
try:
    ...
except MyException as e:
    print(e)

'''
