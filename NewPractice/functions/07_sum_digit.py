# 7. Write a program to find sum of digits of a number.


def sumDigit(num):
    
    total = 0
    
    while (num > 0):
        digit = num % 10
        total = digit + total
        num = num // 10
        
    return total
               


num = int(input('Enter Number: '))

result = sumDigit(num)
print('Sum of digit:',result)