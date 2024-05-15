import os
originalFileName = input('Enter the file you want to copy : ')
if os.path.isfile(originalFileName):
    originalFile = open(originalFileName, 'rb')
    originalData = originalFile.read()
    copyFileName = input('Enter the new file name : ')
    copyFile = open(copyFileName, 'wb')
    copyFile.write(originalData)
    print('Copy process completed')
    originalFile.close()
    copyFile.close()
else:
    print('File does not exists !')

