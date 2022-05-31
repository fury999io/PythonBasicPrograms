#!/bin/python3

ch = str(input("Input a letter\n"))
ch = ch[:1]

if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
	print("The letter is a vowel")
elif ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
	print("The letter is a vowel")
else:
	print("The letter is a consonant")
