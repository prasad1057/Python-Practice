def Series(n,sum):
    
    for i in range(1,n+1):
        sum = sum + i
        
    return sum

n = int(input('Enter the number: '))
sum = 0

result = Series(n,sum)
print('Sum of Series:',result)