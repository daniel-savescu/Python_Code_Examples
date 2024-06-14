file = open('data.txt','w') #create a new file object in write mode

file.write('Hello\n') #write data to the file

file.write('world\n')

file.close() #close file buffer

file = open('data.txt') #r (read) is the default processing minde

data = file.read() #read data from file

print(data) #print data

for line in open('data.txt') : print(data)