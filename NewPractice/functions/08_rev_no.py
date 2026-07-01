# 8. Write a program find reverse of a number

def revNo(n):
    
    rev = 0
    
    while(n > 0):
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
        
    return rev


n = int(input('Enter number:'))

result = revNo(n)
print('Rverse No:',result)