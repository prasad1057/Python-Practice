# 9. Write a program to check if entered number is a palindrome or not.


def pallindrome4(n):
    og_no = n
    rev_no = 0
    
    while (n > 0):
        digit = n % 10
        rev_no = rev_no * 10 + digit
        n = n // 10
        
    return og_no == rev_no

n = int(input('Enter the number: '))
if pallindrome4(n):
    print('Its a Pallindrome')
else:
    print('Its not a Palldindrome')