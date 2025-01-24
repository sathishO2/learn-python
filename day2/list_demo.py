'''
List
'''

class prob1():
    '''
    Creating and Accessing Lists

    Q: Write a Python program to create a list of the first ten prime numbers. How would you access the second last element in this list?
    '''
    def q1(self):
        l = []
        n = 10
        k = 2
        while n>0:
            for i in range(2,k//2+1):
                if k%i==0:
                    break
            else:
                l.append(k)
                n-=1
            k+=1
        print(l)
        print("Second Last Element: ",l[-2])

    
    '''
    Q: How would you create a list that contains the first five Fibonacci numbers?
    '''
    
    def q2(self):
        l = [0,1]
        i,j = 0,1
        t = 3
        while t>0:
            i,j = j,i+j
            l.append(j)
            t-=1
        print(l)

class prob2:
    '''
    '''

    def q1(self):
        '''
        Q: Given the list numbers = [1, 2, 3, 4, 5], how would you insert the number 6 at the second position and then remove the last element from the list?
        '''
        numbers = [1, 2, 3, 4, 5]
        numbers.insert(1,6)
        print(numbers)
    
    def q2(self):
        '''
        Q: Write a program that combines two lists list1 = [1, 3, 5] and list2 = [2, 4, 6] into a single list, alternating elements from each list.
        '''
        l1 = [1, 3, 5]
        l2 = [2, 4, 6]
        l3 = []
        for i in range(len(l1)):
            l3.append(l1[i])
            l3.append(l2[i])
        print(l3)

    def q3(self):
        '''
        Q: Given the list fruits = ['apple', 'banana', 'cherry', 'apple', 'cherry'], write a program to remove all occurrences of 'apple'.
        '''
        fruits = ['apple', 'banana', 'cherry', 'apple', 'cherry']
        for i in fruits:
            if i == "apple":
                fruits.remove("apple")
        print(fruits)
    
    def q4(self):
        '''
        Q: How can you reverse the list numbers = [1, 2, 3, 4, 5] without using the built-in reverse() method?
        '''
        num = [1, 2, 3, 4, 5]
        print(num[::-1])


p1 = prob1()
# p1.q1()
p1.q2()

# p2 = prob2()
# p2.q1()
# p2.q2()
# p2.q3()
# p2.q4()

