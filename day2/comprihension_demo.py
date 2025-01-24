'''
List Comprehension and Dict Comprehension
'''

class LC:
    '''
    List Comprehension
    '''

    def q1(self):
        '''
        Q: Write a list comprehension to create a list of the squares of all even numbers between 1 and 20.
        '''
        l = [i for i in range(1,21)]
        print(l)
    
    def q2(self):
        '''
        Q: How would you use a list comprehension to create a list of tuples, where each tuple contains a number and its cube, for numbers from 1 to 10?
        '''
        l = [(i,(i**3)) for i in range(1,11)]
        print(l)

class DC:
    '''
    Dict Comprehension
    '''

    def q1(self):
        '''
        Q: Given a list of strings ['apple', 'banana', 'cherry'], use dictionary comprehension to create a dictionary where the keys are the strings and the values are the lengths of those strings.
        '''

        l = ['apple', 'banana', 'cherry']
        d = {i:len(i) for i in l}
        print(d)
    
    def q2(self):
        '''
        Q: Write a dictionary comprehension to create a dictionary with keys as numbers from 1 to 5 and values as their factorials.
        '''
        def fc(n):
            if n==0:
                return 1
            return n*fc(n-1)
        
        d = {i:fc(i) for i in range(1,6)}

        print(d)


p1 = LC()
# p1.q1()
# p1.q2()

p2 = DC()
p2.q1()
p2.q2()