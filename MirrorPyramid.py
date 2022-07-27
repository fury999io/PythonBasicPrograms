#Example:
"""
        1
       21
      321
     4321
    54321
   654321
  7654321
 87654321
987654321

"""

print("Enter the length of the pyramid in whole number", end=" ")
n=int(input())
N=n
while(n>=1):
    i=1
    while(i<=N):
        if(i<n):
            print(" ", end=" ")
        else:
            print((N+1)-n, end=" ")
        i=i+1
    print()
    n=n-1