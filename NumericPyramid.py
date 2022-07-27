from re import I
from tkinter.ttk import Separator


i=1

print("Enter the length of the pyramid in whole number", end=' ')
n = int(input())

while(i<=n):
    j=1
    while(j<=i):
        print(i, end=" ")
        j=j+1
    print()
    i=i+1

