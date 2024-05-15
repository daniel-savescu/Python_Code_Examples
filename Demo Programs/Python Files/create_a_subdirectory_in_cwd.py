import os

currentDirectory = os.getcwd()

subDirectory = input('Enter the name of the subdirectory : ')

os.mkdir(currentDirectory+'/'+subDirectory)

print(subDirectory + ' was created')