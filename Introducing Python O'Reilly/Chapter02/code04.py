#Strings examples :

s1 = "String"

s2 = 'String2'

print(s1)

print(s2)

s3 = 'He sayig "Hello"'

s4 = "Let's go!"

print(s3)

print(s4)

bottles = 99

base = ''

base += 'There are currently : '

#Typecasting integer into string :

base += str(bottles)

base += ' bottles'

print(base)

#Typecasting different data types into string : 

print(str(True))

print(str(10.4))

print(str(1.0e4))

print("This is\nA new\nLine")

print("a\tb")

print("ab\tc")

print("Please" + " wait")

print("Hey" " stop")

print("olla " * 3)

letters = 'abcdefgh'


#Accesing string characters using index :

print(letters[0])

print(letters[1])

print(letters[-1])

name = "Henny"


#replace() function example :

print(name.replace('H', 'P'))

#Examples of string sliceing :

print('P' + name[1:])

print(letters[1:])

print(letters[:])

print(letters[-3:])

print(letters[2:-4])

print(letters[::-1])

print(len(letters))

empty = ""

#len() function example for returning the legth of the string

print(len(empty))

todoe = 'get milk, get pasta, get patatoes'

#split() function examples by a specific delimiter :

print(todoe.split(','))

print(todoe.split())

names = ['john', 'bill', 'emily']

#join() function example :

print(', '.join(names))

s5 = 'test'

#find() function example :

print(letters.find(s5))

s6 = 'testing...'

#other string functions examples :

print(s6.strip('.'))

print(s6.capitalize())

print(s6.upper())

print(s6.lower())

print(s6.center(30))

print(s6.ljust(30))