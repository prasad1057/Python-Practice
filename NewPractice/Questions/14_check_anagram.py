# Check anagram.


def anagramCheck():
    
    str1 = str(input('Enter string1: '))
    str2 = str(input('Enter string2: '))
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    if len(str1) != len(str2):
        print('String is not Anagram')
        
    else:
        dict1 = {}
        dcit2 = {}
        
        # for checking str1
        for i in str1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
                
        # for checking str2
        for j in str2:
            if j in dcit2:
                dcit2[j] += 1
            else:
                dcit2[j] = 1
                
        if dict1 == dcit2:
            print('String Anagram')
        else:
            print('String Not Anagram')
            
anagramCheck()