def capitalize(userInput):
    splitted_string = userInput.split()
    result = []
    for letter in splitted_string:
        l = letter[0].upper() + letter[1:-1] + letter[-1].upper()
        result.append(l)
    result = ' '.join(result)
    return result

user = input("Enter a string : ")
print(capitalize(user))