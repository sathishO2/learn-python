def program1():
    '''
    Declare variables for the dimensions of a box (length, width, height). Calculate and print the volume and the surface area of the box.
    "Volume: V=length×width×height
    SA=2×(length×width+length×height+width×height)"	
    "
    length = 5
    width = 3
    height = 4"	
    "
    Volume: 60
    Surface Area: 94"'''

    l = int(input("length: "))
    w = int(input("Width: "))
    h = int(input("Height: "))

    print(f"Valume: {l*w*h}")
    print(f"Surface Area: {2*((l*w) + (l*h) + (w*h))}")

def program2():
    '''
    Create variables for the real and imaginary parts of two complex numbers. Calculate and print the sum and product of these two complex numbers.	"Sum: (a+bi)+(c+di)=(a+c)+(b+d)i
    Product:(a+bi)×(c+di)=(ac−bd)+(ad+bc)i"	"real1 = 2
    imag1 = 3
    real2 = 1
    imag2 = 4"	"Sum: (3 + 7i)
    Product: (-10 + 11i)"
    '''

    r1 = 2
    i1 = 3
    r2 = 1
    i2 = 4

    c1 = complex(r1,i1)
    c2 = complex(r2,i2)
    print(f"Sum: {c1+c2}")
    print(f"Product: {c1*c2}")


def program3():
    '''
    Declare a variable for a person's name, age, height in meters, and whether they are a student. Print a formatted string that includes all these details.		
    "name = ""John Doe""
    age = 30
    height = 1.75
    is_student = False"	Name: John Doe, Age: 30, Height: 1.75 meters, Student: False
    '''

    name = "John Doe"
    age = 30
    height = 1.75
    is_student = False

    print(f"Name: {name}, Age: {age}, Height: {height} meters, Student: {is_student}")

def program4():
    '''
    Declare variables for a car's make, model, year, and current mileage. Calculate the car's age and print whether it is considered a classic car (over 20 years old).		
    "make = ""Toyota""
    model = ""Corolla""
    year = 2000
    mileage = 150000
    current_year = 2024"	
    Car: Toyota Corolla, Age: 24 years, Classic: True
    '''
    make = "Toyota"
    model = "Corolla"
    year = 2000
    mileage = 150000
    current_year = 2024

    age = current_year-year

    print(f"Car: {make}, Age: {age} years, Classic: {True if age > 20 else False}")

def program5():
    '''
    Write a program that converts a temperature from Fahrenheit to Celsius and Kelvin.

    "Celsius C= 5/9 ×(F−32)
    Kelvin K=C+273.15
    "
    fahrenheit = 98.6
    	
    "Celsius: 37.0
    Kelvin: 310.15"
    '''

    fahrenheit = 98.6

    cel = 5/9 * (fahrenheit-32)
    kel = cel + 273.15
    print(f"Celsius: {cel} \n Kelvin: {kel}")

def program6():
    '''
    Write a program to compare the areas of two rectangles given their lengths and widths. Print which rectangle has a larger area or if they are equal		
    "length1 = 5
    width1 = 3
    length2 = 4
    width2 = 4"	
    "Rectangle 1 Area: 15
    Rectangle 2 Area: 16
    Larger Rectangle: Rectangle 2"
    '''

    l1 = 5
    w1 = 3
    l2 = 4
    w2 = 4

    a1 = l1*w1
    a2 = l2*w2 

    print(f"Rectangle 1 Area: {a1}\nRectangle 2 Area: {a2}\nLarger Rectangle: {'Rectangle 2' if a2>a1 else 'Rectangle 1'} ")

def program7():
    '''
    Write a program that takes the grades of three subjects and checks if the average grade is a passing grade (>= 60).		
    "grade1 = 70
    grade2 = 65
    grade3 = 55"	
    "Average Grade: 63.33
    Passing: True"
    '''

    grade1 = 70
    grade2 = 65
    grade3 = 55
    avg = (grade1+grade2+grade3)/3
    print(f"Average Grade: {avg:.2f}\n Passing: {True if avg >=60 else False}")

def program8():
    '''
    Write a program that takes three boolean variables representing if a person has completed certain tasks. Print if the person is eligible for a reward, which is given if they have completed at least two tasks.		
    "task1 = True
    task2 = False
    task3 = True"	
    Eligible for Reward: True
    '''
    t1 = True
    t2 = False
    t3 = True
    print(f"Eligible for Reward: {True if (t1 and t2) or (t1 and t3) or (t2 and t3) else False}")
def program9():
    '''
    Write a function that determines whether a given string is a palindrome (reads the same forwards and backwards).		"racecar"	TRUE
    '''
    s = "racecar"
    print(True if s==s[::-1] else False)

def program10():
    '''
    Implement matrix multiplication for two given matrices.		
    "A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]"	
    Result = [[19, 22], [43, 50]]
    '''

    a = [[1, 2], 
         [3, 4]]
    b = [[5, 6], 
         [7, 8]]
    
    r = [[0,0],[0,0]]
    rr = list()
    # print(r)
    for i in range(len(a)):
        t = []
        for j in range(len(b[0])):
            s = 0
            for k in range(len(b)):
                # r[i][j]+= a[i][k]*b[k][j]
                s+=a[i][k]*b[k][j]
            t.append(s)
        # print(t)
        rr.append(t)

    print(r)

def program11():
    '''
    Write a program that generates a multiplication table for numbers from 1 to N.		
    N=5	
    "1  2  3  4  5
    2  4  6  8 10
    3  6  9 12 15
    4  8 12 16 20
    5 10 15 20 25"
    '''
    n = 5
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i*j,end=" ")
        print()

def program12():
    '''
    Create a program that prints numbers from 1 to N, but for multiples of 3, print “Fizz,” for multiples of 5, print “Buzz,” and for multiples of both 3 and 5, print “FizzBuzz.”	
    N=15	
    1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz
    '''

    n = 15
    for i in range(1,n+1):
        if(i%3==0 and i%5==0):
            print("FizzBuzz",end=" ")
        elif(i%3==0):
            print("Fizz",end=" ")
        elif(i%5==0):
            print("Buzz",end=" ")
        else:
            print(i,end=" ")

def program13():
    '''
    "Write a program that takes a numerical score as input and assigns a letter grade based on the following criteria:
    Score >= 90: Grade is ‘A’
    80 <= Score < 90: Grade is ‘B’
    70 <= Score < 80: Grade is ‘C’
    Score < 70: Grade is ‘F’"	
    
    score = 85	
    Grade: B
    '''

    s = int(input())
    g = 'A'
    if(s>=90):
        g = 'A'
    elif(80 <= s < 90):
        g = 'B'
    elif(70 <= s < 80):
        g = 'C'
    elif(s < 70):
        g = 'F'
    print("Grade "+ g)

def program14():
    '''
    Generate the first k prime numbers.		
    k = 7	
    2, 3, 5, 7, 11, 13, 17
    '''
    k = int(input())
    i = 2
    while k>0:
        for j in range(2,i//2+1):
            if(i%j==0):
                break 
        else:
            k-=1
            print(i,end=",")
        i+=1

def program15():
    '''
    Calculate the sum of the first N natural numbers.	
    N = 5	
    Sum: 15
    '''
    n = int(input())
    print(f"Sum: {(n*(n+1))//2}")

def program16():
    '''
    Generate the first k terms of the Fibonacci series.	
    k = 8	
    0, 1, 1, 2, 3, 5, 8, 13
    '''
    n = int(input())
    i = 0
    j = 1
    k = 0
    print(f"{i}, {j}, ",end="")
    n-=2
    while(n>0):
        k = i+j 
        i = j 
        j = k
        print(k,end=", ")
        n-=1

# program1()
# program2()
# program3()
# program4()
# program5()
# program6()
# program7()
# program8()
# program9()
# program10()
# program11()
# program12()
# program13()
# program14()
# program15()
# program16()

