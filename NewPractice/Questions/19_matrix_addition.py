matrix1 = []
matrix2 = []
result = []

print("Enter elements of Matrix 1")

for i in range(2):
    row = []
    for j in range(2):
        ele = int(input(f"Enter element [{i}][{j}]: "))
        row.append(ele)
    matrix1.append(row)

print("Enter elements of Matrix 2")

for i in range(2):
    row = []
    for j in range(2): 
        ele = int(input(f"Enter element [{i}][{j}]: "))
        row.append(ele)
    matrix2.append(row)

for i in range(2):
    row = []
    for j in range(2):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("Result Matrix:")

for row in result:
    print(row)