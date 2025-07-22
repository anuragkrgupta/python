#here we will encrypt and decrypt some message using python code
#lets begin

#rules for encrytion:-
#if the word is <=3 then reverse the order of characters
#if word is >3 then remove the 1st character and append it to the last,
#now add 3 random characters to the starting and ending of the word.

#rules for decryption:-
#reverse all the task performed for encrypting the message.
import random
import string

msglen = ()
encrypted_db = {}


msg_input = input("Type your message here:- ")
while True:
    req = input("what you want to do?\n press 'e' for encryption & 'd' for decryption Or press 'q' for exit!!")

    if req.lower() == "e":
        ran_letters = ''.join(random.choices(string.ascii_letters, k=4))     
        msglen = len(msg_input)
        # print(msglen)
        if msglen<=3:
            reverse_s = msg_input[::-1]
            print(reverse_s)
        print("encrypted")
        if msglen>3:
            rotate = msg_input[1:] + msg_input[0]
            # print(rotate)
            encrypted = ran_letters + rotate + ran_letters
            encrypted_db[msg_input] = encrypted
            print(encrypted)
    elif req == "d":
        # print(encrypted)
        
        print("decrypted")
    else:
        break