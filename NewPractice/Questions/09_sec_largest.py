# Second Largest

def secLargest():
    
    num = int(input('Enter number of elements: '))    
    list1 = []
    for i in range(1,num+1):
        ele = int(input('Number to put in list: '))
        list1.append(ele)
    print('List:',list1)
    
    
    max = list1[0]
    sec_max = list1[0]
    
    for i in list1:
        if i > max:
            sec_max = max
            max = i
            
    print('Max:',max)
    print('Second Max:',sec_max)
    
    return max,sec_max

    
    

print(secLargest())
    
