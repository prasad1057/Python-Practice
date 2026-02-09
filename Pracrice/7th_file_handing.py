# 🟨 File Handling in Python

# 🔷 Why Learn File Handling?
# Files help your program store data permanently (unlike variables which are temporary in memory).


# file = open("example.txt", 'w')
# file.write("Hello this is a sample file")
# file.close()

# | Mode   | Description             |
# | ------ | ----------------------- |
# | `"r"`  | Read only               |
# | `"w"`  | Write (overwrites file) |
# | `"a"`  | Append to file          |
# | `"r+"` | Read and write          |

# 🔷 Step 1 : Opening a file
# file=open("example.txt","r")


# 🔹 Step 2: Reading a File
# 🔸 Read entire content:

# file=open("example.txt","r")
# content=file.read()
# print(content)
# file.close()

# 🔸 Read line-by-line:
# file1 = open("example.txt","r")
# for line in file1:
#     print(line.strip())
# file1.close() 


# 🔹 Step 3: Writing to a File
# 🔸 Overwrite with "w":
# file2 = open("newfile.txt","w")
# file2.write("Hello my name is prasad \n")
# file2.write("Second line")
# file2.close()


# 🔸 Append with a
# file = open('newfile.txt','a')
# file.write("\n This line is appended")
# file.close()


# 🔹 Step 4: Using with Statement (Best Practice ✅)
# Automatically closes the file, even if errors occur.

with open('newfile.txt','r') as file:
    data = file.read()
    print(data)
    
# No need to write file.close() — Python does it for you.


# 🔹 Step 5 : Writing a List of strings

lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
with open('listdata.txt', 'w') as file:
    file.writelines(lines)
    
# 🔹 Step 6 : Reading Lines of Strings
with open('listdata.txt','r') as file:
    lines = file.readlines()
    print(lines)        # ['Line 1\n', 'Line 2\n', 'Line 3\n']
    
    

# 💡 Bonus: Check if File Exists
import os

if os.path.exists('example.txt'):
    print('File Exist')
else:
    print('File not found')
    

# ✅ Real-World Example: Count Words in a File
with open('example.txt', 'r') as file:
    content = file.read()
    words = content.split()
    print("Total words : ",len(words))
    

# Q.1 Task: User Data Save Program
# name = input("Enter name: ")
# skill = input("Enter skill: ")

# with open("users.txt", "a") as file:
#     file.write(name + " - " + skill + "\n")

# print("Data saved successfully")

with open('users.txt','r') as file:
    lines = file.readlines()
    print(lines)
    

# Q.2 Count how many lines are in a file.
count = 0
with open('users.txt','r') as file :
    for line in file:
        count = count + 1
    
print("Total lines:", count)


# Q.3 Read numbers from file and calculate sum - File contains numbers, one per line.
# total = 0

# with open("users.txt", "r") as file:
#     for line in file:
#         total += int(line)

# print("Sum:", total)


# Q.4 Handle file not found error - Avoid crash if file does not exist.
try:
    with open('users.txt','r') as file:
        print(file.read())
except FileNotFoundError:
    print('File not found')
    

# Q.5 Write list data to file - Save list items into file.
skills = ["Python", "SQL", "PowerBI"]

with open("skills.txt", "w") as file:
    for skill in skills:
        print(skill.strip())


# Copy content from one file to another
with open('users.txt','r') as source:
    content = source.read()
    
with open('newuser.txt','w') as target:
    target.write(content)
    

# | Function/Method          | Purpose                      |
# | ------------------------ | ---------------------------- |
# | `open("file.txt", "r")`  | Open for reading             |
# | `read()`                 | Read full content            |
# | `readlines()`            | Read content into list       |
# | `write("text")`          | Write (overwrite)            |
# | `writelines([...])`      | Write list of lines          |
# | `with open(...)`         | Safe and clean file handling |
# | `os.path.exists("file")` | Check if file exists         |

