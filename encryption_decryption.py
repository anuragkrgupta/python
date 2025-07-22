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

ran_letters = random.choice(string.ascii_letters)

msglen = ()
msg_input = input("Type your message here:- ")

req = input("what you want to do?\n press 'e' for encryption & 'd' for decryption ")

if req.lower() == "e":
    msglen = len(msg_input)
    # print(msglen)
    if msglen<=3:
        reverse_s = msg_input[::-1]
        print(reverse_s)
    print("encrypted")
    if msglen>3:
        rotate = msg_input[1:] + msg_input[0]
        # print(rotate)
        print(f"{ran_letters} + {rotate} + {ran_letters}")

else:
    print("decrypted")