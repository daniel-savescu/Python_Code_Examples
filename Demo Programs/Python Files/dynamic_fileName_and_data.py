fileName = input('Enter file name : ')

f = open(fileName,'w')

while True:
    data = input('Enter data : ')
    f.write(data + '\n')
    option = input('Enter more data ? [ Yes | No ]')
    if option.lower() == 'no':
        break
f.close()