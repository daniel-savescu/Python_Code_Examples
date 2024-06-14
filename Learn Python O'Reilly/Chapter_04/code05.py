T = (1,2,3,4) # a 4 item tuple

print(len(T)) # length of tuple


print(T + (5, 6)) #comcatenation

print(T[0]) #indexing

print(T.index(1)) #value 1 appears at offset 0

print(T.count(4)) #4 is found one time

#tuples are immutable

#T[0] = 2

T=(2,) + T[1:] #make a new tuple for a new value

print(T)

T = 'spam' , 3.0, [11,22,33] #parantheses are optional

print(T[0])

print(T[2][1])

print(type(T))