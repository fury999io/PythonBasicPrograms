import math
print("For the the quadratic equation: ax²+bx+c=0, input the coefficients...")
a = int(input("Input the coefficient of a: "))
b = int(input("Input the coefficient of b: "))
c = int(input("Input the coefficient of c: "))

if a==0:
    print("a cannot be 0")
    exit()

z=b**2-4*a*c

root1=(-b-math.sqrt(z))/2*a
root2=(-b+math.sqrt(z))/2*a

print("The roots are: ", root1, root2)