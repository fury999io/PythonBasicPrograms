#!/bin/python3

num = int(input("Input a number\n"))
factorial=1

counter=1
while counter<=num:
	factorial=factorial*counter
	counter=counter+1

print("The factorial of "+str(num)+" is "+str(factorial))
