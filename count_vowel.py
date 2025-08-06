#counting the vowels from the string..

def counting_vowel():
    vowels = ('a','e','i','o','u')
    msg = str(input("Write your message here: "))
    count = 0
    for vwl in msg.lower():
       if vwl in vowels:
           count += 1
    print(count)
counting_vowel()
