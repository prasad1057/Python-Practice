# 2. Write a program to find maximum and minimum element in a list.


def listfun(num):
    list1 = []
    
    for i in range(1,num+1):
        n = int(input('Enter number that put into the list: '))
        list1.append(n)
    
    return list1


def minMax(result):
    
    maximum = result[0]
    minimum = result[0]

    for i in result:
        if i > maximum:
            maximum = i
        
        if i < minimum:
            minimum = i
            
    return maximum,minimum


#-----------------------------------------------


num = int(input('Enter number: '))
result = listfun(num)
print('User Input List:',result)



maximum, minimum = minMax(result)
print("Maximum element:", maximum)
print("Minimum element:", minimum)
        