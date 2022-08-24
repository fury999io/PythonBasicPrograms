#To display the sum of prime numbers from 0 to 99

def Prime(num):
    div=0
    i=1
    while(i<=num):
        if num%i==0:
            div=div+1
        i=i+1
    if div>2:
        return False
    else:
        return True

sum=0

for q in range(0, 99):
    if Prime(q)==True:
        sum=sum+1

print(sum)