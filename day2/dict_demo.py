'''
Dictionaries
'''

class prob1:
    '''
    Creating and Accessing Dictionaries
    '''

    def q1(self):
        '''
        Q: Write a program to create a dictionary with keys as student names and values as their grades. Then, write a function to find the student with the highest grade.
        '''
        d = {'a':10,'b':30,'c':20}
        m = sorted(d.items(),key=lambda k:k[1],reverse=True)
        print(m[0])
        
    def q2(self):
        '''
        Q: How can you create a dictionary from two lists keys = ['a', 'b', 'c'] and values = [1, 2, 3]?
        '''
        k = ['a', 'b', 'c']
        v = [1, 2, 3]

        d = {k[i]:v[i] for i in range(len(k))}

        print(d)

class prob2:

    '''
    Dictionary Methods
    '''

    def q1(self):
        '''
        Q: Given the dictionary students = {'Alice': 85, 'Bob': 90, 'Charlie': 78}, write a program to increment Bob's grade by 5 and remove Charlie from the dictionary.
        '''
        std = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
        std['Bob']+=5
        std.pop('Charlie')
        print(std)
    
    def q2(self):
        '''
        Q: Write a program to iterate over the dictionary students and print out each student's name and grade in the format "Name: Grade".
        '''

        std = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
        for n,g in std.items():
            print(f"{n}:{g}")
    
    def q3(self):
        '''
        Q: Explain how to use the popitem() method with an example, and describe a scenario where it might be useful.
        '''
        # popitem() remove the last item in dectionary and return it
        
        d = {1:'a',2:'b',3:'c'}
        r = d.popitem()
        print(r,d)

        # example: undo process in application 



# p1 = prob1()
# p1.q1()
# p1.q2()

p2 = prob2()
p2.q1()
p2.q2()
p2.q3()