num = int(input('Enter number: '))

a = 0
b = 1

for i in range(1,num+1):
    c = a + b
    print(c, end=' ')
    a = b
    b = c
    


def fibo(n):
    
    a=0
    b=1
    series = []
    
    for i in range(1,n+1):
        c = a + b
        series.append(c)
        a = b
        b = c
        
    return series

n = int(input('Enter number: '))
print(fibo(n))