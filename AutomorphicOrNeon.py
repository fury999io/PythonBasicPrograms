#To check if a number is automorphic or neon or not

def Automorphic(num):
    l=len(str(num))
    sq=num**2
    if sq%(10**l)==num:
        return "The number is automorphic"
    else:
        return "The number is not automorphic"

def Neon(num):
    sqr=num**2
    sum=0
    while sqr>0:
        sum=sum+(sqr%10)
        sqr=sqr//10
    if sum==n:
        return "The number is neon"
    else:
        return "The number is not neon"

print("Enter a number")
n=int(input())

c=int(input("Enter 1 for checking the number for Automorphic, 2 for Neon "))
if c==1:
    print(Automorphic(n))
elif c==2:
    print(Neon(n))
else:
    exit()