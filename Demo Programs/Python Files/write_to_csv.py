import csv

with open('emp.csv', 'w', newline = '') as f:
    w = csv.writer(f)
    w.writerow(['ENO','ENAME','ESAL','EADDR'])
    while True:
        eno = int(input('Enter employee number : '))
        ename = input('Enter employee name : ')
        esal = float(input('Enter employee salary : '))
        eaddr = input('Enter employee address : ')
        w.writerow([eno,ename,esal,eaddr])
        option = input('Do you want to insert one more record ? : [Yes | No]')
        if option.lower() == 'no':
            break

print('Writing data to the file successfully.')