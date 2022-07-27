#this program finds the sum of numbers between 1 and 7 and progressively prints the sum after each step of addition
sum=0
for n in range(1, 8):
    sum=sum+n
    print("The sum of the natural numbers <=", n, "is", sum)