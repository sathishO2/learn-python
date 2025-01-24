# Defining and Calling Functions

'''
Define a function that takes a list of integers and returns a new list with only the even numbers, but doubled.
'''
def q1(lis):
    return [i*2 for i in lis if i%2==0]

'''
Write a function that accepts a string and returns a dictionary with the frequency of each character in the string.
'''
def q2(s: str) -> dict:
    return {i:s.count(i) for i in s}

# Function Arguments (Positional, Keyword, Default, Variable-length)
'''
Write a function that takes two lists and returns a dictionary where the keys are elements from the first list and the values are elements from the second list. Use positional arguments.
'''
def q3(l1,l2):
    return {l1[i]:l2[i] for i in range(len(l1))}

'''
Create a function that accepts a variable number of positional arguments and keyword arguments, and returns a list of the positional arguments and a dictionary of the keyword arguments.
'''
def q4(*l,**d):
    return [l,d]

'''
Define a function that generates a multiplication table for a given number up to a specified range. If no range is provided, default to 10.
'''
def q5(n,r=10):
    for i in range(1,r+1):
        yield f"{i} x {n} = {i*n}"

'''
Write a function that accepts any number of keyword arguments representing student names and their scores, and returns the name of the student with the highest score.
'''
def q6(**ss):
    l = sorted(ss.items(),key=lambda k:k[1],reverse=True)
    return f"{l[0][0]}:{l[0][1]}"

# Return Values
'''
Define a function that takes a sentence as input and returns a tuple containing the number of words, the number of characters (excluding spaces), and the number of unique words.
'''
def q7(s):
    w = s.split()
    c = s.replace(" ","")
    uw = set(w)
    return ((("num of words",len(w)),("num of char",len(c)),("num of unicque words",len(uw))))

'''
Write a function that accepts a list of numbers and returns a dictionary with the keys 'mean', 'median', and 'mode' representing the respective statistical values of the list.
'''
def q8(l):
    mean = sum(l)/len(l)

    st = sorted(l)
    even = lambda st : (st[len(st)//2] + st[(len(st)-1)//2])//2
    odd = lambda st : st[(len(st)-1)//2]
    median = even(st) if len(st)%2==0 else odd(st)

    modes = [[i, l.count(i)] for i in l]
    modes.sort(key = lambda k:k[1], reverse=True)
    mode = modes[0][0]
    return {'mean':mean,'median':median,'mode':mode}


# r = q1([1,2,3,4,5,6])
# r = q2("innoboon")


# r = q3([1,2,3,4],[5,6,7,8])
# r = q4(1,2,3,4,a=1)

# g = q5(2,5)
# r = [next(g) for _ in range(5)]

# r = q6(a=1,b=4,c=2,d=3)

# r = q7("Define a function that takes a sentence as input and returns a tuple containing the number of words, the number of characters (excluding spaces), and the number of unique words.")

r = q8([1,2,3,4,5])
print(r)
    


        
