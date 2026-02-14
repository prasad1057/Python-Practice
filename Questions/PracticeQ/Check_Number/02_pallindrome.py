# WAP to check number is pallidrome or not

num = int(input('Enter the number to check number is pallindrome or not: '))
original_num = num

    
rem1 = num % 10
num = num // 10
    
rem2 = num % 10
num = num // 10
    
rem3 = num % 10
num = num // 10
    
# print(rem1)
# print(num)    

pallidrome = (rem1 * 100) + (rem2 * 10) + (rem3 * 1)
print(pallidrome)

if original_num == pallidrome:
    print(f'{original_num} is a pallidrome number')

else:
    print(f'{original_num} is not a pallidrome number')    