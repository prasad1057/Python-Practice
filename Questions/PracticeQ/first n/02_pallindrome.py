'''
Q. Write a program to find and print the first n palindrome numbers (starting from 0 or a specific range).
(Example: If n=12, output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22)
'''

num = int(input('Enter the number: '))

count = 0

while count < num:
    
    for i in range(1,num):
        rem = num % 10          # last digit
        num = num // 10         # reamining digits

        count += 1
    print(count)
    
    