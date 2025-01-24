'''
Sets
'''

class prob1:
    '''
    Creating and Accessing Sets
    '''

    def q1(self):
        '''
        Q: Write a program to create a set of unique words from a given sentence and then check if the word 'Python' is in the set.
        '''
        s = "Write a program to create a set of unique words from a given sentence and then check if the word Python is in the set".split()

        st = set(s)
        print(st)
        print('Python' in st)
    
    def q2(self):
        '''
        Q: How can you create a set from a list with duplicate elements and then add a new element to the set?
        '''

        l = [1,2,3,3,2,1]
        s = set(l)
        s.add(9)
        print(s)

class prob2:
    '''
    Set Operations
    '''
    def q1(self):
        '''
        Q: Given two sets set1 = {1, 2, 3, 4} and set2 = {3, 4, 5, 6}, write a program to find the symmetric difference of these sets.
        '''
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
        # s = set1.symmetric_difference(set2)
        s = set1 ^ set2
        print(s)
    
    def q2(self):
        '''
        Q: Write a program to find all elements that are present in either set1 or set2 but not in both (symmetric difference).
        '''

        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
        # s = set1.symmetric_difference(set2)
        s = set1 ^ set2
        print(s)
        
    def q3(self):
        '''
        Q: Given a list of numbers, write a program to remove all duplicates by converting the list to a set and then back to a list.
        '''
        l = [1,2,3,3,2,1]
        print("Bef:",l)
        s = set(l)
        l = list(s)
        print("Aft:",l)





# p1 = prob1()
# p1.q1()
# p1.q2()

p2 = prob2()
p2.q1()
p2.q2()
p2.q3()
