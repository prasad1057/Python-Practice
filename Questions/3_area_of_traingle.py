breadth = float(input('Enter the breadth of traingle: '))
height = float(input('Enter the height of traingle: '))


if breadth <= 0 or height <= 0:
    print("Breadth and height must be positive numbers")
else:
    area_of_traingle = 0.5 * breadth * height
    
    print('Area of a triangle is : ',area_of_traingle)