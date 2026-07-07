# Find common elements in two lists.


def commonEle():
    
    num = int(input('Enter number: '))
    list1 = []
    for i in range(1,num+1):
        ele = int(input('number add into list1: '))
        list1.append(ele)
        
    print('List1:',list1)
    
    
    num = int(input('Enter number: '))
    list2 = []
    for i in range(1,num+1):
        ele = int(input('number add into list2: '))
        list2.append(ele)
        
    print('List2:',list2)
    
    common = []
    for i in list1:
        if i in list2:
            common.append(i)
            
    return common

print(commonEle())