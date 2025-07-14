#method of sets here 

s1 = {1,2,3,4}
s2 = {4,7,2,9}

# print(s1) # printing of sets
# print(s1.union(s2)) # printing the union of two sets
# s1.update(s2)  # updating the values of s1 with s2
# print(s1 ,s2) # now the updated value of s1 will print here
# s3 = s1.intersection(s2)  # this will intersect two sets and print the value which is similar in both sets
# print(s3)

# s1.intersection_update(s2)  # this will intersect two sets and update the value
# print(s3)

# s3 = s1.symmetric_difference(s2)  # this will perform the symmetric diffrence method and print the non similar items from the sets
# print(s3)
 
# s1.symmetric_difference_update(s2)  # this will update the s1 set with the output 
# print(s1)

# s3 = s1.difference(s2)  # basicly performing the subtraction of s1 - s2
# print(s3)  # which will give {1, 3}

# s1.diffrence_update(s2)  # this will update the s1 set with the output 
# print(s1) 

# s3 = s1.isdisjoint(s2) #disjoint method from set theory
# print(s3)

# print(s1.issuperset(s2)) #check, Is s2 is superset of s1

# print(s1.issubset(s2))  #check, Is s2 is subset of s1

# s1.remove(2)  #this will remove the item from the set, if the item is not present in the list, it will through an error message
# print(s1)

# s1.discard(8)  # this will discard the item from the list same as remove method, if the item is not present in the list it will not through an error message
# print(s1)

# s3 = s1.pop()  # pop method used to pop any item from the list, but accessable for future use
# print(s3)

# del s1  # deleting the set

# s1.clear() #clearing the items of set

#check if item exsists
# if 2 in s1:
#     print("2 is present")
# else:
#     print("2 is absent")