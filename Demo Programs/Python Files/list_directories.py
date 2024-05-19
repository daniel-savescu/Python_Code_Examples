import os

targetDirectory = input('Enter the name of the directory you want to list : ')

content = os.listdir(targetDirectory)

print(content)