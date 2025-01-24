'''
File Handling
'''

# Reading from files:

'''
Write a Python program to read the entire content of a text file named "example.txt" and print it to the console.
'''
def q1():
    with open("/home/ib-58/Desktop/learning/day4/FileHandal/example.txt",'r') as f:
        print(f.read())


'''
Write a Python program to read the first 10 lines of a file named "data.txt".
'''

def q2():
    with open('/home/ib-58/Desktop/learning/day4/FileHandal/data.txt','r') as f:
        l = f.readlines()[:10]
        for i in range(10):
            print(i+1,l[i])

    # f = open("data.txt")
    # l = f.readlines()[:10]
    # for i in range(10):
    #     print(i+1,l[i])
    # f.close()
'''
Writing to files:  
'''

'''
3. Write a Python program that writes the string "Hello, World!" to a file named "output.txt".
'''
def q3():
    f = open("output.txt",'x+')
    f.write("Hello, World!")
    f.close()

'''
4. Write a Python program that writes multiple lines of text to a file named "multiline.txt".
'''
def q4():
    f = open("multiline.txt",'w')
    f.writelines("hello\nworld\ni'm here!")
    f.close()

'''
Working with file modes (read, write, append): 
'''

'''
5. Write a Python program to open a file named "log.txt" in append mode and add the line "New log entry" to it.
'''
def q5():
    f = open("log.txt",'a')
    f.write("\nNew log entry")
    f.close()

'''
6. Write a Python program to create a file named "newfile.txt" and write "This is a new file." to it. If the file already exists, it should overwrite the content.
'''
import os
def q6():
    
    if os.path.exists('newfile.txt'):
        f = open('newfile.txt','w')
        f.write('This is a new file.')
        f.close()
    else:
        f = open('newfile.txt','x+')
        f.write('This is a new file.')
        f.close()

'''
File Methods
Using file methods (open, close, read, write, readline, readlines): 
'''

'''
7. Write a Python program to read the content of a file named "info.txt" line by line and print each line using the readline() method. 
'''
def q7():
    f = open('info.txt','r')
    ff = open('info.txt','r')
    l = f.readlines()[-1]
    while True:
        s = ff.readline()
        print(s)
        if s == l:
            break

'''
8. Write a Python program to read all the lines from a file named "list.txt" into a list using the readlines() method and then print the list.
'''
def q8():
    with open('list.txt','r') as f:
        l = f.readlines()
        print(l)

# q1()
# q2()
# q3()
# q4()
# q5()
# q6()
# q7()
q8()