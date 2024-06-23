userInput = input("Enter a string : ")

index = 0

while index < len(userInput):
    print(userInput[index])
    index += 1

#alternative

for letter in userInput:
    print(letter)

for letter in userInput:
    if letter == 's':
        break
    print(letter)