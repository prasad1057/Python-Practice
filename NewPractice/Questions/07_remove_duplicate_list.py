
def userList(num):
    
    list1 = []
    
    for i in range(1,num+1):
        ele = int(input('Enter number of ele to put in list: '))
        list1.append(ele)
        
    return list1


num = int(input('ENter number: '))
result = userList(num)
print('User Input List:',result)


new_list = []

for i in result:
    if i not in new_list:
        new_list.append(i)
        
print(new_list)