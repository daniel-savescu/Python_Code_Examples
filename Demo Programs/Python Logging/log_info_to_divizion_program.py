import logging

logging.basicConfig(filename='appLog.log', 
					level=logging.INFO,
					format='%(asctime)s:%(levelname)s:%(message)s',
					datefmt='%d%m%Y %I:%M:%S %p')
logging.info("Incomming new request")
try:
	firstNumber = int(input('Enter first number: '))
	secondNumber = int(input('Enter second number: '))
	print('The result  = ', firstNumber / secondNumber)
except ZeroDivisionError as msg:
	print('Cannot divide by zero')
	logging.exception(msg)
except ValueError as msg:
	print('Please enter only integers')
	logging.exception(msg)
logging.info("Request finished")