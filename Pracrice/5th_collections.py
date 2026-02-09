# 🟨 Collections in Python
# Learn: List, Tuple, Set, and Dictionary in a well-explained way with examples.

# 🔷 1. Lists – Ordered, Mutable, Duplicates Allowed
# 🔸 What is a List?
# A list is like a basket that can hold multiple items in a specific order, and you can change (update, remove, add) those items.

my_list = [10,20,30,40,50]
print(my_list)
print(type(my_list))

# 🔸 Properties:
# ✅ Ordered (items maintain the order you added them)
# ✅ Mutable (you can change items)
# ❌ Allows Duplicates

# 🔸 Accessing List Items:
fruits = ['Apple', 'Banana', 'Cheery']
print(fruits[1])        # output = Banana

# 🔸 Modifying Lists :
fruits[1] = "Mango"
print(fruits)

# 🔸 List Operations :
fruits.append("Guava")
fruits.insert(1,"Orange")
fruits.remove('Apple')
print(fruits)
print(len(fruits))

# 🔸 Looping Through a list :
for fruit in fruits:
    print(fruit)
    
# for fruit in fruits:
#     for fru in fruit:
#         print(fru)
        
        
# 🔷 2. Tuples – Ordered, Immutable, Duplicates Allowed
# 🔸 What is a Tuple?
# A tuple is like a read-only list . you can store items in order , but once stored , you cannot modify them.

# 🔸 Syntax:
dimensions = (1920, 1080)
# 🔸 Properties:
# ✅ Ordered
# ❌ Immutable (can't change after creation)
# ❌ Allows Duplicates

# 🔸 Accessng Tuple Items:
print(dimensions[0])        # outut = 1920

# 🔸 Why use Tuples?
# Protect data from being changed accidentally
# Faster than lists
# Used in fixed values (like coordinates, months, etc.)



# 🔷 3. Sets – Unordered, Mutable, No Duplicates
# 🔸 What is a Set?
# A set is like a bag that holds items without order and without duplicates.

# 🔸 Syntax:
colors = {"red", "blue", "green"}
print(colors)
print(type(colors))
# print(colors[1])          # gives error

# 🔸 Properties:
# ❌ Unordered (no index, can't access by position)
# ✅ Mutable (can add or remove items)
# ✅ Unique only (removes duplicates automatically)


# 🔸 Examples:
nums = {1,2,3,4,5}
print(nums)

nums.add(6)
nums.remove(2)
print(3 in nums)
print(nums)

# 🔸 Use Case:
# Removing duplicates
# Fast membership tests (checking if item exists)


# 🔷 4. Dictionaries – Key-Value Pairs, Mutable, Ordered
# 🔸 What is a Dictionary?
# A dictionary is like a real dictionary: each word (key) has a meaning (value).

persons = {
    'name' : 'Prasad',
    'age' : 21,
    'city' : 'Alibag'
}

# 🔸 Properties:
# ✅ Key-value pairs
# ✅ Mutable
# ✅ Ordered (from Python 3.7+)
# ✅ Keys must be unique

# 🔸 Accessing Values:
print(persons['name'])

# 🔸 Adding or Updating:
persons['age'] = 22             # update
persons['college'] = 'SCOE'     # add
print(persons)

# 🔸 Deleting:
del persons['city']

# 🔸 Looping :
for key,value in persons.items():
    print(key, ':', value)



# 🔷 Part 1: Lists
# 🧪 Q1. Create a list of your 5 favorite fruits and print the second one.
list1 = ['apple','banana','cherry','mango','orange']
print(list1)
print(list1[1])

# # 🧪 Q2. Add "pineapple" to the end of the list.
list1.append('pineapple')
print(list1)

# # 🧪 Q3. Replace the third item in the list with "kiwi".
list1[2] = 'kiwi'
print(list1)

# # 🧪 Q4. Print the number of fruits in the list.
print(len(list1))

# # 🧪 Q5. Use a loop to print each fruit in the list, one per line.
for fruit in list1:
    print(fruit)
    


# 🔶 Part 2: Tuples
# 🧪 Q6. Create a tuple with 3 values: height, width, depth.
tuple1=(10,20,30)


# 🧪 Q7. Print the second item in the tuple.
print(tuple1[1])

# 🧪 Q8. Try to change the first value in the tuple (what error do you get?).
#tuple1[2] = 40

    # tuple1[2] = 40
    # ~~~~~~^^^
    # TypeError: 'tuple' object does not support item assignment
    

# 🧪 Q9. Convert the tuple to a list, change a value, then convert it back to a tuple.
# # Convert tuple to list
list1 = list(list1)

# # Change a value (e.g., change 20 to 99)
list1[1] = 99

# # Convert back to tuple
tuple1 = tuple(list1)

# # Print the updated tuple
print(tuple1)



# 🟣 Part 3: Sets
# 🧪 Q10. Create a set with values: 2, 3, 5, 7, 5, 2
# Print the set. What happens to duplicates?

set1={2,3,5,7,5,2}
print(set1)

# 🧪 Q11. Add 11 to the set and remove 3.
# set1.add(11)
# print(set1)

# set1.remove(3)
# print(set1)

# 🧪 Q12. Check if 7 exists in the set and print the result.

# print(7 in set1)

# 🧪 Q13. Use a loop to print each item in the set.
# for i in set1:
#     print(i)

# 🟢 Part 4: Dictionaries
# 🧪 Q14. Create a dictionary for a student with keys: name, age, branch

dictionary1={
    'name':'Prasad',
    'age': 20,
    'branch':'IT'
}

# 🧪 Q15. Add a new key "college" with value "IIT Bombay".
# dictionary1['college']='SCOE'
# print(dictionary1)

# 🧪 Q16. Change the value of "age" to 22.
# dictionary1['age']=22
# print(dictionary1)

# 🧪 Q17. Print all keys and values using a loop.
# for key,value in dictionary1.items():
#     print(key , ":", value)

# 🧪 Q18. Delete the "branch" key from the dictionary.
del dictionary1['branch']
print(dictionary1)

# 🏁 Bonus Challenge
# 🧪 Q19. Make a list of 3 dictionaries, each representing a student with keys: name and marks.
# Loop through the list and print each student’s name and marks.

# 🧠 List of student dictionaries
students = [
    {"name": "Pranav", "marks": 99},
    {"name": "Nik", "marks": 99},
    {"name": "Prasad", "marks": 99}
]

# Loop through the list and print each student's name and marks
for student in students:
    print(f"Name: {student['name']}, Marks: {student['marks']}")


