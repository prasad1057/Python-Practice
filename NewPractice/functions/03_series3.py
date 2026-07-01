def powerSeries(n,power):
    
    for i in range(1,n+1):
        power = power + (i ** i)
        
    return power


n = int(input('Enter the number: '))
power = 0

result = powerSeries(n,power)
print('Power of Series:',result)