# Importing Modules and Packages

'''
Write a script that imports the os and sys modules and prints the current working directory and the Python version.
'''
import os
import sys

print("CWD: "+os.getcwd())
print("Python Version:",sys.version)

'''Create a custom module named math_utils with a function that calculates the factorial of a number. Import and use this module in another script.'''

from math_utils import fact
r = fact(5)
print(r)

# Standard Library Modules (os, sys, math, random)

'''
Using the random module, write a function that generates a list of 10 random integers between 1 and 100.
'''

import random
r = [random.randrange(1,100) for i in range(10)]
print(r)


'''
Write a function that uses the math module to calculate the area of a circle given its radius.
'''
import math
r = math.pi * pow(5,2)
print(r)

