# Chay C12
"""
Write a fibnacci sequence
"""



def fibonacci(n):
    
    av = 0
    bv = 1
    for i in range(0,n):
        temporary = av
        av = bv
        bv = temporary + bv
    return av


num = int(input("Enter number of sequence: "))

for e in range(0, num):
    print(fibonacci(e))















































