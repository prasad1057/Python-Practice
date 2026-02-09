'''
# 🟨 Python Functions – Writing Reusable Code

# 🔷 What is a Function?
# A function is a block of code that performs a specific task and can be reused whenever needed.

# 🔹 Why Use Functions?
- Makes your code organised
- Avoids repeating code
- Makes testing and debugging easier
- Helps with modular programming

🔶 Step 1 : Defining a funcion
def greet():
    print("Hello World")

greet()

🔶 Step 2 : Fucntion with parameters (Inputs)
def greet_user(name):
    print("Hello",name)

greet_user("Prasad")


🔶 Step 3 : Function with return (Output)
def square(num):
    retrun num * num

result = sqaure(2)
print(result)
    

🔶 Step 4 : Function with multiple parameters
def add(a,b):
    return a + b

print(add(1,2))


🔶 Step 5: Default parameters

def greet(name="User"):
    print("hello",name)
    
greet()             # hello User
greet("Prasad")     # hello Prasad


🔶 Step 6 : Keyword Arguments
def student_info(age,name):
    print(name,age)

# student_info(age=22,name="Pranav")
    

🔶 Step 7 : Return Multiple Values
def cal(x,y):
    return x+y, x-y
    
s,d = cal(10,5)
print("Sum is :",s)
print("Difference :",d)

 # 📌 Summary Table

| Feature         | Example                         |
| --------------- | ------------------------------- |
| Define function | `def greet():`                  |
| Call function   | `greet()`                       |
| Parameters      | `def greet(name):`              |
| Return value    | `return value`                  |
| Default value   | `def greet(name="User"):`       |
| Multiple return | `return a, b` → `x, y = func()` |

'''

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        False
        
print(is_even(2))       # True


# 🧪 Q1. Create a function called greet() that prints "Welcome to Python!"
def greet():
    print("Welcome to Python !")
greet()


# 🧪 Q2. Create a function hello_name(name) that takes a name and prints "Hello, <name>!"
# Call it with your name.

def hello_name(name):
    print("Hello",name)
    
hello_name("Prasad")


# 🧪 Q3. Create a function square(num) that returns the square of the number.

num = int(input("Enter the number for square: "))
def square(num):
    return num * num

square_of_number = square(num)
print(square_of_number)

# 🔸 Functions with Conditions
# 🧪 Q4. Write a function is_even(num) that returns True if a number is even, else False.

num = int(input("Enter number for checking that s no is even or not : "))
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(num))


# 🧪 Q5. Write a function max_of_two(a, b) that returns the larger of the two numbers.
def max_of_two(a,b):
    if a > b:
        return a
    else:
        return b

print(max_of_two(2,5))


# 🧪 Q6. Write a function grade(score) that returns:
# "A" for 90+
# "B" for 75–89
# "C" for 60–74
# "F" otherwise

def grade(score):
    if score > 90:
        print("A")
    elif score >= 75 and score < 90:
        print("B")
    elif score >= 60 and score < 75:
        print("C")
    else:
        print("F")
        
grade(78)


# 🔸 Functions with Loops

# 🧪 Q7. Write a function print_table(n) that prints the multiplication table of a number up to 10.
def print_table(n):
    for i in range(1,11):
        print(n, "x", i, "=", n*i)
        
print_table(8)


# 🧪 Q8. Write a function count_vowels(text) that counts and returns the number of vowels in a string.
def count_vowels(text):
    count = 0
    vowels = 'aeiou'
    for i in text:
        if i in vowels:
            count = count + 1
    return count
    
print(count_vowels("Prasad"))


def count_vowls(text):
    count = 0
    vowels = 'aeiou'
    vdeict = {}
    for i in text:
        if i in vowels:
            vdeict[i] = count + 1
            count = count + 1
    return vdeict

print(count_vowls("Prasad Nikhil Gauri Sujata Pranav Katta"))


# 🧪 Q9. Write a function reverse_number(n) that reverses a number using a loop.
# Example: 123 → 321

def reverse_number(num):
    reverse_num = 0
    n = num
    while n > 0:
        last = n % 10
        reverse_num = reverse_num * 10 + last
        n = n // 10
    print(reverse_num)
    
reverse_number(1243)


# 🧪 Q10. Write a function sum_digits(n) that returns the sum of the digits of a number.
def sum_digits(n):
    total_sum = 0
    while n > 0:
        last = n % 10
        total_sum = total_sum + last
        n = n // 10
    print(total_sum)
    
sum_digits(111)