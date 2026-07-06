# Sort list without using sort().

def sortList():
    
    list1 = []
    num = int(input('Enter number: '))
    for i in range(1,num+1):
        ele = int(input('Number of ele in list: '))
        list1.append(ele)
        
    print('Before sorting List:',list1)
    
    for i in range(len(list1)):
        for j in range(len(list1)-1):
            if list1[j] > list1[j+1]:
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
            
    print('After sorted:',list1)
    
print(sortList())
        
    