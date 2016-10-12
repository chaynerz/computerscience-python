#Chay C12
"""
Write the code for the number guessing game
"""

secretnum = 9

guess = int(input("Guess the number: "))



if guess > secretnum:
    print("secret number is smaller")
elif guess < secretnum:
    print("secret number is larger")
elif guess == secretnum:
    print(str(guess) + " is the correct number")
