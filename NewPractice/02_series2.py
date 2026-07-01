def factSeries(n,fact):
    
    for i in range(1,n+1):
        fact = fact * i
        
    return fact

n = int(input('Enter the number: '))
fact = 1

result = factSeries(n,fact)
print('Fact of series:',result)