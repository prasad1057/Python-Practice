'''
Q. Write a program to print the first n prime numbers.
(Example: If n=5, output: 2, 3, 5, 7, 11)
'''

num = int(input('Enter the number: '))

count = 0
n = 2

while(count < num):         # loop till last condition (5 < 5)
    
    for i in range(2,n):        # 
        if n % i == 0:      # if loop is break in between then else bloack will not execute
            break           # if break statement is execute firstly and lastly then n only then else bloack will execute 
    else:
        print(n,end=',')
        count += 1          # c is increases to check further condition (5 < 5) 
        
    n += 1
    