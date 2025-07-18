#this is an employee registeration and enquiry point

#question asked
import random

employeeID = random.randint(100, 1000)
while True:
    todo = str(input("Press 'r' for Registeration & 'e' for Enquiry: "))
    ID = employeeID
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
            print(ID)

    else:
        empID = int(input("Enter Employee ID: "))
        print(ID.get('name')) 