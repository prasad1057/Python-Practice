# A prime number is a number greater than 1 that has no divisors other than 1 and itself.
# Examples: 2, 3, 5, 7, 11 …



num = int(input('Enter number: '))

if num <= 1:
    print('Not a prime number')
    
else:
    for i in range(2,num):
        if num % i == 0:
            print('Not a prime number')
            break
    else:
        print('It is a prime number')