'''
Q. Write a program to print the first n prime numbers.
(Example: If n=5, output: 2, 3, 5, 7, 11)
'''

num = int(input('Enter the number: '))
n = 2
count = 0

while(count < n):
    
    for i in range(2,n):
        if num % i == 0:
            break
    else:
        print(num,end=' ')
        count += 1
        
    num += 1
    