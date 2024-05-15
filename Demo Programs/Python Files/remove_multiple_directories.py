import os

firstDirectoryToRemove = input("Enter the first directory name you want to remove : ")
secondDirectoryToRemove = input("Enter the second directory name you want to remove : ")
thirdDirectoryToRemove = input("Enter the third directory name you want to remove : ")

os.removedirs(firstDirectoryToRemove + "/" + secondDirectoryToRemove + "/" + thirdDirectoryToRemove)

print("The directories had been removed succesuflly")