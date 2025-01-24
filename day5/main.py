'''
Introduction to OOP: Understanding Classes and Objects

Question 1: Implement a Class with Special Methods
Write a Python program to create a class named Person. Implement the constructor (__init__) to set attributes like name and age, and the destructor (__del__) to print a message when an object is deleted. Add methods to set and get attribute values using setattr and getattr. Also, include error handling to manage attempts to get non-existent attributes.
'''

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __del__(self):
        print("Object is deleted.")
    
    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\n"
    
    def setter(self, attr_name, value):
        setattr(self, attr_name, value)
        print(f"Set {attr_name} to {value}")

    def getter(self, attr_name):
        try:
            value = getattr(self, attr_name)
            print(f"{attr_name} is {value}")
            return value
        except AttributeError:
            print(f"{attr_name} does not exist")
            return None

def q1():
    p1 = Person("King",33)
    # print(p1)
    print(p1.getter("name"))
    p1.setter("name","sash")
    print(p1.getter("name"))
    # del p1

'''
OOP Concepts: Inheritance, Polymorphism, Encapsulation, Data Abstraction

Question 2: Inheritance with Constructor Overriding
Write a Python program where you define a class named Book with a constructor that initializes the title and author. Then, create a subclass named Ebook that extends Book, adds a new attribute filesize, and overrides the constructor to include this new attribute. Demonstrate creating instances of both classes and accessing their attributes.
'''

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\n"

class Ebook(Book):
    def __init__(self, title, author,filesize):
        super().__init__(title, author)
        self.filesize = filesize
    
    def __str__(self):
        return super().__str__()+f"Filesize: {self.filesize}\n"

'''
Question 3: Polymorphism with Class Methods
Write a Python program to demonstrate polymorphism in a class hierarchy. Create an abstract base class Polygon with a method calculate_area(). Define two subclasses, Triangle and Rectangle, that override calculate_area() to calculate and return their respective areas based on base and height for the triangle, and length and width for the rectangle.
'''

from abc import ABC,abstractmethod

class Polygon(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Triangle(Polygon):
    def calculate_area(self,base,height):
        return 1/2*(base*height)

class Rectangle(Polygon):
    def calculate_area(self,length,width):
        return length*width
    

'''
Question 5: Dynamic Attribute Management in Classes

Write a Python program to create a class named Inventory. In this class, implement dynamic attribute management using setattr, getattr, hasattr, and delattr. Specifically, create a method to add items dynamically, check for an item's existence, retrieve item details, and delete items from the inventory. Demonstrate these capabilities in a test block by creating an instance of Inventory and manipulating its attributes.
'''

class Inventory:
    def add_item(self, item, qunt):
        setattr(self, item, qunt)
        
    def get_item(self, item):
        if hasattr(self, item):
            qunt = getattr(self, item)
            return qunt
        else:
            return "Not available"
    
    def check_item(self, item):
        return hasattr(self,item)

    def delete_item(self, item):
        if hasattr(self, item):
            delattr(self, item)
        else:
            return "Not available"
        
        
'''
Question 6: Encapsulation and Data Abstraction with Property Decorators

Write a Python program where you define a class called Temperature. Use property decorators to encapsulate the temperature in Celsius. The class should have a method to convert the temperature to Fahrenheit. Ensure that the temperature cannot be set to less than -273.15 degrees Celsius (absolute zero) by raising an exception if an attempt is made to set an invalid temperature.
'''

class Temperature:

    def __init__(self,temp=0):
        self._temp = temp

    @property
    def temp(self):
        print("Getting the Temperature")
        return f"{self._temp} C"
    
    @temp.setter
    def temp(self,val):
        
        if val < -273.15:
            raise ValueError("Invalid Temperature.")
        
        print("Setting the Temperature")
        self._temp = val

    def toFahrenheit(self):
        return f"{(9/5)*(self._temp + 32)} F"



        

def q2():
    b = Book("You Can","abcd")
    eb = Ebook("Can You","dcba",'50kb')

    print(b)
    print(eb)

def q3():
    t = Triangle()
    r = Rectangle()

    ta = t.calculate_area(10,7)
    ra = r.calculate_area(10,7)

    print(ta)
    print(ra)

def q4():
    iv = Inventory()
    iv.add_item("laptop",10)

    iv.get_item("laptop")

    print(iv.check_item("laptop"))

    iv.delete_item("laptop")

    iv.delete_item("pen")

def q5():
    t = Temperature()
    # t.temp = -888
    t.temp = 80
    print(t.temp)
    print(t.toFahrenheit())


# q1()
# q2()
# q3()
# q4()
q5()
