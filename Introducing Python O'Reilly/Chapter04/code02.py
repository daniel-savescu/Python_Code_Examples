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