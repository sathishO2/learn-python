class prob1:
    '''
    Tuple
    '''
    def q1(self):
        '''
        Q: Create a tuple containing the elements of the periodic table's first five elements. How would you access the element 'Lithium' in the tuple?
        '''

        p = ("Hydrogen", 'Helium', 'Lithium','Beryllium','Boron')

        print(p[p.index('Lithium')] if 'Lithium' in p else "Not Available")
    
    def q2(self):
        '''
        Q: Write a program that converts a list of integers [1, 2, 3, 4, 5] into a tuple and then finds the maximum value in the tuple.
        '''
        l = [1, 2, 3, 4, 5]
        t = tuple(l)
        print("Max: ",max(t))

class prob2:
    '''
    Tuple Operations and Immutability
    '''

    def q1(self):
        '''
        Q: Explain the concept of immutability in tuples with an example where you attempt to modify a tuple and handle the exception that occurs.
        '''
        # concept of immutability - we can't change/modify the value or element
        # tuple is a Immutable data structure in python 

        t = tuple((1,2,3,1,2,3))
        # t[0] = 200
        '''
        t[0] = 200
        TypeError: 'tuple' object does not support item assignment
        '''

        # but we can
        l = list(t)
        l[0] = 200
        t = tuple(l)
        print(t)
    
    def q2(self):
        '''
        Q: Given two tuples tuple1 = (1, 2, 3) and tuple2 = (4, 5, 6), write a program to concatenate them and then find the sum of all elements in the resulting tuple.
        '''

        tuple1 = (1, 2, 3)
        tuple2 = (4, 5, 6)

        result = tuple1+tuple2
        print(result)



# p1 = prob1()
# p1.q1()
# p1.q2()

p2 = prob2()
p2.q1()
p2.q2()

