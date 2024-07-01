#Loops : while loop examples :

count = 1

while count <= 5:
    print(count)
    count += 1

while True:
    userInput = input("Capitalize string ? [type q to quit]")
    if userInput.lower() == 'q':
        break
    print(userInput.capitalize())

while True:
    number = input("Integer number please [type 'q' to quit]")
    if number.lower() == 'q':
        break
    value = int(number)
    if value % 2 == 0: #even number
        continue
    print(value, " squared is ", value * value)