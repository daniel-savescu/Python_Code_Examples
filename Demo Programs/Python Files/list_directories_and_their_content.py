import os

targetDirectory = input('Enter the directory you want to list his content : ')

data = os.walk(targetDirectory)

for item in data:
    print(item)