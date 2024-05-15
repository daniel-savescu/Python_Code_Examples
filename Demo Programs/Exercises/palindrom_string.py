def checkForPalindrome(userInput):
    if userInput.lower() == userInput[::-1].lower():
        return True

originalString = input("Enter a string to check if it's a palindrome : ")

print(checkForPalindrome(originalString))





