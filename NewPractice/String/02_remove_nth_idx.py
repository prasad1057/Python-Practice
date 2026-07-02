def removeChar(string,n):
    new_string = string[:n] + string[n+1:]
    return new_string
    
# input
s = input('Enter a string: ')
n = int(input('Enter index to remove: '))

# output
res = removeChar(s,n)
print("String after removeing chracter: ",res)