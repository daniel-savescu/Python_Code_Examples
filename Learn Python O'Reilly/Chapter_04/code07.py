X = set('spam') #make a set out of a sequance   
Y = {'h','a','m'} #make a set out of set literals

print(X,Y)

print(X & Y) #intersection

print(X | Y) #union

print(X - Y) #difference

print({ n ** 2 for n in [1, 2, 3, 4]}) #set comprehension

l = list(set([1,2,1,2,3,2,3])) #filter out duplicates
 
print(l)

print(set('spam') - set('ham')) #finding difference in collections

print(set('spam') == set('amps')) #order neutral equality test