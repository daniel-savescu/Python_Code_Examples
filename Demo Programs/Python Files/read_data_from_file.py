fileData = open('test.txt', 'r')

dataFromFile = fileData.read() #all data

# dataFromFile = fileData.read(3) #only 1 character. /n is calculated as a character as well

print(dataFromFile)

fileData.close()