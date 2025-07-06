l = [36,78,1,3,5,7,9,69,88,96]
i = ["a", "b", "c", "d"]
# print(l)

print(l.append(11))  #append is the method to add items at the end of the list
print(i.append("e"))  #works with all type of list
print(l.sort())  #sort all the numbers in the list by assending order
print(l.sort(reverse=True))  # sort in decending order
print(l.reverse())  #this will reverse the order of original list  
print(l.index(1))  #this will return the index value of the number which you will put inside the braket 
print(l.count(6))  #count the number of times that number occurs in the list
