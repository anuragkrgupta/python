#recursion is the process of defining something in term of itself

#python recursion function
#factorial

def factorial(n):  # here we are creating a function
    if (n==0) or (n==1):  #checking the condition
        return 1  #if the condition is true, return 1
    else:  
        return n * factorial(n-1)  #else it will perform this calculation
print(factorial(5))  #calling the function. 

