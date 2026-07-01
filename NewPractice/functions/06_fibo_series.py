'''
Write a program to find print the following Fibonacci series using
functions:
1 1 2 3 5 8 n terms
'''


def fiboSeries(n):
    a = 0
    b = 1
    series = []
    
    for i in range(1,n+1):
        c = a + b
        series.append(c)
        a = b
        b = c
    
    return series


n = int(input('Enter number:'))

result = fiboSeries(n)
print('Series:',result)