#Sets

#This is how you create an empty set :

empty_set = set()

print(empty_set)

#This example show how to create a set already knowing the values

even_numbers = {0, 2, 4, 6, 8}

print(even_numbers)

odd_numbers = {1, 3, 5, 7, 9}

print(odd_numbers)

#Because [] creates an empty list, you might expect that {} creates an empty set.
#Instead {}, creates an empty dict, that's why the interpreter prints an empty set as set() instead of {}
#The reason is, that dictionaries were in Python first and took posession of the curly brackets


#Converting with set()

#You can create set from list, string, tuple, or dictionary discarding the duplicate values

#String example

print(set('letters'))

#List example

print(set( ['Music', 'Dance', 'Music', 'Actor']))

#Tuple example

print(set( (1,2,3,4,4,5) ))

#Dictionary example

#Keep in mind that set() will be used only for keys :

print(set( {'apple' : 'red', 'orange' : 'orange', 'orange' : 'orange', 'cherry' : 'red'} ))

#Get length with len() function :

print(len(even_numbers))

#Add an item to set with add() function : 

s = set( (1, 2, 3) )

print(s)

s.add(4)

print(s)

#Delete an item with remove() function

s.remove(4)

print(s)

#Iterate using 'for' and 'in' :

for number in even_numbers:
    print(number)

#Test for a value using 'in' : 

drinks = {
   'martini': {'vodka', 'vermouth'},
   'black russian': {'vodka', 'kahlua'},
   'white russian': {'cream', 'kahlua', 'vodka'},
   'manhattan': {'rye', 'vermouth', 'bitters'},
   'screwdriver': {'orange juice', 'vodka'}
    }

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)
    
#Combination and operators

#Set interection operator '&'

a = {1, 2}

b = {2, 3}

print(a & b)

#Second example using intersection() function : 

print(a.intersection(b))

#Get members of either sets using ' | ' or union() function : 

print( a | b )

print(a.union(b))

#Get the difference ( members that are in the first set, but not in the second ) using ' - ' or diffence() function :

print(a-b)

print(a.difference(b))

#Set comprehension

a_set = { x for x in range(1,6) if x % 3 == 1}

print(a_set)

#Create an immutable Set with frozenset()

print(frozenset( [1, 2, 3] ))

print(frozenset( (1, 2, 3) ))

print(frozenset( set([1, 2, 3]) ))

print(frozenset( {1, 2, 3} ))
