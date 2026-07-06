# Armstrong number.


def armstrong(num):
    
    og = num
    
    temp = num
    count = 0
    while temp > 0:
        count += 1
        temp = temp // 10
        
    print('Count:',count)
    
    temp = num 
    sum = 0
    while(temp > 0):
        digit = temp % 10
        sum += digit ** count
        temp = temp // 10
        
    if og == sum:
        print(f"{num} is armsrtong number")
    else:
        print(f"{num} is not armstrong")
        
        
    
num = int(input('Enter number:'))
armstrong(num)