#List data type

#Create empty list

l = []

#Adding values to the list

l.append(3)
l.append(2)
l.append(1)

print(l)

#Sorting values of the list in ascending order

l.sort()

print(l)

#Sorting valus in descending order

l.sort(reverse=True)

print(l)

#Counting the appearance of a value in the list

l.append(3)

print(l)

count = l.count(3)

print(count)

#Adding an existing list to another list

l2 = ['car','bus','bike']

l.extend(l2)

print(l)


