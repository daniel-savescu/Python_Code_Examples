import os

newDirectoryName = input('Enter the directoy name you want to create : ')

os.mkdir(newDirectoryName)

print(newDirectoryName + " was created")