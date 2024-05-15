from zipfile import *

zipFileName = input("Enter the zip file name you want to extract : ")

with ZipFile(zipFileName+".zip", 'r') as unzipObject:
    pathOfExtraction = input("Enter the path you want your files to be extracted : ")
    unzipObject.extractall(path=pathOfExtraction)

print("Extraction of the files is completed")