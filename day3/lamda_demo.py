
'''
Create a lambda function that takes a list of tuples (each tuple contains a name and age) and returns a list of names of people older than 30.
'''
opn = lambda lt : [i[0] for i in lt if i[1]>30]

'''
Write a lambda function that takes a list of dictionaries (each dictionary contains keys 'name' and 'score') and returns a sorted list of names based on the scores in descending order.
'''

st = lambda dc : [i[0] for i in sorted(dc.items(),key=lambda k:k[1],reverse=True)]


# r = opn([('a',40),('u',20),('e',35),('i',31)])

r = st({'a':40,'u':20,'e':35,'i':31})

print(r)

d = [
    {'a':1},
    {'b':2},
    {'c':3},
    {'d':4}
]

# print(d[0].items(),type(d[0].values()))

st = lambda d : [list(i.keys())[0] for i in sorted(d,key=lambda k:list(k.values())[0],reverse=True)]

print(st(d))
