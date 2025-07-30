#here we will encrypt and decrypt some message using python code
#lets begin

#rules for encrytion:-
#if the word is <=3 then reverse the order of characters
#if word is >3 then remove the 1st character and append it to the last,
#now add 3 random characters to the starting and ending of the word.

#rules for decryption:-
#reverse all the task performed for encrypting the message.


import random  #for generating random things
import string  #for random string

msglen = ()  #storing message lenth here
encrypted_db = {}   #database


msg_input = input("Type your message here:- ")
while True:  #loop for multiple inputs
    req = input("what you want to do?\n press 'e' for encryption & 'd' for decryption Or press 'q' for exit!!")

    if req.lower() == "e":
        ran_letters = ''.join(random.choices(string.ascii_letters, k=4))   #generating random letter   
        msglen = len(msg_input)  #calculating the length of the message
        # print(msglen)
        if msglen<=3:
            reverse_s = msg_input[::-1]  #reversing the string
            print(reverse_s)
        print("encrypted")
        if msglen>3:
            rotate = msg_input[1:] + msg_input[0]  #appending the 1st char into last
            # print(rotate)
            encrypted = ran_letters + rotate + ran_letters  #adding 4 random char 
            encrypted_db[msg_input] = encrypted  #storing the output to a database
            print(encrypted)
    elif req == "d":
        # print(encrypted)
        if msglen<=3:  
            reverse_s = msg_input[::1]  #if the input len in less then 3 simply reverse it
            print(reverse_s)
        if msglen>3:  
            minus = encrypted[0:-4]  #removing last 4 random char
            rev = minus[::-1]  #reversing the string
            minuss = rev[0:-4] #remove last 4 random char again
            min = minuss[::-1]  #reversing the string again
            decrypted = min[msglen-1] + min[:-1] #msglen-1 for getting the last index and adding the the string by removing the last char

            print(decrypted)
        # print("decrypted")
    else:
        break
