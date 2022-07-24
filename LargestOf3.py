#!bin/python3

print("Input 3 integers:")
n1=input()
n2=input()
n3=input()

if(n1>n2):
    if(n1>n3):
        print("The largest number is: ", n1)
    else:
        print("The largest number is: ", n3)
elif(n2>n1):
    if(n2>n3):
        print("The largest number is: ", n2)
    else:
        print("The largest number is: ", n3)
