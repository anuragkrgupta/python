take_rows = int(input("Enter row: "))

#triangle
# for i in range(1, take_rows+1): #for rows
#     print("*" * i) 


# #reverse - triangle
# for i in range(1, take_rows+1): #for rows
#     count = take_rows - i # to reverse the pattern
#     print("*" * count) 

#cross
for i in range(take_rows):
    rows = ""
    for j in range(take_rows):
        if i == j or i +j == take_rows - 1:
            rows += "*"
        else:
            rows += " "
    print(rows) 
