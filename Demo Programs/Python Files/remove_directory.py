import os

nameOfTheDirectoryForRemoval = input("Enter the name of the directory you want to remove : ")

os.rmdir('test_1' + '/' + nameOfTheDirectoryForRemoval)

print("The directory was removed")