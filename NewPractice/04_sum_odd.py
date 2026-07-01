# 4. Sum of all odd numbers between 1 to n


def oddSum(n,sum):
    
    for i in range(1,n+1):
        if (i % 2) != 0:
            sum = sum + i
            
    return sum
    
    
n = int(input('Enter number: '))
sum = 0

result = oddSum(n,sum)
print('Sum of Odd Series:',result)