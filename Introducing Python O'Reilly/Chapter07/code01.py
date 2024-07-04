#Objects

#Create an empty object

#First example :

class Cat():
    pass

#Second example 

class Cat:
    pass

#Creating an object

a_cat = Cat()

another_cat = Cat()

#Attributes

a_cat.age = 3

a_cat.name = 'Mr. Fuzzybuttons'

print(a_cat.age)

print(a_cat.name)

#Methods

#A method is a function in a class or object. 
#A method looks like any other function, but can be used in special ways

#Initialization

#If you want to assign object attributes at creation time, you need 
#the special Python object initialization method __init__():

class Cat:
    def __init__(self):
        pass

#This is what you’ll see in real Python class definitions. I admit 
#that the __init__() and self look strange. __init__() is the 
#special Python name for a method that initializes an individual 
# object from its class definition. 
# The self argument specifies that it refers to the individual object itself.
#When you define __init__() in a class definition, its first parameter should be named self. 
#Although self is not a reserved word in Python, it’s common usage.
#No one reading your code later (including you!) will need to guess what you meant if you use self.
#But even this second Cat class definition didn’t create an object that really did anything. 
#The third try is the charm that really shows how to create a simple object in Python and assign one of its attributes. 
#This time, we add the parameter name to the initialization method:

class Cat():
    def __init__(self, name):
        self.name = name

#Now we can create an object from the Cat class by passing a string 
#for the name parameter:

furball = Cat('Grumpy')

print('Our latest addition: ',furball.name)

#Inheritance

#Example:

class Car():
    pass

class Yugo(Car):
    pass

print(issubclass(Yugo, Car))

#Second example :

class Car():
    def exclaim(self):
        print("I'm a Car !")

class Yugo(Car):
    pass

give_me_a_car = Car()

give_me_a_yugo = Yugo()

give_me_a_car.exclaim()

give_me_a_yugo.exclaim()

#Override a method

class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo ! Much like a Car !")

give_me_a_car = Car()

give_me_a_yugo = Yugo()

give_me_a_car.exclaim()

give_me_a_yugo.exclaim()

#Adding a new method to the Child class

class Car():
    def exclaim(self):
        print("I'm a Car !")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yogo ! Much like a Car !")

    def need_a_push(self):
        print("A little help here?")

give_me_a_car = Car()

give_me_a_yugo = Yugo()

give_me_a_yugo.need_a_push()

#The super() keyword

#Example :

class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

bob = EmailPerson("Bob Jones", "bob@yahoo.com")

print(bob.name)

print(bob.email)

#Multiple Inheritance

#Example :

class Animal():
    def says(self):
        return 'I speak!'
    
class Horse(Animal):
    def says(self):
        return 'Neigh!'
    
class Donkey(Animal):
    def says(self):
        return 'Hee-haw!'

class Mule(Donkey, Horse):
    pass

class Hinny(Horse, Donkey):
    pass

mule = Mule()

hinny = Hinny()

print(mule.says())

print(hinny.says())


#Getters and Setters

#Example

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

don = Duck('Donald')

print(don.get_name())

don.set_name('Donna')

print(don.get_name())

#Method Types

#Instance methods

#When you see an initial self argument in methods within a class definition, 
#it’s an instance method. These are the types of methods that you 
#would normally write when creating your own classes. 
#The first parameter of an instance method is self, and Python 
#passes the object to the method when you call it.
#These are the ones that you’ve seen so far.

#Class methods

#In contrast, a class method affects the class as a whole. 
#Any change you make to the class affects all of its objects. 
#Within a class definition, a preceding @classmethod decorator 
#indicates that that following function is a class method. 
#Also, the first parameter to the method is the class itself. 
#The Python tradition is to call the parameter cls, because 
#class is a reserved word and can’t be used here. Let’s define 
#a class method for A that counts how many object 
#instances have been made from it:

#Example

class A():
    count = 0

    def __init__(self):
        A.count += 1
    
    def exclaim(self):
        print("I'm an A")

    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects")

easy_a = A()

breezy_a = A()

wheezy_a = A()

A.kids()

#Static methods

#A third type of method in a class definition affects neither the 
#class nor its objects; it’s just in there for convenience 
#instead of floating around on its own. It’s a static method,
#preceded by a @staticmethod decorator, with no initial self 
#or cls parameter. Here’s an example that serves as a commercial 
#for the class CoyoteWeapon:

class CoyoteWeapon():
    @staticmethod
    def commercial():
        print("This CoyoteWeapon has been brought to you by Acme")

CoyoteWeapon.commercial()

#Magic methods

#Example

class Word():
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    

first = Word('ha')

second = Word('Ha')

third = Word('eh')

print(first == second)

print(first == third)

