a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))


# Using a third variable
# temp = a
# a = b
# b = temp
# print('Value of a is:',a, '\nValue of b is:',b)

# -------------------------------------------------

# Without using a third variable (Python way)

# a,b = b,a
# print('Value of a is:',a, '\nValue of b is:',b)

# -------------------------------------------------

# Without third variable (using arithmetic)
a = a + b
b = a - b
a = a - b
print('Value of a is:',a, '\nValue of b is:',b)