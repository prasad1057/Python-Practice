# 2. Python Program to Concatenate Two Dictionaries Into One

'''
We cannot directly concatenate two dictionaries using the + operator.
Here, we copy each key-value pair into a third dictionary.
'''

def userDict():

    dict1 = {}
    dict1_num = int(input("Enter number of key-value pairs for dict1: "))

    for i in range(dict1_num):
        key = input("Enter key: ")
        value = input("Enter value: ")

        dict1[key] = value

    dict2 = {}
    dict2_num = int(input("Enter number of key-value pairs for dict2: "))

    for i in range(dict2_num):
        key = input("Enter key: ")
        value = input("Enter value: ")

        dict2[key] = value

    add_dict = {}

    # Add items from first dictionary
    for i in dict1:
        add_dict[i] = dict1[i]

    # Add items from second dictionary
    for j in dict2:
        add_dict[j] = dict2[j]

    return add_dict


result = userDict()
print("Concatenated Dictionary:", result)