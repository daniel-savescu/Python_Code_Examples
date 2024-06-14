D = {'food': 'Spam' , 'quantity': 4, 'color': 'pink'}

print(D['food']) #fetch value of key 'food'

D['quantity'] += 1

print(D)

D2 = {}

#Create keys by assignment

D2['name'] = 'Bob' 

D2['job'] = 'dev'

D2['age'] = 40

print(D2)

bob1 = dict(name='Bob', job='dev', age=40) #keywords

print(bob1)

bob2 = dict(zip(['name','job','age'], ['Bob', 'dev', 40])) #zipping

print(bob2)

rec = {'name':{'first' : 'Bob', 'last' : 'Smith'},
       'jobs' : ['dev','mgr'],
       'age': 40.5}

print(rec)

print(rec['name'])

print(rec['name']['last'])

print(rec['jobs'])

print(rec['jobs'][-1])

rec['jobs'].append('janitor')

print(rec)

test = {'a': 1, 'b': 2, 'c':3}

print(test)

test['d'] = 4 #assigning new keys grows dictionary

print(test)

# Referencing a nonexistent key is an error

#print(test['f'])

if 'f' in D:
    print(True)
else:
    print('missing')


value = D.get('x',0) #index with a default

print(value)

value2 = D['x'] if 'x' in D else 0 #if/else statement

print(value2)

Ks = list(D.keys()) #unorderd keys list

print(Ks)

Ks.sort() #sorted keys list

print(Ks)

#iterate through sorted keys
for key in Ks: 
    print(key,'=>', D[key])

for character in 'spam':
    print(character.upper())

x = 4

while x > 0:
    print('spam!' * x)
    x -= 1

squares = [ x ** 2 for x in [1, 2, 3, 4]]

print(squares)

squares2 = []

#this is what a list comprehension does
for x in [1, 2, 3, 4]:
    squares2.append(x **2)

print(squares2)