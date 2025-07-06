# tuple is immmutable
#but if we want to change the tuple items we must have to convert the tuple into a list. Then perform operation in the list and convert it back to tuple.

countries = ("India", "Russia", "Italy", "China", "Turkey")
temp = list(countries)     #converting the countries to list
temp.append("Sri Lanka")   #add item at the end
temp.pop(3)                #remove item no. 3
temp[3] = "America"        #add item at the index of 3
countries = tuple(temp)    #converted the countries back to tuple
print(countries)


# how ever we can concatenate a tuple directly without converting them into list

cont = ("India", "Russia", "Italy", "China", "Turkey")
cont2 = ("Sri Lanka", "America")
concatenating = cont + cont2
print(concatenating)


#we can implement all the methods of the list here too..
#we can change the tuple items only by converting them into a list, once converted you can modify as per your need and them convere them into list.

