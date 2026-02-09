'''
🟨 Step 1: Arithmetic Operators

a = 10
b = 10
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(a//b)
print(a%b)
print(a**b)

1. // — Floor Division
It divides two numbers and rounds down (floors) the result to the nearest whole number.
It removes the decimal part completely, even if the number is negative.
📌 Example:

print(5 // 2)     # Output: 2    (5 / 2 = 2.5 → floor is 2)
print(9 // 4)     # Output: 2    (9 / 4 = 2.25 → floor is 2)
print(-5 // 2)    # Output: -3   (-5 / 2 = -2.5 → floor is -3)


2. % — Modulus
It gives the remainder after division.
This is the leftover part after using //.
📌 Example:
print(5 % 2)      # Output: 1    (5 = 2*2 + 1)
print(9 % 4)      # Output: 1    (9 = 4*2 + 1)
print(-5 % 2)     # Output: 1    (In Python, result is always non-negative if divisor is positive)


3. ** — Power / Exponent
Raises a number (base) to the power of another (exponent).
📌 Example:
print(2 ** 3)     # Output: 8     (2 × 2 × 2)
print(5 ** 2)     # Output: 25    (5 × 5)
print(9 ** 0.5)   # Output: 3.0   (Square root of 9)



🟨 Step 2: Comparison Operators

| Operator | Checks If        | Example          |
| -------- | ---------------- | ---------------- |
| `==`     | Equal to         | `5 == 5` → True  |
| `!=`     | Not equal to     | `5 != 3` → True  |
| `>`      | Greater than     | `5 > 3` → True   |
| `<`      | Less than        | `5 < 3` → False  |
| `>=`     | Greater or equal | `5 >= 5` → True  |
| `<=`     | Less or equal    | `5 <= 4` → False |

a=10
b=2
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)


🟨 Step 3: Logical Operators
| Operator | Meaning                      |
| -------- | ---------------------------- |
| `and`    | True if both are True        |
| `or`     | True if at least one is True |
| `not`    | Reverses True/False          |


a=5
b=10

print(a>3 and b>3)
print(a>3 or b>6)
print(not(a>6))


🟩 Step 4: If-Else Conditions

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")



🟦 Step 5: if, elif, and else

marks=int(input("Enter marks :"))

if marks >=90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 35:
    print("Grade D")
else:
    print("Grade: Fail")
    
'''

# -----------------------------------------------------

# 🧠 Q1. Even or Odd
# Task:
# Ask the user to enter a number. Check if it is even or odd.
num1=int(input("Enter number to check if it is even or odd :"))
if(num1 % 2 == 0):
    print("Even")
else:
    print("Odd")
    
# 🧠 Q2. Check Positive, Negative, or Zero
# Task:
# Take a number as input and print whether it is:
num2 = int(input("Enter the numeber to check it is positive, negative or zero : "))
if (num2 > 0):
    print("Positive")
elif (num2 < 0):
    print("Neagtive")
else:
    print("zero")
    

# 🧠 Q3. Simple Calculator
# Task:
# Ask the user to enter 2 numbers and an operator (+, -, *, /). Perform the operation and display the result.
# Enter first number: 5  
# Enter second number: 3  
# Enter operator: *  
# Output: 5 * 3 = 15

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
oprator=input("Enter operator : ")

if oprator=='+':
    print(num1,"+", num2 , "=", num1+num2)
elif oprator=='-':
    print(num1,"-", num2 , "=", num1-num2)
elif oprator=='*':
    print(num1,"*", num2 , "=", num1*num2)
elif oprator=='/':
    print(num1,"/", num2 , "=", num1/num2)
else:
    print("Invalid operator")
    
    
# 🧠 Q4. Voter Eligibility Checker
# Task:
# Ask for the user’s age. If age is 18 or more, print "You can vote", else print "Not eligible yet".

age=int(input("Enter age: "))
if age >= 18:
    print("Ypu are eligible for vote ")
else:
    print("Not eligible for vote ")
    

# 🧠 Q5. Max of 3 Numbers
# Task:
# Ask the user to enter three numbers and print the largest one.
num3 = int(input("Enter the number1 : "))
num4 = int(input("Enter the number2 : "))
num5 = int(input("Enter the number3 : "))

if (num3 > num4) and (num3 > num5):
    print("Largest number is : ", num3)
elif (num4 > num3) and (num4 > num5):
    print("Largest number is : ", num4)
else:
    print("Largest number is : ", num5)
    

# 🧠 Q6. Number in Range
# Task:
# Ask the user to enter a number and check if it is between 1 and 100

num6=int(input("enter a number and check if it is between 1 and 100 : "))
if num6>=1 and num6<=100:
    print("Number is between 1 to 100")
else:
    print("Number is not between 1 to 100")


# 🧠 Q7. Password Checker
# Task:
# Ask the user to enter a password.
# If the password is "admin123" → print: "Access granted"
# Otherwise → "Access denied"

passwd=str(input("Enter password:"))
if passwd=="admin123":
    print("Access granted")
else:
    print("Acess denied")
    
    
# 🧠 Q8. Grading System
# Task:
# Ask user for marks (0–100) and assign:
# A: 90+
# B: 75–89
# C: 60–74
# F: < 60

marks = int(input("Enter your marks (0–100): "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")


# 🧠 Q9. Leap Year Checker
# Task:
# Ask the user for a year and check if it’s a leap year or not.

year=int(input("Enter year to check if its leap or not : "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("Leap year")
else:
    print("Not a leap year")
    

# 🧠 Q10. Calculator with Logical Conditions
# Task:
# Take 2 numbers and:
# Print “Equal” if they are the same
# Print “First is greater” if first > second
# Print “Second is greater” otherwise

num7 = float(input("Enter first number: "))
num8 = float(input("Enter second number: "))

if num7 == num8:
    print("Equal")
elif num7 > num8:
    print("First is greater")
else:
    print("Second is greater")