#Functions

#Here is an example of the most simple Python's function :

def do_nothing():
    pass

#Calling the function :

do_nothing()

#Second example with a function that prints a message :

def make_a_sound():
    print('quack')

make_a_sound()

#The next example is a function that returns a value :

def agree():
    return True

#Using the 'if' statement we can call the function so we can see if the value will be returned :

if agree():
    print('Splendid')
else:
    print('That was unexpected')


#Next we declare a function with a parameter 

def echo(anything):
    return anything + ' ' + anything

print(echo('Hello'))

#Second example :

def commentary(color):
    if color == 'red':
        return 'It\'s a tomato'
    elif color == 'green':
        return 'It\'s a green pepper'
    elif color == 'bee purple':
        return 'I don\'t know what it is, but only bees can see it'
    else:
        return 'I never heard of the color ' + color + '.'

comment = commentary('blue')

print(comment)

#None

#None is a special Python value that holds a place when there is nothing to say.
#It's not the same as the boolean value False

#Example :

thing = None

if thing is None:
    print('It\'s nothing')
else:
    print('It\'s something')

#Second example

def whatis(thing):
    if thing is None:
        print(thing, "is None")
    elif thing:
        print(thing, "it True")
    else:
        print(thing, "is False")

whatis(None)

whatis(True)

whatis(False)

#Positional arguments

#It the case of positional arguments you will need to remember the order of each position.
#For example

def menu(wine, entree, dessert):
    return {'wine': wine, 'entree' : entree, 'dessert' : dessert}

print(menu('chardoney', 'chicken', 'cake'))

#Keyword arguments
#To avoid positional argument confusion, you can specify by the names of their corresponding
#paramenters, even in a different order from their definition in a function

print(menu('frontenac', dessert='flan', entree='fish'))

#Default paramenter values
#You can specify default values for parameters. The default is used if the caller does not provide
#a corresponding argument. This bland-souding feature can actually be quite useful.

def menu(wine, entree, dessert='pudding'):
    return {'wine' : wine, 'entree' : entree, 'dessert' : dessert}

print(menu('chardoney', 'chicken'))

#Explode / Gather positional arguments with '*' :
#When used inside the function paramenter, an asterisk group a variable number of positional
#arguments into a single tuple of parameter values

#For example

def print_args(*args):
    print('Positional tuple ', args)

print_args(1, 2, 3, 'no', 'wait!')

#This is useful for writing functions as print() that accept a variable number of arguments.
#If the function has require positional arguments, as well, put them first; *args goes at
#the and and grabs all the rest

def print_more(required1, required2, *args):
    print("This one is needed : " ,required1)
    print("Need this also : ", required2)
    print("All the rest : ", args)

print_more("cap", "gloves", "car", "bike")

#Explode / Gather keyword arguments with ' ** '
#We can use ** two asterisk to group keyword arguments into a dictionary where the
#argument names are the keys, and their values are the corresponding dictionary values.

#Example

def print_kwargs(**kwargs):
    print('Keyword arguments : ', kwargs)

print_kwargs(wine = 'merlot', entree = 'mutton', desser = 'macaroon')

#Mutable and Immutable arguments
#Example :

outside = ['one', 'fine', 'day']

def mangle(arg):
    arg[1] = 'terrible'

print(outside)

mangle(outside)

print(outside)

#Functions Are First-Class Citizens
#The Python mantra, everything is an object. This includes numbers, strings, tuples, 
#lists, dictionaries—and functions, as well. Functions are first-class citizens in Python. 
#You can assign them to variables, use them as arguments to other functions, and return them from functions. 
#This gives you the capability to do some things in Python that are difficult-to-impossible to carry out in many other languages.

#Example :

def answer():
    print(42)

answer()

def run_something(func):
    func()

run_something(answer)

#Second Example:

def add_args(arg1, arg2):
    print(arg1 + arg2)

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_something_with_args(add_args,5,10)


#Inner functions

#You can define a function whitin another function:

def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

print(outer(5, 5))

#An inner function can be useful when performing some complex task more than once within another function, to avoid loops or code duplication. 
#For a string example, this inner function adds some text to its argument:

def knights(saying):
    def inner(quote):
        return 'We are the knights who say : \'%s\'' %quote
    return inner(saying)

print(knights('Ni'))  

#Generators

#A generator is a Python sequence creation object. With it, you can iterate through potentially huge sequences without creating and 
#storing the entire sequence in memory at once. Generators are often the source of data for iterators. If you recall, we already used one of them, range(), 
#in earlier code examples to generate a series of integers. In Python 2, range() returns a list, which limits it to fit in memory. 
#Python 2 also has the generator xrange(), which became the normal range() in Python 3. This example adds all the integers from 1 to 100:

print(sum(range(1,101)))

#If you want to create a potentially large sequence, you can write a generator
#function. It’s a normal function, but it returns its value with a yield statement rather than return. Let’s write our own version of range():

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

#It's a normal function

print(type(my_range))

ranger = my_range(1, 5)

#And will return a generator object

print(type(ranger))

#We can iterate over this generator object:

for x in ranger:
    print(x)

#If you try to iterate this generator again, you’ll find that it’s tapped out:

for try_again in ranger:
    print(try_again)