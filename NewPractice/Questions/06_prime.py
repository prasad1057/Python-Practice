# Prime Number


def primeNo(num):
    
    count = 0
    
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
            
    if count == 2:
        print('Prime')
    else:
        print('not')
        
num = int(input('Enter number: '))
primeNo(num)







print('To print prime numbers from 1 to 50, use a loop to check each number.')
for num in range(1, 51):

    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num, end=" ")