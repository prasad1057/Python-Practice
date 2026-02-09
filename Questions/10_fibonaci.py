# ✅ Fibonacci Series using if–else and loop

num = int(input('Enter the number: '))

if num <= 0:
    print(' Please enter a positive number')
    
elif num == 1:
    print(0)

else:
    a, b = 0, 1
    print(a,b,end='')
    
    for i in range(2,num):
        c = a + b
        print(c,end='')
        a, b = b, c 
        
        
# ✅ Fibonacci Series using while loop
n = int(input("Enter number of terms: "))

a, b = 0, 1
count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1



# ✅ Fibonacci using recursion
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = int(input("Enter number of terms: "))
for i in range(n):
    print(fib(i), end=" ")
