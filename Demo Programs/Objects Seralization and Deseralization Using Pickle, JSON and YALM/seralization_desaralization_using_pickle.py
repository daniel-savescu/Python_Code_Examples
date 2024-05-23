import pickle
class Employee:
    def __init__(self,employeeNumber,employeeName,employeeAddress):
        self.employeeNumber = employeeNumber
        self.employeeName = employeeName
        self.employeeAddress = employeeAddress
    def display(self):
        print('Employee Number : {}, Employee Name: {}, Employee Address: {}'.format(self.employeeNumber,self.employeeName,self.employeeAddress))

firstEmployee = Employee(100, 'Daniel', 'Hawai')

with open('employee.ser', 'wb') as f:
    pickle.dump(firstEmployee,f)

with open('employee.ser', 'rb') as f:
    deseriliazedObject = pickle.load(f)

deseriliazedObject.display()