# 6.  Write a program to find the factorial of a number using while loop.

number = int(input('Enter number: '))
i = 0

while(i <= number):
    fact = number * i
    i += 1
print(fact)