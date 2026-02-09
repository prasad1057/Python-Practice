'''
# 1️⃣ Variables & Data Types
"""
- IN python , a variable is name that refers to value stored in memory
python is dynamically typed
does not require to define data types
"""

a = 1        # int
b = 3.14     # float
c = "Hello"  # str
d = True     # bool

name = "Prasad"
print(name)

age = 21
is_learing = True
height = 6.2

print(age)
print("Type of age is ", type(age))

print(is_learing)
print("Type of age is ", type(is_learing))

print(height)
print("Type of age is ", type(height))

print(name)
print("Type of age is ", type(name))


# 2️⃣ Input from User

age = int(input("Prasad, Enter ur age "))
height = float(input("Enter u r height : "))

if age >18:
    print('U r eligible for driving licence')
else:
    print('U r not eligible for driving licence')

print("Your age is ", age, "and height is ", height)


city, temp , is_raining="bhiwandi" ,  29, True
print(city, temp , is_raining)


# Convert km to m
distance = int(input("Enter disatnce in kilometers : "))
print("Distance in meters is : ", distance * 1000)

# ARea of Rectangle
width=float(input("Enter width:"))
height=float(input("enter height:"))

print("area = ", width*height)

'''

# ------------------------------------------------------

# Q.1 Swap two variable
a,b = 4,5
print("Before Swapping :", "a =",a, "b =",b)
a,b = b,a
print("After Swapping : ", "a =",a, "b =",b)

# Q.2 Dispaly Data Types of Variable
a = 1
b = 3.14
c = "prasad"
d = True
print("a:",type(a),"b:",type(b),"c:",type(c),"d:",type(d))

# Q.3 Simple Calculator
num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
print("Additon : ",num1 + num2)
print("Subtraction : ",num1 - num2)
print("Multip;ication : ",num1 * num2)
print("Division : ",num1 / num2)

# Q.4 Ask the user to enter seconds. Convert it into miuntes and seconds
sec = int(input("Enter the seconds : "))
print( int(sec/60) ,  "Minutues" , sec%60, "seconds.")

