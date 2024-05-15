f = open('abc.txt', 'r')

print('File name : ', f.name)
print('File mode : ', f.mode)
print('Is File Closed ? : ', f.closed)
print('Is File Readeable ? : ', f.readable())
print('Is File Writable ? : ', f.writable())

f.close()

print('Is File Closed ? : ', f.closed)