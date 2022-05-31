#!/bin/python3

n = int(input("Input the number to be checked for armstrong number "))

len=0 #length of the string
for x in str(n):
	len=len+1

arm=0

for y in str(n):
	arm=arm+(int(y)**len)

if arm==n:
	print(str(n)+" is a armstrong number")
else:
	print(str(n)+" is not a armstrong number")
