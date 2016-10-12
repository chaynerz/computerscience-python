# Chay C12
"""
Write a program to let user input names and output in original and reverse
"""

name = []
done = False
print("Type DONE to finish")

while done != True:
    currentname = input("Enter name: ")
    name.append(currentname)
    if currentname == "DONE":
        done = True

name.pop()

choice = input("Type REVERSE to print reversed or type anything else to print ORIGINAL: \n > ")

if choice == "REVERSE":
    name.reverse()
    print(*name, sep="\n")
else:
    print(*name, sep="\n")



                        
    
    
