# Chay C12
"""
A town has a bus service where passengers under the age of 12 and over the age of 60 do not need to pay a fare

Write a program where the user inputs their age and the output tells them if they need t pay the fare or not

"""

age = input("Enter your age: ")
age = int(age)

if age < 12 or age > 60:
    print("You do not need to pay the fare")
else:
    print("You need to pay the fare")
