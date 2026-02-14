# A year is a leap year if:

# It is divisible by 400

# OR

# It is divisible by 4 AND NOT divisible by 100


year = int(input('Enter the year: '))

if (year % 400 == 0 ) or (year % 4 == 0 and year % 100 != 0):
    print('leap year')
else:
    print('Not leap year')