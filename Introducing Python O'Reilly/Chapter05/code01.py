#Dictionaries

#Create dictionaries with {}

empty_dict = {}

print(empty_dict)

#Dictionary example with quotes

bierce = {
    'day' : 'A period of twenty-four hours, mostly misspent',
    'positive' : 'Mistaken at the top of one\'s voice',
    'misfortune' : 'The kind of fortune that never misses',
}

print(bierce)

#Create dictionary with dict()

acme_customer = dict(first="Wile", middle = "E", last="Coyote")

print(acme_customer)

#Convert with dict()

#In this example we create a dict from a list

lol = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]

print(dict(lol))

#A list of two-item tuples :

lot = [ ('a', 'b'), ('c', 'd'), ('e', 'f') ]

print(dict(lot))

#A tuple of two-item lists:

tol = ( ['a', 'b'], ['c', 'd'], ['e', 'f'] )

print(dict(tol))

#A list of two-character strings

los = ['ab', 'cd', 'ef']

print(dict(los))

#A tuple of two-character strings

tos = ('ab', 'cd', 'ef')

print(dict(tos))

#Add or change an item by key

pythons = {
    'Chapman' : 'Graham',
    'Cleese' : 'John',
    'Idle' : 'Eric',
    'Jones' : 'Terry',
    'Palin' : 'Michael',
}

print(pythons)

#Adding a value by key

pythons['Gilliam'] = 'Gerry'

print(pythons)

#Changing a value by key

pythons['Gilliam'] = 'Terry'

print(pythons)

#Get an item by key or with get()

print(pythons['Cleese'])

print(pythons.get('Palin'))

#But first check if the value in the dict is present using 'in'

print('Idle' in pythons)

#Or place a second paramenter to get() to alert you if the key is not in dict

print(pythons.get('David', 'Not in dict !'))

#Get all keys with keys() function

print(pythons.keys())

#Stoare keys in list

print(list(pythons.keys()))

#Get all dict values with values() function

print(list(pythons.values()))

#Get all dict's key-value pairs with items() function

print(list(pythons.items()))

#Get the length of dict with len() function

print(len(pythons))

#Combine dictionaries using : {**first_dict, **second_dict}

first = {'a' : 'agony', 'b' : 'bliss'}

second = {'c' : 'bagless', 'd' : 'candy'}

print({**first, **second})

#But also you can pass more dictionaries than two :

third = {'e' : 'cake', 'f' : 'jelly'}

print({**third, **second, **first})

#Combine dict with update() function :

first.update(second)

print(first)

#Delete an item by key with 'del' :

del pythons['Idle']

print(pythons)

#Get an item by key and delete it with pop() function :

print(len(pythons))

pythons.pop('Palin')

print(len(pythons))

print(pythons)

#Delete all items with clear() :

first.clear()

print(len(first))

print(first)

#Test for a key with 'in' :

print('Gilliam' in pythons)

#Assign with '='

#As with lists, if you make a change in the dictionary, it will be reflected in all the names
#that refer to it

print(third)

saved_third = third

print(saved_third)

third['e'] = 'vanilla'

print(saved_third)

#Copy with copy() function

#To avoid the previous example from overiding you can use copy():

original_third = third.copy()

print(original_third)

third['e'] = 'chocolate'

print(third)

print(original_third)

#Compare dictionaries

#As with lists from the previous chapter, dictionaries can be compared
#with the simple comparion operators like : == and !=

a = {1:1, 2:2, 3:3}

b = {3:3, 2:2, 1:1}

print(a==b)

print(a != b)

#Iterate with 'for' and 'in'

accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}

for card in accusation:
    print(card)

#Second example using keys() function :

for card in accusation.keys():
    print(card)

#To iterate over values you can use values() function : 

for value in accusation.values():
    print(value)

#To iterate over keys and values you can use items() function :

for item in accusation.items():
    print(item)

#Dictionaries comprehension :

word = 'letters'

letters_count = { letter: word.count(letter) for letter in word}

print(letters_count)

#Similar to lists, dictionary comprehension can also have 'if' test and multiple 'for' clauses :

vowels = 'aeiou'

word = 'onomatopoeia'

vowels_count = {letter : word.count(letter) for letter in set(word) if letter in vowels}

print(vowels_count)