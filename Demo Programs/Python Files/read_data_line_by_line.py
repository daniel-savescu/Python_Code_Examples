file = open('test.txt', 'r')

fileLine = file.readline()

while fileLine != '':
    print(fileLine, end='')
    fileLine = file.readline()

file.close()