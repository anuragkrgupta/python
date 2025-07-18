#this is an employee registeration and enquiry point

#question asked
import random

employee_db = {}

employeeID = random.randint(100, 1000)



while True:
    todo = str(input("Press 'r' for Registeration & 'e' for Enquiry: "))
    ID = employeeID

    while employeeID in employee_db:
     employeeID = random.randint(100,1000)

    if todo.lower() == 'r':

            name = str(input("Enter employee name: "))
            age = int(input("Enter age: "))
            role = str(input("Enter designation/role: "))
            
            ID = {
            'name' : name,
            'age' : age,
            'role' : role,
            'employeeID' : ID
            }
            print(ID, employee_db)

    else:
        empID = int(input("Enter Employee ID: "))
        emp_data = employee_db.get(empID)
        print(employee_db.get(emp_data)) 