'''
# 🟨 Step 1: for Loop with range()

for i in range(5):
    print("prasad",i)
# 🧠 range(5) means → 0, 1, 2, 3, 4 (5 numbers, starting from 0)

# 🔸 Custom Range Examples:
for i in range(1,6):    # from 1 to 5
    print(i, end='')    # 12345

for i in range(2,20,3):     # From 2 to 10, step 3
    print(i, end=' ')       # 5 8 11 14 17 
    


# 🟨 Step 2: while Loop

i = 1
while i >=5:
    print(i)
    i =+ 1
# 🧠 while keeps repeating as long as the condition is True.


# 🟨 Step 3: break and continue

# break stop the loop completely
for i in range(10):
    if i==5:
        break
    print(i)

# continue : skip current iteration
for i in range(5):
    if i==2:
        continue
    print(i)
# 0
# 1
# 3
# 4


# 🟩 Step 4: Looping Over Strings and Lists

# Looping over each character in a string
for it in "Python":
    print(it)
    
# Looping over list
fruits = ["apple","banana","cherry"]
for fruit in fruits:
    for fru in fruit:
        print(fru)

    
# 🟦 Step 5: Nested Loops (Loop inside loop)

# for i in range(1,6):        # i chi value
#     for j in range(1,3):    # j chi value
#         print(i, "*", j, "=", i*j)
        
num1 = int(input("ENter number : "))
for i in range(1,11):
    print(num1, "x", i, "=", num1*i)

'''

# ---------------------------------------------------------
# 🧠 Q1. Print Numbers 1 to 10
# for i in range(1,11):
#     print(i)
    

# 🧠 Q2. Sum of First 10 Numbers
# sum = 0 
# for i in range(1,11):
#     sum = sum + i
# print(sum)


# 🧠 Q3. Multiplication Table of a Number
# Task:
# Ask the user to input a number and print its multiplication table up to 10 using a for loop.

# num=int(input("Enter a number: "))
# for i in range(1,11):
#     print(num,"x",i,"=",num*i)


# 🧠 Q4. Countdown Using While Loop
# num1 = 10
# while (num1 >= 1):
#     print(num1)
#     num1 = num1 - 1
    

# 🧠 Q5. Print Only Even Numbers (1–20)
# for i in range(2,21,2):
#     print(i)


# 🧠 Q6. Skip Multiples of 3
# for i in range(1,21):
#     if i % 3 == 0:
#         continue
#     print(i)
    
    
# 🧠 Q7. Break Loop When Number = 13
# for i in range(1,21):
#     if i == 13:
#         break
#     print(i)


# # 🧠 Q8. Calculate Factorial
# ans = 1
# num = int(input("Enter num: "))
# for i in range(1,num+1):
#     ans = ans * i
#     i = i + 1
# print(ans)


# 🧠 Q9. Sum of Digits
# Task:
# Ask the user for a number. Use a while loop to calculate the sum of its digits.

# number=int(input("Enter number : "))
# total=0

# while number>0:
#     digit=number%10
#     total+=digit
#     number//=10
    
    
# 🧠 Q10. Reverse a String
# Task:
# Ask the user for a word and print the reverse using a loop.

# rev_str=''
# string=input("Ener string : ")
# for i in string:
#     rev_str=i+rev_str
# print(rev_str)

# string=input("Ener string : ")
# rev_string=string[::-1]
# print(rev_string)

# string=input("Ener string : ")
# rev_string=''.join(reversed(string))
# print(rev_string)


# string=input("Ener string : ")
# list1=[]
# rev_string=''
# for ch in string:
#     list1.append(ch)
    
# while list1:
#     ch=list1.pop()
#     rev_string+=ch
# print(rev_string)

#Hi this is wonderful day!
#day! wonderful is this Hi

#  better luck next time 



