#print good morning , good afternoon, good evening, good night using time module...

import time  #import Python’s built-in time module, which lets us access the system’s current time.
timestamp = time.strftime("%H : %M : %S")  #using time.strftime and %H , %M, %S to get hours , minutes, seconds
print(timestamp) 

hour = int(time.strftime("%H")) #time.strftime("%H") gives the current hour in 24-hour format as a string, We use int(...) to convert it to an integer so we can use it in numerical comparisons. 

if 4 <= hour < 12:
    print("Good morning!")
elif 12 <= hour < 16:
    print("Good afternoon!")
elif 16 <= hour < 19:
    print("Good Evening!")
else: print("Good Night!")