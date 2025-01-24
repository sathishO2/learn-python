'''
Error Handling
'''

# Understanding exceptions:  
'''
9. Write a Python program that attempts to open a non-existent file named "nofile.txt" and handles the resulting exception by printing "File not found."
'''
def q9():
    try:
        with open("nofile.txt") as f:
            print(f)
    except FileNotFoundError as e:
        print("File not found.")

'''
10. Write a Python program that attempts to divide two numbers provided by the user and handles division by zero using try, except, and finally blocks. The finally block should print "Execution complete."
'''
def q10():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))

    try:
        print(x//y)
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("Execution complete.")

'''
Raising exceptions:

11. Write a Python function that takes an integer as an argument and raises a ValueError if the integer is negative, with the message "Negative value not allowed."
'''

def q11():
    n = int(input("Enter num: "))
    if n<0:
        raise ValueError("Negative value not allowed.")
    



# q9()
# q10()
q11()



