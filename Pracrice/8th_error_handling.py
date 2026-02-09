# 🟨 Error Handling in Python using try, except

# 🔷 Why Do We Need Error Handling?
# Without it, any unexpected issue (like dividing by zero or missing files) will crash your program.

# ✅ Good code doesn’t avoid errors – it handles them gracefully.

# 🔹 Step 1: Basic try / except block
try:
    x = 10 / 0
except:
    print('Something went wrong')
# This prevents the crash, and shows a custom message instead.


#  🔹 Catch specific errors
try:
    x = 10 / 0
except ZeroDivisionError:
    print('You cant divide by zero to any number')

# You can be more precise in handling known issues.

# # 🔹 Step 3 : Handle Multiple Error Types:
# try:
#     num = int(input('Error number: '))
#     result = 10 / num
#     print(int(result))
# except ValueError:
#     print('Input must be number')
# except ZeroDivisionError:
#     print('Cant divide by zero')
    

# # 🔹 Step 4: Using else and finally
# try:
#     num = int(input('Enter a number : '))
#     result = 100 / num
#     #print(int(result))
# except ZeroDivisionError:
#     print('Zero error !')
# except ValueError:
#     print('Invalid Input')
# else:
#     print('Success ! Result is : ', result)
# finally:
#     print('This block always run')
    
# | Block     | Purpose                        |
# | --------- | ------------------------------ |
# | `try`     | Code that might cause an error |
# | `except`  | Code that runs if error occurs |
# | `else`    | Runs if no error occurs        |
# | `finally` | Always runs, error or not      |


# 🔹 Step 5: Raising your own Errors
# age = int(input('Enter age: '))
# if age < 0:
#     raise ValueError('Age cant be negative')


# ✅ Real Example: Safe Division

def safe_divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return ('Divide by zero is not allowed')

print(safe_divide(12,2))    # 6.0
print(safe_divide(10,0))    # Divide by zero is not allowed


# 🔥 Bonus Example: Handle File Not Found

try:
    with open('users.txt','r') as files:
        data = files.readlines()
        print(data)
except FileNotFoundError:
    print('File not found')
    

# ✅ 1. try + except
# Handles any error (general catch-all):
try:
    result = 10 / 0
except:
    print("❌ An error occurred.")

# ✅ 2. except TypeError: (Specific error)
try:
    x = 'hello' + 5
    print(x)
except TypeError:
    print("❌ Cant add string and integer.")
    

# ✅ 3. else: (Runs if try block has no error)
try:
    num = int(input('Enter number: '))
except ValueError:
    print('❌ Thats not a number')
else:
    print("✅ You entered:", num)


# ✅ 4. finally: (Always runs, even if error occurs)
try:
    f = open('users.txt','r')
    data = f.readlines()
    print(data)
except FileNotFoundError:
    print('❌ File not found.')
finally:
    print('✅ Program ended (finally block runs.)')
    

# ✅ 5. raise (Manually trigger an error)
age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("❌ Age cannot be negative.")
else:
    print("✅ Age accepted.")
