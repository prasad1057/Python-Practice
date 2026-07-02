# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not

def userDict():
    
    dict1 = {}
    num = int(input('ENter the numer of key-value pairs: '))
    
    for i in range(1,num+1):
        key = input(f'Enter key {i}: ')
        value = input(f'Enter value {i}: ')
        
        dict1[key] = value
        
    return dict1


def checkKey(r):
    k = input('Enter key to search: ')
    
    if k in r:
        return 'Yes, key Exist!'
    else:
        return 'Key does not exist!'
    


user_dict = userDict()
print('User Input Dictionary:',user_dict)


result = checkKey(user_dict)
print(result)

