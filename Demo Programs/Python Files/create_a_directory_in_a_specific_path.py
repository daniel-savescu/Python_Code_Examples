import os

pathAndNameOfNewDirectory = input('Enter the path and the name of directory you want to create: ')

os.mkdir(pathAndNameOfNewDirectory)

print(pathAndNameOfNewDirectory + " was successfully created")