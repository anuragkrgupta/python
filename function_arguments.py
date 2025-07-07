# there are 4 types of arguments := 1. default argument
#                                   2. keyword argument
#                                   3. variable length argument
#                                   4. required 

#Default argument:

def defaultArgument(a=3, b=3): #here we pass the default value of a nd b in the argument
    c = (a + b)/2  
    print("this is the average of two numbers: " , c)

defaultArgument()  #function calling

#Keyword argument
#here the order of the argument is not necessary... 
# for ex:= defaultArgument(b=9 , a=33)

#required argument
def defaultArgument(a, b=3): #here we provide only one value, it means the 'a' become the required argument, now we have to give a value to 'a' anyhow.
    c = (a + b)/2  
    print("this is the average of two numbers: " , c)

defaultArgument()  

#variable length argument
def keyword(*numbers):  # *numbers is taking numbers as tuple. (arbitrary number of argument)
    sum = 0  #initializing sum by 0
    for i in numbers: # for loop
        sum = sum + i  #add all numbers 
    print(sum/len(numbers))  # adding all numbers and diving it by there length

keyword(7, 8, 9, 1, 2, 3, 4)  #in this case the length of numbers is 7


#practice logic
#returning values
def keyword(*numbers):  
    sum = 0  
    for i in numbers: 
        sum = sum + i 
    return (sum/len(numbers))
takeInput = list(map(int, input("Enter the numbers: ").split()))  # Take multiple inputs from the user in one line

store = keyword(*takeInput)  # Use the unpacking operator * to pass as separate arguments

print(store)