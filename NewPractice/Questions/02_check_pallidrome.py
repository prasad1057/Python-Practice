# Check palindrome.


def pallidrome(num):
    og_n = num
    rev = 0
    
    while(num > 0):
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
        
    if og_n == rev:
        print('Pallindrome')
    else:
        print('not')


num = int(input('Enter the number: '))
pallidrome(num)    
