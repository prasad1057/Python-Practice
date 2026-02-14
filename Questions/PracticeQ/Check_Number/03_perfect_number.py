# WAP to check number is perfect or not

num = int(input('ENter the number to check if it is perfect or not: '))

sum = 0

for i in range(1,num):
    if num % i == 0:
        sum += i

if sum == num:
    print(f'{num} is a perfect number')
else:
    print(f'{num} is not a perfect number')