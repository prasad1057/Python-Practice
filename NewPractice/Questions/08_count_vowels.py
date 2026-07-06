def countVowels():
    
    vowels = ['a','e','i','o','u']
    count = 0
    
    str1 = input('ENter string: ')
    
    for i in str1:
        if i.lower() in vowels:
            count += 1
            
    return count


result = countVowels()
print('Count of vowels:',result)