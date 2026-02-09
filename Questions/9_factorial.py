# ✅ Factorial using if–else and loop

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial not defined for negative numbers.")
else:
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial of", num, "is", fact)
    
    
'''

# ✅ Factorial using while loop
num = int(input("Enter a number: "))

fact = 1
i = 1

while i <= num:
    fact *= i
    i += 1

print("Factorial is:", fact)




# ✅ Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial is:", factorial(num))


'''