# 🟨 Python Modules and Libraries

# 🔷 What is a Module?
# A module is just a file with Python code (.py) that you can import and reuse.

import math 
print(math.sqrt(2))

# 🔷 What is a Library?
# A library is a collection of modules. For example:

# math → built-in library
# random → built-in library
# datetime → built-in library

# pandas, numpy, matplotlib → external libraries (you install them)


# 🔹 Step 1: Importing Modules
# Import full module:

import math
print(math.pi)

# Import specific function:
from math import sqrt,pi
print(sqrt(25))

# Rename during import:
import math as m
print(m.sqrt(100))


# 🔹 Step 2: Built-in Python Modules
# ✅ math - mathemtical fucntions

import math
print(math.ceil(5.2))   # 6
print(math.floor(5.9))  # 5
print(math.factorial(5))    # 120

# ✅ random - generate random values
import random
print(random.randint(1,10))     # Gives us random integer between 1 - 10
print(random.choice(['apple','banana','mango'])) ## Gives us random value

# ✅ datetime - work with dates and time
from datetime import datetime
now = datetime.now()
print('Current time: ',now)


# 🔹 Step 3: Create your own module
# File: mymath.py

import Pracrice.mymath as mymath
print(mymath.add(2,3))

# 5

# 🔹 Step 4: Installing External Libraries
# To use third-party libraries like pandas or numpy:

# 🔹 Step 4: Installing External Libraries
# To use third-party libraries like pandas or numpy:

# pip install pandas
# pip install numpy
# Then use:

# import pandas as pd
# import numpy as np


# 🔹 Step 5: Useful External Libraries (Preview)
# | Library      | Purpose                |
# | ------------ | ---------------------- |
# | `pandas`     | Data analysis          |
# | `numpy`      | Numerical computation  |
# | `matplotlib` | Data visualization     |
# | `requests`   | Work with web APIs     |
# | `flask`      | Build web applications |

# import random

# def roll_dice():
#     return random.randint(1, 6)

# print("🎲 You rolled:", roll_dice())


# 📌 Summary Table

# | Task                     | Code                          |
# | ------------------------ | ----------------------------- |
# | Import module            | `import math`                 |
# | Import specific function | `from math import sqrt`       |
# | Rename module            | `import math as m`            |
# | Create your module       | Write functions in `.py` file |
# | Use external libraries   | `pip install` then `import`   |



























