# A dynamic calculator using python which calculates all the basic mathematics calculation

user_name = str(input("Hey user what is your name ")) #taking input from user side
print("Hello", user_name, "welcome to python calculator")

value1 = float(input("Please enter your first number "))
value2 = float(input("Please enter your second number "))
sign = input("Please enter the operation type..  ")

if sign == '+':  #using if else logic
    result = value1 + value2 
elif sign == '-':  #in python 'else if' is 'elif'
    result = value1 - value2
elif sign == '*':
    result = value1 * value2
elif sign == '**':
    result = value1 ** value2
elif sign == '/':
    result = value1 / value2
elif sign == '//':
    result = value1 // value2
elif sign == '%':
    result = value1 % value2


print("your result is: ", result)