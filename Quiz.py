print("Rules: after every correct answer you will win 10000 points")
name = str(input("Enter your name: "))
age = str(input("Enter your age: "))
points = 00
req = str(input("Are you ready to play KBC with me (Y/N): "))

if req == 'Y' or 'y':
    print("lets go")
    print("Here is your question:- ")
    
    ques = [("what is your name? ", name), ("what is your age? ", age)]

    for que in ques:
        print(que[0])
        ans = input()
        if ans == que[1]:
            print("correct answer")
            points = points + 10000
            print("you have won: ",points," points")
        else:
            print("wrong answer")
            print("you have won: ",points," points")
            break

else: 
    print("Thank you ",name," for showing interest!")
