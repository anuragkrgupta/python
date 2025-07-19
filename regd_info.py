#this is an employee registeration and enquiry point

import random

employee_db = {}
while True:
    employeeID = random.randint(100, 1000)

    todo = str(input("Press 'r' for Registeration & 'e' for Enquiry & 'q' for Quit: "))
    ID = employeeID

    while employeeID in employee_db:
     employeeID = random.randint(100,1000)

    if todo.lower() == 'r':
        try:
            name = str(input("Enter employee name: "))
            if not name.isalpha():
                raise ValueError("Only alphabets are allowed for name input!")
            try:
                age = int(input("Enter age: "))
            except ValueError :
                print("use integer for age!")
                continue
            role = str(input("Enter designation/role: "))
            if not role.isalpha():
                raise ValueError("Only alphabets are allowed for role input!")
            
            data = {
            'name' : name,
            'age' : age,
            'role' : role,
            'employeeID' : ID
            }
            print(ID)
            employee_db[employeeID] = data
            print("Registeration complete")
        except ValueError as e:
            print(e)
        
            
    elif todo.lower() == 'e':
        empID = int(input("Enter Employee ID: "))
        emp_data = employee_db.get(empID)
        if emp_data:
            print("Employee Data: ", emp_data)
        else:
            print("No Employee Found!")

    else:
        break
        