# 5. Sum of all prime numbers between 1 to n


def primeSum(n):
    sum = 0
    
    for i in range(1,n+1):
        count = 0
        
        for j in range(1,i+1):
            if i % j == 0:
                count +=1
                
        if count == 2:
            sum += 1
    
    return sum


n = int(input('Enter number: '))

result = primeSum(n)
print('Sum of Prime Numbers:',result)