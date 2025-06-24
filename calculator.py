# A dynamic calculator using python which calculates all the basic mathematics calculation

user_name = str(input("hey user what is your name "))
print("hello", user_name, "welcome to python calculator")

value1 = float(input("Please enter your first number "))
value2 = float(input("Please enter your second number "))
sign = input("please enter the operation type.. ex:- *, /, +, -, **, //, %  ")

if sign == '+':
    result = value1 + value2
elif sign == '-':
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