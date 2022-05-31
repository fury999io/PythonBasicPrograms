#!/bin/python3
yr = int(input("Input the year to be checked for leap year\n"))
chk = 0
# 0 refers to non-leap year
if yr%4==0:
	chk=1
	if yr%100==0:
		if yr%400==0:
			chk=1
		else:
			chk=0
if chk==1:
	print("The year "+str(yr)+" is a leap year")
else:
	print("The year "+str(yr)+" is not a leap year")
