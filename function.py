def calculate (a, b):  #we are creating a function here named calculate
    add = a+b
    print(add)

a=9     
b=9
calculate (a, b)        #here we are calling the function


###############################


def divide(a,b):
    div = a/b
    print(div)

a = int(input("enter your 1st number "))
b = int(input("enter your 2nd number "))

divide(a,b)


#######################################


def isPrime(a):   # checking prime number dynamically!!!!
    if a%2 == 0:
        print(a," is a prime number.")
    else: 
        print(a," is not a prime number.")

a = int(input("enter a number "))
isPrime(a)