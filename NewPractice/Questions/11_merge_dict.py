# Merge Dictionaries

def mergeDict():
    
    dict1 = {}
    num = int(input('ENter number for dict1: '))
    
    for i in range(1,num+1):
        key = input(f'enter key {i}: ')
        value = input(f'enter value{i}: ')
        
        dict1[key] = value
        
        
    dict2 = {}
    num = int(input('ENter number for dict2: '))
    
    for i in range(1,num+1):
        key = input(f'enter key {i}: ')
        value = input(f'enter value{i}: ')
        
        dict2[key] = value
        
    add_dct = {}
    
    for i in dict1:
        add_dct[i] = dict1[i]
    
    for j in dict2:
        add_dct[j] = dict2[j]
        
    return add_dct
             

print(mergeDict())