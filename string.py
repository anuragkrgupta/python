# here we are practicing type of stings in python

print("Anurag kumar") #simple print statment for printing a string 

A = "anurag" # this is a End of line string EOL
B = '''Hello my name is Anurag Kumar 
I am a PG student''' # this is a multi-line string having no EOL error , used for printing multiple lines without using \n
print(B)

print(A[0]) # this is for printing characters.
 
#lets use a for loop for printing charaters 
for character in A:  #character contains all the characters of A
    print(character) # printing character which contains all the characters of A

#string slicing

lenA = len(A) #this is how you find length of a string
print(lenA) #printing the length

print(A[0:4]) # we are printing only from character [0 to 4-1=3] of a string
print(A[0:-3]) # this will subtract the length of the string by 3, interpriter will execute it like: ''print(A[0:len(A)-3])''

#String are immutable 
print(A.upper()) #changing into upperCase
print(A.lower()) #changing into lowerCase
print(A.rstrip("a")) #this will strip all 'a' from the string
print(A.replace("anurag", "aman")) #this will replace all the occurances string content
print(B.split(" ")) #this is a split method of spliting all the words from a string, eg: ['Hello', 'my', 'name', 'is', 'Anurag', 'Kumar', '\nI', 'am', 'a', 'PG', 'student']
print(B.capitalize()) #this capitalize method changes the 1st char in capital form and rest into small, this is the special feature of python which is not present in JS.
print(A.center(50)) #this will make the text to center by adding 50 char space

# count(): The count() method returns the number of times the given value has occurred within the given string.
str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)
# endswith(): The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

# find(): The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))

# index(): The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))

# isalnum(): The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
str1 = "WelcomeToTheConsole"
print(str1.isalnum())

# isalpha(): The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
str1 = "Welcome"
print(str1.isalpha())

# islower(): The islower() method returns True if all the characters in the string are lower case, else it returns False.
str1 = "hello world"
print(str1.islower())

# isprintable(): The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())

# isspace(): The isspace() method returns True only and only if the string contains white spaces, else returns False.
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())

# istitle(): The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
str1 = "World Health Organization" 
print(str1.istitle())

# isupper(): The isupper() method returns True if all the characters in the string are upper case, else it returns False.
str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())

# startswith(): The endswith() method checks if the string starts with a given value. If yes then return True, else return False.
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

# swapcase(): The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

# title(): The title() method capitalizes each letter of the word within the string.
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())