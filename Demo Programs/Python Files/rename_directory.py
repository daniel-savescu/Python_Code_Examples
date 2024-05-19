import os

originalFileName = input('Enter the name of the file you want to rename : ')
newFileName = input('Enter the new file name : ')

os.rename(originalFileName,newFileName)

print('Task competed')