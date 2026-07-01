def leap_year3(year):
        
    return ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

year = int(input('Enter the year: '))

if leap_year3(year):
    print(f'{year} is leap year.')
else:
    print(f'{year} is not leap year.')
    