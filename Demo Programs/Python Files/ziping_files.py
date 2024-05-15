from zipfile import *

zipName = input("Enter the zip file name : ")

zipObject = ZipFile(zipName + '.zip', 'w', ZIP_DEFLATED)

while True:
    fileName = input("Enter the file name you want to zip : ")
    zipObject.write(fileName)
    option = input("Do you want to zip another file ? [YES | NO] : ? ")
    if option.lower() == 'no':
        break

print("Ziping process completed !")