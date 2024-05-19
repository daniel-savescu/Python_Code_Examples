import os

targetDirectory = input('Enter the directory you want to list his content : ')

data = os.walk(targetDirectory)

for dirpath, dirname, files in data:
    print("Directory Path : ", dirpath)
    print("Directory Name : ", dirname)
    print("File Name : ", files)

    