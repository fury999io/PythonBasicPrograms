print("Enter the length of the inverted pyramid in whole number", end=" ")
n=int(input())

while(n>=1):
    i=1
    while(i<=n):
        print(n, end=" ")
        i=i+1
    n=n-1
    print()
