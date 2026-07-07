# Count frequency of words.

def freqWords():
    
    str1 = input('Enter string: ')
    words = str1.split()
    result = {}
      
    
    for w in words:
        if w in result:
            result[w] += 1
        else:
            result[w] = 1
            
    
        
    return result

print(freqWords())