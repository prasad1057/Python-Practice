# ✅ Hour 6: Python String Manipulation
# Strings are sequences of characters, like words, sentences, or even numbers in quotes.

text="C++ is awesome"
print(text)
# Strings are always inside quotes: " " or ' '

# 🔹 Step 2: Accessing Characters
text1='Python'
# print(text1[0])     #P
# print(text1[-1])    #n (last character)

# Indexing starts at 0
# Negative indexes go from the end

# text="Programming"
# print(text[0:5])   # Progr
# print(text[3:])    # gramming
# print(text[:6])    # Progra

# Syntax: string[start:end] → end is exclusive

# 🔹 Step 4: Common String Methods

# text = "hello world"
# print(text.upper())     # HELLO WORLD
# print(text.lower())     # hello world
# print(text.title())     # Hello World
# print(text.capitalize()) # Hello world
# print(text.replace("world", "Python"))  # hello Python

# 🔹 Step 5: Searching & Checking
# text = "I love Python"
# print("love" in text)       # True
# print(text.find("Python"))  # 7 (index)
# print(text.startswith("I")) # True
# print(text.endswith("n"))   # True

# 🔹 Step 6: Removing Spaces
text='  hello  '
# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())

# 🔹 Step 7: Splitting and Joining
sentence = "Python is fun"
# words = sentence.split()       # ['Python', 'is', 'fun']
# print(words)
# joined = "-".join(words)       # Python-is-fun
# print(joined)

# 🔹 Step 8: String Formatting
# name='Pranav'
# age=20
# print(f"My name is {name} and I am {age} years old.")

# 🔹 Step 9: Looping Through a String
# for char in "Python":
#     print(char, end='')

# 🔹 Step 10: Useful Functions
# len("Python")          # 6
# "o" in "Python"        # True
# "Python".count("o")    # 1

# ✅ Summary Table
# | Function / Method | Example                   | Output            |
# | ----------------- | ------------------------- | ----------------- |
# | `len()`           | `len("hello")`            | `5`               |
# | `upper()`         | `"abc".upper()`           | `ABC`             |
# | `lower()`         | `"ABC".lower()`           | `abc`             |
# | `find()`          | `"hello".find("l")`       | `2`               |
# | `replace()`       | `"a b".replace("a", "c")` | `c b`             |
# | `split()`         | `"a b c".split()`         | `['a', 'b', 'c']` |
# | `join()`          | `' '.join(['a', 'b'])`    | `"a b"`           |
# | `strip()`         | `"  hi  ".strip()`        | `"hi"`            |


# 🧠 Practice Set: String Manipulation (Hour 6)

# 🔹 Part 1: Indexing & Slicing
# 🧪 Q1. Given the string:

text = "Programming"
# Print:
# First character
# Last character
# Characters from index 3 to 7

# print(text[0])
# print(text[-1])
# print(text[3:7])

# 🧪 Q2. Given:
# word = "Python"
# Print the word in reverse using slicing.
# print(word[::-1])

# 🧪 Q3. Ask the user to input a word and print:
# First three letters
# Last two letters

# word=input("Enter word:")
# print(word[:3])
# print(word[-2:])

# 🔸 Part 2: String Methods
# 🧪 Q4. Convert the following to uppercase:
# sentence = "python is fun"
# print(sentence.upper())

# 🧪 Q5. Replace "fun" with "awesome" in the above sentence.
# change=sentence.replace('fun','awesome')
# print(change)

# 🧪 Q6. Count how many times the letter "o" appears in:
# text = "hello world, good morning"
# print(text.count('o'))
# 5

# 🧪 Q7. Check if the string "Python is cool":
# Starts with "Python"
# Ends with "cool"

# sentence="Python is cool"
# print(sentence.startswith('Python'))
# print(sentence.endswith('cool'))

# 🟣 Part 3: Trimming and Formatting
# 🧪 Q8. Remove leading and trailing spaces from:
# msg = "   welcome to python   "
# print(msg.strip())

# 🧪 Q9. Ask the user to enter their name and age, then print:
# Hello, <name>. You are <age> years old.
# (using f-string formatting)

# name='Pranav'
# age=20
# print(f"My name is {name} and I am {age} years old.")

# 🧪 Q10. Ask the user to input a sentence and print each word on a new line using split().

# sentence=input("Enter sentence : ")
# word=sentence.split()
# for i in word:
#     print(i)

# 🟢 Bonus Challenges
# 🧪 Q11. Write a function count_vowels(text) that returns the number of vowels in a string.

# def count_vowels(text):
#     count=0
#     vowels='aeiou'
#     for i in text:
#         if i in vowels:
#             count += 1
#     return count

# print(count_vowels("Pranav"))

# 🧪 Q12. Ask the user to enter a word and check whether it is a palindrome (reads same forward & backward).
# Examples: madam, level, noon

# word=input("Enter to check palindrome: ")
# if word == word[::-1]:
#     print("Palindrome")
# else:
#     print("Not palindrome")












