S = 'Spam' #make a 4-character string, and assing it to a name

print(len(S)) #print the length of the string

print(S[0]) #the first item in S, indexing by zero-based position

print(S[1]) #second item from left

print(S[-1]) #last item from the end of S

print(S[-2]) #second to last item from the end

print(S[-1]) #the last item from S

print(S[len(S)-1]) #negativ index the hard way

print(S[1:3]) #Slice of S offset from 1 to 2 (not 3)

print(S[1:]) #everything past the first

print(S) #S itself hasn't changed

print(S[0:3]) #eveything but the last

print(S[:3]) #same as S[0:3]

print(S[:-1]) #eveything but the last again, but simpler (0:-1)

print(S[:]) #all of S as top-level copy (0:len(S))

print(S + 'xyz') #concatenation

print(S) #S is unchanged

print(S * 8) #repetition

S2 = 'car'

L = list(S2)

L[-1] = 't'

print(''.join(L))

S3 = 'test'

print(S3.find('es')) #find the offset of a substring in S3

print(S3)

print(S3.replace('es', 'XYZ')) #replace occurrences of a string in S3 with another

print(S3)


line = 'aaa,bbb,ccc,dd'
print(line.split(',')) #split on a delimiter into a list of substrings

testString = 'test'

print(testString.upper()) #upper-case conversion

print(testString.isalpha()) #content test : isalpha, isdigit, etc

print(dir(S))