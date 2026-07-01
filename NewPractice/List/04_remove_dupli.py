def listfun(num):
    list1 = []
    
    for i in range(1,num+1):
        n = int(input('Enter the number that add into list:  '))
        list1.append(n)
        
    return list1

num = int(input('ENter number: '))
result = listfun(num)
print('User Input List:',result)

new_result = []
for i in result:
    if result[i] not in new_result:
        new_result.append(result[i])
        
print(new_result)