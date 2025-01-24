'''
Frozenset
'''

class prob1:
    '''
    Creating and Accessing Frozensets
    '''

    def q1(self):
        '''
        Q: Write a program to create a frozenset from the list ['apple', 'banana', 'cherry']. How would you check if the element 'banana' is in the frozenset?
        '''

        l = ['apple', 'banana', 'cherry']
        fs = frozenset(l)
        # print(fs)
        print(True if 'banana' in fs else False)
    
    def q2(self):
        '''
        Q: Explain how frozensets are different from sets and provide an example where a frozenset would be more appropriate than a set.
        '''

        # frozenset - Unchangeable and we cant add elements in to it

        # set - we can add element and it has set manupulating methods in it

        fs = frozenset([1,2,3,3,2,1])
        '''
        fs[0] = 9
        TypeError: 'frozenset' object does not support item assignment
        '''

        s = set([1,2,3,3,2,1])
        s.add(98)
        s.remove(1)

        print(fs,s)

class prob2:
    '''
    Frozenset Operations
    '''
    def q1(self):
        '''
        Q: Given two frozensets fs1 = frozenset([1, 2, 3, 4]) and fs2 = frozenset([3, 4, 5, 6]), write a program to find their union and intersection.
        '''
        fs1 = frozenset([1, 2, 3, 4])
        fs2 = frozenset([3, 4, 5, 6])

        r1 = fs1.union(fs2)
        r2 = fs2.intersection(fs2)

        print("Union: ",fs1 | fs2)
        print("intersection: ",fs1 & fs2)
    
    def q2(self):
        '''
        Q: Write a program to find the difference between two frozensets fs1 and fs2 and explain the result.
        '''

        fs1 = frozenset([1, 2, 3, 4])
        fs2 = frozenset([3, 4, 5, 6])
        r = fs1.difference(fs2)
        print("Difference: ",fs1-fs2)

        # it remove the elements from fs1 which is present in the fs2 and return it




# p1 = prob1()
# p1.q1()
# p1.q2()

p2 = prob2()
p2.q1()
p2.q2()
