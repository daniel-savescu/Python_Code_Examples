#Lists

empty_list = []

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

big_birds = ['emu', 'ostrich', 'cassowary']

first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']

leap_years = [2000, 2004, 2008]

random_elements = [1, {'groundhog': 'Phill' }, 'Feb. 2']

#first_names shows that values do not need to be unique

#You can make lists from using the list() function

another_empty_list = list()

print(type(another_empty_list))

#The list() function can convert any iterable data type into lists like ( sets, dictionaries, tuples and strings)

#The following example shows how to convert a string litteral into a one-character string list : 

print(list('dog'))

#This example converts tuple into a list :

a_tuple = ('car', 'bike', 'bus')

print(list(a_tuple))

#Create a list unsing split() string method

birthday = '8/8/1990'

print(birthday.split('/'))

#This example shows if you have one then more separator in your string.
#The conclusion is that you will get a empty string value as a result in your list

random_text = 'a/bc//de/fg//h'

print(random_text.split('/'))

#You can acces lists element values by using they index

marks = ['A', 'D', 'F']

print(marks[0])

print(marks[1])

print(marks[2])

#Like with strings, the value elements can be returned using theire negative value

#For example :

print(marks[-1])

print(marks[-2])

print(marks[-3])

#Like with strings, you can slice subsequnces in that list values:

print(marks[0:2])

#A slice of a list is also a list

#The same principles as string sliceing is the same for lists

#For example you can reverse a list as follows:

print(marks[::-1])

#reverse() function to reverse values in a list :

numbers = ['1', '2', '3' ,'4' ,'5']

numbers.reverse()

print(numbers)

#To add an item to the end of the list you can use the append() method.

#For example :

numbers.append('6')

print(numbers)

#To add a item into a particula position in the list you can use insert() method.
#For the first position into the list you can put 0 value and if you want to add a value
#to the end of the list don't worry if the index is to large.

#For example : 

#Inserting -1 to beginning of the list :

numbers.insert(0,'-1')

print(numbers)

#Inserting -2 to the end of the list using a bigger index of the list size :

numbers.insert(99, '-2')

print(numbers)

#Duplicating the value in list using  *

print(['hey !'] * 3)

#Extend list with other values of another list using extend() function or +, +=

more_numbers = ['11','99']

numbers.extend(more_numbers)

print(numbers)

again_more_numbers = ['55', '100']

numbers += again_more_numbers

print(numbers)

#If we had used append() function then the values will be added as a single list item rather then merging the items :

numbers.append(more_numbers)

print(numbers)

#You can change a value in a list using index of value.

#For example :

numbers[0] = '99999'

print(numbers)

#Another example of this is by changing values is by using sliceing :

numbers[1:3] = ['888', '777']

print(numbers)

#You can delete a item in a list by using del

del numbers[0]

print(numbers)

#Another way to delete a item in a list is by using remove() function

numbers.remove('888')

print(numbers)

#If you have duplicate items in the list by that value only the first one that is find will be deleted

#Another way to remove a item in a list is by using pop() function.
#If you use pop() with no argument, than the last item in the list will be removed.

numbers.pop()

print(numbers)

numbers.pop(1)

print(numbers)

#If you want to remove all items in a list you can use clear() function

numbers.clear()

print(numbers)

#If you want to find the index of a particular value in a list you can use index() function :

print(marks.index('A'))

#If the value is more then once in the list, only the fist one is returned.

#If you want to check if a particular value is in a list, you can use in keyword

print('A' in marks)

#If the value is present multiple times in the list, then it always will return True

#If you want to find how many times a value is in a list you can use count() function

print(marks.count('A'))

#If you want to combine a list into a string you can use join() function

print(''.join(marks))

#Join is the opposite of split()

#If you want to sort a list you can use sort() or sorterd()

#sort() -> sorts the list itself

#sorted() -> returns a new sorted list

sorted_marks = sorted(marks)

print(sorted_marks)

#by default the sorting is in ascending order

#if you want in reverse order just use the argument 'reverse=True'

sorted_marks.sort(reverse=True)

print(sorted_marks)

#If you want to get the length of a list you can use len() functions

print(len(marks))

#If you want to copy a list you can use the following tehniques:

# copy() function

# list conversion

# the slice operator [:]

a = [1, 2, 3]

b = a.copy()

c = list(a)

d = a[:]

print(b)

print(c)

print(d)

#Comparing lists 

b = [2,3,4]

print(a == b)

print(a <= b)

print(a < b)

#Iterate using for in a list

for number in a:
    print(number)

#List comprehension basic example

l = [value for value in range(1,10)]

print(l)

#Even numbers using list comprehension

even = [even for even in range(1,11) if even % 2 == 0]

print(even)

#Now we can make the same example in a more traditional way

even2 = []

for n in range(1,11):
    if n % 2 == 0:
        even2.append(n)

print(even2)

#Nested Comprehension Lists

#Traditional way :

rows = range(1,4)

cols = range(1,4)

for row in rows:
    for col in cols:
        print(row, col)

#Now lets use comprehension and assign it to variable cells, making it a list of (row, col) tuple :

rows = range(1,4)

cols = range(1,4)

cells = [(row, col) for row in rows for col in cols]

for cell in cells:
    print(cell)

#Another way to print the values is to use tuple unpacking like :

for row, cel in cells:
    print(row, cel)

#You can have lists inside other lists, for example :

small_birds = ['hummingbird', 'finch']

extinct_birds = ['dodo', 'passenger pigeon', 'Norvegian Blue']

carol_birds = [3, 'French hens', 2, 'turtledoves']

all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]

print(all_birds)

#You can access the values as same as a normal list by using the index / offset

print(all_birds[0])

#You can access every element by using the exact position. For example : hummingbird

print(all_birds[0][0])