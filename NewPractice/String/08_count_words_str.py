# 9. Python Program to Calculate the Number of Words and the Number of Characters Present in a String



def countWC(str1):
    
    # count words
    words = str1.split()
    word_count = len(words)
    
    # count characters
    char_count = len(str1)
    
    return word_count, char_count


str1 = str(input("Enter the string: "))

w, c = countWC(str1)

print("Number of words:", w)
print("Number of characters:", c)