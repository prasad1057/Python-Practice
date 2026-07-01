def armstrongNumber(n):
    
    og = n
    
    temp = n
    count = 0
    while (temp > 0):
        count += 1
        temp = temp // 10
        
    temp = n
    sum = 0
    while (temp > 0):
        digit = temp % 10
        sum += digit ** count
        temp = temp // 10
        
    return og, (og == sum)

    
n = int(input('ENter number: '))

num, result = armstrongNumber(n)


if result:
    print(f'{num} is armstrong number')
else:
    print(f'{num} is not a armstrong number')