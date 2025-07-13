import random


secret_number = random.randint(1, 100) #random generates random number. randint(a, b) is a function from random module.

print("Welcome to the Number Guessing Game!")
print("I have picked a number between 1 and 100. Can you guess it?")

while True:
    try:
        guess = int(input("Enter your guess: "))

        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
            continue

        # Calculate percentage difference
        percentage_diff = abs(secret_number - guess) / secret_number * 100

        if guess < secret_number:
            print(f"Too low! You are off by {percentage_diff:.2f}%. Try again.")
        elif guess > secret_number:
            print(f"Too high! You are off by {percentage_diff:.2f}%. Try again.")
        else:
            print("🎉 Congratulations! You guessed the number correctly.")
            break
    except ValueError:
        print("Please enter a valid number.")
