f = open('abc.txt', 'w')

l = ["Python\n", "C\n", "Java\n"]
f.writelines(l)

f.close()
print("Data written succesfully to the file")

