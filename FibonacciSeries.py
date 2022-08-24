#To generate the Fibonacci Series upto the N th term

print("Enter the value of N")
N=int(input())

a=0
b=1
print(a, b, sep=", ", end=", ")

count=1

while(count<=N):
    c=a+b
    print(c, end=", ")
    a, b = b, c
    count=count+1
