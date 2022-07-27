print("Input the number to find the factorial of")
n = int(input())
factorial=1
for n in range(1, n+1):
    factorial=factorial*n

print("The factorial of", n, "is", factorial)