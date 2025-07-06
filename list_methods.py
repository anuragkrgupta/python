l = [36,78,1,3,5,7,9,69,88,96]
i = ["a", "b", "c", "d"]
# print(l)

# print(l.append(11))  #append is the method to add items at the end of the list
# print(i.append("e"))  #works with all type of list
# print(l.sort())  #sort all the numbers in the list by assending order
# print(l.sort(reverse=True))  # sort in decending order
# print(l.reverse())  #this will reverse the order of original list  
# print(l.index(1))  #this will return the index value of the number which you will put inside the braket 
# print(l.count(6))  #count the number of times that number occurs in the list
# print(l.index(1, 899))  #it this we are inserting 899 into the l list with index 1 , so the 1 is the index and 899 is the item of the list which we are inserting 

m = [1000,1100,1200,1300]  # we are creating a new list m
# l.extend(m)     #using extend method we are adding the items of the list m into list l
# print(l)  #printing list l with extended items of m

#if we want to merge these two lists with changing the original list items, we will use concatenation method
k = l+m
print(k)  # the result is same as extend method but we are creating changes in the new list k now.