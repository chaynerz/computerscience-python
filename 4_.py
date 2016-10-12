# Chay C12
"""
a program allows the user to enter as many numbers as they wish. Once they enter 0, the program stops and tells
them the smallest, the largest and the average of the numbers they entered 
"""

num = []
current = int

while current != 0:
    current = int(input("Input your number: "))
    num.append(current)

num.pop()
min = min(num)
max = max(num)
average = sum(num) / len(num)

print("Maximum Number: " + str(max))
print("Minimum Number: " + str(min))
print("Average: " + str(average))
