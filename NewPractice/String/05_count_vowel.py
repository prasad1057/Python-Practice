# 5. Python Program to Count the Number of Vowels in a String

def countVowel(str1):
    
    vowels = ['a','e','i','o','u']
    
    count = 0
    
    for i in str1:
        if i.lower() in vowels:
            count += 1
            
    return count 


str1 = str(input('Enter the string: '))

result = countVowel(str1)
print('Number of vowels in string:',result)