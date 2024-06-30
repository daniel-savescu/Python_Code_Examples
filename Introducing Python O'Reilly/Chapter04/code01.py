empty_tupple = ()

print(type(empty_tupple))

one_value = 1,

print(type(one_value))

#no comma separation

t = ('test')

print(type(t))

multiple_values = (1,2,3,4)

print(type(multiple_values))

print(multiple_values)

marks = (1,2,3)

a, b, c = marks

print(a)

print(b)

print(c)

#exchange values

password = 'test'

icecream = 'vanilla'

password, icecream = icecream, password

print(password)

print(icecream)

#tuple conversion

l = ['a','b','c']

t2 = tuple(l)

print(t2)

print(('a',) + ('b','c'))

print(('hello',) * 3)

#compare tuples

t3 = (7,2)
t4 = (7,2,9)

print(t3 == t4)

print(t3 <= t4)

print(t3 < t4)

#tuple iteration

x = (1,2,3,4,5)

for number in x:
    print(number)

#immutability of tuple

t5 = ('a','b')

t6 = ('c',)

print(id(t5))

t5 += t6

print(id(t5))
