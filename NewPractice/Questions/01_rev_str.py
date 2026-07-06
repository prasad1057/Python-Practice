str1 = input('Enter the string: ')

rev = ''

for i in str1:
    rev = i + rev

print('Reverse string:',rev)



# Using Slicing (Most Common)

rev = str1[::-1]
print('Reverse:',rev)