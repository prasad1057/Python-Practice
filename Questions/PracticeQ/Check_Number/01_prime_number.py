# WAP to check it is prime number or not.

num = int(input('Enter the number to check if it is prime or not: '))

count = 0

for i in range(1,num+1):
    if num % i == 0:
        count += 1
        
if count == 2:
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')
    