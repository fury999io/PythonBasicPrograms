x=int(input("Enter the vale of x "))
N=int(input("Enter the value of N "))

def val(q):
    fac=1
    c=q
    while(c>1):
        fac=fac*c
        c=c-1
    return (x**q)/fac

sum=x
w=2
while(w<=N):
    if(w%2==0):
        sum=sum-val(w)
    else:
        sum=sum+val(w)
    w=w+1

print("The sum of the series is", sum)
