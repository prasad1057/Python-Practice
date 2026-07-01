
def listfun(num):
    
    list1 = []    
    for i in range(1,num+1):
        n = int(input('Enter the numbers that add into list: '))
        list1.append(n)
    
    return list1
    
    
num = int(input('ENter number: '))
result = listfun(num)
print('User Input List:',result)


def sumEle():
    
    sum = 0
    count = 0
    
    # for i in result:
    #     count += 1
    # print('COunt',count)
        
    # for i in range(0,count):
    #     sum += i
    
    for i in result:
        sum += i
    
    return sum

print(sumEle())
    

