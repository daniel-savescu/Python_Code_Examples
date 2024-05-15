import os

firstDirectory = input("Enter the first directory name : ")
secondDirectory = input("Enter the second directory name : ")
thirdDirectory = input("Enter the third directory name : ")

os.makedirs(firstDirectory + "/" + secondDirectory + "/" + thirdDirectory)

print("Directories had been created")