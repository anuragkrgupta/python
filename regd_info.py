#this is an employee registeration and enquiry point

#question asked
import random

employee_db = {}
while True:
    employeeID = random.randint(100, 1000)

    todo = str(input("Press 'r' for Registeration & 'e' for Enquiry & 'q' for Quit: "))
    ID = employeeID

    while employeeID in employee_db:
     employeeID = random.randint(100,1000)

    if todo.lower() == 'r':

            name = str(input("Enter employee name: "))
            age = int(input("Enter age: "))
            role = str(input("Enter designation/role: "))
            
            data = {
            'name' : name,
            'age' : age,
            'role' : role,
            'employeeID' : ID
            }
            print(ID)
            employee_db[employeeID] = data
            print("Registeration complete")

    elif todo.lower() == 'e':
        empID = int(input("Enter Employee ID: "))
        emp_data = employee_db.get(empID)
        if emp_data:
            print("Employee Data: ", emp_data)
        else:
            print("No Employee Found!")

    else:
        break
        