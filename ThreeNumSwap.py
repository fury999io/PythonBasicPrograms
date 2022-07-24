print("Enter 3 numbers")
n1=int(input())
n2=int(input())
n3=int(input())

nTemp=n1

n1=n2
n2=n3
n3=nTemp

print("The numbers are: "+str(n1), str(n2), str(n3), sep=", ")