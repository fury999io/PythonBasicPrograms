#!/bin/python3

ch = input("Enter a character ")

if ch>='a' and ch<='z':
	print(ch+" is a letter")
elif ch>='A' and ch<='Z':
	print(ch+" is a letter")
elif int(ch)>=0 and int(ch)<=9:
	print(ch+" is a digit")
else:
	print(ch+" is neither a letter nor a digit")
