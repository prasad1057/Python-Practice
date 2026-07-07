def missingNumber():

    n = int(input("Enter n: "))

    list1 = []

    for i in range(n - 1):
        list1.append(int(input("Enter number: ")))

    for i in range(1, n + 1):
        if i not in list1:
            print("Missing Number:", i)
            break

missingNumber()