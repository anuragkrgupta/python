# building an atm machine functions just for fun.. 

user_name = str(input("Please enter your name: ")) 
acc_no = int(input("Register your account number: "))
acc_pass = int(input("set your password" ))

print("Welcome",user_name)
reacc_no = int(input("Enter your account number: "))
if acc_no == reacc_no:
    passs = int(input("Enter your password: "))

    if acc_pass == passs:
        amount = float(input("Enter the amount: "))
        print(amount," has been debited from your account \n Please collect your cash!")
    else: print("Password dosen't match!")

else:
    print("Account not found!")