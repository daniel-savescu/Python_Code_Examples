L = [123,'spam',1.23] #a list of three different-type objects

print(len(L)) #print the number of items in the list

print(L[0]) #indexing by position

print(L[:-1]) #slicing a list returns a new list

print(L + [4,5,6]) #concatenate make new list too

print(L * 2) #repeat list make new list too

print(L) #we are not changing the original list

L.append('NI') #growing : add object at end of list

print(L)

print(L.pop(2)) #Shrinking : delete an item at position 2 index

print(L)

M = ['bb','aa','cc']

M.sort() #sort the list content in ascending order

print(M)

M.reverse() #sorts the list content in descending order

print(M)

M2 = [[1,2,3], #A 3x3 matrix, as nested lists
      [4,5,6],
      [7,8,9]]

print(M2)

print(M2[1]) #get row 2

print(M2[1][2]) #get row 2, then get item 3 within the row

column2 = [row[1] for row in M2] #collect the items in column 2

print(column2)

print(M2) #the matrix is unchanged

newValue = [row[1] + 1 for row in M2] #add 1 to each item in column2

print(newValue)

odd = [row[1] for row in M2 if row[1] % 2 == 0] #filter out odd items in column 2

print(odd)

doubles = [c * 2 for c in 'spam'] #repeat characters in a string

print(doubles)

print(list(range(4))) #0,3 list

print(list(range(-6,7,2))) # -6 to 6 list increment by 2

G = (sum(row) for row in M2) #create a generator of row sums

print(next(G)) #iter (G) not required here

print(next(G))

print(next(G))