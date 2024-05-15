#immutable data type

#int, float, tuple, complex, string, fronze set

#Example of immutability

name = "Daniel"

name[0] = 'X'

print(name)

#Paradox example using a immutable object with a mutable object inside

t = (1,['a','b','c'], 'word')

#This won't work (eg. 1)

t[0] = 2

print(t)

#Also this won't work (eg. 2)

t[2][0] = 'X'

print(t)

#But this will work

t[1][0] = '?'

print(t)



