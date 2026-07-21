# 4. Write a program to reverse the list.

def listfun(num):
    list1 = []
    
    for i in range(1,num+1):
        n = int(input('Enter the number that add into list:  '))
        list1.append(n)
        
    return list1


def revList(result):
    start = 0
    end = len(result) - 1
        
    while (start < end):
        temp = result[start]
        result[start] = result[end]
        result[end] = temp
        
        start += 1
        end -= 1
        
    return result

num = int(input('ENter number: '))
result = listfun(num)
print('User Input List:',result)


revresult = revList(result)
print(revresult)