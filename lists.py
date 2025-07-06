# here we are practicing about lists in python

L = [1,2,3, "anurag", True]  #we can actually add numbers, strings and boolean walues in string
print(L)

print(L[0])  #printing list's item individually by index values 
print(L[1])
print(L[2])

print(L[-3]) #negative index
print(len(L)-3) #positive index
print(L[5-3]) #positive index


if 3 in L:  #if using 'in'
    print("yes")
else:
    print("no")

#same thing applies for string as well
if "anu" in "anurag kumar":
    print("yes")
else:
    print("no")

print(L[:]) #this is printing 0 to 4
print(L[1:4]) # this is printing 1 to 4
print(L[1:-1])  # this is printing 1 to total-1
print(L[1:len(L)-1])  # this is printing 1 to length_of_list -1 

#print(start : end : jumpIndex)  this is the formula of jumpIndex
print(L[1:5:2])  # this is printing 1 to 5 while jumping 2 indexes , this is called jumpIndex



# List comprehension 

Lst = [i*i for i in range(10)] #This is called list comprehension in Python
print(Lst)


Lst = [i*i for i in range(10) if i%2==0] # we can apply condition in this comprehension too
print(Lst)