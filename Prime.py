#!/bin/python3

n = int(input("Input the number to be checked for prime number\n"))

counter = 0

i=1
while(i<=n):
	if n%i==0:
		counter=counter+1
	i=i+1

if counter<=2:
	print(str(n)+" is a prime number")
else:
	print(str(n)+" is not a prime number")

