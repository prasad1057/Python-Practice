'''
Q. Write a program to find and print the first n palindrome numbers (starting from 0 or a specific range).
(Example: If n=12, output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22)
'''


n = int(input("Enter how many palindrome numbers you want: "))

count = 0
num = 0

while count < n:
    original = num
    reverse = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp = temp // 10

    if original == reverse:
        print(original, end=" ")
        count += 1

    num += 1
