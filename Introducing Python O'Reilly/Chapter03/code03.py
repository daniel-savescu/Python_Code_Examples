#if / break statement example : 

numbers = [1,3,5]

position = 0

while position < len(numbers):
    
    number = numbers[position]

    if number % 2 == 0:
        print('Found even number : ', number)
        break
    position += 1

else:
    print('No even number found.')

