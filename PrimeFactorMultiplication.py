print("Enter a number")
num=int(input())
n=num

def prime(x):
    count=0
    for i in range(1, x+1):
        if x%i==0:
            count=count+1
    if count>2:
        return False
    else:
        return True        

print("1", end="")

f=2
while(n>1):
    if(n%f==0 and prime(f)==True):
        n=n/f
        print(" x ", end="")
        print(f, end="")
    else:
        f=f+1
