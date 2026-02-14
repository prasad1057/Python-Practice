# WAP to check number is fibonacci number or not

number = int(input("Enter the number: "))

a = 0
b = 1

while b <= number:
    if b == number:
        print(f"{number} is a Fibonacci number")
        break
    c = a + b
    a = b
    b = c
else:
    print(f"{number} is not a Fibonacci number")
