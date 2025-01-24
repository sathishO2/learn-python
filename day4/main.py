'''
Iterators and Generators
'''

'''
Iterators: 
12. Write a Python class MyRange that mimics the built-in range function using iterators. The class should take start, stop, and step arguments.
'''
class MyRange:
    def __init__(self,start=0,stop=0,step=1):
        self.start = start
        self.stop = stop
        self.step = step 
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < self.stop:
            x = self.start
            self.start += self.step
            return x
        else:
            raise StopIteration

# ran = MyRange(0,10)

for i in MyRange(0,10):
    print(i,end=" ")

print()

'''
Generators:
13. Write a Python generator function Fibonacci that generates an infinite sequence of Fibonacci numbers.
'''

def fibo():
    a,b = 0,1
    while True:
        yield a 
        a,b = b,a+b

fib = fibo()

for i in range(10):
    print(next(fib),end=" ")

print()


'''
Decorators: 
14. Write a Python decorator time_it that measures and prints the time a function takes to execute. Apply this decorator to a function that calculates the factorial of a number.
'''

import time

def time_it(fun):
    def wrapper():
        s = time.time()
        fun()
        e = time.time() - s 
        print("Taken time:",e)
    return wrapper

@time_it
def fun():
    for i in range(10):
        pass
    # pass

fun()

